# ea-prep-02-aws — site brief

**URL:** https://iprash.github.io/learn/ea-prep-02-aws/
**Type:** static
**Created:** 29 Oct 2026
**Evidence last checked:** 29 Oct 2026

## What it is

AWS Enterprise Architect interview prep, built without a job description. It covers the most common AWS deployment patterns in a generic form. Sections: seven-session study plan (about 12 hours), a 15-question self-check, three core refresh cards, twelve deployment-pattern cards, a "What changed 2024–2026" pair of tables (retired services and new defaults), Well-Architected and FinOps cards, thirteen interview questions with model answers, extra questions, an AWS story frame, a system design walkthrough, free resources and a cheat sheet.

## Why it exists

Prash worked with AWS on earlier projects but has been away from it. The site refreshes fundamentals, replaces stale service names with current ones, and prepares him for an EA panel. The slug names the technology so it is clear at a glance. The next site, ea-prep-03-intg, covers an integration architecture assessment (Dynamics 365 and MuleSoft). The planned ea-prep-03-mule was replaced by it.

## Structure

| File | Role |
|---|---|
| `_site.json` | Config. Static, no `pages` list, so the build leaves the site alone. |
| `index.html` | Hand-written. Self-contained: inline CSS, JS and SVG. No backup other than git. |

## Editing rules

**Everything here is hand-written.** Edit `index.html` directly.

The page was first assembled in Claude's cloud workspace from section fragments with a script that also wrapped acronyms in `<abbr title>` tags from a glossary. The script is not in the repo. Treat `index.html` as the source now. When adding content, wrap new acronyms by hand in the same form. Text inside `<code>`, `<pre>`, `<svg>`, `<nav>`, `<summary>`, `<h1>`, `<figcaption>` and buttons is deliberately left unwrapped.

The `<meta name="robots" content="noindex,nofollow">` is hand-maintained. Put it back if the file is replaced.

Progress ticks use localStorage keys prefixed `ea2.`, keyed by each card's `id` (`c-*`, `core-*`, `p-*`, `d-*`, `q*`, `x-*`, `res-*`, `stories`, `cheat-card`). Renaming an id resets that tick and breaks in-page links.

Diagrams are inline SVG with class `d`. Their colours come from CSS variables, so they follow dark mode. Keep using the `rect.ou`, `rect.band`, `text.t`, `text.s` classes.

## Content standards

**The repo is public.** No employer, client or interview names. The story frame uses [brackets] for facts only Prash can supply. Do not fill them with invented numbers.

Each card ends with "Go deeper (free)" links and a Sources line with a check date. Version-sensitive facts carry a `ver` mark. Sources are graded [P] (AWS primary) and [S] (credible secondary) in the What changed section.

## Time-sensitive content

Checked 29 Oct 2026 against AWS lifecycle pages and launch posts:

- Retirements and maintenance: Migration Hub (closed 7 Nov 2025), App Mesh (ended 30 Sep 2026), App Runner (maintenance 30 Apr 2026), Proton and WAF Classic (end 7 Oct 2026), CloudTrail Lake (closed 31 May 2026), Kendra, Q Business, Bedrock Agents Classic, Simple AD (maintenance 30 Jul 2026), Q Developer IDE plugins (end 30 Apr 2027), Pinpoint (end 30 Oct 2026), Inspector Classic (ended 20 May 2026), QLDB (ended 31 Jul 2025).
- CodeCommit was closed in Jul 2024 and returned to GA on 24 Nov 2025.
- New defaults: RCPs, centralised root access, declarative policies (Nov–Dec 2024), Control Tower landing zone 4.0 (17 Nov 2025), EKS Auto Mode, ECS Express Mode, Lambda Managed Instances and durable functions, S3 Tables, S3 Vectors, Aurora DSQL, Security Hub (new, Dec 2025), ARC Region switch, AWS Transform, AgentCore (GA Oct 2025), Bedrock Managed Knowledge Base (GA 17 Jun 2026), Amazon Quick, Kiro.
- Less certain, marked `ver`: VPC Block Public Access date, Pinpoint replacement, Amazon EVS, Aurora PostgreSQL as the QLDB replacement, AWS European Sovereign Cloud status.

AWS publishes service availability updates about every quarter. Check for a new batch before each interview.

## Open items

- Prash fills the story frame (`#stories`) with real facts from projects that ran on AWS.
- Re-check the What changed tables the week before the interview.
- When two Cowork sessions work on this repo, only one commits at a time. Both write to the same `.git`.
