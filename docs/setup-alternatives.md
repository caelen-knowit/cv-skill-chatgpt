# Other ways to set it up

Use these only if uploading the zip (see the [README](../README.md)) doesn't work.

## Skill or Project?

**Use the skill.** A Project doesn't produce better answers: the model and the rules are the same. The difference is how the rules are delivered and kept up to date.

| | Skill (recommended) | Project |
|---|---|---|
| Setup for colleagues | None once it's shared | Each person or team copies the files and instructions |
| Updates | Re-upload once, and everyone has the new version | Every project copy must be updated by hand, so versions drift |
| Works in | Any chat, including chats inside projects | Only chats inside that project |
| Rule-following | Instructions load as part of the skill, and reference files are read when needed | Files are retrieved by search, so a rule can be missed more easily |
| Privacy | Each chat stands alone | Chats in a project can share context, so CVs from different cases can mix |

**Where a Project is still useful:** as a folder for one large tender, holding the request, all candidate CVs and the chats about it, possibly shared with colleagues working on the same bid. The skill works inside it as usual, so you don't need to copy any instructions into the project.

## A. ChatGPT Project (if Skills are not available)

1. Sidebar → **Projects** → **New project** → name it `CV Match Coach`.
2. Unzip `cv-match-coach.zip` and upload **all `.md` files** from it to the project's files.
3. In the project's **Instructions**, paste:
   ```
   You are CV Match Coach. The file SKILL.md in this project's files is your complete instruction set. Read it at the start of every chat and follow it exactly, including all hard rules (no invented facts, ask when anything is unclear). Read the reference files it points to before each task (they are in this project's files without folder prefixes). Never copy facts from the example files. Never use facts from CVs in other chats.
   ```
4. Start every case as a **new chat inside the project**. Share the project with colleagues if your workspace allows it.

## B. Create with chat (if the zip upload fails)

1. **Plugins → Skills → Create → Create with chat**.
2. Unzip `cv-match-coach.zip` and attach all files from it.
3. Paste:
   ```
   Create a skill named "cv-match-coach" from the attached files. Use SKILL.md exactly as the skill's name, description and instructions, without shortening or rephrasing it. Add the other files with unchanged names and content, in the folders SKILL.md refers to (references/, examples/, assets/). Do not add instructions of your own. When done, list all files in the skill.
   ```
4. Check that the file list includes SKILL.md, 9 files in `references/` and the example files.

## C. Quick try without setup (nothing is saved)

New chat → attach `cv-match-coach.zip` and a CV → paste:
```
Unzip the attached cv-match-coach.zip, read SKILL.md and follow it exactly as your instructions for this whole chat, using its reference files. Then match the attached CV to this assignment:

<paste the client request>
```
If ChatGPT can't open the zip, unzip it yourself and attach the files instead.
