# FIFA26 — site brief

**URL:** https://iprash.github.io/FIFA26/
**Type:** static, hand-written single-file app with a service worker
**Created:** June 2026, moved into this repo September 2026

## What it is

MyFIFA26, a what-if analyser for the 2026 World Cup. Group standings, a clinch checker,
third-place qualification worked out from FIFA's Annex C table, and a knockout bracket the user
picks through. Live scores come from ESPN's public API at runtime.

The first project on the landing page.

## Why it is here

It used to be its own repo, `github.com/iPrash/FIFA26`, serving `/FIFA26/` as a project site.
That is the same arrangement that collided with the user site over `/TPM/` in Sept 2026 and
forced a repo rebuild. Consolidating removes the second claim on the path.

**How the move actually went.** Unpublishing the old repo's Pages site was not enough. With the
files committed here and the deployment green, `/FIFA26/` still returned 404 while the landing
page and `/learn/` served correctly from the same commit, because a repo *named* `FIFA26`
keeps its claim on that path. Renaming it to `FIFA26-archive` released the path immediately.
Waiting did not help and archiving would not have. Anyone consolidating the next project in
should rename that project's repo first.

## Structure

| File | Role |
|---|---|
| `index.html` | The entire app, HTML + CSS + JS in one file, ~140KB |
| `r32-bracket.js` | Round of 32 bracket logic |
| `scores.json` | Match results: scores, goal scorers, extra time, penalties. The source of truth for results |
| `sw.js` | Service worker. Network-first same-origin, cache-first for flag images |
| `manifest.json` | PWA manifest |
| `icons/` | PWA icons, 192, 512, and SVG |
| `CLAUDE.md` | Its own project instructions, for Claude Code sessions working in this folder |
| `CHANGELOG.md`, `README.md`, `LICENSE` | MIT |
| `_site.json` | Config. Static, so the build never touches any of the above |

## Editing rules

**Everything here is hand-written. The build does not generate any of it.** `_site.json` exists
only so the folder is accounted for in the registry.

**The folder name cannot change.** A service worker's scope is its own directory, and the
manifest and precache list are relative to it. Renaming the folder changes the scope and
orphans every installed copy on someone's phone.

**To finalize a match, only update `scores.json`.** Its own `CLAUDE.md` explains the data model;
read that before touching the app.

**One file, zero build, zero dependencies** is a hard constraint of the app itself, stated in
its `CLAUDE.md`. It must still run by opening `index.html` directly from disk.

## Checked before publishing

Reviewed on 25 Sept 2026 before the move: no API keys or tokens, no absolute root-relative
paths, and the only external calls are ESPN's public API and flagcdn.com. The service worker
and manifest use relative paths throughout, so the move did not change behaviour.

## Open items

- Screenshot for the landing page card, at `assets/shots/FIFA26.png`. Until then the card shows
  a generated tile.
- `github.com/iPrash/FIFA26` was renamed to `FIFA26-archive` on 25 Sept 2026, which is what
  made `/FIFA26/` serve from here. Archiving it too is optional tidiness.
- The icon files were copied in by hand, because binaries moved through the Claude file bridge
  come back with C2PA provenance metadata added and are no longer byte-identical.
