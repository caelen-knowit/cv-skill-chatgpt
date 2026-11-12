# Other ways to set it up

Use these only if uploading the zip (see the [README](../README.md)) doesn't work.

## Can a prompt set everything up for me?

**Not from a normal chat.** A chat can't create a skill or a project. Only the *Create* buttons can. These two options come closest:

- **Skill: Create with chat + link** (option B). You click *Create with chat* once and paste a prompt with the link, and the skill builder does the rest. This is **untested**: it works only if the builder can open web links. If it can't, attach the file instead.
- **Project with a link in its instructions** (option A2). You create the project and paste one instruction, with no files to upload. It always uses the latest version from GitHub.

## Skill or Project?

**Use the skill.** A Project doesn't produce better answers: the model and the rules are the same. The difference is how the rules are delivered and kept up to date.

| | Skill (recommended) | Project |
|---|---|---|
| Setup for colleagues | None once it's shared | Each person or team creates or joins a project |
| Updates | Re-upload once, and everyone has the new version | A1: re-upload the file in each project. A2: automatic (link). |
| Works in | Any chat, including chats inside projects | Only chats inside that project |
| Rule-following | Instructions load as part of the skill, and files are read when needed | Depends on reading the file or link correctly each time |
| Exact-format Word files | Yes (script included) | Yes, but ChatGPT first recreates the script from the text |
| Privacy | Each chat stands alone | Chats in a project can share context, so CVs from different cases can mix |

**Where a Project is still useful:** as a folder for one large tender, holding the request, all candidate CVs and the chats about it. The skill works inside it as usual.

## A. ChatGPT Project (if Skills are not available)

1. Sidebar → **Projects** → **New project** → name it `CV Match Coach`.
2. Choose **A1 or A2**:

**A1 – file (most reliable):** upload [`cv-match-coach-all-in-one.md`](../cv-match-coach-all-in-one.md) to the project's files, and paste this into the project's **Instructions**:
```
You are CV Match Coach. The file cv-match-coach-all-in-one.md in this project's files is your complete instruction set. Read it at the start of every chat. Follow its SKILL.md part exactly, including all hard rules (no invented facts, ask when anything is unclear), and use its other parts as the reference files and scripts SKILL.md points to. Never copy facts from the example parts. Never use facts from CVs in other chats.
```

**A2 – link (nothing to upload, always the latest version):** needs web browsing in your workspace. Paste this into the project's **Instructions**:
```
You are CV Match Coach. At the start of every chat, open https://raw.githubusercontent.com/caelen-knowit/cv-skill-chatgpt/main/cv-match-coach-all-in-one.md and read the whole file; check that its last line starts with END-OF-CV-MATCH-COACH, otherwise tell me it could not be read completely. Follow its SKILL.md part exactly, including all hard rules (no invented facts, ask when anything is unclear), and use its other parts as the reference files and scripts SKILL.md points to. Never copy facts from the example parts. Never use facts from CVs in other chats.
```

3. Start every case as a **new chat inside the project**. Share the project with colleagues if your workspace allows it.

## B. Create the skill with chat (if the zip upload fails)

1. **Plugins → Skills → Create → Create with chat**.
2. Paste:
   ```
   Create a skill named "cv-match-coach" from https://raw.githubusercontent.com/caelen-knowit/cv-skill-chatgpt/main/cv-match-coach-all-in-one.md. The file contains several parts, each starting with "=== FILE: <path> ===". Create one skill file per part with exactly that path and exactly that content (for the .py part, the code inside the code block). Use the SKILL.md part as the skill's name, description and instructions without shortening or rephrasing it. Do not add instructions of your own. When done, list all files in the skill.
   ```
   If the builder can't open the link, download the file, attach it, and replace the link in the prompt with "the attached file".
3. Check the file list: `SKILL.md`, 10 files in `references/`, 2 in `examples/`, and `scripts/docx_inplace.py`.

## C. Quick try without setup

See "Try it without installing or downloading" in the [README](../README.md).
