# Benchmark

A fixed test set with 4 fictional CVs, 5 client requests and an answer key. Run it **every time you change the skill**, and once with plain ChatGPT as a baseline. Then you can see whether a change made things better or worse.

All people and companies are fictional, so this is safe in a public repo.

## How to run (≈1 hour)

1. For each case, open a **new chat**. Attach the CV file from `cases/` and paste the matching request from `cases/requests.md`.
   **Never attach anything from `answer-keys/`.**

   | Case | CV | Request | Then also run |
   |---|---|---|---|
   | 1 | cv-A | R1 | `Experience check: Java, Kafka, Azure, Terraform` → `Write the CV` |
   | 2 | cv-A | R2 | – |
   | 3 | cv-B | R3 | `Experience check` → `Write the CV` → `write it anyway` |
   | 4 | cv-C | R4 | (type in Swedish: `Matcha CV:t mot uppdraget`) |
   | 5 | cv-D | R5 | `Improve CV: medium` → new chat: `Improve CV: light` → `Suggest changes` → `apply 1, 2` |

   Start each case with: `Match this CV to this assignment`. When the skill asks questions, reply `skip` unless the step says otherwise. The test checks what it does *without* extra information.
2. Score each check in `answer-keys/answer-keys.md` as 1 (pass) or 0 (fail).
3. Run **case 1 and case 3 a second time** for the consistency check (W.6).
4. Add a row to `results.md`.

## Pass criteria for a release
- **All ⛔ critical checks pass.** One failure means: don't release, fix it first.
- Total score is equal to or higher than the last release.
- Consistency check (W.6) passes.

## Baseline: plain ChatGPT
Run the same cases once in a chat **without** the skill, using a typical prompt:
```
Match this CV to this role. Tell me how well it fits, the gaps, how many years of experience the person has for each requirement, and then write an improved version of the CV tailored to the role.
```
Score it with the same answer key and record it as "baseline" in `results.md`. The difference between the two totals is the skill's measurable value.

## When a check fails
1. Copy the exact output into an issue (or a note).
2. Fix the relevant rule in `cv-match-coach/references/` (or SKILL.md).
3. Run `./build.sh`, re-upload, and re-run the whole benchmark, not just the failed case, because rule changes can break other things.

## Extending
- Add a case when you find a new failure in real use. Fictionalise it and add an answer key with ⛔ for anything that would cause a factual error.
- Optional: export a CV to PDF, or print and scan it, to test file reading.
- Later, for developers: the skill follows the open agent-skills standard, so the benchmark can be automated through the OpenAI API, with the answer keys checked by script or by a second model. That's only worth it once you change the skill often.
