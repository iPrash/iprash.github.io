# ClaudeCert progress

Short hand-off file. Read it at the start of a ClaudeCert study session. Update it at the end of each day ("wrap up"). Keep it under 60 lines.

## Start of a session

1. Read `_project/README-FIRST.md`, this file, then the Day block Prash names in `learn/claudecert/developer.md` (or `start.md` for Days 1 to 3).
2. Ask for folder access if not connected: the site repo (`C:\Users\ipras\OneDrive\Documents\Claude\iprash.github.io`) and CertLab (`C:\Users\ipras\workspace\CertLab`). Test deletes (`touch _rmtest; rm _rmtest`) before any commit; request the delete grant if it fails.
3. Before editing a hand-written file (TPM, ea-prep-01), check `git log -3 -- <file>` to see whether another chat changed it.

## State (28 Oct 2026)

- Exam: Developer Foundations, Saturday 5 Dec 2026 (confirmed by Prash on 23 Oct). The site calendar still shows Tue 10 Nov. Do NOT change the dates on the site (they show the fastest pace; he is about a week behind and that is fine). He may move the exam earlier.
- Done: Days 1 to 6 (Day 5 was rest; Prash also took extra rest days for an interview). Day 6 finished 30 Oct. `01_API/basics.py` committed (a3f73cc). Prash saw `max_tokens`, `end_turn`, `stop_sequence`, and that thinking tokens count against `max_tokens`. Day 4 drills added to the bank (Q2.4, Q2.5, Q5.4). Day 6 files: `01_API/tokens.py`, `variation.py`, `notes.md` (commit ddc6071 in CertLab). Day 6 drills added (Q4.4, Q5.5, Q6.4). Next is Day 7.
- CertLab repo: `C:\Users\ipras\workspace\CertLab` (private, GitHub iPrash). Folder is connected when Prash grants it. Delete grant must be requested each session.
- Focus skills from baseline: Claude API Mechanics, Agent Construction with Claude, Agent Patterns and Frameworks. Domains 7 and 8 are all rated 1 and come next.
- Closed: Console "Last used" on `CertLabDev` showed 28 Oct 2026. Do not ask again.

## Decisions

- Python tooling is `uv` (not venv). Run scripts with `uv run python <file>`.
- Names: `CertLab` repo and workspace, `CertLabDev` key, folders `01_API`, `02_Prompts`, `03_Agent`, `04_MCP`. CamelCase, acronyms in capitals, underscore after the number. Python files lowercase.
- IDE: VS Code, opened on the CertLab folder. No other IDE.
- Prash writes the build code himself. Do not write solutions. Exception: drill questions. Drill procedure (developer.md "Drill." blocks, since 28 Oct): Claude asks each question with no options; Prash answers cold, no docs; Claude marks and corrects him and holds him to a correct answer; only then does Claude add the multiple-choice version (own wording, never from the exam guide) to `drills.md`. Review his files against the day's checkbox only when he asks.
- Never copy exam-guide sample questions into any file or chat.
- Git: before any commit in any repo, check `git config user.email`. In CertLab and in iprash.github.io it must be `136493+iPrash@users.noreply.github.com`. Prash's global identity is CoachPrash, so repo-level config is required. Claude commits, Prash pushes.
- Commands go in separate code blocks, one command per block.

- Site links: external links on all learning sites open in a new tab with a ↗ arrow. Generated sites use `external_links_new_tab` in `_site.json`; hand-written TPM and ea-prep-01 have it in the HTML. A chat in 25 Oct overwrote ea-prep-01 and removed it; restored in 3c04666. Never save a whole hand-written file from an older copy.
- Every course with a Partner Academy (Skilljar) copy links there so progress records for his organisation. Path courses use `/path/claude-developer/...`; R17, R20, R21, R22 use the catalog copy (R17 = `/claude-with-the-anthropic-api`). Only R108 and the tutorials R109 to R113 stay on Claude Academy (no partner copy; checked 28 Oct).
- Day 4 lessons: `stop_reason` has seven documented values; `output_tokens` includes thinking (`output_tokens_details.thinking_tokens`); `max_tokens` caps thinking plus text; the matched stop sequence is in `msg.stop_sequence` and is not in the text.

- Day 6 lessons: token counting is free and returns a number only; text costs about 2.8 characters per token on Haiku 5.5 (count with the exact model); image cost follows pixel size, not file size; identical requests vary in wording, so test facts, never exact strings; the context window holds input plus the reply (thinking included).

## Next

- Day 7: model tiers, thinking and effort. Start with Recall (5 bank questions, include Q5.5 and Q4.4), then the Build. Run the Drill procedure at the end. Wait for his output after every command.
