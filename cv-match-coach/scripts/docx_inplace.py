#!/usr/bin/env python3
"""
docx_inplace.py – edit a CV .docx IN PLACE so the result keeps the original's exact
format: fonts, sizes, colours, styles, spacing, margins, headers/footers, logos, tables.

Only the text inside existing paragraphs/runs/table cells is changed. New paragraphs or
table rows are deep copies of existing ones, so they inherit identical formatting.
Styles, page setup, headers, footers and images are never touched.

Usage (requires python-docx):
  python docx_inplace.py dump   original.docx                 > structure.json
  python docx_inplace.py apply  original.docx plan.json out.docx
  python docx_inplace.py verify original.docx out.docx
  python docx_inplace.py text   out.docx                       (plain text, to read back)

Block ids (from `dump`):
  p<N>                 body paragraph N              e.g. p12
  t<T>.r<R>.c<C>.p<P>  paragraph P in table cell     e.g. t0.r3.c1.p0
  t<T>.r<R>            table row (for row operations)
  Nested tables: t0.r1.c0.t0.r2.c0.p0

Plan (JSON list, applied in order; all ids refer to the ORIGINAL document, plus any
"new_id" you create with insert_after):
  {"op": "set", "id": "p12", "text": "New text"}
      Replace the paragraph's text; keeps the formatting of its first non-empty run.
      "\\n" becomes a line break inside the same paragraph.
  {"op": "set_runs", "id": "p20", "runs": [{"like": 0, "text": "Technologies: "},
                                           {"like": 1, "text": "Java, Kafka"}]}
      For mixed formatting (e.g. bold label + normal text). "like" = index of the
      original run (from `dump`) whose formatting to copy.
  {"op": "insert_after", "id": "p20", "like": "p19", "text": "...", "new_id": "n1"}
      New paragraph after "id", formatted exactly like "like" (default: same as "id").
      Optional "runs" instead of "text", as in set_runs (indices refer to "like").
  {"op": "delete", "id": "p21"}
  {"op": "insert_row_after", "id": "t0.r3", "like": "t0.r3", "cells": [["Role"], ["Line 1", "Line 2"]],
   "new_id": "row1"}
      Copy row "like" after row "id"; "cells" = list of paragraph texts per cell.
      A paragraph may be {"runs": [{"like": 0, "text": "Technologies: "}, {"like": 1, "text": "Java"}]}
      to keep mixed formatting (run indices as in the copied row's paragraph).
  {"op": "delete_row", "id": "t0.r4"}
"""
import copy
import hashlib
import json
import sys

try:
    import docx  # python-docx
    from docx.oxml.ns import qn
    from docx.table import Table
    from docx.text.paragraph import Paragraph
except ImportError:  # pragma: no cover
    sys.exit("python-docx is required: pip install python-docx")


# ---------------------------------------------------------------- structure

def _walk_tables(tables, prefix, out):
    for ti, table in enumerate(tables):
        tid = f"{prefix}t{ti}"
        for ri, row in enumerate(table.rows):
            rid = f"{tid}.r{ri}"
            out[rid] = row
            seen = set()
            for ci, cell in enumerate(row.cells):
                if id(cell._tc) in seen:  # merged cells repeat; skip duplicates
                    continue
                seen.add(id(cell._tc))
                cid = f"{rid}.c{ci}"
                for pi, p in enumerate(cell.paragraphs):
                    out[f"{cid}.p{pi}"] = p
                _walk_tables(cell.tables, f"{cid}.", out)


def index_blocks(document):
    """Map of id -> Paragraph or _Row, in document order."""
    out = {}
    pi = 0
    ti = 0
    body = document.element.body
    for child in body.iterchildren():
        if child.tag == qn("w:p"):
            out[f"p{pi}"] = Paragraph(child, document._body)
            pi += 1
        elif child.tag == qn("w:tbl"):
            table = Table(child, document._body)
            tmp = {}
            _walk_tables([table], "", tmp)
            for k, v in tmp.items():  # renumber t0 -> t<ti>
                out[f"t{ti}" + k[2:]] = v
            ti += 1
    return out


def _run_info(run):
    f = run.font
    return {
        "text": run.text,
        "bold": f.bold,
        "italic": f.italic,
        "size": f.size.pt if f.size else None,
        "font": f.name,
    }


