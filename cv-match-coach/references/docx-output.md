# Word output that keeps the original's exact format

Goal: the delivered CV looks exactly like the uploaded one, with the same fonts, sizes, colours, spacing, margins, header/footer, logo and table layout. Only the text changes.

**Rule: never build a new document. Always edit a copy of the uploaded .docx in place with `scripts/docx_inplace.py`.** Do not use python-docx's `add_paragraph`, `add_heading` or style changes directly, and do not create documents from scratch, when the user uploaded a .docx.

## 1. Which input allows exact format

| Uploaded CV | Exact format possible? | What to do |
|---|---|---|
| .docx (e.g. Cinode Word export) | **Yes** | Edit in place (section 2) |
| .doc / .odt / .rtf | Usually | Convert to .docx with LibreOffice if available, then edit in place. Tell the user to check the result once. |
| .pdf, scan, image | **No.** A PDF can't be edited back into its original layout reliably. | Ask: *"For the exact same format I need the Word version (Cinode: export as Word). Can you upload it? Otherwise I can give you the texts for Cinode, or a draft in a simple layout."* Never claim a rebuilt document has the original format. |

## 2. Procedure (use code execution)

If the script file is not available as a file (e.g. the skill was loaded from the all-in-one text), first write its code from the `scripts/docx_inplace.py` part to a file, unchanged.

1. **Copy, don't overwrite:** work on the uploaded file; the output is a new file.
2. **Dump the structure:**
   `python docx_inplace.py dump original.docx > structure.json`
   This gives every paragraph and table cell with an id, its style, text, and runs where formatting is mixed (e.g. bold "Technologies:" plus normal text). Note `not_editable` (text boxes, headers) and tell the user if CV content sits there.
3. **Write the plan** (`plan.json`) mapping the approved new CV text onto the ids:
   - Changed text → `set` (keeps the paragraph's formatting).
   - Mixed formatting (label + value, bold role + normal client) → `set_runs`, reusing the run indices from the dump.
   - Longer description → split into the same number of paragraphs as before where possible. Extra paragraphs → `insert_after` with `like` = an existing paragraph of the **same kind** (an assignment description paragraph, not a heading).
   - Removed content → `delete` (paragraphs) or `delete_row` (table rows). Grouping old assignments: keep one row/paragraph, `set` its text, delete the rest.
   - New assignment in a table layout → `insert_row_after` with `like` = an existing assignment row; use `{"runs": [...]}` for mixed-format cell lines.
   - Headings, the name and the template's fixed labels are not changed unless the user asked (e.g. language switch).
4. **Apply:** `python docx_inplace.py apply original.docx plan.json <output>.docx`
5. **Verify (mandatory):** `python docx_inplace.py verify original.docx <output>.docx`
   - `FORMAT CHECK: OK` → continue.
   - `FAILED` → fix the plan (usually wrong `like` or a missing `set_runs`) and redo from step 4. **Never deliver a file that fails the check.**
6. **Read back:** `python docx_inplace.py text <output>.docx` and compare against the approved CV text: is everything there, nothing duplicated, no old text left behind, and nothing extra?
7. **Deliver** the file, named `<Initials>_<Role>_<Client or "tailored">_<YYYY-MM-DD>.docx`, with one line: "Same format as your original (format check passed). Page count: before X, after Y, if it changed."

## 3. Length and page breaks
Formatting stays identical, but more or less text can move page breaks. If the result is longer than the original or a limit, say so and offer `Shorter`. Don't change font sizes or margins to make it fit.

## 4. PDF output
- Best: the user opens the .docx in Word and chooses *Save as PDF*, or exports from Cinode. That uses their installed company fonts.
- If the user wants the PDF from here: convert with LibreOffice if available, but warn: *"Company fonts may not be installed in my environment, so the PDF can use a substitute font. For the exact look, save as PDF from Word."*

## 5. Cinode
For CVs living in Cinode, the official layout comes from Cinode. Offer both: the Word file in exact format (for sending now), and the `Cinode` field-by-field texts (to update the master CV).
