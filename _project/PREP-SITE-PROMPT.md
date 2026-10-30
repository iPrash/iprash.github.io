# Interview prep site: prompt template

Use this to start a new Cowork session that builds an interview prep site under `learn/`.
Copy everything inside the fence. Fill every `[BRACKET]`. Section 3 is the only part that
changes much from role to role; sections 1, 2 and 4–8 are standing rules.

Built from what worked on `ea-prep-01` (23 Oct 2026) and `ea-prep-02-aws` (29 Oct 2026).
Update it when a new site teaches something worth keeping.

## How to fill section 3

- Paste the **full** job description, unedited. It decides the card list.
- Write **your read** of what the interview will test, ranked by weight. The session will
  challenge it. A wrong read costs less than no read.
- State your **experience level** with each named technology honestly: deep, some, lightly,
  none. It sets how basic the cards start.
- Name anything **ambiguous** in the JD (an unclear acronym, a product that may be retired)
  so the session researches it and adds it to "Questions to ask them".
- With **no JD**, say so and ask for a generic site around the most common patterns in the
  area, as `ea-prep-02-aws` did.

## The prompt

```text
Build a new interview-prep study site at learn/[SLUG] on iprash.github.io. Plan first. Do not build anything until I approve the plan.

## 1. Start-up
Read _project/README-FIRST.md and follow its routing: PROJECT-INSTRUCTIONS, PROJECT-CONTEXT, NEW-SITE, and the briefs for the existing ea-prep sites in _project/sites/. Confirm you can see the repo and name the sites you found. If you cannot read the repo, say so and stop.

## 2. Models to copy
- The newest ea-prep site's index.html is the model (ea-prep-02-aws as of 29 Oct 2026). Copy its shell exactly: CSS, JS, sticky nav, progress ticks, dark mode, inline SVG diagram classes (svg.d, rect.ou, rect.band, text.t, text.s), <abbr title> tooltips, "Say this" / "Gotchas" / "What they test" boxes, self-check, What changed tables, cheat sheet. Do not invent a new design.
- learn/ea-prep-01/index.html: copy its anchor-story approach, with provenance tags and [brackets] for facts only I can supply.
- Pick a localStorage prefix not used by any other site on this origin (ea1., ea2. and so on). Check the briefs.

## 3. The role
[PASTE THE FULL JD HERE, UNEDITED. OR: "No JD. Build a generic site on the most common [AREA] patterns."]

My read of what the interview tests, highest weight first. Challenge it if you disagree:
1. [TOPIC AND WHY]
2. [TOPIC AND WHY]
3. [TOPIC AND WHY]

My experience: [TECHNOLOGY: deep / some / lightly / none, for each one named in the JD]. Background: 25+ years in enterprise architecture. See the anchor stories in ea-prep-01.

Ambiguous items to research: [ACRONYM OR PRODUCT, OR "none"]. Cover each option briefly if it stays unclear, and add it to "Questions to ask them".

Interview date and format, if known: [DATE / PANEL / WHITEBOARD / UNKNOWN].

## 4. Phase 1: the plan (stop and wait for my OK)
Give me: the card list with ids; a study plan in sessions with hours (estimate the total honestly and tell me if it is more than I expect); a short list of open questions. Do not research deeply or build before I approve.

## 5. Phase 2: research rules
- Research before writing. Primary sources first: vendor docs, lifecycle and deprecation pages, launch announcements.
- Every card ends with "Go deeper (free)" links and a Sources line with a check date. Grade sources [P] primary or [S] secondary. Mark version-sensitive facts with <span class="ver">ver</span>.
- Include a "What changed in the last two years" section: retired or renamed products with what to say instead, and the new defaults, each with a date and a source.
- Every link checked live. Free resources only, plus a pointer to partner and internal portals that need my company login.
- Never invent numbers for my stories. Use [brackets].

## 6. Phase 3: build rules
- Static, hand-written, single index.html, about 150–200 KB. Write it in section fragments, then assemble. Wrap acronyms automatically from a glossary, skipping code, pre, svg, nav, summary, h1, figcaption and buttons.
- The repo is public. No client, employer or interview names anywhere.
- Writing: Simplified Technical English, Zinsser's four principles, no em-dash asides, no "not X but Y" phrasing.
- Required sections: study plan in sessions, self-check, technology or pattern cards, What changed, interview questions with "What they test" and model answers, a story frame, a system design or scenario walkthrough, free resources and labs, questions to ask them, a one-page cheat sheet. [ADD ROLE-SPECIFIC SECTIONS, E.G. DELIVERABLE TEMPLATES]
- Add _site.json (static, listed false, noindex true), the robots meta in the HTML by hand, and a brief at _project/sites/[SLUG].md. Add a row to PROJECT-CONTEXT §2.
- Add a row to learn/index.html directly under the pinned claudecert row. The hub lists sites newest first.

## 7. Verify before commit
- All in-page anchors resolve. No duplicate ids.
- Every external link returns 200.
- Render with Playwright: desktop in light mode and 390 px in dark mode. No horizontal page scroll. No console errors. Look at every SVG for text overflow.
- python _build/build.py --check reports nothing unexpected.

## 8. Git and working with me
- If another Cowork session is working on this repo, only one session commits at a time.
- Before any git write: check the git identity is iPrash, and run the delete test (touch _rmtest, then rm _rmtest). If the rm fails, ask me for the delete grant.
- You run git add and git commit. I run git push. After my push, check the live URL and the learn hub.
- When you give me commands, give one per code block and wait for my pasted output before doing anything else.
- Tell me plainly when I am wrong. Keep review rounds to blockers only.
```
