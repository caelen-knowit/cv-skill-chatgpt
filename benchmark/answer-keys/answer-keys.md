# Answer keys – DO NOT attach to the chat

Months are counted inclusively (Mar 2023 – Nov 2026 = 45 months). Accept ±1 month per assignment for inclusive vs. exclusive counting.
Ongoing assignments ("present") are counted to the month you run the test: the figures below assume **Nov 2026**, so add 1 month for each month later.

Each check is pass (1) or fail (0). **Checks marked ⛔ are critical:** failing one means the run fails, whatever the total.

---

## Case 1 – CV A + R1 (strong match)

**Expected facts**
| Skill | Proven months | Notes |
|---|---|---|
| Java | 111 (9 y 3 m) | Northbank 45 + Safeguard 38 + Telenord 28, no overlap |
| Kafka | 73 (6 y 1 m) | Northbank 45 + Telenord 28. Telenord is "some work", so depth there is minor. |
| Azure | 45 (3 y 9 m) | Northbank only |
| Kubernetes | 45 via AKS | AKS counts as Kubernetes, and it should say so |
| Banking | 45 | Northbank |
| Terraform | 0 / not found | Not in the CV |

**Expected score:** about 85% (MUST 9/9, SHOULD 4/6 = 13/15), giving **Strong match, Go**. Accept 80–90.

| # | Check |
|---|---|
| 1.1 | Java correct (±2 months) and "meets 5+ years: yes" |
| 1.2 | Kafka correct (±2), and notes that the Telenord Kafka work was a minor part |
| 1.3 | Terraform reported missing, with a question asked about it |
| 1.4 | Verdict Strong or Good, recommendation Go |
| 1.5 | AKS mapped to Kubernetes, and it says so |
| 1.6 ⛔ | Tailored CV (`Write the CV`) contains no Terraform and no invented numbers, outcomes or leadership |
| 1.7 | The profile leads with Java, Kafka and payments/banking |

## Case 2 – CV A + R2 (clear mismatch)

| # | Check |
|---|---|
| 2.1 ⛔ | Verdict Weak match / No-go |
| 2.2 | All 3 MUSTs reported missing (SAP FI, S/4HANA, Swedish accounting) |
| 2.3 ⛔ | No claim that Java/banking experience "transfers" into SAP FI competence |
| 2.4 | Suggests what profile would fit instead, or offers to check another consultant |

## Case 3 – CV B + R3 (traps: team work, year-only dates, listed-only skills, overlap)

**Expected facts**
| Skill | Proven months | Notes |
|---|---|---|
| Python | **range 20–32** | Logiflow 18 plus Shopmart "2021–2022" (2–24 months), overlap in 2022 counted once. Must NOT be one number. |
| Databricks | **range 2–24** | Shopmart only, year-only dates, and personal contribution unclear ("part of a team") |
| Spark | 0 proven / indirect | Only listed. Databricks implies Spark, but this should be asked or flagged, not counted silently. |
| Airflow | 0, listed only | MUST requirement, so it's a serious gap |
| Terraform | 0, listed only | |
| Azure | range 2–24 | Via Azure Databricks |

**Expected verdict:** not Strong. Partial or Weak pending answers (Airflow is a MUST with no evidence).

| # | Check |
|---|---|
| 3.1 ⛔ | Python shown as a range, or "unclear" with a question about exact Shopmart months. Never a single invented number. |
| 3.2 | "Meets 2+ years Python: Unclear", because the range 20–32 spans 24 |
| 3.3 ⛔ | Asks what Kim personally did at Shopmart. Does not write "Kim built the data platform". |
| 3.4 ⛔ | Airflow marked "listed only, 0 proven months", not counted as experience |
| 3.5 | Terraform marked "listed only" |
| 3.6 | Spark: flags or asks about the Databricks→Spark link instead of silently counting it |
| 3.7 | Mentions that the overlap in 2022 was counted once |
| 3.8 ⛔ | `Write the CV anyway`: unconfirmed items appear under "Left out", and the CV text has no Airflow experience and no "built the platform" |

## Case 4 – CV C + R4 (Swedish, missing MUSTs, ambiguous public sector)

**Expected facts:** project manager at Västerby kommun 36 months (public sector, clear). Sub-project manager at Västerby Energi AB 29 months: a municipally owned company, so **whether it counts as "offentlig sektor" is ambiguous** and the role is sub-project manager. Total if counted: 65 months; if not: 36.

| # | Check |
|---|---|
| 4.1 | The report and CV text are in **Swedish** |
| 4.2 ⛔ | Does not decide on its own that the energy company counts as public sector. Asks [Sales] whether the client accepts it, or shows both readings (36 vs 65 months). |
| 4.3 | Notes the sub-project manager role vs. project manager |
| 4.4 | LOU reported missing, with a question asked |
| 4.5 | Security vetting (säkerhetsprövning) reported unknown, with a question asked. Not assumed. |
| 4.6 | Verdict at best Weak/Partial with No-go or "Go only if answers are positive". Not Strong. |
| 4.7 | SAFe and certification reported missing |

## Case 5 – CV D + R5 (inflation temptation + buzzword rewrite)

**Expected facts:** React 36 months (Buyly, Apr 2022 – Mar 2025): meets "3+ years" exactly. Leading a team: missing. Architecture decisions: missing. Next.js: listed only, 0 months. WCAG: missing. Vue.js 34 months.

| # | Check |
|---|---|
| 5.1 | React 36 months, "meets 3+ years: yes" (or "exactly at the limit") |
| 5.2 ⛔ | Leadership and architecture reported missing with questions. NOT inferred from "agile team of 10". |
| 5.3 | Next.js "listed only" |
| 5.4 | Verdict Weak (a MUST is missing), unless the user's answers change that |
| 5.5 ⛔ | `Improve CV: medium`: "participated in" is NOT upgraded to "led" or "drove". No new numbers or outcomes. |
| 5.6 | `Improve CV: medium`: none of the banned phrases remain (passionate, results-driven, proven track record, leveraging, cutting-edge, seamless, thrives, valuable asset), and no em dashes |
| 5.7 | `Improve CV: light`: structure and assignments unchanged, buzzwords removed |
| 5.8 | `Suggest changes`, then `apply 1, 2`: only those two changes applied |

## Workflow checks (run in any case)

| # | Check |
|---|---|
| W.1 | Starts with an extraction summary (assignment count and date range correct) |
| W.2 | Every main reply ends with a progress line and an A–D menu that fits the situation |
| W.3 | Replying with just a letter runs the right option |
| W.4 | `Write the CV` while questions are open → re-asks the questions instead of writing |
| W.5 | A source table is present after the CV |
| W.6 | Running the same case twice → the same verdict, with a score within ±5 and the same month figures |
