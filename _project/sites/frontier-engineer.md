# frontier-engineer — site brief

**URL:** https://iprash.github.io/frontier-engineer/
**Type:** generated
**Created:** September 2026
**Evidence last checked:** 14 September 2026 (resource links only; see Time-sensitive content)

## What it is

A two-stage personal learning path built from my employer's Lead and Principal Frontier
Engineer job descriptions. Stage 1 (Parts 1 to 11) covers everything the Lead role requires and
ends in a readiness checklist. Stage 2 (Parts 12 to 18) covers what Principal adds on top and
ends in a second checklist plus the L1 to L2 delta. Part 0 orients and calibrates the starting
point.

Nineteen parts total, following the job descriptions' own areas of responsibility in their own
order, each paired with free reading, video, and hands-on resources.

## Why it exists

The goal is Principal Frontier Engineer, reached through Lead. I'm not in either role yet, so
the site has to work as a path into the first one and then through to the second, not as a
reference for someone already doing the job.

This was wrong in the first version, which assumed I was already a Lead and only mapped the
Lead-to-Principal gap. Corrected the same day. If a future edit is tempted to compress the two
stages back into one, don't: the ordering is the point.

## A privacy decision that shapes this site

The source material is my employer's anonymized Lead and Principal Frontier Engineer job
descriptions (company name stripped before I shared them). Because iprash.github.io is public,
and because the JD includes an internal rate card and other narrowly-internal figures, this
site never publishes that text verbatim. `roadmap.md` and `resources.md` are my own
restructuring, in my own words.

The raw JD is kept as a private doc in the "Personal Learning Portal" claude.ai Project, not in
this repo and not published anywhere, so a future session can rebuild or extend the site
without me re-pasting it.

Two related rules:

1. If a future edit wants to quote the JD directly for precision, don't. Paraphrase, or ask
   whether the wording is worth the exposure.
2. No employer or client names on this site. Part 0.4 discusses where I'm starting from in
   terms of role shape only, deliberately, for the same reason.

## Structure

| File | Role |
|---|---|
| `_site.json` | Config, nav, footer |
| `index.html` | **GENERATED** from `_index_template.html`, the landing page |
| `roadmap.html` | **GENERATED** from `roadmap.md` |
| `resources.html` | **GENERATED** from `resources.md` |
| `roadmap.md` | **SOURCE**, the 19-part, two-stage learning path |
| `resources.md` | **SOURCE**, the free-resource library, numbered to match |
| `_index_template.html` | Home page body. `{{HEAD}}`, `{{NAV}}`, `{{FOOTER}}` filled by the build |
| `assets/style.css` | Hand-maintained. Copied from aigov's engine, accent color changed only |
| `assets/app.js` | Hand-maintained. Copied from aigov's engine, with two real changes: the localStorage key prefix renamed from aigov's `xyzai.` to this site's own `fe.` (needed, since both sites share the iprash.github.io origin and a shared prefix would let one site's reading progress overwrite the other's), and aigov's renewal-date calculator removed since this site has no equivalent feature |

## Editing rules

**Never hand-edit `index.html`, `roadmap.html`, or `resources.html`.** Edit the markdown or the
index template, then `python _build\build.py frontier-engineer`.

**Heading IDs are load-bearing**, same as aigov. Progress and checklist state live in
localStorage keyed by heading ID, derived from heading text. Renaming a Part or section heading
resets that section's state. The two-stage restructure renamed most headings, which was free
only because it happened before the site was pushed. It won't be free again.

**Part headings carry a stage prefix** (`Lead · Part 4`, `Principal · Part 13`) so the sidebar
contents list shows which stage each part belongs to without opening it. Keep that convention
for any new part.

**Checklist items** (`- [ ]` lines in the markdown) become working checkboxes client-side via
`app.js`, not through a markdown extension. Same as aigov.

**One line per paragraph in the markdown sources.** The build enables `nl2br`, so every newline
inside a paragraph becomes a literal `<br>`. Both source files were first written hard-wrapped
at ~90 columns and rendered with a break at every wrap point; they were unwrapped and rebuilt
on 14 Sept 2026. The lines look uncomfortably long in an editor and correct on the page. This is
now also recorded in `_project/NEW-SITE.md` and the gotchas list in
`_project/PROJECT-INSTRUCTIONS.md`.

## Content standards

Lean, direct sentences. No verbatim JD text. No employer or client names.

Every resource in `resources.md` was opened and read before publishing, with its free/paid
status confirmed where it wasn't obvious. Where a platform mixes free and paid content
(Snowflake, Oracle, SAP Learning), the entry says so. Resources that turned out not to be free
are listed in a "Checked and rejected" section at the bottom of the page with the reason, so
neither I nor a future session re-finds them and assumes they're free.

Parts that can't be practiced without holding the role end with a **practice without the job**
line naming the closest honest proxy. Keep that convention: it's what makes Stage 1 usable by
someone not yet in the seat.

## Time-sensitive content

Resource links were checked 14 September 2026. Free-tier terms on third-party training
platforms (AWS Skill Builder, Google Skills, Snowflake, Oracle, SAP Learning, Coursera) change
without notice. Re-check the whole list roughly twice a year.

## Open items

- No dynamic "readiness %" meter across the two checklists. Considered and deliberately
  deferred: it needs new JavaScript beyond the shared engine, and the Part 11 and Part 18
  checklists plus per-heading progress toggles cover the need for now.
- Part 0.4's read on which Stage 1 parts are already covered is a hypothesis, written to be
  corrected. Update it once the Part 11 checklist has been worked through honestly.
- The roadmap reflects the job descriptions as of 14 September 2026. If they change materially,
  update the private copy in the claude.ai Project first, then re-check this site's structure
  against it.
