# aigov — state of play

*Upload to project knowledge. Update when something material changes; delete lines that stop being true.*

**Last updated:** 14 September 2026
**Market evidence in the documents:** checked 17 August 2026

---

## 1. What exists

| Thing | Where |
|---|---|
| Live site | https://iprash.github.io/aigov/ |
| Sibling site | https://iprash.github.io/TPM/ (Senior TPM interview prep) |
| Landing page | https://iprash.github.io/ |
| Repo | github.com/iPrash/iprash.github.io |
| Local | `C:\Users\ipras\OneDrive\Documents\Claude\iprash.github.io` |

## 2. Repository layout

```
iprash.github.io/              one git repo, branch: main
├── .nojekyll                  critical — see §6
├── .gitignore                 Thumbs.db, desktop.ini, .DS_Store
├── index.html                 landing page listing both sites
├── TPM/                       static, unrelated to aigov
└── aigov/
    ├── index.html             GENERATED — plan hub
    ├── playbook.html          GENERATED — 11-part playbook
    ├── resources.html         GENERATED — 12-section resource library
    ├── playbook.md            SOURCE, ~15,000 words
    ├── resources.md           SOURCE, ~3,000 words, 100+ graded links
    ├── README.md              deployment notes
    ├── assets/
    │   ├── style.css          hand-maintained
    │   └── app.js             hand-maintained
    └── _build/
        ├── build.py           md → html
        └── index_template.html  home page structure
```

GitHub Pages: **Deploy from a branch → main → / (root)**. No Actions workflow, no Jekyll.

## 3. Build and deploy

```powershell
cd C:\Users\ipras\OneDrive\Documents\Claude\iprash.github.io\aigov
python _build\build.py          # needs: pip install markdown
cd ..
git add -A
git commit -m "..."
git push
```

Then check `github.com/iPrash/iprash.github.io/actions` is green and hard-refresh the browser (Ctrl+Shift+R).

Verify:

```powershell
curl.exe -sI https://iprash.github.io/aigov/ | Select-Object -First 1
curl.exe -sI https://iprash.github.io/aigov/assets/style.css | Select-Object -First 1
```

## 4. The content in one page

**The brief.** A fashion brand, XYZ Corp, wants three workstreams: (1) AI consumption and governance on their OpenAI estate, converting visibility into renewal leverage; (2) a multi-model access strategy after a Copilot trial was withdrawn and teams objected; (3) a GenAI landscape review against their current estate.

**The read.** Behind eleven deliverables sit three decisions: **D1** what to sign at renewal, **D2** one model platform or several, **D3** where to build, buy or partner. Every artifact is written to serve one of them.

**Playbook structure.**

| Part | Content |
|---|---|
| 0 | How to use it |
| 1 | Read of the brief — the five traps, operating principles, success criteria |
| 2 | Engagement design — spine, phases, renewal-driven schedule, RACI, deliverable specs, first five days |
| 3 | WS1 consumption — data acquisition, truth layer schema, seven-cohort segmentation, decision matrix, seven-layer governance, negotiation brief |
| 4 | WS2 multi-model — Copilot post-mortem as trust repair, workload mapping, evaluation framework, Bedrock assessment, gateway architecture, cost model, revisit triggers |
| 5 | WS3 landscape — 12-domain fashion taxonomy, vendor scorecard, research protocol, estate cross-check, build/buy/partner/consume rules |
| 6 | The CoE build — archetype, charter, decision rights, roles, stage gates, risk tiering, 90/180/365 |
| 7 | Risk and compliance — EU AI Act position, fashion-specific exposures, GenAI security |
| 8 | Templates |
| 9 | Anti-patterns |
| 10 | Twelve-week calendar |
| 11 | Making it a reference engagement |

**Resource library.** Section 0 is a two-week study sprint. Sections 1–12 are graded sources: OpenAI admin and commercial docs, Copilot billing, Bedrock, FinOps 2026, AI Act and standards, OWASP and MITRE, DORA and SPACE, gateways and evals, CoE operating models, fashion retail, books, and a pre-ship checklist.

## 5. Site behaviour

