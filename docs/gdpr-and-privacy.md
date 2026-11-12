# GDPR and privacy checklist – CV Match Coach in ChatGPT Enterprise

> This is a practical checklist, **not legal advice**. Approval comes from your **DPO / legal team** and IT security. Use this page as the agenda for that meeting.

CVs are personal data. Using AI to assess and rewrite them is new processing of that data, so it needs to be documented and approved before you use real CVs from colleagues.

## 1. Contract and platform (IT / procurement)

| # | Check | Notes |
|---|---|---|
| 1.1 | **The OpenAI Data Processing Addendum (DPA)** covers your ChatGPT Enterprise workspace | Third-party guides say OpenAI Ireland Ltd. is the contracting party for EU customers. Confirm in your own contract. |
| 1.2 | **Sub-processors and transfers** reviewed (SCCs / EU–US Data Privacy Framework) | OpenAI is US-based. Your DPO decides whether the transfer assessment is acceptable. |
| 1.3 | **EU data residency**: decide if needed | It's opt-in through OpenAI sales, may only apply to newly created workspaces or projects, and some logs (e.g. abuse monitoring) may still be outside the EU. Ask OpenAI for specifics. |
| 1.4 | **No training on your data** | Enterprise data isn't used for training by default. Verify in the admin console and contract. |
| 1.5 | **Retention** of chats set to a defined period | For example, delete CV chats after X days or months. Align with your HR/CV retention policy. |
| 1.6 | **SSO/SCIM, audit logs** enabled | Needed to know who processed what, and to remove access when people leave. |

## 2. Workspace settings (ChatGPT admin)

| # | Check |
|---|---|
| 2.1 | **Memory**: off for users of this skill, or a policy that CV details must not be saved. The skill itself tells ChatGPT not to save CV content to memory. |
| 2.2 | **Public chat links / sharing outside the workspace** disabled |
| 2.3 | **Apps/connectors** limited to what's needed, so CV chats can't be sent to other tools by mistake |
| 2.4 | **Skill sharing** limited to the sales/management group that needs it |
| 2.5 | Workspace-wide **custom instructions** don't conflict with the skill |

## 3. Legal basis, transparency and DPIA (DPO / HR)

| # | Check | Notes |
|---|---|---|
| 3.1 | **Legal basis** documented | For employees' CVs used in sales, usually **legitimate interest** (with a balancing test) or the employment relationship, since presenting CVs to clients is already part of the job. Subcontractors and candidates need their own basis and information. |
| 3.2 | **Privacy notice to employees** updated | Say that CVs may be processed with an AI tool (ChatGPT Enterprise) to match and improve them, and that a human always reviews and decides. |
| 3.3 | **DPIA** (data protection impact assessment) | Strongly advised: new technology plus evaluation of employees. Your DPO decides whether it's mandatory. |
| 3.4 | **No automated decisions** (GDPR Art. 22) | The skill only *supports*. A person decides who is offered and what is sent. Write this into the routine. |
| 3.5 | **Information to and consultation with employee representatives** | In Sweden, introducing a new tool that processes employee data may trigger information or negotiation duties under MBL. Check with HR. |
| 3.6 | **Client confidentiality** | Client requests may contain confidential information or names of client staff. Check that framework agreements and NDAs allow processing in ChatGPT Enterprise. |

## 4. EU AI Act

- AI used in **employment** (e.g. evaluating people or allocating tasks based on personal characteristics) can be **high-risk** under Annex III. Whether matching consultants to assignments falls under this is a **legal assessment**: ask legal.
- According to current reporting, the high-risk obligations for Annex III were **postponed to 2 December 2027** by the Digital Omnibus on AI. Prepare anyway, because the measures below are good practice: human oversight, informing employees, logging, and user training.
- **AI literacy** (Art. 4) already applies: users should be trained in what the tool does and doesn't do. The 30-minute demo and the [command list](commands.md) are part of this. Document who was trained.

## 5. How the skill helps (built in)

| Measure | Where |
|---|---|
| No invented facts; asks instead of guessing | SKILL.md hard rules |
| Doesn't repeat personal ID numbers, home addresses or private phone numbers | SKILL.md rule 8 |
| Ignores special-category data (health, religion, union membership, ethnicity, etc.) and suggests removing it | SKILL.md rule 8 |
| Doesn't save CV content to memory | SKILL.md rule 8 |
| Reminds the user to start a new chat per consultant | workflow.md |
| Anonymisation on request | `Anonymise`, `Prepare for library` |
| Human review required, with a source table for every claim | Output formats |
| Example library only with consent, anonymisation and two-person approval, and never in the public repo | cv-quality-rubric.md |

## 6. User rules (put these in the rollout demo)

1. Use only the company's **ChatGPT Enterprise** account, never a personal account.
2. **One chat per consultant/case.** Delete chats you no longer need.
3. Upload the CV **without** personal ID number, home address or photo when possible. A Cinode export template without private details is ideal.
4. Never upload CVs of people who haven't been informed (e.g. external candidates) unless HR/DPO has approved it.
5. **A human checks everything** before it's sent to a client.
6. Don't paste a client's confidential documents unless the client agreement allows it.

## 7. Sign-off

| Role | Name | Date | Approved |
|---|---|---|---|
| DPO / legal | | | |
| IT security | | | |
| HR | | | |
| Business owner (sales) | | | |
