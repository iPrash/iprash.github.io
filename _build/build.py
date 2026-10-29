#!/usr/bin/env python3
"""
Build every site in iprash.github.io.

Repo layout:

    iprash.github.io/
    ├── .nojekyll
    ├── index.html              GENERATED — landing page
    ├── <slug>/                 one folder per site
    │   ├── _site.json          site config — required for every site
    │   ├── *.md                markdown sources (only for generated sites)
    │   ├── *.html              generated pages, or hand-written for static sites
    │   └── assets/
    └── _build/
        ├── build.py            this file
        └── templates/
            └── landing.html

Every site folder carries a `_site.json`. Sites with a `pages` list are generated
from markdown. Sites without one are static and left untouched — but they still
appear on the landing page.

Usage:
    pip install markdown
    python _build/build.py              build everything
    python _build/build.py aigov        build one site
    python _build/build.py --landing    landing page only
    python _build/build.py --check      report what would change, write nothing
"""
import json
import re
import sys
import pathlib
import difflib

try:
    import markdown
except ImportError:
    sys.exit("Missing dependency. Run:  pip install markdown")

HERE = pathlib.Path(__file__).resolve().parent      # <repo>/_build
REPO = HERE.parent                                  # <repo>
TEMPLATES = HERE / "templates"

FONTS = ("https://fonts.googleapis.com/css2?"
         "family=Space+Grotesk:wght@500;700&"
         "family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&"
         "family=IBM+Plex+Mono:wght@400;500;600&display=swap")

FAVICON = ("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>"
           "<rect width='100' height='100' rx='12' fill='%230B5563'/>"
           "<text y='68' x='50' text-anchor='middle' font-size='52' "
           "font-family='monospace' fill='white'>{glyph}</text></svg>")


def head(title, desc, css="assets/style.css", glyph="AI", noindex=False):
    robots = '\n<meta name="robots" content="noindex,nofollow">' if noindex else ""
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">{robots}
<meta name="color-scheme" content="light dark">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="{css}">
<link rel="icon" href="{FAVICON.format(glyph=glyph)}">
</head>
<body>"""


def nav(cfg, current):
    """Navigation bar, derived from the site's page list so it stays in sync."""
    items = [{"out": "index.html", "nav": cfg.get("home_nav", "Home")}]
    items += [{"out": p["out"], "nav": p["nav"]} for p in cfg.get("pages", [])]
    links = "\n".join(
        '      <a href="{out}"{cur}>{nav}</a>'.format(
            out=i["out"], nav=i["nav"],
            cur=' aria-current="page"' if i["out"] == current else "")
        for i in items)
    return f"""<header class="masthead">
  <div class="masthead-in">
    <a class="brand" href="index.html">
      <span class="mark">{cfg.get("brand_mark", cfg["slug"])}</span>
      <span class="name">{cfg.get("brand_name", cfg["title"])}</span>
    </a>
    <nav class="nav">
{links}
      <button class="iconbtn" id="themeBtn" type="button" aria-label="Switch theme">&#9790;</button>
    </nav>
  </div>
</header>"""


DOCPAGE = """{head}
{nav}
<div class="wrap">
  <div class="shell">
    <aside class="side">
      <div class="side-head">
        <span class="eyebrow">Contents</span>
        <span class="eyebrow" id="progPct">0%</span>
      </div>
      <input class="tocsearch" id="tocSearch" type="search" placeholder="Filter sections…" aria-label="Filter sections">
      <ul class="toc" id="toc"></ul>
      <div class="progress-card">
        <div class="progress-num"><span class="eyebrow">Sections read</span><span id="progNum">0 / 0</span></div>
        <div class="bar"><i id="progBar"></i></div>
        <button class="reset" id="resetProg" type="button">Reset progress</button>
      </div>
    </aside>
    <main class="doc" data-doc="{docid}">
{body}
    </main>
  </div>
</div>
<footer class="foot"><div class="wrap"><div class="wrapin">
  <span>{footer}</span>
  <span><a href="{md}" download>Download the markdown</a></span>
</div></div></footer>
<button class="totop" type="button" aria-label="Back to top">&#8593;</button>
<script src="assets/app.js"></script>
</body>
</html>"""


