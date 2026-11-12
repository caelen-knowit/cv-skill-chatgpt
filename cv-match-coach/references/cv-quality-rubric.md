# CV Quality Rubric and Example Library

Two uses:
1. `Grade this CV` – score any CV's quality (independent of a specific assignment).
2. `Prepare for library` – decide whether a CV can become an approved example in `examples/`, and anonymise it.

## 1. Quality scorecard (1–5 per criterion)

| # | Criterion | 5 = excellent | 1 = poor |
|---|---|---|---|
| 1 | **Accuracy & traceability** | Every claim specific and checkable; dates complete and consistent | Vague or contradictory claims, missing dates |
| 2 | **Specificity** | Concrete systems, team sizes, durations, scope, outcomes where known | Generic phrases, "worked with various technologies" |
| 3 | **Personal contribution** | Clear what *this person* did vs. the team | Only describes the project/team |
| 4 | **Relevance & prioritisation** | Recent/relevant work gets space; old work is short | Everything equal length; old work dominates |
| 5 | **Human tone** | Reads like a competent person; varied sentences; no buzzwords | Buzzwords, adjective stacking, AI patterns (see writing guide banned list) |
| 6 | **Readability & structure** | Easy to scan, follows template, consistent tense/person | Walls of text, inconsistent formatting |
| 7 | **Skills credibility** | Skills list backed by assignments; levels realistic | Long skill lists with no evidence |
| 8 | **Length** | Fits purpose (typically 2–4 pages) | Far too long or too thin |

**Output for `Grade this CV`:**
| Criterion | Score | Why (with a quote/example from the CV) | Fix |
|---|---|---|---|
Then: total average, the 3 most valuable fixes, and the verdict below. Each score must cite something concrete in the CV; do not give scores without evidence.

**Verdict:**
- **Library candidate**: average ≥ 4.3 and no criterion below 4.
- **Good**: average ≥ 3.5, no criterion below 3.
- **Needs work**: anything else.

## 2. Approval process for the example library (human decides, not the AI)

The skill never adds anything to its own examples. A CV becomes an example only through this process:

1. **Candidate** – a CV (often a tailored one) that scored "Library candidate" AND has a positive real-world signal: client shortlisted/interviewed the consultant, assignment won, or a sales lead considers it a model CV.
2. **Consent/GDPR** – the consultant agrees (or your DPO has approved the legal basis) that an anonymised version is used as an internal example.
3. **Anonymise** with `Prepare for library` (rules below), then a human checks the result line by line.
4. **Two-person review** – e.g. a sales lead + a consultant manager / practice lead. Both must agree it is exemplary for its role type.
5. **Annotate** – add a short header to the example: role type, language, why it is good (2–4 bullets), date approved, approved by (roles, not names).
6. **Add** to `examples/` and re-upload the skill (new version). Keep max ~2 per role type and language; replace older ones rather than accumulating.
7. **Review twice a year** – remove outdated examples (old tech, old template).

## 3. Anonymisation rules for `Prepare for library` (strict)
- Name → role label ("Consultant A"). Remove photo, birth year, personal ID, contact details, LinkedIn URL, home city if not needed.
- Client and employer names → industry description ("a large Nordic bank", "a public agency").
- Unique project/product names that identify a client → generic ("the customer's payment platform").
- Exact dates → keep years and duration only ("2022–2024, 2 years") to reduce identifiability.
- Rare combinations that identify the person (e.g. unusual certification + small town + niche domain) → generalise and flag to the reviewer.
- Keep the writing itself unchanged: the value of the example is the style and structure.
- End with a checklist of everything that was changed, so the human reviewer can verify.

## 4. Before/after pairs (very valuable)
When a tailored CV is clearly better than its original, the anonymised pair (original section → improved section) can be added as `examples/before-after-<role>.md`. Pairs teach "what good looks like" better than finished CVs alone.
