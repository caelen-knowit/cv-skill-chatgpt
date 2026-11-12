# Getting started – 3 ways, pick one

A ChatGPT chat **cannot create a skill or project by itself** from a pasted prompt. You always click "Create" once. These paths keep it to a few clicks plus one paste.

| Path | Who | Time | Result |
|---|---|---|---|
| **1. Upload the skill** (recommended) | Owner/admin, Skills enabled in the workspace | 5 min | Shared skill for the whole team, works in any chat |
| **2. Create with chat** | Owner, if upload doesn't work | 10 min | Same as path 1 |
| **3. Project** (fallback) | Anyone, if Skills are not enabled | 5 min | Works for you and people you share the project with |
| **Try it now** | Anyone | 1 min | Test in a normal chat, nothing saved |

With Cinode no template is needed: the uploaded Cinode export is used as the template. Then follow `TEST-SCRIPT.md` for your first test.

---

## Path 1 – Upload the skill (recommended)

1. ChatGPT sidebar → **Plugins** → **Skills** tab → **Create** → **Upload from your computer**.
2. Select `cv-match-coach.zip` (or the `cv-match-coach` folder).
3. Open the skill → **•••** → **Share** → your sales group or the whole workspace.
4. Test: open a new chat, attach a CV, paste a client request and type:
   ```
   Match this CV to this assignment
   ```

*Menu names may differ slightly as OpenAI updates ChatGPT. If you can't see Skills, ask your ChatGPT admin to enable Skills for your role (Workspace settings → Permissions & roles).*

---

## Path 2 – Create with chat (paste prompt)

1. **Plugins** → **Skills** → **Create** → **Create with chat**.
2. Attach all files from `cv-match-coach/` (SKILL.md, everything in `references/`, `examples/`, and your template from `assets/`).
3. Paste this prompt:

```
Create a skill named "cv-match-coach" from the attached files.

- Use the attached SKILL.md exactly as the skill's name, description and instructions. Do not shorten, summarise or rephrase it.
- Add the attached files from references/ as reference files under references/, with unchanged file names and content.
- Add the example files under examples/ and the .docx template(s) under assets/.
- Do not add any instructions of your own.
When done, list the skill's files so I can check that all of them are included:
SKILL.md, references/cv-writing-guide.md, references/cv-quality-rubric.md, references/experience-check.md, references/file-handling.md, references/improve-cv.md, references/match-scoring-rubric.md, references/output-formats.md, references/cinode.md, examples/... (2 example files + README), assets/README.md
```

4. Check the file list it shows, then share as in path 1.

---

## Path 3 – ChatGPT Project (if Skills are not available)

1. Sidebar → **Projects** → **New project** → name it `CV Match Coach`.
2. **Project files**: upload SKILL.md, all files in `references/`, `examples/` and your template.
3. **Project instructions** (project settings → Instructions), paste:

```
You are CV Match Coach. The file SKILL.md in this project's files is your complete instruction set. Read it at the start of every chat and follow it exactly, including all hard rules (no invented facts, ask when anything is unclear). Read the reference files it points to (they are in this project's files without the references/ folder prefix) before each task. Never copy facts from the example files. Never use facts from CVs in other chats.
```

4. Share the project with colleagues (project → Share), if shared projects are enabled in your workspace.
5. Start each case as a **new chat inside the project**.

---

## Try it now (1 minute, no setup)

New chat → attach **SKILL.md + all files in references/** + the CV → paste:

```
Follow the attached SKILL.md exactly as your instructions for this whole chat, and use the attached reference files as it describes. Then: match the attached CV to this assignment:

<paste the client request here>
```

Good for a demo. For daily use, choose path 1 or 3.

---

## First 5 things to try
```
Match this CV to this assignment
Experience check: Java, Azure, team lead
Suggest changes
Improve CV: medium
Write the CV, light
```
See `COMMANDS.md` for everything else.
