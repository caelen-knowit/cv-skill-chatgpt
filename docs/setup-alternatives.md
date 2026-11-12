# Other ways to set it up

Use these only if uploading the zip (see the [README](../README.md)) doesn't work.

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
4. Check that the file list includes SKILL.md, 8 files in `references/` and the example files.

## C. Quick try without setup (nothing is saved)

New chat → attach all files from the unzipped skill plus a CV → paste:
```
Follow the attached SKILL.md exactly as your instructions for this whole chat, and use the attached reference files as it describes. Then match the attached CV to this assignment:

<paste the client request>
```
