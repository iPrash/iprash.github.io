# aigov — site brief

**URL:** https://iprash.github.io/learn/aigov/
**Moved:** 25 Sept 2026, from /aigov/. A redirect stub remains at the old path.
**Type:** generated
**Created:** August 2026
**Evidence last checked:** 17 August 2026

## What it is

A consulting engagement playbook and resource library for a fictional client, XYZ Corp — a
fashion brand. Three workstreams: AI consumption governance on their OpenAI estate, a
multi-model access strategy after a withdrawn Copilot trial, and a GenAI landscape review.

Written as a working reference for a lead Enterprise Architect, not as a tutorial.

## Why it exists

To upskill in enterprise AI governance, FinOps for AI, vendor negotiation and building an AI
Centre of Excellence. Solid theory, limited hands-on with the mechanics.

## The engagement in one paragraph

Behind eleven deliverables sit three decisions: **D1** what to sign at renewal, **D2** one model
platform or several, **D3** where to build, buy or partner. Every artifact serves one of them.
The plan runs backwards from a fixed renewal date.

## Structure

| File | Role |
|---|---|
| `_site.json` | Config, nav, footer |
| `index.html` | **GENERATED** from `_index_template.html` — plan hub |
| `playbook.html` | **GENERATED** from `playbook.md` |
| `resources.html` | **GENERATED** from `resources.md` |
| `playbook.md` | **SOURCE** — ~15,000 words, 11 parts |
| `resources.md` | **SOURCE** — ~3,000 words, 100+ graded links |
| `_index_template.html` | Home page body. `{{HEAD}}`, `{{NAV}}`, `{{FOOTER}}`, `{{EVIDENCE}}` filled by the build. |
| `assets/style.css` | Hand-maintained |
| `assets/app.js` | Hand-maintained |
| `README.md` | Deployment notes |

## Editing rules

**Never hand-edit `index.html`, `playbook.html` or `resources.html`.** Edit the markdown, then
`python _build\build.py aigov`.

**Heading IDs are load-bearing.** Progress is stored in localStorage keyed by heading ID, derived
from heading text. Renaming a heading resets that section's tick and breaks anchors —
`_index_template.html` cross-links into `playbook.html` by anchor.

## Playbook structure

| Part | Content |
|---|---|
| 0 | How to use it |
| 1 | Read of the brief — five traps, operating principles, success criteria |
| 2 | Engagement design — spine, phases, renewal-driven schedule, RACI, first five days |
| 3 | WS1 consumption — data acquisition, truth-layer schema, seven-cohort segmentation, decision matrix, seven-layer governance, negotiation brief |
| 4 | WS2 multi-model — Copilot post-mortem, workload mapping, evaluation framework, Bedrock, gateway architecture, cost model, revisit triggers |
| 5 | WS3 landscape — 12-domain fashion taxonomy, vendor scorecard, research protocol, estate cross-check, build/buy/partner/consume |
| 6 | The CoE build — archetype, charter, decision rights, roles, stage gates, risk tiering, 90/180/365 |
| 7 | Risk and compliance — EU AI Act, fashion exposures, GenAI security |
| 8 | Templates |
| 9 | Anti-patterns |
| 10 | Twelve-week calendar |
| 11 | Making it a reference engagement |

Resource library: section 0 is a two-week study sprint; sections 1–12 are graded sources.

## Site behaviour

- **Week ruler** — 13 columns, five phase bands, milestone pins, linking into Part 10.
- **Renewal calculator** — enter a date, get the backward schedule (R−150 data access, R−135
  baseline locked, R−120 BATNA costed, R−105 brief approved, R−90 first session). Past
  milestones turn red; under 150 days triggers a compressed-plan warning.
- **Countdown** to the Codex model retirement.
- **Progress tracking** per part and section, playbook and resources tracked separately.
- Contents filter, scroll-spy, light/dark, print styles. localStorage keys namespaced `xyzai.*`.

## Content standards

**Evidence grading throughout** — [P] primary, [S] credible secondary, [C] commentary. Preserve
it. Do not upgrade a [C] claim to unmarked fact.

Every factual claim carries a source and a date.

## Time-sensitive content — checked 17 Aug 2026, re-verify before reuse

- OpenAI Global Admin Console with credit analytics and spend controls (June 2026): group limits,
  user overrides, member cost visibility, Codex analytics API, Cost API.
- Codex moved to token-aligned credit pricing April 2026 (Enterprise 23 April). Pre-April data
  is not comparable.
- **GPT-5.4 and GPT-5.4 mini retired in Codex on 31 August 2026** (ChatGPT-signed-in users),
  replaced by GPT-5.6 Terra and Luna. **This date has now passed.** Playbook §2.8 still presents
  it as upcoming and the home page counts down to it. Needs an edit.
- ChatGPT Enterprise workspaces migrating from weekly role-based to monthly usage limits during
  August 2026.
- GitHub Copilot moved to usage-based AI Credits 1 June 2026. Business $19/user/mo including $19
  credits; Enterprise $39 including $39. Completions free and unmetered. Org-pooled credits.
- Bedrock: on-demand, batch (~50% discount), provisioned throughput. AWS became a third-party
  cloud distributor for OpenAI frontier models (Feb 2026) — relevant to concentration risk.
- **EU AI Act:** Regulation (EU) 2026/1744 (Digital Omnibus) in force 27 July 2026. Article 50
  transparency applies from 2 August 2026 — not deferred. Art 50(2) legacy marking plus new
  prohibitions from 2 Dec 2026. Annex III high-risk deferred to 2 Dec 2027; Annex I to 2 Aug 2028.
  Art 4 AI literacy already applies.
- FinOps Framework 2026 introduced Scopes and FinOps for AI; 98% of practices manage AI spend;
  innovation scopes should tolerate higher waste.

## The learning plan

Build an artifact each week, read the reference when stuck.

| Week | Build | Read |
|---|---|---|
| 1 | Consumption baseline and segmentation on real personal usage data, using the §3.2 schema and §3.3 measures | §3.1–3.3, §3.5 |
| 2 | LiteLLM gateway locally, two providers, virtual key with a budget. Then a 30-example eval set in promptfoo across two models | §4.3–4.6 |
| 3 | The four-page directional guidance note from §4.7 for a real or invented org | §4.7, §5.5, Part 6, §7.1 |

Three-hour priority order if time collapses: §3.7 negotiation brief → §4.0–4.1 Copilot analysis
→ Part 6 CoE → §7.1 AI Act → Part 9 anti-patterns.

## Open items

- The 31 Aug 2026 Codex retirement has passed. Update §2.8 and the home page countdown.
- Nothing re-verified since 17 Aug 2026. A quarterly check against the primary sources in the
  resource library is about the right cadence.
- Considered and not done: search across both documents, cross-device progress sync.
