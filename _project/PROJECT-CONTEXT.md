# iprash.github.io — state of play

*Upload to project knowledge. Update when something material changes.*

**Last updated:** 25 September 2026

---

## 1. The setup

| Thing | Value |
|---|---|
| Repo | github.com/iPrash/iprash.github.io |
| Live | https://iprash.github.io/ |
| Local | `C:\Users\ipras\OneDrive\Documents\Claude\iprash.github.io` |
| Branch | `main` |
| Pages source | Deploy from a branch → main → / (root) |
| Jekyll | Disabled via `.nojekyll` |
| Build dependency | `markdown` (pip). Nothing else. |

One repo, one Pages site, several subsites at `/<slug>/`.

## 2. Sites

The root page is a **project index**. Study material is deliberately not listed on it.

**Projects** (shown on the landing page, driven by `_build/projects.json`):

| Slug | URL | Title | Type | Brief |
|---|---|---|---|---|
| `FIFA26` | /FIFA26/ | MyFIFA26, World Cup 2026 what-if analyser | Static HTML, PWA | `_project/sites/FIFA26.md` |

**Learning sites** (unlisted and noindexed, reached only through /learning/):

| Slug | URL | Title | Type | Brief |
|---|---|---|---|---|
| `learning` | /learning/ | Hub listing the three study sites | Static HTML | this file |
| `frontier-engineer` | /frontier-engineer/ | Frontier Engineer: Lead → Principal | Generated from markdown | `_project/sites/frontier-engineer.md` |
| `aigov` | /aigov/ | AI governance & multi-model strategy | Generated from markdown | `_project/sites/aigov.md` |
| `TPM` | /TPM/ | Senior TPM interview prep | Static HTML | `_project/sites/TPM.md` |

Read the site brief before working on a site. Conventions differ between them.

## 3. Layout

```
iprash.github.io/
├── .nojekyll                    disables Jekyll — do not delete
├── .gitattributes               * text=auto eol=lf
├── .gitignore                   Thumbs.db, desktop.ini, .DS_Store, *.zip
├── index.html                   GENERATED project index, from _build/projects.json
├── assets/shots/                landing page screenshots, <slug>.png, optional
├── FIFA26/                      static single-file PWA, moved in from its own repo
├── learning/                    static hub, unlisted, reached from the footer mark
├── TPM/
│   ├── _site.json               static, no pages list
│   └── index.html               hand-written
├── aigov/
│   ├── _site.json
│   ├── index.html               GENERATED
│   ├── playbook.html            GENERATED
│   ├── resources.html           GENERATED
│   ├── playbook.md              SOURCE
│   ├── resources.md             SOURCE
│   ├── _index_template.html     home page structure
│   ├── README.md
│   └── assets/{style.css,app.js}   hand-maintained
├── frontier-engineer/
│   ├── _site.json
│   ├── index.html               GENERATED
│   ├── roadmap.html             GENERATED
│   ├── resources.html           GENERATED
│   ├── roadmap.md               SOURCE
│   ├── resources.md             SOURCE
│   ├── _index_template.html     home page structure
│   └── assets/{style.css,app.js}   hand-maintained, copied from aigov's engine with the
│                                    localStorage prefix changed to avoid cross-site collision
├── _build/
│   ├── build.py
│   ├── projects.json            the portfolio list shown on the landing page
│   └── templates/landing.html
└── _project/
    ├── README-FIRST.md          entry point — Claude reads this first
    ├── INSTRUCTIONS-FIELD.txt   the text pasted into the Claude Project settings
    ├── PROJECT-INSTRUCTIONS.md  full working rules
    ├── PROJECT-CONTEXT.md       this file
    ├── NEW-SITE.md
    └── sites/{TPM.md,aigov.md,frontier-engineer.md,_TEMPLATE.md}
```

`_build/` and `_project/` are published (harmless — no index.html, nothing links to them) but
are not part of any site.

## 4. How the build works

`build.py` globs `*/_site.json` to discover sites. Each config drives:

- the nav bar, derived from `pages` so it stays in sync automatically
- page titles, descriptions and the footer line
- whether the site is generated at all — a config without `pages` is static and untouched
- `noindex: true` adds a `robots` meta to every page the build generates for that site

**The landing page no longer comes from the site list.** It is built from
`_build/projects.json`, which is a separate list on purpose: a project may live in another
repo, or be a link with no page here at all. A folder having a `_site.json` no longer puts it
on the front page. See §9.

```
python _build/build.py             everything
python _build/build.py aigov       one site
python _build/build.py --landing   landing page only
python _build/build.py --check     report changes, write nothing
```

Output is LF regardless of platform. The script prints `unchanged` for files it did not need
to rewrite, so a clean run on untouched content should report almost everything unchanged.

## 5. Publish

```powershell
cd C:\Users\ipras\OneDrive\Documents\Claude\iprash.github.io
python _build\build.py
git add -A
git commit -m "..."
git push
```

Then check `github.com/iPrash/iprash.github.io/actions` is green and hard-refresh (Ctrl+Shift+R).

```powershell
curl.exe -sI https://iprash.github.io/ | Select-Object -First 1
curl.exe -sI https://iprash.github.io/aigov/ | Select-Object -First 1
curl.exe -sI https://iprash.github.io/aigov/assets/style.css | Select-Object -First 1
```

