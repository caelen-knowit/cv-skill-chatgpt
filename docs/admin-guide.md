# Admin guide – CV Match Coach

For the skill's owner and admin. Users only need the [README](../README.md) and the [command list](commands.md).

## 1. Why a skill (and not a Custom GPT)

OpenAI is retiring Custom GPTs and moving them to **Plugins and Skills**. On Enterprise, creating new GPTs ended around 26 Oct 2026, and existing GPTs stop working on 11 Dec 2026. A **skill** is a folder with a `SKILL.md` (instructions) plus reference files. It follows the open agent-skills standard.

| Option | Use for | Verdict |
|---|---|---|
| **Skill** (Plugins → Skills) | One shared, versioned tool for the whole team. Works in any chat. | **Recommended** |
| **Workspace agent** | A named "CV Match Coach" entry in the agent directory that uses the skill. Optional. Agents may use credit-based pricing, so check with your admin. | Optional, later |
| **Project** | Big tenders: one project per tender with the request, all candidate CVs and the chats. Also the fallback if Skills are disabled. | Use alongside the skill |
| Custom GPT | – | Being retired |

ChatGPT menus and limits change often. Check names and settings against your workspace and OpenAI's help center.

## 2. What's in this folder

```
cv-agent/
├── README.md                 ← start here (users)
├── docs/                     ← commands (EN/SV), test script, admin guide, setup alternatives
├── cv-match-coach.zip        ← ready-to-upload skill (rebuild after changes)
└── cv-match-coach/           ← THE SKILL
    ├── SKILL.md              ← instructions: hard rules, workflow, commands
    ├── references/
    │   ├── workflow.md             ← progress line + A–D next-step menus
    │   ├── file-handling.md        ← reading docx/pdf/scans/exports + extraction check
    │   ├── match-scoring-rubric.md ← how matches are scored
    │   ├── experience-check.md     ← months per skill, overlaps, ranges
    │   ├── improve-cv.md           ← suggest changes + light/medium/heavy rewrites
    │   ├── cv-writing-guide.md     ← human tone, banned phrases, section rules
    │   ├── cv-quality-rubric.md    ← grading CVs + example-library approval process
    │   ├── output-formats.md       ← fixed layouts for all outputs
    │   └── cinode.md               ← Cinode exports + field-by-field paste-back output
    ├── examples/             ← approved example CVs (style only), English and Swedish fictional starters
    └── assets/               ← optional CV template(s) (.docx)
```

## 3. Setup (Enterprise)

**Admin, one time:**
1. Workspace settings → Permissions & roles: make sure **Skills** are enabled, and decide which roles may create and share skills (for example, only the owner creates, and the sales group may use).
2. Confirm your data settings with IT/DPO. On Enterprise, OpenAI does not train on your business data by default. Check retention settings, since CVs are personal data under GDPR.
3. Optional: decide whether **memory** should be off for this use case. CV details should not end up in users' memory, and the skill tells ChatGPT not to save them.

**Owner (for example a sales lead):**
1. Optional: put a template in `cv-match-coach/assets/`. **This isn't needed with Cinode.** The uploaded Cinode export is used as the template automatically, keeping its sections, order and headings, and the final layout comes from Cinode's own export.
2. Rebuild the zip from the `cv-agent` folder:
   ```bash
   rm -f cv-match-coach.zip && zip -r cv-match-coach.zip cv-match-coach -x "*.DS_Store"
   ```
   Without a terminal: right-click the `cv-match-coach` folder → *Compress* (Mac) or *Send to → Compressed folder* (Windows).
3. Upload the zip via **Plugins → Skills → Create → Upload from your computer** (see the README).
4. Run [the test script](test-script.md) on your own CV first, then the **test plan** (section 7) with more cases.
5. **Share** the skill with the sales group, and post [commands.md](commands.md) / [kommandon.md](kommandon.md) on Teams or the intranet.

**Optional workspace agent:** create an agent called "CV Match Coach", add the `cv-match-coach` skill, and use these instructions:
`Use the cv-match-coach skill for every request. Follow it exactly.` Share it with chat-only access.

## 4. Supported CV formats

| Format | Notes |
|---|---|
| .docx | Best. Tables are read too (common in CV-system exports such as Flowcase/Cinode). |
| .pdf (text) | Good. Two-column layouts are checked for mixed-up text. |
| .pdf scanned / .jpg / .png / photo | Works, but with **low confidence**. The skill asks you to confirm key dates and numbers. |
| .doc, .odt, .rtf | Converted first. Dates are re-checked. |
| .pptx (one-page CV), .txt, .html, LinkedIn PDF, pasted text | Supported |
| Several files per consultant | Read together and cross-checked. Conflicts are asked about. |

