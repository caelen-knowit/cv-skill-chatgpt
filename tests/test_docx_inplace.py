#!/usr/bin/env python3
"""Self-test for cv-match-coach/scripts/docx_inplace.py.
Run: pip install python-docx && python tests/test_docx_inplace.py
Builds a formatted CV, applies every edit operation, checks the format check passes,
then breaks the formatting on purpose and checks the format check fails."""
import json, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "..", "cv-match-coach", "scripts", "docx_inplace.py")

def run(*args):
    return subprocess.run([sys.executable, SCRIPT, *args], capture_output=True, text=True)

def build(path, logo):
    import base64, docx
    from docx.shared import Pt, RGBColor, Cm
    d = docx.Document()
    s = d.sections[0]; s.left_margin = Cm(1.7); s.top_margin = Cm(2.2)
    png = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==")
    open(logo,"wb").write(png)
    s.header.paragraphs[0].add_run().add_picture(logo, width=Cm(2))
    s.header.add_paragraph("Company CV")
    h = d.add_paragraph(); r = h.add_run("Alex Berg"); r.font.name="Georgia"; r.font.size=Pt(22); r.bold=True; r.font.color.rgb=RGBColor(0x1F,0x3A,0x5F)
    t = d.add_paragraph(); r = t.add_run("Senior Backend Developer"); r.font.name="Georgia"; r.font.size=Pt(13); r.italic=True
    d.add_heading("Profile", level=1)
    p = d.add_paragraph(); r = p.add_run("Alex is a passionate and results-driven developer."); r.font.name="Calibri"; r.font.size=Pt(10.5)
    d.add_heading("Assignments", level=1)
    tbl = d.add_table(rows=2, cols=2); tbl.style = "Table Grid"
    for i,(period,role,desc) in enumerate([("2023 – present","Backend Developer · Northbank","Develops the payment service."),("2020 – 2023","Developer · Safeguard","Maintained the claims system.")]):
        c0, c1 = tbl.rows[i].cells
        rr = c0.paragraphs[0].add_run(period); rr.font.size=Pt(9); rr.font.name="Calibri"
        rr = c1.paragraphs[0].add_run(role); rr.bold=True; rr.font.size=Pt(10.5); rr.font.name="Calibri"
        pp = c1.add_paragraph(); rr = pp.add_run(desc); rr.font.size=Pt(10.5); rr.font.name="Calibri"
        pp = c1.add_paragraph(); a = pp.add_run("Technologies: "); a.bold=True; a.font.size=Pt(9); a.font.name="Calibri"
        b = pp.add_run("Java, Kafka" if i==0 else "Java, Jenkins"); b.font.size=Pt(9); b.font.name="Calibri"
    d.add_heading("Languages", level=1)
    p = d.add_paragraph(); r = p.add_run("Swedish, English"); r.font.name="Calibri"; r.font.size=Pt(10.5)
    d.save(path)

PLAN = [
 {
  "op": "set",
  "id": "p3",
  "text": "Alex is a backend developer with nine years of Java experience, the last four in banking.\nAlex has built payment services on Spring Boot and Kafka."
 },
 {
  "op": "set",
  "id": "t0.r0.c1.p1",
  "text": "Develops the payment notification service for the bank's mobile app. Team of 7 developers."
 },
 {
  "op": "insert_after",
  "id": "t0.r0.c1.p1",
  "like": "t0.r0.c1.p1",
  "text": "Maintains the Kafka topics for payment events.",
  "new_id": "n1"
 },
 {
  "op": "set_runs",
  "id": "t0.r0.c1.p2",
  "runs": [
   {
    "like": 0,
    "text": "Technologies: "
   },
   {
    "like": 1,
    "text": "Java 17, Spring Boot, Kafka, AKS"
   }
  ]
 },
 {
  "op": "insert_row_after",
  "id": "t0.r1",
  "like": "t0.r1",
  "cells": [
   [
    "2017 – 2019"
   ],
   [
    "Developer · Telenord",
    "Developed billing integrations.",
    {
     "runs": [
      {
       "like": 0,
       "text": "Technologies: "
      },
      {
       "like": 1,
       "text": "Java 8, Oracle"
      }
     ]
    }
   ]
  ],
  "new_id": "row1"
 },
 {
  "op": "delete",
  "id": "p6"
 },
 {
  "op": "insert_after",
  "id": "p5",
  "like": "p6",
  "text": "Swedish (native), English (fluent)"
 }
]

def main():
    with tempfile.TemporaryDirectory() as tmp:
        src, out, bad = (os.path.join(tmp, n) for n in ("cv.docx", "out.docx", "bad.docx"))
        build(src, os.path.join(tmp, "logo.png"))
        plan = os.path.join(tmp, "plan.json")
        json.dump(PLAN, open(plan, "w"))
        r = run("apply", src, plan, out); assert r.returncode == 0, r.stderr
        r = run("verify", src, out); assert r.returncode == 0, r.stdout
        text = run("text", out).stdout
        for expected in ("nine years of Java", "Maintains the Kafka topics", "Developer · Telenord",
                         "Technologies: Java 8, Oracle", "Swedish (native)"):
            assert expected in text, expected
        assert "passionate" not in text
        import docx
        from docx.shared import Pt
        d = docx.Document(out); d.paragraphs[3].runs[0].font.size = Pt(12); d.save(bad)
        r = run("verify", src, bad); assert r.returncode == 1, "format change was not detected"
    print("OK: in-place edits keep the format, and a format change is detected")

if __name__ == "__main__":
    main()
