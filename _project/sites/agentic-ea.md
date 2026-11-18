# agentic-ea — site brief

**URL:** https://iprash.github.io/learn/agentic-ea/
**Type:** static
**Created:** 18 Nov 2026 (quick interview page), rebuilt the same day as the full design-phase guide
**Evidence last checked:** 18 Nov 2026

## What it is

A step-by-step field guide for the design phase of an agentic underwriting programme in the London specialty market. It teaches the insurance domain from zero (Lloyd's, placement routes, SOV, geocoding, cat modelling, pricing), sets out the target design around the decision ladder (code, rules, LLM with a confidence score, human, then audit and four eyes), gives agentic pattern references, a week-by-week playbook (W0 to W4), templates, governance, buy-or-build, a question bank, resources and a cheat sheet.

## Why it exists

Prash moved from interview prep to delivery: he is the lead architect on a UK and London market track of an agentic underwriting programme, with a roughly four-week design SOW, then a lighthouse MVP, then engineering. He comes from banking, so the domain cards start from zero and use a banking bridge. Help him by building artifacts (spike, templates filled in privately) and pointing at the card to read while building.

## Structure

| File | Role |
|---|---|
| `_site.json` | Config. Static, `listed: false`, `noindex: true`. |
| `index.html` | Hand-written. Self-contained: inline CSS, JS and SVG. Shell copied from ea-prep-02-aws. No backup other than git. |
| `_glossary.json` | Site overrides: BI (business interruption), ODS (Open Data Standards), OS (Ordnance Survey), PDF (the shared entry carries a site-specific "bill image" note). |

## Editing rules

**Everything here is hand-written.** Edit `index.html` directly, then run `python _build/build.py --acronyms-fix` and confirm `--acronyms` reports "All acronyms have tooltips."

The `<meta name="robots" content="noindex,nofollow">` is hand-maintained.

Progress ticks use localStorage keys prefixed `aea.`, keyed by each card's `id` (`plan-*`, `c-check`, `d-*`, `p-*`, `c-asis`, `c-pain`, `t-*`, `a-*`, `w-*`, `tp-*`, `g-*`, `b-market`, `x-changed`, `q-bank`, `res-*`, `cheat-card`). Renaming an id resets that tick and breaks in-page links.

SVG arrows use one shared marker `#ar` defined in a hidden `<svg id="defs">` at the top of the body; lines get `class="ar"`. Extra rect classes: `wr` (manual effort, warn colours) and `hu` (human decision, brass).

## Content standards

**The repo is public.** No client name, no people's names, no internal figures from the client conversations. Facts only Prash can supply are `[bracket]` prompts (`span.prov.m`). Keep real numbers in private notes.

Sources graded [P] primary or [S] secondary, with a check date. Version-sensitive facts carry a `ver` mark.

Insurance acronyms (SOV, TIV, AAL, OED, CDR, UPRN and others) were added to the shared `_build/glossary.json` on 18 Nov 2026, so later insurance sites get them for free.

## Time-sensitive content

- Lloyd's Blueprint Two sunset (19 Mar 2026) and CDR scope (full lifecycle by Oct 2026).
- UK Sanctions List as single source since 28 Jan 2026.
- MCP current spec 2026-07-28 (stateless). A2A at the Linux Foundation.
- Guidewire agreement to acquire hyperexponential (27 Oct 2026; close expected Guidewire fiscal Q2 2027). Re-check after close.
- EU AI Act high-risk obligations delayed to 2 Dec 2027 (secondary sources; confirm).
- OED field names from v3; OED v4 in development.

## Dates and links

The W0–W4 plan assumes a design start on Mon 23 Nov 2026 (W4 ends Fri 18 Dec 2026). Scope (classes of business, placement routes) is not confirmed; the page carries a `[scope]` prompt in B3. General agentic patterns, definitions and learning links live in `learn/agentic-guide/`; Part E and session L6 link there.

## Open items

- Fill the `[bracket]` baselines privately once week-1 data arrives.
- Add a card on bordereaux validation if delegated authority enters scope.
- Re-check the hx acquisition status and the EU AI Act date in Feb 2027.
