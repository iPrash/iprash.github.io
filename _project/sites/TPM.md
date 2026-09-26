# TPM — site brief

**URL:** https://iprash.github.io/learn/TPM/
**Moved:** 25 Sept 2026, from /TPM/. A redirect stub remains at the old path.
**Type:** static
**Created:** before the repo consolidation, Sept 2026

## What it is

A Senior Technical Program Manager interview preparation guide. Covers system design, program
sense and behavioural preparation, with progress tracking built into the page.

## Why it exists

Interview preparation I can work through from any device.

## Structure

| File | Role |
|---|---|
| `_site.json` | Config. Static — no `pages` list, so the build leaves the site alone. |
| `index.html` | Hand-written. Self-contained. |

## Editing rules

**Everything here is hand-written.** The build script does not generate any file in this folder.
Edit `index.html` directly.

**The `robots` meta is hand-maintained.** This site is unlisted and noindexed, but because it is
static the build cannot inject the tag the way it does for aigov and frontier-engineer. The
`<meta name="robots" content="noindex,nofollow">` in `index.html` was added by hand on
25 Sept 2026. If `index.html` is ever regenerated or replaced wholesale, put it back.

The only thing the build reads from this folder is `_site.json`, and only to place the card on
the landing page.

## Open items

- Content has not been reviewed since the repo consolidation.
- If it grows, consider converting to a generated site on the aigov pattern. Not worth doing
  while it is a single page.
- `index_old.html` was a pre-consolidation draft, superseded by the current
  `index.html` (53 insertions / 25 deletions newer). Removed Sept 2026,
  recoverable from git at c0eb9a6.