def load_link_tips(site, spec):
    """Map each URL in a resource table to a tooltip. spec = {"table": "x.md", "tips": "x.json"}.
    The table rows look like: | R29 | [Title](url) | ... | and the JSON maps "R29" to a one-line description."""
    import json
    table = (site / spec["table"]).read_text(encoding="utf-8").split("\n")
    tips = json.loads((site / spec["tips"]).read_text(encoding="utf-8"))
    out, missing = {}, []
    for line in table:
        m = re.match(r"^\| (R\d+) \|(.*)$", line)
        if not m:
            continue
        rid, rest = m.groups()
        links = re.findall(r"\[((?:[^\[\]]|\[[^\]]*\])*)\]\(<?([^)>\s]+)>?\)", rest)
        if rid not in tips:
            missing.append(rid)
            continue
        first = links[0][0] if links else rid
        for text, url in links:
            out.setdefault(url, (rid, text, first, tips[rid]))
    for key, tip in tips.items():   # a key that is a URL gives a tooltip to a link outside the table
        if key.startswith("http"):
            out.setdefault(key, ("", "", "", tip))
    if missing:
        print("  warning: no tooltip text for " + ", ".join(missing))
    return out


def add_link_tips(html, tips):
    import html as H
    def one(m):
        url = H.unescape(m.group(1))
        hit = tips.get(url)
        if not hit:
            return m.group(0)
        rid, text, first, tip = hit
        plain = re.sub(r"<[^>]+>", "", m.group(3)).strip()
        if not rid:
            label = f"{plain} \u2014 {tip}"
        else:
            label = f"{rid} \u2014 {tip}" if plain == text and plain == first else f"{first if plain.startswith('R') else plain} ({rid}) \u2014 {tip}"
        return m.group(0).replace('<a class="ext"', '<a class="ext" title="' + H.escape(label, quote=True) + '"', 1)
    return re.sub(r'<a class="ext" href="([^"]+)"( target="_blank" rel="noopener noreferrer")>(.*?)</a>', one, html)


def md_to_html(path, new_tab=False, tips=None):
    """Markdown to HTML, with the structural fixes the stylesheet expects.

    new_tab: open external (http/https) links in a new tab and mark them class="ext"."""
    html = markdown.markdown(
        path.read_text(encoding="utf-8"),
        extensions=["tables", "fenced_code", "sane_lists", "attr_list", "toc", "nl2br"],
        extension_configs={"toc": {"permalink": False}},
    )
    html = html.replace("<table>", '<div class="tablewrap"><table>')
    html = html.replace("</table>", "</table></div>")
    html = html.replace("<pre>", '<div class="codewrap"><pre>')
    html = html.replace("</pre>", "</pre></div>")
    html = html.replace("<br />\n</td>", "</td>")
    html = re.sub(r'<h1 id="([^"]+)">', r'<h1 class="doctitle" id="\1">', html, count=1)
    html = re.sub(r"(?s)(?<=</h1>)\s*<h2 id=\"[^\"]+\">(.*?)</h2>",
                  lambda m: '\n<p class="subtitle">' + m.group(1) + "</p>", html, count=1)
    html = re.sub(r"<hr />\s*(?=<h1 id=)", "", html)
    if new_tab:
        html = re.sub(r'<a href="(https?://[^"]+)"',
                      r'<a class="ext" href="\1" target="_blank" rel="noopener noreferrer"', html)
        if tips:
            html = add_link_tips(html, tips)
    return html


CHANGED = []
CHECK_ONLY = False


def write(path, content):
    """Write with LF endings. In --check mode, report instead of writing."""
    existing = path.read_text(encoding="utf-8") if path.exists() else None
    rel = path.relative_to(REPO)
    if existing == content:
        print(f"  unchanged  {rel}")
        return
    CHANGED.append(str(rel))
    if CHECK_ONLY:
        n = len(list(difflib.unified_diff(
            (existing or "").splitlines(), content.splitlines(), n=0))) if existing else 0
        print(f"  WOULD EDIT {rel}  ({n} diff lines)" if existing else f"  WOULD ADD  {rel}")
        return
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(content)
    print(f"  wrote      {rel}  {len(content):,} bytes")


def load_sites():
    """Find every site config.

    Two levels deep, not one: projects sit at the repo root, and study sites sit
    under learn/ so the root stays readable as more of them are added. A site's
    slug stays its folder name; `_path` is where it actually lives, which is what
    the URL follows.
    """
    found = set(REPO.glob("*/_site.json")) | set(REPO.glob("*/*/_site.json"))
    sites = []
    for cfg_path in sorted(found):
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
        cfg["slug"] = cfg.get("slug", cfg_path.parent.name)
        cfg["_dir"] = cfg_path.parent
        cfg["_path"] = cfg_path.parent.relative_to(REPO).as_posix()
        sites.append(cfg)
    sites.sort(key=lambda c: (c.get("order", 99), c["slug"]))
    return sites


