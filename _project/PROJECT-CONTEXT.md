# iprash.github.io — state of play

*Upload to project knowledge. Update when something material changes.*

**Last updated:** 14 September 2026

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

| Slug | URL | Title | Type | Brief |
|---|---|---|---|---|
| `TPM` | /TPM/ | Senior TPM interview prep | Static HTML | `_project/sites/TPM.md` |
| `aigov` | /aigov/ | AI governance & multi-model strategy | Generated from markdown | `_project/sites/aigov.md` |

Read the site brief before working on a site. Conventions differ between them.

## 3. Layout

```
iprash.github.io/
├── .nojekyll                    disables Jekyll — do not delete
├── .gitattributes               * text=auto eol=lf
├── .gitignore                   Thumbs.db, desktop.ini, .DS_Store, *.zip
├── index.html                   GENERATED landing page
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
├── _build/
│   ├── build.py
│   └── templates/landing.html
└── _project/
    ├── PROJECT-INSTRUCTIONS.md
    ├── PROJECT-CONTEXT.md       this file
    ├── NEW-SITE.md
    └── sites/{TPM.md,aigov.md,_TEMPLATE.md}
```

`_build/` and `_project/` are published (harmless — no index.html, nothing links to them) but
are not part of any site.

## 4. How the build works

`build.py` globs `*/_site.json` to discover sites. Each config drives:

- the landing page card (`title`, `blurb`, `order`, `listed`)
- the nav bar, derived from `pages` so it stays in sync automatically
- page titles, descriptions and the footer line
- whether the site is generated at all — a config without `pages` is static and untouched

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

## 8. Open items

- Archive `github.com/iPrash/TPM` once `/TPM/` is confirmed working from this repo.
- A third site is planned. Follow `_project/NEW-SITE.md`.
- `aigov` evidence was last checked 17 Aug 2026 and includes at least one now-passed date.
  See its site brief.