- **Week ruler** on the home page — 13 columns, five phase bands, milestone pins, each week links to the calendar in Part 10.
- **Renewal calculator** — enter a date, get the backward schedule (R−150 data access, R−135 baseline locked, R−120 BATNA costed, R−105 brief approved, R−90 first session). Past milestones turn red; under 150 days triggers a compressed-plan warning.
- **Countdown** to the 31 Aug 2026 Codex model retirement.
- **Progress tracking** — every part and section heading has a Mark read toggle; sidebar shows a count and bar; playbook and resources tracked separately.
- **Contents filter**, scroll-spy, light/dark theme, print styles.
- All state is localStorage. Nothing syncs between devices. Keys are namespaced `xyzai.*`.

## 6. Things that broke, and why

| Symptom | Cause | Fix |
|---|---|---|
| Themed 404 at `/aigov/` despite files being in the repo | Repo had a Jekyll scaffold; `_config.yml` had a YAML error at line 15; build failed; Pages kept serving the last good build | Added `.nojekyll`, deleted `_config.yml`, `Gemfile`, `index.md`, `about.md` |
| Empty folder pushed | Nested `.git` inside a site subfolder becomes a submodule pointer | Remove nested `.git` before `git init` |
| — | `robocopy` returns exit code 1 on success | Not an error |
| — | Bare `curl` in PowerShell is `Invoke-WebRequest` | Use `curl.exe` |

Final structure was reached by deleting the repo and starting clean. Old `github.com/iPrash/TPM` repo should be archived once `/TPM/` is confirmed working from the new setup.

## 7. Market facts the documents rely on

All checked 17 Aug 2026. **Re-verify before reuse.**

- OpenAI shipped a Global Admin Console with credit analytics and spend controls (June 2026): group limits, user overrides, member cost visibility, Codex analytics API, Cost API.
- Codex moved to token-aligned credit pricing April 2026 (Enterprise 23 April). Pre-April data is not comparable.
- GPT-5.4 and GPT-5.4 mini retire in Codex for ChatGPT-signed-in users on **31 August 2026**, replaced by GPT-5.6 Terra and Luna.
- ChatGPT Enterprise workspaces migrating from weekly role-based to monthly usage limits during August 2026.
- GitHub Copilot moved to usage-based AI Credits **1 June 2026**. Business $19/user/mo including $19 credits; Enterprise $39 including $39. Completions free and unmetered. Org-pooled credits, user budgets.
- Bedrock: on-demand, batch (~50% discount), provisioned throughput. AWS became a third-party cloud distributor for OpenAI frontier models (Feb 2026) — relevant to the concentration-risk argument.
- **EU AI Act:** Regulation (EU) 2026/1744 (Digital Omnibus) in force 27 July 2026. Article 50 transparency applies from **2 August 2026** — not deferred. Art 50(2) legacy marking plus new prohibitions from 2 Dec 2026. Annex III high-risk deferred to 2 Dec 2027; Annex I to 2 Aug 2028. Art 4 AI literacy already applies.
- FinOps Framework 2026 introduced Scopes and FinOps for AI; 98% of practices now manage AI spend; innovation scopes should tolerate higher waste.

## 8. The learning plan

Method: build an artifact each week, read the reference when stuck.

| Week | Build | Read |
|---|---|---|
| 1 | Consumption baseline and segmentation on real personal usage data, using the §3.2 schema and §3.3 measures | §3.1–3.3, §3.5 |
| 2 | LiteLLM gateway locally, two providers, virtual key with a budget. Then a 30-example eval set in promptfoo across two models | §4.3–4.6 |
| 3 | The four-page directional guidance note from §4.7 for a real or invented org | §4.7, §5.5, Part 6, §7.1 |

Three-hour priority order if time collapses: §3.7 negotiation brief → §4.0–4.1 Copilot analysis → Part 6 CoE → §7.1 AI Act → Part 9 anti-patterns.

## 9. Open items

- Archive `github.com/iPrash/TPM` once `/TPM/` is confirmed serving from the consolidated repo.
- Nothing in the documents has been re-verified since 17 Aug 2026.
- Considered and not done: shared CSS across TPM and aigov, a search across both documents, cross-device progress sync.

