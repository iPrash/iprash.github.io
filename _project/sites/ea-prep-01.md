# ea-prep-01 — site brief

**URL:** https://iprash.github.io/learn/ea-prep-01/
**Type:** static
**Created:** 23 Oct 2026
**Evidence last checked:** 23 Oct 2026

## What it is

Solution Architect interview prep. Part 1: one half-page card per technology in the job description (Kafka, event-driven patterns, Cassandra, Kubernetes/AKS, Azure, Java/Spring Boot, React, observability/Grafana/SRE, quality engineering, security, resilience/DR, EA methods, modernization). Part 2: likely interview questions grouped in eight themed sections, with the intent behind each, model answers, an anchor-project card (Customer-360), extra questions, a system design walkthrough and a cheat sheet.

## Why it exists

Short, focused prep organised as six study sessions. The `-01` suffix leaves room for later EA prep sites.

## Structure

| File | Role |
|---|---|
| `_site.json` | Config. Static, no `pages` list, so the build leaves the site alone. |
| `index.html` | Hand-written. Self-contained: inline CSS, JS and SVG. No backup other than git. |

## Editing rules

**Everything here is hand-written.** Edit `index.html` directly.

The `<meta name="robots" content="noindex,nofollow">` is hand-maintained. Put it back if the file is replaced.

Progress ticks use localStorage keys prefixed `ea1.`, keyed by each card's `id` (`t-*`, `q*`, `x-*`). Renaming an id resets that tick and breaks the in-page links.

**Acronyms are wrapped in `<abbr title="Expansion: one-line definition.">`** (about 750 on the page, applied in Oct 2026). A small script at the end of `index.html` turns them into hover and tap tooltips. When adding content, wrap new acronyms the same way. Text inside `<code>`, `<svg>`, `<nav>` and buttons is deliberately left unwrapped. "Entra ID" is not wrapped (product name).

## Content standards

**The repo is public.** The page must contain no client names and no reference to any specific past or upcoming interview. Keep it reading as general interview prep.


Each Part 1 card ends with a Sources line and a check date. Version-sensitive facts carry a `ver` mark.

## Time-sensitive content

Checked 23 Oct 2026: Kafka 4.0 (ZooKeeper removed, KIP-848 GA), KIP-932 share groups (preview in 4.1, GA status unverified), ingress-nginx retirement (March 2026), Spring Boot 4.0 (Nov 2025), React 19 and React Compiler 1.0, Grafana Agent EOL (1 Nov 2025), Entra External ID replacing B2C for new customers.

## Domain

Part 1 card 15 frames the target as a generic global logistics and freight company. Keep all domain content generic: no company names, no details that identify the client.



## Story D provenance tags

Story D (card `q0d`) is the same project as story A, seen through the Kafka and Cassandra lens. Its numbers are reconstructions for a provider with about 10 million accounts, because the real figures are not remembered. Every line carries a tag: YOURS (from Prash's own project notes), EST (estimate) or IF TRUE (plausible scenario, to use only if it happened). Prash must replace EST numbers with real ones where he can. Do not remove the tags or present EST values as fact.

## Open items

- Anchor stories D (high-volume Kafka/Cassandra pipeline, the lead story), A (Customer-360), B (scale modelling) and C (agentic AI platform, Q7) are written from his resume with [bracketed] gaps for numbers he must fill. No client or employer names on the page: the repo is public.