def dump(path):
    d = docx.Document(path)
    blocks = []
    for bid, obj in index_blocks(d).items():
        if not isinstance(obj, Paragraph):
            continue
        item = {"id": bid, "style": obj.style.name if obj.style is not None else None, "text": obj.text}
        runs = [r for r in obj.runs if r.text]
        fmts = {json.dumps({k: v for k, v in _run_info(r).items() if k != "text"}) for r in runs}
        if len(runs) > 1 and len(fmts) > 1:  # mixed formatting: show runs so set_runs can be used
            item["runs"] = [dict(i=i, **_run_info(r)) for i, r in enumerate(obj.runs)]
        if obj.paragraph_format is not None and _has_hyperlink(obj):
            item["hyperlink"] = True
        blocks.append(item)
    unsupported = _unsupported_text_locations(d)
    return {"blocks": blocks, "not_editable": unsupported}


def _has_hyperlink(p):
    return p._p.find(qn("w:hyperlink")) is not None


def _unsupported_text_locations(d):
    notes = []
    if d.element.body.findall(".//" + qn("w:txbxContent")):
        notes.append("Document contains text boxes; their text is not listed and will not be edited.")
    for s in d.sections:
        for part, name in ((s.header, "header"), (s.footer, "footer")):
            if part is not None and any(p.text.strip() for p in part.paragraphs):
                notes.append(f"Section {name} has text (kept unchanged).")
    return sorted(set(notes))


# ---------------------------------------------------------------- editing

def _first_text_run(p):
    for r in p.runs:
        if r.text.strip():
            return r
    return p.runs[0] if p.runs else None


def _clear_runs(p, keep=None):
    for child in list(p._p):
        if child.tag in (qn("w:r"), qn("w:hyperlink"), qn("w:proofErr")):
            if keep is not None and child is keep._r:
                continue
            p._p.remove(child)


def set_text(p, text):
    keep = _first_text_run(p)
    if keep is None:
        p.add_run(text)
        return
    _clear_runs(p, keep=keep)
    keep.text = text  # python-docx converts \n to <w:br/> and \t to <w:tab/>


def set_runs(p, runs, source=None):
    source = source if source is not None else p
    originals = [copy.deepcopy(r._r) for r in source.runs]
    if not originals:
        sys.exit(f"set_runs: source paragraph has no runs to copy formatting from")
    _clear_runs(p)
    for spec in runs:
        idx = spec.get("like", 0)
        if not 0 <= idx < len(originals):
            sys.exit(f"set_runs: run index {idx} out of range (0..{len(originals) - 1})")
        new_r = copy.deepcopy(originals[idx])
        p._p.append(new_r)
        from docx.text.run import Run
        Run(new_r, p).text = spec["text"]


def apply(src, plan_path, out):
    d = docx.Document(src)
    blocks = index_blocks(d)
    with open(plan_path, encoding="utf-8") as fh:
        plan = json.load(fh)
    log = []
    for n, op in enumerate(plan, 1):
        kind = op.get("op")
        target = blocks.get(op.get("id"))
        if target is None:
            sys.exit(f"step {n}: unknown id {op.get('id')!r}")
        if kind == "set":
            set_text(target, op["text"])
        elif kind == "set_runs":
            set_runs(target, op["runs"])
        elif kind == "insert_after":
            like = blocks.get(op.get("like", op["id"]))
            if like is None:
                sys.exit(f"step {n}: unknown like {op.get('like')!r}")
            new_p = copy.deepcopy(like._p)
            target._p.addnext(new_p)
            para = Paragraph(new_p, target._parent)
            if "runs" in op:
                set_runs(para, op["runs"], source=like)
            else:
                set_text(para, op.get("text", ""))
            if op.get("new_id"):
                blocks[op["new_id"]] = para
        elif kind == "delete":
            target._p.getparent().remove(target._p)
        elif kind == "insert_row_after":
            like = blocks.get(op.get("like", op["id"]))
            new_tr = copy.deepcopy(like._tr)
            target._tr.addnext(new_tr)
            from docx.table import _Row
            row = _Row(new_tr, target._parent)
            cells = op.get("cells", [])
            seen, ci = set(), 0
            for cell in row.cells:
                if id(cell._tc) in seen:
                    continue
                seen.add(id(cell._tc))
                texts = cells[ci] if ci < len(cells) else [""]
                paras = cell.paragraphs
                for i, t in enumerate(texts):
                    if i < len(paras):
                        para = paras[i]
                    else:
                        np_ = copy.deepcopy(paras[-1]._p)
                        cell._tc.append(np_)
                        para = Paragraph(np_, cell)
                    if isinstance(t, dict):  # {"runs": [...]} keeps mixed formatting
                        set_runs(para, t["runs"])
                    else:
                        set_text(para, t)
                for extra in paras[len(texts):]:
                    extra._p.getparent().remove(extra._p)
                ci += 1
            if op.get("new_id"):
                blocks[op["new_id"]] = row
        elif kind == "delete_row":
            target._tr.getparent().remove(target._tr)
        else:
            sys.exit(f"step {n}: unknown op {kind!r}")
        log.append(f"{n}: {kind} {op.get('id')}")
    d.save(out)
    print(f"Saved {out} ({len(log)} edits)")


