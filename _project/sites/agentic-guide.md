# agentic-guide — site brief

**URL:** https://iprash.github.io/learn/agentic-guide/
**Type:** static
**Created:** 18 Nov 2026
**Evidence last checked:** 18 Nov 2026

## What it is

A general learning guide to agentic AI for an architect: definitions, the augmented LLM, the agent loop, the complexity ladder, enterprise layers, every orchestration pattern with its own diagram, a vendor-name mapping, a worked example, how to choose (including the single versus multi-agent debate), building well (context, tools, memory, evals, observability, security), protocols (MCP, A2A), frameworks, and curated courses, videos, reading and docs.

## Why it exists

Prash asked for a reusable agentic learning section after the agentic-ea rebuild dropped the first page's pattern and layer diagrams. This site restores them (layers in 1.5, the eight-pattern overview in 2.0, the submission-to-quote example in 2.11) and keeps general material out of the domain guide. agentic-ea links here from Part E and session L6.

## Structure

| File | Role |
|---|---|
| `_site.json` | Config. Static, `listed: false`, `noindex: true`. |
| `index.html` | Hand-written. Self-contained: inline CSS, JS and SVG. Shell copied from ea-prep-02-aws. No backup other than git. |
| `_glossary.json` | Site override: PDF (the shared entry carries a site-specific "bill image" note). |

## Editing rules

**Everything here is hand-written.** Edit `index.html`, then run `python _build/build.py --acronyms-fix` and confirm `--acronyms` reports "All acronyms have tooltips."

The robots meta is hand-maintained. Progress ticks use localStorage prefix `agg.`, keyed by card id (`plan-sessions`, `c-check`, `f-*`, `p-*`, `ch-*`, `b-*`, `fw-*`, `r-*`, `cheat-card`).

SVG arrows: shared marker `#ar` in a hidden `<svg id="defs">`; `line.ar` (one-way) and `line.ar2` (two-way). Rect classes: `band` (worker or code), `ou` (control), `wr` (warning or high cost), `hu` (human, also on circles).

## Content standards

General content only; no client material. Sources graded [P]/[S] with check dates; `ver` marks on version-sensitive facts. The vendor-name mapping in 2.10 is the guide's own synthesis and says so.

## Time-sensitive content

- MCP current spec 2026-07-28.
- Microsoft Agent Framework 1.0 (Apr 2026); Semantic Kernel and AutoGen in maintenance.
- Anthropic multi-agent research figures (90.2%, 4x and 15x tokens) from the June 2025 post.
- Cognition follow-up post (Apr 2026).
- Course details (lengths, certificates) for DeepLearning.AI, Anthropic Academy, Hugging Face, Kaggle.

## Open items

- Add more video talks once their URLs are verified.
- The shared glossary's PDF entry is site-specific ("Here, the bill image"); consider making the shared entry generic.
