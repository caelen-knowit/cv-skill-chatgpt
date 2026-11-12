# File handling – reading CVs in any format

CVs arrive as Word, PDF, exports from CV systems, LinkedIn exports, scans and pasted text. Wrong extraction is a hidden source of hallucination (scrambled columns, missing table cells, OCR errors). So: extract carefully, then show the user what you read before analysing.

## 1. Supported formats and how to read them

Use code (Python) to extract text when possible. Reading the file "by eye" is a fallback.

| Format | How | Typical problems |
|---|---|---|
| .docx | python-docx: read paragraphs AND tables (CV-system exports such as Flowcase/Cinode often put assignments in tables), headers/footers, text boxes if needed | Content in tables or text boxes missed; skill levels shown as icons/dots are lost |
| .doc (old Word), .odt, .rtf | Convert to .docx or text (e.g. LibreOffice/pandoc if available), then read | Conversion may drop formatting; check dates |
| .pdf (text-based) | pdfplumber / pypdf; check layout | Two-column layouts get mixed (skills column mixed into assignment text); headers repeated per page |
| .pdf (scanned) / .jpg / .png / photo | No text layer. Use OCR if available, or read the image visually | Misread dates and numbers (2018 vs 2016, 6 vs 8), missing lines. LOW confidence. |
| .pptx (one-page CV slides) | python-pptx, read all text frames | Order of text boxes may be random |
| .txt / .md / pasted text | Read directly | Usually fine |
| .html / web profile export / LinkedIn PDF | Read text | LinkedIn: job titles and dates fine, descriptions often short or missing |
| Several files for one consultant (e.g. CV + skills matrix) | Read all, cross-check | Conflicting dates → ask |

If a format is unknown or can't be opened: say so and ask for .docx, .pdf or pasted text. Do not guess the content.

## 2. Extraction check (always, before any analysis)

After reading, show a short summary like this and ask the user to confirm or correct only if something looks wrong:

> **Read from `erik_cv.pdf`** (text-based PDF, 4 pages)
> - Name: Erik L. · Title: Senior Backend Developer · Language: Swedish
> - 11 assignments, 2012 – present (most recent: Bank X, 2022 – present)
> - Skills section: 34 skills · Education: 1 · Certifications: 2 · Languages: 2
> - ⚠️ Could not read: page 3 assignment table, column "Technologies" partially garbled (Telecom Y, 2019–2020)
> - ⚠️ Uncertain: Retail Z dates "2016–2O18" (OCR), please confirm
>
> Continue with the match, or correct anything first?

Rules:
- If there are ⚠️ items that affect the requested task, ask about them before continuing. Do not quietly use uncertain text.
- If everything was read cleanly, keep the summary to 3 lines and continue in the same reply (do not wait for confirmation).
- For scans/images: always state "scanned – dates and numbers may be misread" and ask the user to confirm the key dates/numbers you rely on.
- Never fill in a cell, date or technology that could not be read.

## 3. Client request formats
Requests come as email text, PDF/Word tender documents (often public-sector "förfrågningsunderlag" with "ska-krav"/"bör-krav"), or broker portal text. Same rules: extract, list what you found (number of must/should requirements), flag unreadable parts. For long tender documents, ask which section/role applies if there are several.

## 4. Output files
Follow `docx-output.md`: the Word file is the uploaded .docx edited in place, so it keeps the exact format. PDF/scan input can't be returned in its exact format, so ask for the Word version.
