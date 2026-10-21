# claudecert — site brief

**URL:** https://iprash.github.io/learn/claudecert/
**Type:** generated
**Created:** 14 October 2026
**Evidence last checked:** 14 October 2026 (exam guides v1.0 July 2026, certification FAQ, every link in resources.md)

## What it is

A daily study plan for three Claude certification exams, taken in this order: Developer Foundations (CCDV-F), Architect Foundations (CCAR-F), Architect Professional (CCAR-P). Each day has one build, one Learn step from an Anthropic course, reference docs, three self-written questions, and a done-when checkbox. Associate (CCAO-F) is skipped unless the December buffer is unused.

## Why it exists

My employer is a Claude Partner Network member, so I can sit the exams. Top-tier partners sit them free until 31 December 2026. The calendar is built backwards from that date: last planned exam on 15 December, so every exam can be retaken once, 14 days later, before the offer ends.

I have long architecture experience and limited hands-on Claude mechanics. That is why half of every day is building, and why Developer comes first: it forces the API mechanics that the Architect exam assumes.

## Structure

| File | Role |
|---|---|
| `_site.json` | Config, nav, footer. Add `architect.md` and `professional.md` to `pages` when they are written |
| `index.html` | **GENERATED** from `_index_template.html` |
| `start.html`, `developer.html`, `drills.html`, `resources.html` | **GENERATED** from the matching `.md` |
| `start.md` | **SOURCE**. Part 0 (exams, order, calendar, routine, build spine, rules), setup days 1 to 3, exam-day checklist |
| `developer.md` | **SOURCE**. Days 4 to 28 |
| `drills.md` | **SOURCE**. Question bank. Grows by three questions a study day |
| `resources.md` | **SOURCE**. Numbered library, R1 onward. Days refer to resources by number |
| `_index_template.html` | Home page body. The Architect and Professional cards are plain `div`s until those pages exist; make them links then |
| `assets/style.css` | Hand-maintained. Copied from frontier-engineer. Changed: accent and signal colors, plus a `details` style for answer reveals at the end |
| `assets/app.js` | Hand-maintained. Copied from frontier-engineer. Changed: storage prefix `cc.`, and the home-page progress list names this site's page ids |

## Editing rules

**Never hand-edit the generated HTML.** Edit the markdown or the template, then `python _build\build.py claudecert`.

**Heading IDs are load-bearing.** Read progress is keyed by heading text. Day headings (`## Day 14 · Structured output and defensive parsing`) freeze once pushed. Fix a wording problem in the body, not the heading.

**Checkbox IDs come from the first 90 characters of the item text.** Identical text means a shared tick. Every daily checkbox therefore starts with its day number (`D14:`). Keep that prefix on new items. Exam-day checklist items in `start.md` are intentionally shared across all three exams.

**One line per paragraph,** because the build runs `nl2br`. The one deliberate exception is in `drills.md`: a question stem and its four options are consecutive lines in one paragraph, so each option renders on its own line.

**Answer reveals** in `drills.md` are raw `<details><summary>Answer</summary>…</details>` on a single line, separated from the question by a blank line. Markdown inside them is not processed, so keep them plain text.

**Just-in-time blocks.** `architect.md` is written in the week of 2 November and `professional.md` in the week of 23 November, using the domain report from the previous exam. Do not write them earlier: the score report decides where the time goes. Use the same day format as `developer.md`. Architect days are 29 to 46; Professional days are 47 to 62.

## Content standards

- **No exam content, ever.** Every candidate signs an NDA covering questions, options and scenarios (R1, section 13), and this repo is public. After an exam, do not add, reword or hint at anything seen. Drills are written only from the public blueprints and my builds.
- Do not copy the sample questions from the exam guides. Link the PDFs.
- No employer or client names. Discount tiers are described generically.
- **Anthropic's own courses are the baseline** (since 20 Oct 2026). Every day's Learn step names an Anthropic course segment: the exam prep course (R12, modules R103 to R107) or the Claude Developer path (R97) and its Claude Academy courses. Docs are reference. Third-party material only where Anthropic has nothing. Before writing the Architect or Professional block, inventory that exam's prep course and the matching Anthropic learning path first.
- Every reference to a resource is a link. Write `[R24](url)`, with the URL copied from that row of `resources.md`, never a bare `R24`. Check new links resolve before committing. If a resource's URL changes, update `resources.md` and every page that links it.
- Every fact carries a source and a date. Sources are graded [P] primary or [S] secondary in `resources.md`. Do not upgrade an [S] fact to unmarked fact.
- Where the docs and the exam guide disagree, the site follows the guide for exam purposes and says so.
- Lean STE: short sentences, active voice, one idea per sentence. Written in first person.

## Time-sensitive content

| Fact | Source | Checked |
|---|---|---|
| Exam items, fees, weights, policies | R1 to R4, v1.0 July 2026 | 14 Oct 2026 |
| Free exams for Global Premier partners until 31 Dec 2026 | R6 | 14 Oct 2026 |
| My employer's tier | Secondary sources only. Confirm by a $0 fee at checkout | Not confirmed |
| Practice exam retired | R11 [S] | 14 Oct 2026 |
| Prep course module lengths | R12, R14 | 14 Oct 2026 |

Re-check the relevant exam guide in the week before each exam. If a guide's version changes, re-check that block's domain table and day tags.

## Open items

- Write `architect.md` (week of 2 Nov) and `professional.md` (week of 23 Nov). Add both to `_site.json` and turn their home cards into links.
- Add Architect and Professional seed questions to `drills.md` with those blocks.
- After 31 December 2026, the calendar and free-exam framing go stale. Either archive the site as a record, or rewrite Part 0 for renewal (free, unproctored, before each 12-month expiry).
- Optional, deferred: a "today is day N" readout on the home page. It needs new JavaScript beyond the shared engine.
