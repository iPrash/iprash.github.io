# Adding a site to iprash.github.io

Ten minutes. The landing page and nav update themselves — never hand-edit the root `index.html`.

Replace `<slug>` throughout. The slug becomes the URL: `iprash.github.io/<slug>/`. Use lowercase,
no spaces. It is hard to change later because it appears in every link anyone saves.

---

## 1. Decide the type

**Static** — one or more hand-written HTML files. Simplest. Choose this unless the content is
long-form prose you will revise repeatedly.

**Generated** — long documents written in markdown, built into HTML pages with a contents
sidebar, progress tracking, search filter and print styles. Choose this when the content is
more than a couple of thousand words and will be edited over time. `aigov` is the model.

## 2. Create the folder

```powershell
cd C:\Users\ipras\OneDrive\Documents\Claude\iprash.github.io
mkdir <slug>
```

## 3. Write `_site.json`

Every site needs one. It is how the build discovers the site.

**Static site — minimal:**

```json
{
  "slug": "<slug>",
  "order": 3,
  "title": "Human readable title",
  "blurb": "One line for the landing page card",
  "static": true
}
```

**Generated site — full:**

```json
{
  "slug": "<slug>",
  "order": 3,
  "title": "Human readable title",
  "blurb": "One line for the landing page card",
  "glyph": "XX",
  "brand_mark": "SHORT",
  "brand_name": "Workspace name",
  "home_nav": "Home",
  "footer": "Footer line shown on every page.",
  "index_template": "_index_template.html",
  "index_title": "Browser tab title for the home page",
  "index_desc": "Meta description for the home page",
  "pages": [
    {
      "src": "guide.md",
      "out": "guide.html",
      "id": "guide",
      "nav": "Guide",
      "title": "Browser tab title",
      "desc": "Meta description"
    }
  ]
}
```

Field notes:

- `order` sets landing page position. Lower first.
- `listed: false` hides it from the landing page while keeping the URL live.
- `id` must be unique within the site — it keys the reading-progress storage.
- `glyph` is the two-character favicon text.
- Adding an entry to `pages` automatically adds it to the nav bar.

## 4. Add content

**Static:** write `index.html`. Keep asset paths relative.

**Generated:** copy the working parts from aigov, then replace the content.

```powershell
mkdir <slug>\assets
copy aigov\assets\style.css <slug>\assets\
copy aigov\assets\app.js <slug>\assets\
copy aigov\_index_template.html <slug>\
```

Then write your markdown, and edit `<slug>\_index_template.html` — it is the home page body,
with `{{HEAD}}`, `{{NAV}}` and `{{FOOTER}}` left in place for the build to fill.

Markdown conventions the build understands:

- First `#` heading is the document title. The `##` immediately after it becomes a subtitle.
- Subsequent `#` headings are parts, `##` are sections. Both get progress toggles and appear
  in the sidebar; `###` appear in the sidebar only.
- Tables get horizontal scroll wrappers automatically.
- `- [ ]` lines become working checkboxes.
- A `---` immediately before a `#` heading is removed, to avoid a doubled rule.
- **Keep each paragraph on a single line.** The build runs markdown's `nl2br`
  extension, so every newline inside a paragraph becomes a literal `<br>`. Hard-wrapping
  prose at 80 or 90 columns, the way most markdown is written, produces a visible line
  break at every wrap point. Long lines look wrong in the editor and right on the page.
  Use `nl2br` deliberately where stacked short lines are wanted, as aigov does for its
  document header block and source-grading legend.

## 5. Build and check

```powershell
python _build\build.py --check
```

Read what it says it would change. Nothing outside your new folder and the root `index.html`
should be listed. Then:

```powershell
python _build\build.py
```

## 6. Review locally

Open `<slug>\index.html` in a browser. Check the nav, the landing page, and — on a generated
site — the sidebar, progress toggles and dark mode.

## 7. Publish

```powershell
git add -A
git status
git commit -m "Add <slug> site"
git push
```

Confirm the Actions run is green, then:

```powershell
curl.exe -sI https://iprash.github.io/<slug>/ | Select-Object -First 1
curl.exe -sI https://iprash.github.io/<slug>/assets/style.css | Select-Object -First 1
```

## 8. Write the site brief

Copy `_project/sites/_TEMPLATE.md` to `_project/sites/<slug>.md` and fill it in. Add a row to the
table in `PROJECT-CONTEXT.md` §2 so the routing in `README-FIRST.md` finds it.

Nothing to upload anywhere — Claude reads these from disk.

Do not skip this. A site without a brief is a site that future-you will not be able to pick up.