# ---------------------------------------------------------------- verification

def _canon(el):
    if el is None:
        return "-"
    el = copy.deepcopy(el)
    for e in el.iter():
        for a in list(e.attrib):
            if "rsid" in a:
                del e.attrib[a]
    from lxml import etree
    return hashlib.sha1(etree.tostring(el, method="c14n")).hexdigest()[:12]


def _fingerprints(d):
    para_fmt, run_fmt = set(), set()
    for p in d.element.body.iter(qn("w:p")):
        para_fmt.add(_canon(p.find(qn("w:pPr"))))
        for r in p.iter(qn("w:r")):
            run_fmt.add(_canon(r.find(qn("w:rPr"))))
    return para_fmt, run_fmt


def _part_hash(part):
    return hashlib.sha1(part.blob).hexdigest() if hasattr(part, "blob") else None


def verify(orig_path, new_path):
    a, b = docx.Document(orig_path), docx.Document(new_path)
    problems = []
    # styles, numbering, theme, fonts, headers/footers, images: must be byte-identical
    pa = {str(p.partname): p for p in a.part.package.iter_parts()}
    pb = {str(p.partname): p for p in b.part.package.iter_parts()}
    for name, part in pa.items():
        if name == "/word/document.xml" or name.startswith("/docProps/"):
            continue
        other = pb.get(name)
        if other is None:
            problems.append(f"missing part {name}")
        elif name.endswith(".xml") or "/media/" in name:
            if _part_hash(part) != _part_hash(other):
                problems.append(f"changed part {name}")
    for name in pb:
        if name not in pa:
            problems.append(f"new part {name}")
    # page setup
    for i, (sa, sb) in enumerate(zip(a.sections, b.sections)):
        for attr in ("page_width", "page_height", "left_margin", "right_margin",
                     "top_margin", "bottom_margin", "orientation"):
            if getattr(sa, attr) != getattr(sb, attr):
                problems.append(f"section {i}: {attr} changed")
    if len(a.sections) != len(b.sections):
        problems.append("number of sections changed")
    # every paragraph/run format in the new document must exist in the original
    pfa, rfa = _fingerprints(a)
    pfb, rfb = _fingerprints(b)
    if pfb - pfa:
        problems.append(f"{len(pfb - pfa)} new paragraph format(s) not present in original")
    if rfb - rfa:
        problems.append(f"{len(rfb - rfa)} new text format(s) not present in original")
    if problems:
        print("FORMAT CHECK: FAILED")
        for p in problems:
            print(" -", p)
        return 1
    print("FORMAT CHECK: OK – styles, fonts, sizes, page setup, headers/footers and images "
          "are identical to the original; all text uses formats from the original.")
    return 0


def text(path):
    d = docx.Document(path)
    for bid, obj in index_blocks(d).items():
        if isinstance(obj, Paragraph) and obj.text.strip():
            print(f"[{bid}] {obj.text}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cmd = sys.argv[1]
    if cmd == "dump":
        print(json.dumps(dump(sys.argv[2]), ensure_ascii=False, indent=1))
    elif cmd == "apply" and len(sys.argv) == 5:
        apply(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == "verify" and len(sys.argv) == 4:
        sys.exit(verify(sys.argv[2], sys.argv[3]))
    elif cmd == "text":
        text(sys.argv[2])
    else:
        sys.exit(__doc__)
