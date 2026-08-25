# aigov — XYZ AI engagement workspace

A three-page static site for the XYZ Corp AI consumption, multi-model access and GenAI landscape engagement. No build step, no dependencies, no framework. Drop the folder into a GitHub Pages repo and it works.

## Files

```
aigov/
├── index.html          Plan hub — week ruler, renewal calculator, first-five-days list
├── playbook.html       The full engagement playbook (11 parts)
├── resources.html      The annotated resource library (12 sections)
├── playbook.md         Markdown source, kept alongside and linked from the page footer
├── resources.md        Markdown source
└── assets/
    ├── style.css
    └── app.js
```

## Deploying to iprash.github.io

Put the folder inside the repo rather than at the root, so it does not clash with anything already published there:

```bash
cd iprash.github.io
mkdir -p aigov
cp -r ~/Downloads/aigov/* aigov/
git add aigov
git commit -m "Add aigov: XYZ AI engagement workspace"
git push
```

Live at `https://iprash.github.io/aigov/` within a minute or two.

To publish it at the root instead, move the four files and the `assets` folder up one level. The links between pages are relative, so nothing needs editing.

## What the pages do

**Progress tracking.** Every part and section heading has a *Mark read* toggle. The sidebar shows a running count and the contents list ticks off what you have covered. Progress for the playbook and the resource library is tracked separately.

**Renewal calculator.** Set the renewal date on the home page and it computes the backward schedule from playbook §2.3 — data access at R−150, baseline locked at R−135, brief approved at R−105, first negotiation session at R−90. Milestones already in the past are flagged, and it warns you when the date is inside 150 days and the compressed plan applies.

**Live countdown.** The home page counts down to the 31 August 2026 Codex model retirement.

**Filter.** The sidebar search box filters the contents list on both document pages.

**Theme.** Light and dark, remembered between visits. Follows the system setting the first time.

All state — reading progress, checklist ticks, renewal date, theme — lives in the browser's localStorage. Nothing is sent anywhere, and progress does not follow you between devices.

## Editing the content

Edit the markdown, then regenerate. The build script is plain Python with one dependency:

```bash
pip install markdown
python3 build.py
```

Headings become anchors automatically, tables get horizontal scroll wrappers on narrow screens, and `- [ ]` lines become working checkboxes.

## Print

Both document pages have print styles: the navigation, sidebar and toggles drop out, tables avoid page breaks, and the text sets to 11pt. Use *Print to PDF* if you want an offline copy for a flight.

---

Market evidence in these documents was checked on 17 August 2026. Re-verify every price, SKU and date against the primary source before putting a figure in front of a client.
