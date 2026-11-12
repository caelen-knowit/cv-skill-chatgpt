# CV Match Coach – ChatGPT skill

Upload a consultant CV and a client request. You get an honest match, gaps, an experience check per skill, and an improved, human-sounding CV ready to paste back into Cinode.
**It never invents facts.** If something is unclear, it asks.

## Setup (once, about 2 minutes)

1. **[⬇ Download cv-match-coach.zip](https://github.com/caelen-knowit/cv-skill-chatgpt/raw/main/cv-match-coach.zip)**
2. In ChatGPT: **Plugins → Skills → Create → Upload from your computer**, and choose the zip.
3. **••• → Share** the skill with your team (or the whole workspace). Colleagues then don't need to install anything.

Can't see *Skills*? Ask your ChatGPT admin to enable it. Until then, use the [Project fallback](docs/setup-alternatives.md).

## Use

Open a new chat, attach a CV (a Cinode Word export works best), paste the client request, and type:
```
Match this CV to this assignment
```
After that, **just follow the menu**. Every answer ends with the next steps. Reply with a letter:
```
Progress: ✓ CV read → ✓ Match → ◻ Questions → ◻ CV → ◻ Cinode/Word
A – Answer the questions above
B – Experience check on the requirements
C – Suggest changes to the CV
D – Something else
```
Not sure where to start? Type `help`.

You can also type commands directly:

| Type | You get |
|---|---|
| `Match this CV to this assignment` | Score, gaps, and questions to answer |
| `Experience check: Java, Azure` | Proven years/months per skill |
| `Suggest changes` | A list of improvements. Reply `apply 1, 3`. |
| `Improve CV: light` / `medium` / `heavy` | A rewritten CV (small, medium or big changes) |
| `Cinode` | The new texts, ready to paste into Cinode |

Swedish works too: `Matcha`, `Erfarenhetskoll`, `Föreslå ändringar`, `Förbättra CV: lätt / mellan / mycket`.

**Always read the result before sending it to a client.**

## More
- All commands: [English](docs/commands.md) · [Svenska](docs/kommandon.md)
- First test with your own CV: [docs/test-script.md](docs/test-script.md)
- Is it better than plain ChatGPT? [docs/compare-with-plain-chatgpt.md](docs/compare-with-plain-chatgpt.md)
- Benchmark (run after every change): [benchmark/](benchmark/README.md)
- GDPR and privacy checklist: [docs/gdpr-and-privacy.md](docs/gdpr-and-privacy.md)
- Owner/admin guide: [docs/admin-guide.md](docs/admin-guide.md)
