# Claude Certified Developer, Foundations
## One Anthropic course and one build a day

I am preparing for one exam: Claude Certified Developer, Foundations (CCDV-F). The plan runs six days a week. Each day pairs a build with a segment of an Anthropic course, and takes 1.5 to 2.5 hours. The dates show the fastest pace, ending with the exam on Tuesday 10 November 2026.

I plan to take the Architect exams later. They are parked until this exam is done. Nothing on this site asks for work on them.

Read this page once. Then work one day at a time from the Developer page.

| Page | What it holds |
|---|---|
| Start (this page) | The exam, what Anthropic recommends, the calendar, the routine, the rules, and setup days 1 to 3 |
| [Developer](developer.html) | Days 4 to 28, and the blueprint checklist |
| [Drills](drills.html) | My question bank, by blueprint domain |
| [Resources](resources.html) | Every link, numbered. Days refer to them by number, such as [R24](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) |

---

# Part 0 · The plan

## 0.1 The exam

All facts in this section come from the official exam guide, version 1.0, effective July 2026 ([R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf)), checked 14 October 2026.

| Code | Items | Time | List fee | Pass | Validity |
|---|---|---|---|---|---|
| CCDV-F | 53 | 120 minutes | $125 | 720 of 1,000 | 12 months |

The exam is proctored by Pearson and has no mandatory prerequisite. No notes, books or second monitors are allowed. The score report shows percent correct by domain.

Policy facts from [R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf), sections 10 to 14:

- Retake waiting periods are 14 days after the first fail, 30 after the second, 90 after the third. The limit is four attempts in 12 months.
- Cancel or reschedule up to 24 hours before the appointment. Later changes, and no-shows, forfeit the fee.
- The name on the ID must match the registration exactly. Fix a mismatch through certifications-support@anthropic.com before scheduling.
- Renewal before expiry is free, through an unproctored assessment on Partner Academy.
- Every candidate accepts a non-disclosure agreement covering all questions, answer options and scenarios.

