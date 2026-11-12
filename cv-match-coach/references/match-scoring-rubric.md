# Match Scoring Rubric

Use this to score how well a consultant's CV matches an assignment. Be consistent and honest. The score is a decision aid for sales, not a marketing number.

## 1. Classify each requirement
- **MUST** – stated as required, "krav", "ska-krav", "mandatory", "required", or obviously essential to do the job.
- **SHOULD** – "meriterande", "nice to have", "preferred", "plus", "bör-krav".
- **IMPLICIT** – not stated but possibly implied (e.g. senior role → stakeholder communication; Swedish client team → Swedish language). Max 3. Ask the user to confirm them before they affect the score; if unconfirmed, show them separately as ASSUMPTION and exclude them from the score.

If you cannot tell whether a requirement is MUST or SHOULD, ask the user. Do not decide yourself.

## 2. Rate the evidence for each requirement

| Rating | Meaning | Points (MUST) | Points (SHOULD/IMPLICIT) |
|---|---|---|---|
| Strong | Used it hands-on in a real assignment, recently (last ~3 years), for a meaningful period (6+ months), ideally more than once | 3 | 2 |
| Partial | Has done it but older, short, as a minor part, or adjacent tech (e.g. GCP when AWS required) | 2 | 1 |
| Weak | Only listed as a skill, course, or mentioned in passing; no real assignment evidence | 1 | 0.5 |
| Missing | No evidence at all | 0 | 0 |

When the requirement asks for "X years", count actual assignment time, not the career length. If dates are missing, overlapping or unclear, ask; do not estimate.

If the evidence is ambiguous (e.g. unclear whether the consultant personally did the work), rate it by what is proven (usually Weak or Partial), mark it **Unclear**, and add a question. Never round up.

## 3. Calculate the score
Score % = (points achieved / max possible points) × 100, rounded to nearest 5.

Then apply the **MUST rule**: if any MUST is "Missing", the verdict can be no better than "Weak match", regardless of score, unless the user says the requirement is negotiable.

## 4. Verdict

| Score | Verdict | Recommendation |
|---|---|---|
| 85–100 | Strong match | Go. Present with confidence. |
| 70–84 | Good match | Go. Address the gaps in profile text and pitch. |
| 50–69 | Partial match | Go only if few candidates or the gaps are trainable/negotiable. Prepare the consultant for gap questions. |
| <50 or a MUST missing | Weak match | No-go, unless the sales person has client info that changes the picture. Suggest what kind of profile would fit instead. |

## 5. Risks to always check
- **Recency**: key skill last used 5+ years ago.
- **Seniority mismatch**: over- or under-qualified relative to role and likely rate.
- **Role mismatch**: e.g. developer applying for architect role with no design ownership evidence.
- **Domain**: client industry (finance, public sector, health, telecom, industry/manufacturing) vs. consultant background.
- **Practical**: location/on-site demand, language, start date, security clearance, availability, part-time.
- **CV quality issues** that hurt the chances regardless of match: vague assignment descriptions, no dates, long lists of skills without evidence, typos, inconsistent language.

## 6. Questions for the consultant
For every Partial/Weak/Missing MUST, and for important unknowns, write one specific question the sales person can ask the consultant, e.g.:
- "Have you worked with Kafka outside Bank X? If yes, where and for how long?"
- "In the Telecom Y assignment, were you the one designing the API, or implementing it?"
These answers can turn a Partial into a Strong. Until answered, the rating stays at what is proven.

Good follow-up questions are:
- Specific (name the assignment, technology and period).
- Closed or short-answer where possible ("How many months?", "Were you the lead or a member?").
- Grouped: max ~8 questions at a time, most important first, numbered so the user can answer "1: yes, 2: 8 months ...".
- Labelled with who should answer: **[Sales]** (client/request questions) or **[Consultant]** (experience questions).
