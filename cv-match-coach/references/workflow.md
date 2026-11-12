# Guided workflow – next steps after every reply

Users should never have to remember commands. Every substantial reply ends with a **progress line** and a **next-step menu**. The user answers with a single letter (or types anything else freely).

## 1. Format (always at the very end of the reply)

```
---
**Progress:** ✓ CV read → ✓ Match → ◻ Questions → ◻ CV → ◻ Cinode/Word
**Next – reply with a letter:**
**A** – Answer the questions above (e.g. "1: yes, 18 months. 2: he led it")
**B** – Experience check on the requirements
**C** – Suggest changes to the CV
**D** – Something else (type freely)

💡 **My suggestion: A**, because 3 open questions affect the score (Kafka depth, Terraform, start date).
```

Rules:
- **Letters A–D** for next steps. Never numbers: numbers are used for questions ("1: yes").
- **2–4 options**, the most likely useful one as **A**. The last option is always "Something else" or "Done".
- Options must fit the current state (see section 2). Don't offer things that are already done unless redoing makes sense.
- When the user replies with only a letter (also lowercase, "a", "A.", "alt A", "B please"), run that option. If the letter is ambiguous because the menu is far back in the chat, repeat the menu and ask.
- If the user replies with question answers or free text instead, handle that; the menu is a shortcut, not a requirement.
- Write the menu in the user's chat language (Swedish: "**Nästa steg – svara med en bokstav:**", "Något annat (skriv fritt)").
- Short replies (a one-line clarification, a single question) can skip the menu.
- After the menu, add **one line "💡 My suggestion: <letter>, because <concrete reason from this case>"**. The reason must refer to this case (open questions, a gap, a weak section), not be generic.

## 1b. Heads-up (proactive observations)
When you notice something the user didn't ask about but should know, add at most 2 short **⚠️ Heads-up** lines before the menu. Only when it is concrete and useful, for example:
- "The CV's most recent assignment ended 14 months ago. Is the CV up to date in Cinode?"
- "Kafka is listed with 8 years in Cinode, but the assignments prove 3 years. The client may ask about it."
- "The request asks for security vetting. Check availability and citizenship requirements early."
- "Two assignments have no technologies listed, which weakens the experience check."
- "This CV mentions a health condition. I've ignored it and suggest removing it from the CV."
Never invent problems to fill the space. No heads-up is better than a weak one.
- The progress line shows the main track only. Use ✓ for done, ◻ for not done, and ◐ for "done but with open questions".

## 2. States and their default menus

| State (what just happened) | A | B | C | D |
|---|---|---|---|---|
| **Start** – user said hi / asked what you can do / no files yet | Match a CV to a client request (attach both) | Improve a CV without a request | Check experience in a CV | Compare several CVs for one request |
| **CV read, no request** | Improve CV (I'll ask: light, medium or heavy) | Suggest changes | Experience check / Skill profile | Add a client request to match against |
| **Request read, no CV** | Attach the CV | Analyse the request only (requirements, questions to the client) | – | Something else |
| **Match report delivered, questions open** | Answer the questions | Experience check on the requirements | Write the CV anyway (unconfirmed items left out) | Quick pitch / Something else |
| **Questions answered** | Write the tailored CV (medium) | Suggest changes instead (you pick) | Write the CV light / heavy | Something else |
| **Change list delivered** | Apply all High | Apply all | Pick specific changes ("apply 1, 3") | Write a full improved CV instead |
| **CV / improved CV delivered** | Word file in the same format as the original (if a .docx was uploaded), otherwise Cinode texts | Cinode texts (update the master CV) | Pitch email to the client | Lighter / Heavier / Show diff |
| **Cinode / Word delivered** | Pitch email to the client | Interview prep for the consultant | Anonymised version | Done |
| **Experience check delivered** | Match against a request | Answer the open questions | Improve the CV | Something else |
| **Compare delivered** | Full match for the top candidate | Experience check across all CVs on a skill | Pitch for the top candidate | Something else |
| **Weak match / No-go** | See what kind of profile would fit instead | Check another consultant (attach CV) | Write the CV anyway | Done |
| **Done** | Start a new case (open a new chat for the next consultant) | – | – | – |

Adapt the wording to the case (use the consultant's name and the actual skills/role), but keep the structure.

## 3. Start menu

When the skill is triggered without enough input (e.g. "hi", "what can you do?", "help", "hjälp"), reply with 2–3 lines and the Start menu:

> I help you match a consultant's CV to a client request and improve the CV, without inventing anything.
> Attach the CV (a Cinode Word export works best) and paste the request, or choose:
>
> **A** – Match a CV to a client request
> **B** – Improve a CV (no request needed)
> **C** – Check experience in a CV ("how many years of X?")
> **D** – Compare several CVs for one request

## 4. Privacy reminder at "Done"
When the user picks Done or starts a new case, remind them in one line: "Start a new chat for the next consultant so CVs don't mix."
