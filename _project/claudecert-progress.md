# ClaudeCert progress

Short hand-off file. Read it at the start of a ClaudeCert study session. Update it at the end of each day ("wrap up"). Keep it under 60 lines.

## State (23 Oct 2026)

- Exam: Developer Foundations, Saturday 5 Dec 2026 (confirmed by Prash on 23 Oct). The site calendar still shows Tue 10 Nov. Do NOT change the dates on the site. He may move the exam earlier.
- Done: Days 1, 2, 3. Day 4 in progress (started 23 Oct).
- CertLab repo: `C:\Users\ipras\workspace\CertLab` (private, GitHub iPrash). Folder is connected when Prash grants it. Delete grant must be requested each session.
- Focus skills from baseline: Claude API Mechanics, Agent Construction with Claude, Agent Patterns and Frameworks. Domains 7 and 8 are all rated 1 and come next.
- Open: Console "Last used" on key `CertLabDev` was still empty on 22 Oct. Local check already proves the key was used. Ask once whether it now shows a time.

## Decisions

- Python tooling is `uv` (not venv). Run scripts with `uv run python <file>`.
- Names: `CertLab` repo and workspace, `CertLabDev` key, folders `01_API`, `02_Prompts`, `03_Agent`, `04_MCP`. CamelCase, acronyms in capitals, underscore after the number. Python files lowercase.
- IDE: VS Code, opened on the CertLab folder. No other IDE.
- Prash writes the build code himself. Do not write solutions. Review his files against the day's checkbox only when he asks.
- Never copy exam-guide sample questions into any file or chat.
- Git: before any commit in any repo, check `git config user.email`. In CertLab and in iprash.github.io it must be `136493+iPrash@users.noreply.github.com`. Prash's global identity is CoachPrash, so repo-level config is required. Claude commits, Prash pushes.
- Commands go in separate code blocks, one command per block.

## Next

- Day 4: build `01_API/basics.py` (three `stop_reason` values), MSO Foundations course (R103), write three drill questions. Prep questions given on 22 Oct.