The skill always starts with an **extraction check**: a short summary of what it read (number of assignments, date range, anything it couldn't read). That way reading errors are caught before the analysis starts.

Output: **`Cinode`** gives the changed texts field by field, ready to paste back into Cinode (recommended, because it keeps the official layout). There's also a **Word file** that reuses the uploaded .docx, or a **PDF**.

**Cinode export:** open the CV in Cinode and use its export/download with your company template, preferably as Word (.docx). Menu names vary, so ask your Cinode admin if you can't find it.

**Languages:** Swedish and English. CV text stays in the CV's language unless you ask otherwise. Commands work in both languages (see [kommandon.md](kommandon.md)).

## 5. How users work with it

1. New chat. Attach the CV and paste the client request. Type `Match this CV to this assignment`.
2. Check the extraction summary, then read the match report.
3. Answer the numbered questions (`1: yes, 18 months. 2: he led it`).
4. Choose one:
   - `Suggest changes` → accept or reject per item (`apply 1, 3, 5`, `apply all High`)
   - `Write the CV` (medium rewrite), or `Write the CV, light` / `heavy`
   - `Improve CV: light | medium | heavy` (works without a client request too)
5. Check the **source table**, then use `Word file` / `PDF file` / `Pitch`.
6. A person always reads the result before it's sent.

| Level | Changes | Use when |
|---|---|---|
| **Light** | Language, consistency, buzzwords. Keeps about 90% of the wording and the structure. | The consultant wants to keep "their" CV |
| **Medium** | + new profile, reordered skills, assignments rewritten as context → contribution → technologies → outcome, old work shortened | Default for tailoring |
| **Heavy** | + full rewrite in house style, old assignments grouped, skills trimmed to evidenced ones | A weak original, an important bid, or moving a CV into your template |

No level adds facts. Heavier levels usually raise more questions.

## 6. Does it learn from the CVs we upload?

**Not automatically, and that's good.** ChatGPT Enterprise doesn't train models on your data, and the skill doesn't change itself based on chats. That's the right setup for personal data and for consistency.
The skill improves only when **you curate its example library**:

1. **Start now without real examples.** The skill includes a fictional example and detailed writing rules, which is enough to get going.
2. **Find good candidates.** `Grade this CV` scores any CV on 8 criteria (accuracy, specificity, personal contribution, relevance, human tone, readability, how credible the skills list is, length). Each score has to cite evidence from the CV. "Library candidate" means an average of at least 4.3 and no criterion below 4.
3. **Check it against real results.** Score alone isn't enough. A candidate also needs a positive outcome: the client shortlisted or interviewed the consultant, the deal was won, or a sales lead calls it a model CV.
4. **Consent and anonymisation.** `Prepare for library` anonymises strictly: names, clients, unique project names, exact dates, and rare combinations that could identify someone. A human checks it line by line. The consultant agrees, or your DPO approves the legal basis.
5. **Two-person approval.** For example, a sales lead plus a practice lead. A short note says why the example is good.
6. **Add it to `examples/`, rebuild the zip, and re-upload.** ⚠️ If the GitHub repo is public, do this in a private copy (a company drive or private fork). Never commit real CVs, even anonymised ones, to the public repo. Keep at most about 2 examples per role type and language, and replace old ones rather than piling them up. Before/after pairs are especially useful.
7. **Measure.** Keep a simple log (Excel/SharePoint) with date, role, match score, rewrite level, and outcome (shortlisted / interview / won / lost). Once a quarter, check what works and update the rules and examples.

The details are in `references/cv-quality-rubric.md`. Examples are used **for style only**. The skill is told never to copy facts from them.

## 7. Test plan before rollout

| Test | Expected |
|---|---|
| Strong match | Score 80+, Go |
| Obvious mismatch (e.g. frontend dev for an SAP role) | Weak match, No-go, missing MUST flagged |
| A requirement not in the CV | Gap flagged, question asked, nothing invented |
| "Part of a team that built X" | Asks what the consultant personally did |
| Overlapping or missing dates | Asks. Does not calculate years on its own. |
| `Write the CV` without answering questions | Asks again. After "write it anyway", unconfirmed items are left out. |
| Scanned PDF / photo of a CV | Low-confidence warning, asks to confirm key dates |
| Two-column PDF and a Flowcase/Cinode .docx export | Extraction summary correct (count the assignments yourself) |
| `Experience check` with overlapping assignments | Overlap counted once. Check the months by hand once. |
| Skill only in the skills list | "Listed only", 0 proven months |
| Year-only dates | A range plus a question, not a single number |
| `Suggest changes` then `apply 1, 3` | Only changes 1 and 3 applied |
| `Improve CV: light` vs `heavy` on the same CV | Light keeps the structure and most wording. Heavy restructures. Neither adds facts. |
| Source table | Every claim maps to the CV or the chat. Spot-check 5. |
| Swedish CV | Swedish output |
| Any rewritten text | No banned phrases, no em dashes, no facts copied from `examples/` |

If something is off, add a concrete rule or example to the relevant reference file. Examples fix behaviour faster than more rules.

## 8. Maintenance

- **One owner** edits the skill. Keep the source files in a shared folder (SharePoint/Git), rebuild the zip and re-upload after each change.
- Collect bad outputs in a Teams channel. Once a month, update the banned-phrases list and examples.
- When the CV template changes, replace the file in `assets/` and re-upload.
- Twice a year, review `examples/` and remove outdated ones.
