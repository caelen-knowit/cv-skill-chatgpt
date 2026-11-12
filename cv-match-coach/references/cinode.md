# Cinode CVs

The company keeps CVs in Cinode. The official layout is produced by Cinode's own templates. Two consequences:
1. A CV exported from Cinode (Word or PDF) is both **the CV and the template**: keep its sections, order and headings.
2. The best output is often **text to paste back into Cinode, field by field**, so Cinode's export keeps producing the official layout. A Word file from ChatGPT is a draft.

## 1. Recognising a Cinode export
Typical elements (exact headings depend on the company's Cinode template and language, so always use the headings actually in the uploaded file):
- Name, title/role, sometimes photo
- Presentation / profile text (*Presentation*, *Profil*, *Sammanfattning*)
- Key competences / highlighted skills, sometimes with levels (e.g. 1–5 or dots) and years
- Assignments (*Uppdrag*, *Projects*, *Assignments*): role, customer, period, description, technologies/skills
- Employments (*Anställningar*), Education (*Utbildning*), Courses and certifications (*Kurser och certifieringar*), Languages (*Språk*)

Notes:
- Skill levels shown as dots/bars/icons are often lost in text extraction. If levels matter, say they couldn't be read and ask; never guess a level.
- "Years of experience" figures printed next to skills in Cinode are the consultant's own entries. Show them as "stated in Cinode", separately from the proven months from assignments (experience-check.md). If they differ a lot, mention it as a question, not as an error.
- Assignment periods are usually month + year. Use them as-is.

## 2. Output command: `Cinode` / `Cinode format`
Give the improved or tailored content **per Cinode field**, in the order of the CV, so it can be pasted straight in. Only include fields that changed, and say so.

Format:

**Presentation** *(changed)*
```
<new text>
```

**Key competences** *(changed: order)*
Order: Java, Kafka, Spring Boot, Azure, ...
*(Reorder in Cinode by dragging, or by the highlight/key-competence setting.)*

**Assignment: <Role> – <Customer> – <period>** *(changed: description)*
```
<new description>
```
Technologies to add/remove in Cinode: + Testcontainers (source: user, chat Q3) · − none

**Assignment: <Role> – <Customer> – <period>** *(unchanged)*

Then the usual **Source check** and **Left out – not confirmed**.

Rules:
- Use code blocks for texts to paste (easy to copy, no formatting noise).
- Never suggest adding a skill or technology to Cinode unless it is in the CV or the user confirmed it in the chat.
- Mention "Use Cinode's export with your company template for the final CV."

## 3. Exporting from Cinode (tell the user if asked)
Open the consultant's CV in Cinode and use its export/download function, choosing the company's CV template and Word (.docx) if available, otherwise PDF. Word gives the most reliable text extraction. Menu names vary by Cinode version and company setup; if unsure, the user should ask their Cinode admin. Do not claim exact Cinode menu paths.
