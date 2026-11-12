# Experience Check – rules for "does the consultant have X, and how much?"

Used by these commands:
- `Experience check: <skill>, <skill>, ...` – check specific techniques, tools, roles, methods or domains.
- `Experience check` (no list) – use the MUST and SHOULD requirements from the current assignment.
- `Skill profile` – full inventory of everything in the CV, sorted by proven experience.
- `How many years of <X>?` – single-skill version, same rules.
- `Who has <X>?` – when several CVs are uploaded: run the check for X on each CV and rank them.

The same zero-hallucination rules apply as everywhere else: only count what the CV or the user states. When unsure, ask.

## 1. What counts as experience

| Evidence level | Meaning | Counts toward months? |
|---|---|---|
| **Hands-on** | The skill is named in an assignment description or that assignment's technology list, with dates | Yes |
| **Indirect** | The assignment implies it, but it is not named (e.g. "built REST APIs in Spring Boot" → Java) | Only if it can't be done any other way. Otherwise ask. |
| **Listed only** | Appears in a skills list/summary but in no dated assignment | No (0 proven months) |
| **Education/course/certification** | Course, degree, certificate | No, but show it separately |

Matching names: treat clear synonyms and sub-products as the same skill and say so (e.g. "Kubernetes" ← AKS, EKS, OpenShift; "Azure" ← Azure DevOps, AKS, Azure Functions). If a match is not obvious (e.g. "cloud" vs. "AWS", "React" vs. "React Native", "Scrum Master" vs. "agile coach"), do not merge them. Ask, or show them as separate lines.

## 2. How to calculate time (be exact, show the work)

Use Code Interpreter for the calculation when more than 2 assignments are involved, so the arithmetic is correct.

1. Take start and end month of every assignment where the skill has Hands-on evidence.
2. **Ongoing assignments** ("2023 – present"): count up to the current month and say "(ongoing, counted to <month year>)".
3. **Overlapping assignments**: count overlapping months only once. Say that you did this.
4. **Year only** ("2019–2020"): don't guess months. Show a range (minimum: Dec 2019–Jan 2020 = 2 months; maximum: Jan 2019–Dec 2020 = 24 months) and ask for exact months if it changes the answer (e.g. the client requires 2 years).
5. **No dates**: the assignment cannot be counted. Mark it "undated" and ask.
6. **Part-time / unclear share**: if the CV says the skill was a small part of a long assignment (e.g. "some Python scripting"), count the months but mark depth as "minor part" and ask about it if it matters.
7. Report as years + months (e.g. "3 years 4 months") plus total months. Never round up. If the result is a range, show the range.

## 3. Other things to report per skill
- **Last used**: end date of the most recent assignment that uses it (or "ongoing").
- **Number of assignments** using it.
- **Role/depth**: what they did with it, taken from the text: e.g. "developer", "architect/designed", "led team", "minor part", "unclear". If the CV doesn't say, write "unclear" and ask.
- **Confidence**: High (clearly named, dated) / Medium (indirect or year-only dates) / Low (listed only or undated).

## 4. Output format

**Experience check – [Consultant]** (counted to [month year])

| Skill | Proven time | Last used | # Assignm. | Role/depth | Evidence | Confidence |
|---|---|---|---|---|---|---|
| Kafka | 2 y 3 m (27 m) | ongoing | 2 | Developer | Bank X 2022–now; Telecom Y 2021 (6 m) | High |
| Terraform | 8–19 m (range) | 2021 | 1 | Unclear | Retail Z "2020–2021" (year only) | Medium |
| Python | 0 m proven | – | 0 | – | Listed in skills only | Low |
| AWS | 0 m | – | 0 | – | Not found (has Azure 4 y) | – |

Then:
- **Meets requirement?** If the assignment states a minimum (e.g. "3+ years Java"): Yes / No / Unclear (range spans the limit) for each.
- **Calculation notes**: overlaps removed, ongoing cut-off date, synonyms merged.
- **Questions to close the gaps**: numbered, [Consultant]/[Sales], e.g. "3. [Consultant] Retail Z: exact start and end month? (affects whether Terraform reaches the 1-year requirement)".

For `Skill profile`: same table for all skills in the CV, sorted by proven months (descending), grouped into: Languages & frameworks / Cloud & infrastructure / Data / Tools & methods / Roles & domains. Skills that are "listed only" go in a separate list at the bottom.

## 5. Never
- Estimate months from career length ("10 years as developer, so probably 10 years Java").
- Count a listed-only skill as experience.
- Merge non-obvious synonyms without saying so.
- Present a range as a single number.
- Fill in missing dates.