## 6. History — problems already solved

| Symptom | Cause | Resolution |
|---|---|---|
| Themed 404 at `/aigov/` despite files being present | Repo had a Jekyll scaffold; `_config.yml` had a YAML error at line 15; build failed; Pages served the last good build | Added `.nojekyll`, deleted `_config.yml`, `Gemfile`, `index.md`, `about.md` |
| Empty folder pushed | Nested `.git` inside a site subfolder becomes a submodule pointer | Remove nested `.git` before `git init` |
| Files show modified, `git diff` empty | Python wrote CRLF on Windows; `autocrlf=true` normalised it on comparison | `build.py` writes LF explicitly; `.gitattributes` enforces it; `git add -A` clears the flag |
| — | `robocopy` returns exit code 1 on success | Not an error |
| — | Bare `curl` in PowerShell is `Invoke-WebRequest` | Use `curl.exe` |
| `device_bash` (Claude's shell on this machine) dead: "no Plan9 drive shares mounted" | Windows update KB5124008/KB5124012 (8 Sept 2026) broke Cowork's Plan9 folder-sharing on Windows. Confirmed by Anthropic and Microsoft; no fix shipped yet as of 14 Sept 2026 | No repo-side fix. Workaround in the meantime: build/generate files in Claude's cloud workspace instead of on this machine, then transfer with `device_stage_files` / `device_commit_files`, which still work. Used to build the `frontier-engineer` site. Revert to running `build.py` directly on this machine once Microsoft ships the fix — check status.claude.com |

Repo was deleted and recreated clean in Sept 2026 after the TPM project-site repo and the user
site repo both tried to serve `/TPM/`. Old `github.com/iPrash/TPM` should be archived once
`/TPM/` is confirmed serving from this repo.

## 7. Deliberate decisions

- **Per-site assets, not shared.** Duplication is the price of each site being independently
  restyleable and of relative paths that work at any depth. Do not consolidate into a root
  `/assets/`.
- **No framework, no bundler, no SSG.** One Python script and one dependency. These sites must
  still work untouched in five years.
- **localStorage only.** No accounts, no sync, no analytics. Progress does not follow between
  devices, and that is accepted.
- **Site tooling at repo root, not per site.** One build script serves all sites.
- **The landing page is a project index, not a directory of everything here.** Study material
  is reachable but not advertised. What is on the front page is decided by
  `_build/projects.json` alone.
- **Hidden means tidy, not private.** This repo is public, so anyone can read every folder
  whatever the landing page links to. The noindex tags keep the study sites out of search
  results; they do not restrict access, and nothing here should be treated as if they did.
- **localStorage keys are namespaced per site** (e.g. aigov's `xyzai.*`, frontier-engineer's
  `fe.*`). All sites share one origin, so two sites reusing the same key prefix would silently
  overwrite each other's reading progress. Pick a short, distinct prefix for every new site.

## 9. The portfolio list

`_build/projects.json` holds one entry per card, in display order:

```json
{
  "slug": "FIFA26",
  "title": "MyFIFA26",
  "url": "FIFA26/",
  "repo": "https://github.com/iPrash/FIFA26",
  "blurb": "One or two sentences.",
  "tags": ["Single file", "No dependencies"],
  "status": "Live",
  "glyph": "26",
  "accent": "#1E6B4F",
  "listed": true
}
```

- `url` is relative when the path is served from iprash.github.io, so an entry does not need
  editing when a project is consolidated into this repo from its own.
- A card uses `assets/shots/<slug>.png` when that file exists, and falls back to a generated
  tile built from `glyph` and `accent` when it does not. The check happens at build time.
  Roughly 16:10 suits the card; about 1200px wide is plenty.
- `listed: false` parks an entry without deleting it.
- Adding a project needs no folder here. An entry pointing at an external URL is enough.

## 10. Open items

- Archive `github.com/iPrash/TPM` once `/TPM/` is confirmed working from this repo.
- `aigov` evidence was last checked 17 Aug 2026 and includes at least one now-passed date.
  See its site brief.
- `frontier-engineer` added Sept 2026. Its resource links were checked 14 Sept 2026; see its
  site brief for the re-verification cadence.
- **No `robots.txt` yet, deliberately.** A disallow would stop crawlers fetching the study
  pages, and a crawler that cannot fetch a page never sees its noindex, so anything already
  indexed could sit there indefinitely. Let the noindex tags de-index them first, over a few
  weeks, then add a disallow if it still seems worth it.
- The FIFA26 card shows the fallback tile until a screenshot is added at
  `assets/shots/FIFA26.png`.
- Other projects to write cards for when ready: FlippedMath, Language Conversation,
  Progressive_ACV. Each needs a line of description and a decision on whether it goes public.
- The old `github.com/iPrash/FIFA26` repo should be archived now the app is served from here.
  Unpublishing its Pages site is reversible: any future commit to its publishing branch
  republishes it and the `/FIFA26/` collision returns. Archiving makes it read-only, which
  makes the unpublish stick.
- `device_bash` (Claude's shell on this machine) has been down since 8 Sept 2026 pending a
  Microsoft fix for the Plan9 regression. See §6. Nothing to do here except wait and use the
  stage/commit workaround for anything that needs a build step.