def build_site(cfg):
    site = cfg["_dir"]
    pages = cfg.get("pages", [])
    if not pages:
        print(f"[{cfg['_path']}] static — nothing to generate")
        return
    print(f"[{cfg['_path']}]")
    footer = cfg.get("footer", "")
    tips = load_link_tips(site, cfg["link_tips"]) if cfg.get("link_tips") else None

    for p in pages:
        src = site / p["src"]
        if not src.exists():
            sys.exit(f"  Missing source: {src}")
        body = "\n".join("      " + line for line in md_to_html(src, cfg.get("external_links_new_tab", False), tips).split("\n"))
        write(site / p["out"], DOCPAGE.format(
            head=head(p["title"], p["desc"], glyph=cfg.get("glyph", "AI"),
                      noindex=cfg.get("noindex", False)),
            nav=nav(cfg, p["out"]),
            docid=p["id"], body=body, md=p["src"], footer=footer))

    tpl_name = cfg.get("index_template")
    if tpl_name:
        tpl = site / tpl_name
        if not tpl.exists():
            sys.exit(f"  Missing template: {tpl}")
        out = tpl.read_text(encoding="utf-8")
        out = out.replace("{{HEAD}}", head(cfg["index_title"], cfg["index_desc"],
                                           glyph=cfg.get("glyph", "AI"),
                                           noindex=cfg.get("noindex", False)))
        out = out.replace("{{NAV}}", nav(cfg, "index.html"))
        out = out.replace("{{FOOTER}}", footer)
        out = out.replace("{{EVIDENCE}}", cfg.get("evidence_date", ""))
        write(site / "index.html", out)


def load_projects():
    """The portfolio list. Separate from the site list, because a project may
    live in another repo, or be a link with no page in this repo at all."""
    path = HERE / "projects.json"
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return [p for p in data.get("projects", []) if p.get("listed", True)]


def project_card(p):
    """One card. Uses assets/shots/<slug>.png when present, and falls back to a
    generated tile so a project without a screenshot still renders complete."""
    slug = p.get("slug", "")
    # Any common image format, so renaming a file does not silently drop the card
    # back to its tile. First match wins.
    shot = next((f"{slug}{ext}" for ext in (".png", ".jpg", ".jpeg", ".webp")
                 if (REPO / "assets" / "shots" / f"{slug}{ext}").exists()), None)
    if shot:
        media = f'<img src="assets/shots/{shot}" alt="{p["title"]} screenshot" loading="lazy">'
    else:
        media = ('<span class="tile" aria-hidden="true">'
                 f'<b>{p.get("glyph", "")}</b></span>')

    tags = "".join(f"<em>{t}</em>" for t in p.get("tags", []))
    repo = p.get("repo", "")
    source = f'<a class="src" href="{repo}">Source</a>' if repo else ""
    status = p.get("status", "")
    badge = f'<span class="status">{status}</span>' if status else ""

    return f"""  <article class="card" style="--accent:{p.get('accent', '#0B5563')}">
    <a class="shot" href="{p['url']}" tabindex="-1" aria-hidden="true">{media}</a>
    <div class="meta">
      <h2><a href="{p['url']}">{p['title']}</a></h2>
      <p>{p.get('blurb', '')}</p>
      <div class="tags">{tags}</div>
      <div class="links">{badge}{source}</div>
    </div>
  </article>"""


def build_landing(sites):
    """The landing page is a project index. Learning sites are deliberately not
    listed here; they are reached through learn/ instead."""
    print("[landing]")
    tpl = TEMPLATES / "landing.html"
    if not tpl.exists():
        sys.exit(f"Missing template: {tpl}")
    projects = load_projects()
    if not projects:
        print("  note: _build/projects.json is missing or empty")
    cards = "\n".join(project_card(p) for p in projects)
    write(REPO / "index.html", tpl.read_text(encoding="utf-8").replace("{{CARDS}}", cards))


def main():
    global CHECK_ONLY
    args = [a for a in sys.argv[1:]]
    CHECK_ONLY = "--check" in args
    args = [a for a in args if not a.startswith("--")]
    landing_only = "--landing" in sys.argv[1:]

    sites = load_sites()
    if not sites:
        sys.exit("No sites found. Every site folder needs a _site.json.")

    print(f"Repo: {REPO}")
    print("Sites: " + ", ".join(c["_path"] for c in sites))
    print("MODE: check only, nothing written\n" if CHECK_ONLY else "")

    if not landing_only:
        for cfg in sites:
            if args and cfg["slug"] not in args and cfg["_path"] not in args:
                continue
            build_site(cfg)

    if not args or landing_only:
        build_landing(sites)

    print()
    if not CHANGED:
        print("Everything already up to date.")
    elif CHECK_ONLY:
        print(f"{len(CHANGED)} file(s) would change:")
        for f in CHANGED:
            print("  " + f)
    else:
        print(f"{len(CHANGED)} file(s) written. Commit and push to publish.")


if __name__ == "__main__":
    main()
