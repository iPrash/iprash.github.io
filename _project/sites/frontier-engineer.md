# frontier-engineer — site brief

**URL:** https://iprash.github.io/frontier-engineer/
**Type:** generated
**Created:** September 2026
**Evidence last checked:** 14 September 2026 (resource links only; see Time-sensitive content)

## What it is

A personal learning roadmap for progressing from Lead Frontier Engineer to Principal
Frontier Engineer at my own employer. It restructures the two roles' job descriptions into
13 study parts, in the same order as the job descriptions' own areas of responsibility, each
paired with free reading, video, and hands-on resources.

## Why it exists

To have one working reference for closing the Lead-to-Principal gap: what to learn, in what
order, from which free sources, plus a standing checklist of the evidence a promotion case
actually needs.

## A privacy decision that shapes this site

The source material is my own company's anonymized Lead and Principal Frontier Engineer job
descriptions (company name already stripped before I shared them). Because iprash.github.io
is public, and because the JD includes an internal rate card and other narrowly-internal
figures, this site never publishes that text verbatim. `roadmap.md` and `resources.md` are my
own restructuring of the material, in my own words. The raw JD is kept as a private doc in
the "Personal Learning Portal" claude.ai Project (not in this repo, not published anywhere)
so a future session can rebuild or extend this site without me re-pasting it.

If a future edit is tempted to quote the JD directly for precision, don't. Paraphrase instead
or ask whether the wording is worth the exposure.

## Structure

| File | Role |
|---|---|
| `_site.json` | Config, nav, footer |
| `index.html` | **GENERATED** from `_index_template.html`, the landing page |
| `roadmap.html` | **GENERATED** from `roadmap.md` |
| `resources.html` | **GENERATED** from `resources.md` |
| `roadmap.md` | **SOURCE**, the 13-part learning path |
| `resources.md` | **SOURCE**, the free-resource library, numbered to match the roadmap |
| `_index_template.html` | Home page body. `{{HEAD}}`, `{{NAV}}`, `{{FOOTER}}` filled by the build |
| `assets/style.css` | Hand-maintained. Copied from aigov's engine, accent color changed only |
| `assets/app.js` | Hand-maintained. Copied from aigov's engine, with two real changes: the localStorage key prefix was renamed from aigov's `xyzai.` to this site's own `fe.` (needed, since both sites share the iprash.github.io origin and reusing the same prefix would let one site's reading progress overwrite the other's), and the aigov-specific renewal-date calculator was removed since this site has no equivalent feature |

## Editing rules

**Never hand-edit `index.html`, `roadmap.html`, or `resources.html`.** Edit the markdown or
the index template, then `python _build\build.py frontier-engineer`.

**Heading IDs are load-bearing**, same as aigov. Progress is stored in localStorage keyed by
heading ID, derived from heading text. Renaming a Part or section heading resets that
section's read/checklist state.

**Checklist items** (`- [ ]` lines in the markdown) become working checkboxes client-side,
via `app.js`, not through a markdown extension. This is consistent with how aigov's
checklists work.

## Content standards

Lean, direct sentences. No verbatim JD text (see above). Every resource in `resources.md` was
checked before publishing: fetched and read, not just found in a search result, with its
free/paid status confirmed where it wasn't obvious. Where a platform mixes free and paid
content on the same page (Snowflake, Oracle, SAP Learning, Coursera Professional
Certificates), the entry says so rather than implying the whole platform is free.

## Time-sensitive content

Resource links were checked 14 September 2026. Free-tier terms on third-party training
platforms (Coursera, AWS Skill Builder, Google Skills, Snowflake, Oracle, SAP Learning)
change without notice. Re-verify a link's price before recommending this site to someone
else, and re-check the whole resource list roughly twice a year.

## Open items

- No dynamic "promotion readiness %" meter. Considered for v1 and deliberately deferred: it
  would need new JavaScript logic beyond the shared engine, and the Part 12 checklist plus
  the existing per-heading progress toggles cover the same need for now.
- The roadmap doesn't yet reflect any changes to the underlying job descriptions since
  14 September 2026. If the JD changes materially, the private copy in the claude.ai Project
  needs updating first, then this site's structure re-checked against it.