Facts from the certification FAQ ([R6](https://anthropic-partners.skilljar.com/page/faq-certifications)), checked 14 October 2026:

- Only people at organizations in the Claude Partner Network can register. A personal email address does not work.
- Select, Preferred and Global Premier partners get 50% off. Global Premier partners pay nothing until 31 December 2026.
- A retake costs the full fee again.

Fact from a secondary source ([R11](https://trainingcamp.com/articles/claude-certifications-explained-all-four-anthropic-exams-costs-and-who-can-take-them/), 17 September 2026), not found on a primary page: the official practice exam was retired. The only official practice is the sample questions in [R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf), section 8. That is why this site has its own question bank.

## 0.2 What Anthropic recommends

[R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf), section 7, says no single course is required. It asks candidates to combine hands-on experience with study. The recommended background is at least six months of hands-on work with Claude or a similar LLM system. My builds stand in for that. This table maps each point in section 7 to the site, checked 22 October 2026.

| [R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf) section 7 asks me to | Where the site does it |
|---|---|
| Study the blueprint and self-assess against each objective | Day 3 baseline. The blueprint checklist on the Developer page |
| Review the official docs for the API, models, prompt engineering, Claude Code, Skills and MCP | The Reference line on every day |
| Build and operate at least one Claude application with tools, prompt and context engineering, and simple security and evaluation | Builds 1 to 4 in `CertLab` |
| Practise the developer competencies: prompts, agents and workflows, Claude Code configuration, tokens and cost, guardrails, custom tools and MCP servers | The Build step on every day |
| Complete the sample questions | Day 3 |

Anthropic's own courses carry the Learn step: the exam prep course ([R12](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations)) and the Claude Developer learning path ([R97](https://anthropic-partners.skilljar.com/path/claude-developer)). The Developer page lists every course and the days that use it.

## 0.3 Calendar

Day 1 is Wednesday 14 October 2026. Sundays are rest days. Saturdays are long days.

| Days | Dates | Block | Exam | Earliest retake |
|---|---|---|---|---|
| 1 to 3 | 14 to 16 Oct | Setup and baseline | | |
| 4 to 28 | 17 Oct to 10 Nov | Developer | **Tue 10 Nov** | Tue 24 Nov |

The dates show the fastest pace. If I need more time, I move the exam, not the plan. Changes are free until 24 hours before the appointment.

If I fail, I book the earliest retake. Then I spend 30 minutes a day on the two weakest domains from the score report, using my drills and that domain's days.

## 0.4 The daily routine

| Block | Minutes | What |
|---|---|---|
| Recall | 10 | Answer 5 questions from my bank, written on earlier days. Mark the ones I miss. |
| Build | 40 to 45 | The day's artifact. Build first, then learn. |
| Learn | 40 to 105 | The Anthropic course segment named for the day, tied to what I just built. Docs are reference during the build. |
| Write | 10 | Write 3 exam-style questions from today's work into the Drills page format. Log gotchas. |

Each week: five build days, one long Saturday (a longer build or a timed mock), and one rest day on Sunday. If a day runs over, I finish the build and move the Learn step to the next sitting or to Sunday. I do not skip a required course segment. Also items are optional.

## 0.5 The build spine

All builds live in one private repo called `CertLab`. Each build maps to blueprint domains.

| # | Build | Days | Domains |
|---|---|---|---|
| 1 | API basics: messages, tokens, models, streaming, async, vision, caching, batches | 4 to 11 | D2, D5 |
| 2 | Prompt lab: a classifier with a test set, few-shot, structured output, validation, evals | 13, 14, 24 | D4, D6 |
| 3 | Tool-use agent: manual loop, then Agent SDK, with a blocking hook and security layers | 15 to 18, 20, 23 | D1, D7, D8 |
| 4 | MCP server, connected to Claude Code, plus Claude Code configuration and a plugin | 21, 22, 27 | D2, D3, D8 |

API usage is billed separately from a Claude Pro plan. Budget about $20 to $50 in Console credits. Use the smallest model that does the job, and use batches where a task allows it.

## 0.6 Rules for this site

- **No exam content, ever.** This repo is public, and every candidate signs a non-disclosure agreement ([R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf), section 13). After an exam, I do not add, reword or hint at anything I saw. The Drills page is written from the public blueprints and my builds only.
- No employer or client names.
- Do not copy the sample questions from the exam guides. Link to the guides instead.
- Every fact carries a source and a check date. Re-read the exam guide in the week before the exam, in case the version has changed.
- When the docs and the exam guide disagree, the exam guide wins for exam purposes. The guides predate some current models and features.

---

# Week 1 · Setup

## Day 1 · Eligibility and registration

Wednesday 14 October. Goal: confirm I can sit the exam for free, and book it.

- [ ] D1: Sign in to Partner Academy ([R5](https://anthropic-partners.skilljar.com/page/partner-certifications)) with my company email. If it fails, email partner-support@anthropic.com today, because adding a domain takes 7 to 10 days ([R7](https://anthropic-partners.skilljar.com/page/certification-eligibility)).
- [ ] D1: Open the Developer Foundations registration. Confirm the fee shows $0 at checkout. If it does not, stop and recheck the tier before paying.
- [ ] D1: Register for the Developer prep course ([R12](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations)). It is free.
- [ ] D1: Book the Developer exam for Tuesday 10 November through Pearson ([R9](https://www.pearsonvue.com/us/en/anthropic.html)). Choose online or test center. Changes are free until 24 hours before.
- [ ] D1: Check that my Pearson profile name matches my government ID exactly.
- [ ] D1: Download the exam guide ([R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf)) and read it in full.

## Day 2 · Tooling

Thursday 15 October. Goal: a working build environment, so Day 4 starts with code, not setup.

- [ ] D2: In the Console ([R23](https://platform.claude.com/docs/en/get-started)), create a `CertLab` workspace with a monthly spend limit, and a `CertLabDev` API key scoped to it ([R132](https://platform.claude.com/docs/en/manage-claude/workspaces)). Credits belong to the organization, not to a key, so add credits only if the balance is low.
- [ ] D2: Create the private `CertLab` repo. Add a `.env` for the key and put `.env` in `.gitignore` before the first commit.
- [ ] D2: Install the Python SDK (`pip install anthropic`) and send one message from a script.
- [ ] D2: Confirm Claude Code runs in the repo. Run `/init` and read what it writes into CLAUDE.md.

## Day 3 · Baseline

Friday 16 October. Goal: know where I start, by domain, before any study.

- [ ] D3: Answer the sample questions in [R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf), section 8, cold. No docs. Record my answers before reading the answer key.
- [ ] D3: Rate myself 1 to 3 on every Developer skill line in [R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf) section 6 (1 = never done it, 3 = done it in production). Write the ratings into `CertLab/baseline.md`.
- [ ] D3: Mark the three lowest-rated Developer skills. Those get extra time when a day touches them.

---

# Exam day

## Before every exam

- [ ] Exam guide re-read in the week before. Version number checked against the one this site used.
- [ ] Online proctoring: system test run on the exam computer, on the exam network, at least 2 days before ([R8](https://anthropic-partners.skilljar.com/page/computer-and-network-setup)).
- [ ] Government ID ready. Name matches the Pearson profile.
- [ ] Desk clear. No second monitor, no phone in reach, no notes.
- [ ] Light review only on the day before. Recall drills from Drills, no new topics.

## In the exam

Each item states how many answers to select. Read that number first. Scenario items reward design judgment: prefer a programmatic control over a stronger instruction, least privilege over logging, and the managed feature over a hand-built one, unless the scenario rules it out.

Plan for about 135 minutes in the seat, including check-in. Flag and move on after 2 minutes on one item.

## After every exam

- [ ] Record the scaled score and the percent correct per domain in `CertLab/results.md`. That file is private.
- [ ] Pass: claim the Credly badge. Fail: book the earliest retake and start 30 minutes a day on the two weakest domains.
