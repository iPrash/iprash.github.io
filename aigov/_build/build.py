#!/usr/bin/env python3
"""
Rebuild the aigov HTML pages from the markdown sources.

Layout this expects:

    aigov/
    ├── playbook.md            source
    ├── resources.md           source
    ├── index.html             generated
    ├── playbook.html          generated
    ├── resources.html         generated
    ├── assets/                hand-maintained (style.css, app.js)
    └── _build/
        ├── build.py           this file
        └── index_template.html

Run from anywhere:

    pip install markdown
    python _build/build.py

Only the three HTML pages are generated. Everything else is edited by hand.
"""
import re
import sys
import pathlib

try:
    import markdown
except ImportError:
    sys.exit("Missing dependency. Run:  pip install markdown")

HERE = pathlib.Path(__file__).resolve().parent      # .../aigov/_build
SITE = HERE.parent                                  # .../aigov

EVIDENCE_DATE = "17 Aug 2026"

NAV = """<header class="masthead">
  <div class="masthead-in">
    <a class="brand" href="index.html">
      <span class="mark">XYZ / AI</span>
      <span class="name">Engagement workspace</span>
    </a>
    <nav class="nav">
      <a href="index.html"{a_home}>Plan</a>
      <a href="playbook.html"{a_pb}>Playbook</a>
      <a href="resources.html"{a_rs}>Resources</a>
      <button class="iconbtn" id="themeBtn" type="button" aria-label="Switch theme">&#9790;</button>
    </nav>
  </div>
</header>"""

HEAD = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='12' fill='%230B5563'/><text y='68' x='50' text-anchor='middle' font-size='52' font-family='monospace' fill='white'>AI</text></svg>">
</head>
<body>"""

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
  <span>Market evidence checked {evidence}. Re-verify every price and date against the primary source before client use.</span>
  <span><a href="{md}" download>Download the markdown</a></span>
</div></div></footer>
<button class="totop" type="button" aria-label="Back to top">&#8593;</button>
<script src="assets/app.js"></script>
</body>
</html>"""


def convert(md_path):
    """Markdown to HTML, with the structural fixes the stylesheet expects."""
    text = md_path.read_text(encoding="utf-8")
    html = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list", "toc", "nl2br"],
        extension_configs={"toc": {"permalink": False}},
    )
    # tables and code blocks need scroll wrappers on narrow screens
    html = html.replace("<table>", '<div class="tablewrap"><table>')
    html = html.replace("</table>", "</table></div>")
    html = html.replace("<pre>", '<div class="codewrap"><pre>')
    html = html.replace("</pre>", "</pre></div>")
    html = html.replace("<br />\n</td>", "</td>")
    # first h1 is the document title, not a section
    html = re.sub(r'<h1 id="([^"]+)">', r'<h1 class="doctitle" id="\1">', html, count=1)
    # the h2 straight after it is a subtitle
    html = re.sub(
        r"(?s)(?<=</h1>)\s*<h2 id=\"[^\"]+\">(.*?)</h2>",
        lambda m: '\n<p class="subtitle">' + m.group(1) + "</p>",
        html,
        count=1,
    )
    # the rule before a part heading doubles up with the heading's own border
    html = re.sub(r"<hr />\s*(?=<h1 id=)", "", html)
    return html


def nav_for(page):
    return NAV.format(
        a_home=' aria-current="page"' if page == "home" else "",
        a_pb=' aria-current="page"' if page == "playbook" else "",
        a_rs=' aria-current="page"' if page == "resources" else "",
    )


def build_doc(md_name, out_name, docid, title, desc, page):
    src = SITE / md_name
    if not src.exists():
        sys.exit("Missing source file: " + str(src))
    body = convert(src)
    body = "\n".join("      " + line for line in body.split("\n"))
    out = DOCPAGE.format(
        head=HEAD.format(title=title, desc=desc),
        nav=nav_for(page),
        docid=docid,
        body=body,
        md=md_name,
        evidence=EVIDENCE_DATE,
    )
    (SITE / out_name).write_text(out, encoding="utf-8")
    print("  wrote {:<16} {:>7,} bytes".format(out_name, len(out)))


def main():
    print("Building aigov from", SITE)

    build_doc(
        "playbook.md", "playbook.html", "playbook",
        "Engagement Playbook — XYZ AI Program",
        "Analysis, strategy, design and execution playbook for the XYZ Corp enterprise AI engagement.",
        "playbook",
    )
    build_doc(
        "resources.md", "resources.html", "resources",
        "Resource Library — XYZ AI Program",
        "Annotated resource library and two-week study sprint for the lead enterprise architect.",
        "resources",
    )

    tpl = HERE / "index_template.html"
    if not tpl.exists():
        sys.exit("Missing template: " + str(tpl))
    index = tpl.read_text(encoding="utf-8")
    index = index.replace(
        "{{HEAD}}",
        HEAD.format(
            title="XYZ Corp AI Program — Engagement Workspace",
            desc="Plan, playbook and resource library for the XYZ Corp AI consumption, "
                 "multi-model access and GenAI landscape engagement.",
        ),
    )
    index = index.replace("{{NAV}}", nav_for("home"))
    index = index.replace("{{EVIDENCE}}", EVIDENCE_DATE)
    (SITE / "index.html").write_text(index, encoding="utf-8")
    print("  wrote {:<16} {:>7,} bytes".format("index.html", len(index)))

    print("Done. Commit and push to publish.")


if __name__ == "__main__":
    main()
