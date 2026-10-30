# ea-prep-03-intg — site brief

**URL:** https://iprash.github.io/learn/ea-prep-03-intg/
**Type:** static
**Created:** 30 Oct 2026
**Evidence last checked:** 30 Oct 2026

## What it is

Interview prep for an Enterprise Architect role that runs an independent review of a quote-to-cash landscape: Dynamics 365 CRM and ERP, a CPQ, an OMS, MuleSoft and other middleware. Sections: eight-session study plan (about 13 hours, with a 10-hour core path), a 15-question self-check, nine assessment-method cards (A), nine integration-risk cards (B), eight platform cards (C), "What changed 2024–2026" tables for Dynamics 365, Power Platform and MuleSoft, five deliverable templates (D), three client-behaviour cards (E), two anchor stories, fourteen interview questions, extra questions, an assessment walkthrough case, free resources and a cheat sheet.

## Why it exists

Prash has deep MuleSoft and integration experience and light Dynamics 365 experience. The site weights the assessment method highest, then the Dynamics limits that cause real symptoms. It replaces the planned `ea-prep-03-mule`, which was never built.

## Structure

| File | Role |
|---|---|
| `_site.json` | Config. Static, no `pages` list, so the build leaves the site alone. |
| `index.html` | Hand-written. Self-contained: inline CSS, JS and SVG. No backup other than git. |

## Editing rules

**Everything here is hand-written.** Edit `index.html` directly.

The page was assembled in Claude's cloud workspace from section fragments, with a script that copied the ea-prep-02-aws shell (CSS, JS) and wrapped acronyms in `<abbr title>` tags from a glossary. The script is not in the repo. Treat `index.html` as the source now. When adding content, wrap new acronyms by hand in the same form. Text inside `<code>`, `<pre>`, `<svg>`, `<nav>`, `<summary>`, `<h1>`, `<figcaption>`, `<th>`, links and buttons is deliberately left unwrapped.

The `<meta name="robots" content="noindex,nofollow">` is hand-maintained. Put it back if the file is replaced.

Progress ticks use localStorage keys prefixed `ea3.`, keyed by each card's `id` (`c-check`, `a-*`, `i-*`, `pl-*`, `c-d365`, `c-pp`, `c-mule`, `t-*`, `b-*`, `stories`, `s-scale`, `s-c360`, `q1`–`q14`, `x-*`, `d-walk`, `res-*`, `cheat-card`). Renaming an id resets that tick and breaks in-page links.

Diagrams are inline SVG with class `d` and the `rect.ou`, `rect.band`, `text.t`, `text.s` classes, so they follow dark mode.

## Content standards

**The repo is public.** No client, employer or interview names. The role description is paraphrased in general terms only.

Story cards use provenance tags: YOURS (from Prash's notes or statements), IF TRUE (plausible framing, use only if it happened). [Brackets] mark facts only Prash can supply. Never fill them with invented numbers.

Each card ends with "Go deeper (free)" links and a Sources line with a check date. Version-sensitive facts carry a `ver` mark. Sources are graded [P] primary and [S] credible secondary.

All 77 external links returned HTTP 200 on 30 Oct 2026. The English CloudHub 1.0/2.0 comparison page on docs.mulesoft.com now 404s; the site links `cloudhub-2/ch2-features` instead.

## Time-sensitive content

Checked 30 Oct 2026:

- Dataverse service protection limits (6,000 requests, 20 min execution time, 52 concurrent per user per web server per 5 min); Power Platform request allocations (40,000 per Dynamics 365 Enterprise user per 24 h; transition-period enforcement).
- Finance and Operations: integration pattern volumes, priority-based throttling, LCS project creation freeze for new customers (16 Feb 2026).
- Dual-write limits: 2 min, 1,000 records per transaction, 250 legal entities.
- Unified Service Desk deprecated from 1 Apr 2026; end of support 30 Jun 2028 per trade press [S].
- Release waves retired; Release Planner retires by 15 Nov 2026; AI at Work roadmap.
- Mule 4.9 LTS (Java 17) to Aug 2027; 4.6 LTS standard support ended Aug 2026; OpenTelemetry export from 4.11; Omni Gateway (May 2026); Agent Fabric (from Oct 2025).
- Azure: ISE retired Aug 2024; Logic Apps hybrid GA Jun 2025; APIM Premium v2 GA Nov 2025; BizTalk 2020 final version, support to 2030 [S].
- Uncertain, marked `ver`: Intelligent Order Management status (no retirement notice found), CloudHub 1.0 end date (none found).

## Open items

- "USD CPQ" in the role is ambiguous: Unified Service Desk or a CPQ name. The site covers both and lists it as a question to ask. Update card C5 once known.
- ERP assumed to be Dynamics 365 Finance and Supply Chain. Update if the client runs another ERP.
- Prash fills the [brackets] in `#s-scale` and `#s-c360` with real facts.
- Re-check the What changed tables the week before the interview.
