# ea-prep-03-intg — site brief

**URL:** https://iprash.github.io/learn/ea-prep-03-intg/
**Type:** static
**Created:** 30 Oct 2026
**Evidence last checked:** 30 Oct 2026

## What it is

Interview prep for an Enterprise Architect role reviewing a quote-to-cash landscape: Dynamics 365 Sales with a custom CPQ app, MuleSoft and Azure Functions, an IBM order management system, Oracle ERP and an Oracle warehouse system. Rebuilt on 4 Nov 2026 after two internal briefings showed the real problem: **order status drifting out of sync** across asynchronous systems (edits during picking, cancels that ship anyway, credit left held).

Structure: a five-session study plan to the interview, a 12-question self-check, part P (the problem as described), part S (solution options: ownership handoff, shared state model, requested states, versioning, ordering and idempotency, reliable delivery, reconciliation, decision matrix, roadmap), part F (positioning: gap statement, Salesforce-to-Dynamics terms, supply chain vocabulary, RACI), then the original assessment method (A), integration risks (B), platform cards (C: IBM OMS, Oracle, Dataverse, CPQ, "USD", MuleSoft, Azure), What changed, seven templates (D) including a cross-system status map and an allowed-actions matrix, client behaviour (E), 14 interview questions, a 30-minute walkthrough, resources and a cheat sheet.

Every card carries a **Core** or **Extra** badge. Core cards are what the interview needs; Extra cards are background.

## Why it exists

Prash has deep MuleSoft and integration experience, no hands-on Dynamics 365, ERP or supply chain experience. The page positions him as the cross-system architect working with the client's Dynamics specialists, and prepares him to discuss the order-sync problem credibly.

## Structure

| File | Role |
|---|---|
| `_site.json` | Config. Static, no `pages` list, so the build leaves the site alone. |
| `index.html` | Hand-written. Self-contained: inline CSS, JS and SVG. No backup other than git. |

## Editing rules

**Everything here is hand-written.** Edit `index.html` directly.

The page was assembled in Claude's cloud workspace from section fragments, with a script that copied the ea-prep-02-aws shell (CSS, JS) and wrapped acronyms in `<abbr title>` tags from a glossary. The script is not in the repo. Treat `index.html` as the source now. When adding content, wrap new acronyms by hand in the same form. Every occurrence is wrapped, including table headers and link text (fixed 30 Oct 2026). Text inside `<code>`, `<pre>`, `<svg>`, `<nav>`, `<summary>`, `<h1>`, `<figcaption>` and buttons is deliberately left unwrapped. See the acronym rule in PROJECT-INSTRUCTIONS.

The `<meta name="robots" content="noindex,nofollow">` is hand-maintained. Put it back if the file is replaced.

Progress ticks use localStorage keys prefixed `ea3.`, keyed by each card's `id` (`c-check`, `pr-*`, `sol-*`, `f-*`, `a-*`, `i-*`, `pl-*`, `c-d365`, `c-pp`, `c-mule`, `t-*`, `b-*`, `stories`, `s-scale`, `s-c360`, `q1`–`q14`, `x-*`, `d-walk`, `res-*`, `cheat-card`). The 4 Nov 2026 rebuild removed `pl-fo` and `pl-dw` and reused other ids with new content. Renaming an id resets that tick and breaks in-page links.

Diagrams are inline SVG with class `d` and the `rect.ou`, `rect.band`, `text.t`, `text.s` classes, so they follow dark mode.

## Content standards

**The repo is public.** No client, employer, person or location names, and nothing from the briefings that identifies the client. The client is "a large distributor of physical products". Product families (Dynamics 365, MuleSoft, IBM order management, Oracle) are named; nothing else. Before each commit, search the page for the client, employer, staffing-group and people names Prash has mentioned, and confirm zero hits. Briefing facts carry a BRIEFING tag.

Story cards use provenance tags: YOURS (from Prash's notes or statements), IF TRUE (plausible framing, use only if it happened). Problem cards use BRIEFING (from the internal briefings). [Brackets] mark facts only Prash can supply. Never fill them with invented numbers.

Each card ends with "Go deeper (free)" links and a Sources line with a check date. Version-sensitive facts carry a `ver` mark. Sources are graded [P] primary and [S] credible secondary.

On 4 Nov 2026, 58 of 60 external links returned HTTP 200. The two ibm.com links return 403 to automated checks from Claude's workspace (bot blocking); their content was read through a fetch tool the same day.

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

- Confirm in the interview: "USD" is the client's name for its Dynamics CPQ app (card C5 now treats this as resolved).
- Oracle flavour (Fusion Cloud or E-Business Suite) unknown; card C2 covers both.
- IBM order management product and version unknown; card C1 assumes Sterling Order Management, marked `ver`.
- Prash fills the [brackets] in `#s-c360` and `#s-scale` with real facts.
- The section fragments and assembly script live in Claude's cloud workspace only. Treat `index.html` as the source.
