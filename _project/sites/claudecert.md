# claudecert — site brief

**URL:** https://iprash.github.io/learn/claudecert/
**Type:** generated
**Created:** 14 October 2026
**Evidence last checked:** 22 October 2026 (Developer exam guide v1.0 July 2026, certification FAQ, every link in resources.md, full blueprint coverage audit)
**Scope:** Developer Foundations only, since 22 October 2026. See Parked.

## What it is

A daily study plan for one exam: Claude Certified Developer, Foundations (CCDV-F). Each day has one build, one Learn step from an Anthropic course, reference docs, three self-written questions, and a done-when checkbox. The Developer page has a blueprint checklist: one checkbox per skill line in R1, section 6, with the days that cover it.

## Why it exists

My employer is a Claude Partner Network member, so I can sit the exam. I have long architecture experience and limited hands-on Claude mechanics. R1, section 7, asks candidates to combine hands-on work with study, so half of every day is building.

**Developer focus (22 Oct 2026).** Prash asked to keep the site on the Developer exam only. No page may ask for work on another exam: no Architect or Professional guides, tasks, cards or framing. The later-exam plan is parked below.

## Structure

| File | Role |
|---|---|
| `_site.json` | Config, nav, footer |
| `index.html` | **GENERATED** from `_index_template.html` |
| `start.html`, `developer.html`, `drills.html`, `resources.html` | **GENERATED** from the matching `.md` |
| `start.md` | **SOURCE**. Part 0 (the exam, what Anthropic recommends, calendar, routine, build spine, rules), setup days 1 to 3, exam-day checklist |
| `developer.md` | **SOURCE**. Block map (domain weights, blueprint checklist, course map), then days 4 to 28 |
| `drills.md` | **SOURCE**. Question bank. Grows by three questions a study day |
| `resources.md` | **SOURCE**. Numbered library, R1 onward. Days refer to resources by number |
| `_index_template.html` | Home page body. Four cards: Developer, Start, Drills, Resources |
| `assets/style.css` | Hand-maintained. Copied from frontier-engineer. Changed: accent and signal colors, plus a `details` style for answer reveals at the end |
| `assets/app.js` | Hand-maintained. Copied from frontier-engineer. Changed: storage prefix `cc.`, and the home-page progress list names this site's page ids |

## Editing rules

**Never hand-edit the generated HTML.** Edit the markdown or the template, then `python _build\build.py claudecert`.

**Heading IDs are load-bearing.** Read progress is keyed by heading text. Day headings (`## Day 14 · Structured output and defensive parsing`) freeze once pushed. Fix a wording problem in the body, not the heading.

**Checkbox IDs come from the first 90 characters of the item text.** Identical text means a shared tick. Every daily checkbox therefore starts with its day number (`D14:`). Keep that prefix on new items. Blueprint checklist items start with `BP` and the skill number (`BP 2.5`).

**One line per paragraph,** because the build runs `nl2br`. The one deliberate exception is in `drills.md`: a question stem and its four options are consecutive lines in one paragraph, so each option renders on its own line.

**Answer reveals** in `drills.md` are raw `<details><summary>Answer</summary>…</details>` on a single line, separated from the question by a blank line. Markdown inside them is not processed, so keep them plain text.

**Coverage rule.** Every skill line in R1, section 6, must map to at least one day's Build, Learn or Write step, and to a `BP` line. When the exam guide version changes, redo the audit: list each named item in each skill line and grep the day plans for it.

## Content standards

- **No exam content, ever.** Every candidate signs an NDA covering questions, options and scenarios (R1, section 13), and this repo is public. After an exam, do not add, reword or hint at anything seen. Drills are written only from the public blueprints and my builds.
- Do not copy the sample questions from the exam guides. Link the PDFs.
- No employer or client names. Discount tiers are described generically.
- **Anthropic's own courses are the baseline** (since 20 Oct 2026). Every day's Learn step names an Anthropic course segment: the exam prep course (R12, modules R103 to R107) or the Claude Developer path (R97) and its Claude Academy courses. Docs are reference. Third-party material only where Anthropic has nothing. 
- Every reference to a resource is a link. Write `[R24](url)`, with the URL copied from that row of `resources.md`, never a bare `R24`. Check new links resolve before committing. If a resource's URL changes, update `resources.md` and every page that links it.
- Every fact carries a source and a date. Sources are graded [P] primary or [S] secondary in `resources.md`. Do not upgrade an [S] fact to unmarked fact.
- Where the docs and the exam guide disagree, the site follows the guide for exam purposes and says so.
- Names I invent for the study setup use CamelCase, with acronyms in capitals: `CertLab` repo and workspace, `CertLabDev` key, folders `01_API`, `02_Prompts`, `03_Agent`, `04_MCP`. A number prefix is followed by an underscore (`01_API`) for readability. Python files stay lowercase, per Python convention.
- Lean STE: short sentences, active voice, one idea per sentence. Written in first person.

