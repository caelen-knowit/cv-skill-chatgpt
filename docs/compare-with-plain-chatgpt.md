# Is the skill better than plain ChatGPT? – a 1–2 hour test

Run the same cases twice: once in plain ChatGPT, once with the skill. Score both blind against an answer key you write **before** you look at any output.

## 1. Prepare 5 cases (30 min)

Use CVs you know well. Your own CV is the best start, because you know every true fact. Mix:

| Case | Why |
|---|---|
| Your CV + a request that fits | Normal case |
| Your CV + a request that does **not** fit | Does it admit a weak match? |
| A CV with a trap: "part of a team that built X", year-only dates, or a skill only in the skills list | Does it guess or ask? |
| A CV + a request with a MUST the CV lacks | Does it flag the gap or talk around it? |
| A scanned PDF or a two-column PDF | Does it read correctly? |

**Answer key:** for each case, write down *before running anything*:
- the true months of experience for 3 skills
- the real gaps (MUSTs the consultant doesn't meet)
- your honest verdict: fits, partly fits, or doesn't fit
- what the traps are, and what a good assistant should ask about them

## 2. Run both versions (30 min)

- **A – plain ChatGPT:** a new chat with no skill. If your workspace has a temporary chat option, use it so memory doesn't affect the result. Attach the CV and request, and paste the kind of prompt people would actually write:
  ```
  Match this CV to this role. Tell me how well it fits and the gaps, how many years of <skill 1>, <skill 2> and <skill 3> the person has, and then write an improved version of the CV tailored to the role.
  ```
- **B – the skill:** a new chat. Attach the same files and type `Match this CV to this assignment`, then `Experience check: <the same 3 skills>`, then `Write the CV`. Answer its questions the way you truly would.

**Blind:** ask a colleague to paste both outputs into a document labelled **X** and **Y** in random order. You score them without knowing which is which.

## 3. Score each output (30 min)

| # | Criterion | How to score | X | Y |
|---|---|---|---|---|
| 1 | **Invented or inflated facts** | Count every claim in the analysis and the CV that isn't in the source, or is upgraded ("took part" → "led", an added technology, a made-up number) | | |
| 2 | **Experience accuracy** | For the 3 skills: months off from your answer key (sum of differences) | | |
| 3 | **Gaps found** | Real gaps found out of the total in the answer key | | |
| 4 | **False strengths** | Strengths claimed without real evidence | | |
| 5 | **Traps handled** | Asked about or flagged the trap (1) or guessed (0) | | |
| 6 | **Honest verdict** | Matches your verdict? (yes/no) | | |
| 7 | **Would I send this CV?** | 1–5 | | |
| 8 | **Sounds human** | 1–5, plus a count of buzzwords | | |
| 9 | **Fits Cinode/template** | 1–5 | | |
| 10 | **Minutes to a sendable result** | Including your own edits and fact-checking | | |

**Consistency check:** run one case **twice** in each version. Do the score, verdict and experience numbers stay the same?

## 4. Decide

- **Criterion 1 matters most.** A single invented fact in a client CV costs more than any amount of nicer wording. If the skill has fewer invented facts and no worse results elsewhere, it's better.
- **Also weigh** experience accuracy, traps handled and minutes to a sendable result. Those are the daily value.
- **If plain ChatGPT ties**, the skill still gives you the same process, format and rules for the whole team, plus Cinode output. If that isn't worth it to you, use plain ChatGPT and keep a few good prompts. That's a fine outcome, and you'll have the data to back it.
- **If the skill loses on something**, copy the outputs and fix that specific rule. That's the test doing its job.

## 5. Over time: real results
Keep a simple log of date, consultant role, tool (skill or plain), rewrite level, and outcome (shortlisted, interview, won, lost). After 2–3 months, compare interview and win rates. That's the real proof, but it needs volume, so start with the 5-case test above.
