# Read this first

You are working on **iprash.github.io** — one GitHub Pages repo publishing several independent
reference sites at `iprash.github.io/<slug>/`. Prash is the sole author. He uses these sites to
upskill and to work from.

This file is the entry point. It tells you what to read and when. Read it fully, then follow the
routing table below before doing anything else.

## Step 1 — always, at the start of a session

Read these two, in order:

1. **`_project/PROJECT-INSTRUCTIONS.md`** — the working rules. How the build works, what is
   generated versus hand-written, writing style, content standards, and the gotchas that have
   already cost real time. Non-negotiable.
2. **`_project/PROJECT-CONTEXT.md`** — current state. Repo layout, the site list, deploy
   commands, history of problems already solved, deliberate design decisions, open items.

Together these are about 12KB. Read them properly rather than skimming.

## Step 2 — route by task

| If the task is | Read next |
|---|---|
| Working on a specific site's content | `_project/sites/<slug>.md` — **always, before editing anything in that folder**. Briefs are named by slug even though study sites now live at `learn/<slug>/` |
| Adding a new site | `_project/NEW-SITE.md` |
| Changing the build, or debugging it | `_build/build.py` |
| Changing a site's styling or interactive behaviour | that site's `assets/style.css` and `assets/app.js` |
| Changing a site's home page structure | that site's `_index_template.html` |
| Deploy, git or GitHub Pages trouble | `PROJECT-CONTEXT.md` §5 and §6 — the problem may already be solved there |

The site briefs in `_project/sites/` are the most important thing in this folder. Each one records
**which files in that site are generated and which are hand-written**, and the answer differs
between sites. Getting this wrong destroys work: one site's `index.html` is disposable build
output, another's is a hand-written file with no backup other than git.

## Step 3 — confirm before acting

At the start of a session, confirm out loud that you can see the repo on disk and name the sites
you found. If you cannot read files, say so immediately rather than working from assumption.

Before any edit, state which files you intend to change and whether each is generated or
hand-written. Prash will catch a wrong answer; a silent wrong edit destroys content.

## The four rules that matter most

Stated here as well as in PROJECT-INSTRUCTIONS.md, because being wrong about any of them is
expensive.

1. **Never hand-edit a generated file.** The next build destroys the change. The site brief says
   which files are generated.
2. **`.nojekyll` must exist at the repo root.** Without it GitHub Pages runs Jekyll, which
   processes `.md` files instead of serving them and can fail the whole build on an unrelated
   config file. This once cost an afternoon.
3. **Asset paths stay relative.** A leading slash resolves to the domain root and 404s from
   inside a subfolder.
4. **No frameworks, no bundlers, no dependencies beyond `markdown`.** These sites must still work
   untouched in five years. If a change seems to need tooling, say so and discuss it rather than
   drifting into it.

## Maintaining this folder

`_project/` is documentation for you, not part of any site. When something material changes —
a new site, a changed workflow, a solved problem worth recording — update the relevant file and
tell Prash you did. Stale context is worse than none, because it is trusted.