## Time-sensitive content

| Fact | Source | Checked |
|---|---|---|
| Exam items, fee, weights, policies | R1, v1.0 July 2026 | 14 Oct 2026 |
| Free exams for Global Premier partners until 31 Dec 2026 | R6 | 14 Oct 2026 |
| My employer's tier | Secondary sources only. Confirm by a $0 fee at checkout | Not confirmed |
| Practice exam retired | R11 [S] | 14 Oct 2026 |
| Course lengths | Claude Academy and Partner Academy pages | 20 Oct 2026 |
| Extended thinking page marked legacy; adaptive thinking is the default on current models | R30 | 22 Oct 2026 |

Re-check the exam guide in the week before the exam. If its version changes, redo the coverage audit.

## Open items

- After the Developer exam, ask Prash whether to unpark the Architect plan.
- After 31 December 2026, the free-exam framing goes stale. Rewrite it, or note renewal (free, unproctored, before the 12-month expiry).
- Optional, deferred: a "today is day N" readout on the home page. It needs new JavaScript beyond the shared engine.

## Parked: later exams

Not on the site. Kept here so nothing is lost. Unpark only when Prash asks.

- Planned order after Developer: Architect Foundations (CCAR-F), then Architect Professional (CCAR-P). Associate (CCAO-F) skipped; it does not count toward partner tier.
- Earlier calendar (14 Oct plan): Architect Days 29 to 46, exam Sat 28 Nov; Professional Days 47 to 62, exam Tue 15 Dec. Dates will change.
- Builds parked with them: 5 Claude Code team configuration and a headless CI job; 6 extraction pipeline with batches and human review routing; 7 multi-agent research system with provenance; 8 RAG with an eval harness and an architecture decision pack.
- Method when unparked: inventory that exam's prep course and matching Anthropic learning path first, then write the block just in time, using the previous exam's domain report. Same day format as `developer.md`.
- Resource numbers R2, R3, R4, R13, R14, R15, R16, R95 and R96 are reserved. Their rows, removed from `resources.md` on 22 Oct 2026:

| R2 | [Architect Foundations exam guide (PDF, v1.0, July 2026)](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf) | [P] | Blueprint, 6 scenarios, 4 prep exercises, in-scope and out-of-scope lists |
| R3 | [Architect Professional exam guide (PDF, v1.0, July 2026)](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf) | [P] | Blueprint, 7 domains |
| R4 | [Associate Foundations exam guide (PDF, v1.0, July 2026)](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542847%2FClaude+Certified+Associate+%E2%80%93+Foundations+Exam+Guide.pdf) | [P] | Only if the December buffer is unused |
| R13 | [Architect Foundations prep courses](https://anthropic-partners.skilljar.com/page/claude-certified-architect-foundations-prep-courses) | 7 public courses | Architect block |
| R14 | [Architect Professional prep course](https://anthropic-partners.skilljar.com/path/claude-certified-architect-professional) | 5 modules, about 12 h | Professional block |
| R15 | [Associate Foundations prep course](https://anthropic-partners.skilljar.com/path/claude-certified-associate-foundations) | 7 modules, about 7 h | Optional |
| R16 | [Claude Code partner badge](https://anthropic-partners.skilljar.com/path/partner-badge-claude-code) | about 25 h | Not a certification. Useful after December |
| R95 | [Claude Code: A Highly Agentic Coding Assistant (DeepLearning.AI)](https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant) | [S] | About 2 h | Architect block. Taught by Anthropic's head of technical education. Free during the platform beta |
| R96 | [Code w/ Claude 2026, San Francisco recordings](https://claude.com/code-with-claude/san-francisco) | [P] | 19 sessions | Newer features than the 2025 talks. Browse in the Architect and Professional blocks |
