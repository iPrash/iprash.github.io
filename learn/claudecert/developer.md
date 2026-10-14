# Developer Foundations
## Days 4 to 28 · exam CCDV-F on Tuesday 10 November 2026

This block prepares the Claude Certified Developer, Foundations exam: 53 items, 120 minutes, pass at 720 of 1,000. The blueprint is in [R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf), section 6. Read it before Day 4.

Each day has the same shape: a goal, a build, a reading, prompts for the 3 questions I write, and a done-when checkbox. Domain tags show the blueprint weight, so I can see where the points are.

---

# Block map

## Where the points are

Weights from [R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf), version 1.0, July 2026. The right column shows which days cover each domain.

| Domain | Weight | Largest skill lines | Days |
|---|---|---|---|
| D1 Agents and Workflows | 14.7% | Agent construction 5.3%, patterns and frameworks 4.9% | 17, 18, 20 |
| D2 Applications and Integration | 33.1% | Application design 8.6%, software engineering 7.4%, API mechanics 6.8% | 4, 8, 9, 11, 22, 24, 27 |
| D3 Claude Code | 3.1% | Claude Code operation 3.1% | 22 |
| D4 Eval, Testing and Debugging | 2.6% | Debugging and error handling 2.6% | 8, 24 |
| D5 Model Selection and Optimization | 16.8% | Technical fundamentals 6.1%, LLM fundamentals 5.2% | 4, 6, 7, 8, 10 |
| D6 Prompt and Context Engineering | 11.0% | Prompt engineering 4.6%, context engineering 3.8% | 13, 14, 20 |
| D7 Security and Safety | 8.1% | Application security 3.2%, guardrails 2.3% | 18, 23 |
| D8 Tools and MCPs | 10.6% | Tool implementation 4.4%, agentic customization 4.1% | 15, 16, 21, 22 |

Two things stand out. D2 and D5 together are half the exam, and a lot of D2 is general software engineering. D3 and D4 together are under 6%, so I do not over-invest in Claude Code here. Claude Code is worth 20% on the Architect exam, and the Architect block covers it in depth.

## The reading spine

The Developer prep course ([R12](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations)) has five modules, about 13 hours in total. The days below place each module next to the build it supports.

| Module | Minutes | Days |
|---|---|---|
| MSO Foundations | 57 | 4 |
| Production-Grade Prompting, Agents & Tool Use | 209 | 13 to 17 |
| Claude Code, MCP & Integration | 142 | 20 to 22 |
| Production Engineering, Evals & Security | 211 | 23, 24, 27 |
| Accelerators & IP Contribution | 155 | 27, platform-choice part only. The rest after the exam |

Docs pages ([R23](https://platform.claude.com/docs/en/get-started) onward) are for reference during builds. I read the section I need, not the whole page.

---

# Week 1 · API basics

## Day 4 · First real calls

Saturday 17 October · long day, 2 hours · Dev D2 API mechanics, D5 LLM fundamentals

**Goal.** Understand one Messages API request and response completely.

**Build (60 min).** In `cert-lab/01-api/`, write `basics.py`. Send a request with a system prompt and two user turns. Print the full response object, not only the text. Identify `stop_reason`, `usage.input_tokens` and `usage.output_tokens`. Set `max_tokens` to 20 and watch `stop_reason` change to `max_tokens`. Add a stop sequence and watch it change to `stop_sequence`.

**Read (60 min).** MSO Foundations module ([R12](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations)), all of it. Keep [R24](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) open for reference.

**Video backup.** [R17](https://anthropic.skilljar.com/claude-with-the-anthropic-api), section Accessing Claude with the API.

**Write.** One question on `stop_reason` values. One on where a system prompt goes in the request. One on what `max_tokens` controls and what it does not.

- [ ] D4: `basics.py` prints three different `stop_reason` values, and I can explain each.

## Day 5 · Rest

Sunday 18 October. No study. If a read from this week ran over, it can move here.

## Day 6 · Tokens, context and sampling

Monday 19 October · Dev D5 LLM fundamentals (5.2%)

**Goal.** Make tokens, context windows and non-determinism concrete.

**Build (45 min).** Use the token counting endpoint ([R29](https://platform.claude.com/docs/en/build-with-claude/token-counting)) on three inputs: a short prompt, a 20-page text, and an image. Record the counts. Send the same open-ended prompt five times and diff the outputs. Repeat with a prompt that has one correct answer. Note where variation matters and where it does not.

**Read (35 min).** [R32](https://platform.claude.com/docs/en/build-with-claude/context-windows) Context windows. Then the first part of [R39](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), the sections on being clear and on examples.

**Write.** One question on why outputs vary between identical requests. One on what counts against the context window. One on zero-shot versus few-shot.

- [ ] D6: A table in `01-api/notes.md` with token counts for three inputs and a one-line finding on output variation.

## Day 7 · Model tiers, thinking and effort

Tuesday 20 October · Dev D5 model selection (2.7%), LLM fundamentals

**Goal.** Choose a model from evidence, not habit.

**Build (45 min).** Run three tasks on the current Haiku, Sonnet and Opus models ([R35](https://platform.claude.com/docs/en/models/overview)): a short classification, a structured summary, and a multi-step reasoning problem. Record latency, tokens and a quality grade for each. Run the reasoning task again with extended thinking on ([R30](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)) and with a different effort setting ([R31](https://platform.claude.com/docs/en/build-with-claude/effort)).

**Read (30 min).** [R36](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model) Choosing a model. [R37](https://platform.claude.com/docs/en/about-claude/model-deprecations) Model deprecations: note what changes when a model version is retired.

**Write.** One question that gives a workload and asks for a model tier. One on when extended thinking is worth its cost. One on why pinning a model version matters.

- [ ] D7: A 3 by 3 table (task by model) with latency, cost and quality, and a one-line rule I would apply.

---

# Week 2 · Production mechanics

## Day 8 · Streaming, errors and raw HTTP

Wednesday 21 October · Dev D2 API mechanics, D4 debugging, D5 technical fundamentals (6.1%)

**Goal.** Handle the API the way production code must.

**Build (45 min).** Call the API once with plain HTTP (`requests` or `curl`), then with the SDK. Compare what the SDK adds: retries, typed errors, streaming helpers. Stream a long response ([R25](https://platform.claude.com/docs/en/build-with-claude/streaming)) and print text as it arrives. Force three errors: a bad API key, an invalid request, and a too-large `max_tokens`. Write a retry wrapper that retries only errors that a retry can fix.

**Read (30 min).** [R40](https://platform.claude.com/docs/en/api/errors) API errors. [R25](https://platform.claude.com/docs/en/build-with-claude/streaming) Streaming, the event-types section.

**Write.** One question on which HTTP errors to retry. One on what streaming changes for the user and what it does not change for cost. One on SDK versus raw REST.

- [ ] D8: `02-errors.py` shows each forced error caught by type, with retry only on retryable errors.

## Day 9 · Vision and documents

Thursday 22 October · Dev D2 API mechanics, application design (8.6%)

**Goal.** Send non-text input correctly.

**Build (45 min).** Send an image by base64 and by URL. Ask for a structured description. Send a short PDF as a document block and ask for a table from it. Measure the token cost of each input.

**Read (30 min).** [R26](https://platform.claude.com/docs/en/build-with-claude/vision) Vision. [R24](https://platform.claude.com/docs/en/build-with-claude/working-with-messages), the section on content blocks.

**Video backup.** [R17](https://anthropic.skilljar.com/claude-with-the-anthropic-api), section Features of Claude: Image support and PDF support.

**Write.** One question on image versus document input. One on the cost of large images. One on where in the message to put an image relative to the question.

- [ ] D9: Image and PDF inputs both return correct structured output, with token cost recorded.

## Day 10 · Prompt caching and the cost model

Friday 23 October · Dev D5 cost and token management (2.8%)

**Goal.** Cut repeated-prefix cost and prove it with numbers.

**Build (45 min).** Put a long, fixed system prompt (over the minimum cacheable length in [R27](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)) before a short user question. Add a cache breakpoint. Send the request three times. Record `cache_creation_input_tokens` and `cache_read_input_tokens`. Build a small cost model: requests per day, prefix size, hit rate, saving. Then change one word in the prefix and show the cache miss.

**Read (30 min).** [R27](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) Prompt caching, including what invalidates the cache.

**Video backup.** [R17](https://anthropic.skilljar.com/claude-with-the-anthropic-api), section Features of Claude: the three prompt caching lessons.

**Write.** One question on what makes a cache miss. One on ordering content so the stable part comes first. One that asks which workload benefits most from caching.

- [ ] D10: A cost-model sheet showing cached versus uncached cost for one realistic workload.

## Day 11 · Batches and the first mini-mock

Saturday 24 October · long day, 2 hours · Dev D2 API mechanics, batch versus realtime

**Goal.** Know when batch beats realtime, and run my first timed drill.

**Build (60 min).** Submit a batch of 20 requests with unique `custom_id` values ([R28](https://platform.claude.com/docs/en/build-with-claude/batch-processing)). Include one request that will fail. Poll until the batch ends. Match results to inputs by `custom_id`, not by order. Resubmit the failed one.

**Mock (60 min).** 20 questions from my bank and the Drills page, timed at 2 minutes each. Then review every miss and write down why I missed it.

**Write.** One question on matching batch results. One on a latency-tolerant workload. One on what batches do not support.

- [ ] D11: Batch run completes with one failure handled by `custom_id`. Mock score recorded in `cert-lab/results.md`.

## Day 12 · Rest

Sunday 25 October.

## Day 13 · Prompt engineering

Monday 26 October · Dev D6 prompt engineering (4.6%)

**Goal.** Improve a prompt by measurement, not by feel.

**Build (45 min).** In `cert-lab/02-prompts/`, build a support-ticket classifier with five categories. Write 20 labeled test tickets, including 5 ambiguous ones. Score version 1 of the prompt. Then change one thing at a time: clear instructions, XML tags around the ticket, a system-prompt role, and 3 examples that target the ambiguous cases. Score each version.

**Read (40 min).** [R12](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations) module 2, Production-Grade Prompting, Agents & Tool Use, first segment.

**Video backup.** [R85](https://www.youtube.com/watch?v=ysPbXH0LpIE) Prompting 101. [R17](https://anthropic.skilljar.com/claude-with-the-anthropic-api), section Prompt engineering techniques.

**Write.** One question on system versus user placement. One on why examples should target the ambiguous cases. One on input sanitization.

- [ ] D13: A score table: prompt version by accuracy on 20 tickets, with the change that helped most.

## Day 14 · Structured output and defensive parsing

Tuesday 27 October · Dev D6 output handling (2.6%)

**Goal.** Get output my code can trust.

**Build (45 min).** Make the classifier return JSON: category, confidence, and a short reason. First try with instructions only, and count parse failures over 20 runs. Then use structured outputs or strict tool use ([R34](https://platform.claude.com/docs/en/build-with-claude/structured-outputs), [R47](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use)). Validate with Pydantic. On a validation failure, retry once with the error message included.

**Read (40 min).** [R12](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations) module 2, second segment. [R34](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) for reference.

**Write.** One question on schema-guaranteed output versus instruction-only JSON. One on what validation cannot catch. One on a confident but wrong answer.

- [ ] D14: Zero parse failures over 20 runs, and a retry path that I have seen fire.

---

# Week 3 · Tools, agents and MCP

## Day 15 · Tool use, by hand

Wednesday 28 October · Dev D8 tool implementation (4.4%)

**Goal.** Run the tool-use loop myself before any framework does it for me.

**Build (45 min).** In `cert-lab/03-agent/`, define three tools for an order-support case: `lookup_order`, `get_policy`, `issue_refund`. Write the loop: send, check `stop_reason`, run the tool when it is `tool_use`, return a `tool_result`, repeat until `end_turn`. Return `is_error: true` with a clear message when an order is not found. Add a maximum-turns limit.

**Read (40 min).** [R12](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations) module 2, third segment. [R43](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works) and [R45](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) for reference.

**Video backup.** [R17](https://anthropic.skilljar.com/claude-with-the-anthropic-api), section Tool use with Claude, up to Multi-turn conversations with tools.

**Write.** One question on what ends the loop. One on how to report a tool failure to the model. One on client-side versus server-side tools.

- [ ] D15: The loop handles a two-tool request and a not-found error, and stops at the turn limit.

## Day 16 · Tool choice and tool descriptions

Thursday 29 October · Dev D8 tool implementation, tool set construction

**Goal.** Control which tool runs, and make the model pick the right one.

**Build (45 min).** Try `tool_choice` set to auto, any, a named tool, and none. Note what each does. Add a fourth tool, `get_order_status`, that overlaps with `lookup_order`. Send 10 ambiguous requests and count wrong picks. Rewrite both descriptions to separate them clearly. Count again. Ask for two independent lookups in one message and watch for parallel tool calls ([R46](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use)).

**Read (40 min).** [R12](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations) module 2, fourth segment. [R78](https://www.anthropic.com/engineering/writing-tools-for-agents) Writing effective tools for agents.

**Write.** One question on forcing a tool. One on fixing tool confusion. One on splitting versus merging two tools.

- [ ] D16: Wrong-pick count before and after the description rewrite.

## Day 17 · Workflow or agent

Friday 30 October · Dev D1 agent architecture (4.5%)

**Goal.** Decide when a fixed workflow is better than an agent.

**Build (45 min).** Add a human approval checkpoint before `issue_refund`. The loop pauses, prints the planned refund, and waits for yes or no. Add a spend budget that stops the agent. Then sketch, in `notes.md`, the same case as a fixed workflow (classify, look up, apply policy, draft reply) and list what each design is better at.

**Read (40 min).** [R12](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations) module 2, last segment. [R77](https://www.anthropic.com/engineering/building-effective-agents) Building effective agents.

**Video backup.** [R84](https://www.youtube.com/watch?v=D7_ipDqhtwk) How We Build Effective Agents, 15 minutes. [R17](https://anthropic.skilljar.com/claude-with-the-anthropic-api), section Agents and workflows.

**Write.** One question on workflow versus agent. One on where to place a human checkpoint. One on supervisor and subagent roles.

- [ ] D17: The refund pauses for approval, and `notes.md` compares the two designs.

## Day 18 · The Agent SDK and a blocking hook

Saturday 31 October · long day, 2 hours · Dev D1 agent construction (5.3%), D7 hooks (1.0%)

**Goal.** Rebuild the agent on the Agent SDK and enforce a rule in code.

**Build (75 min).** Follow [R56](https://code.claude.com/docs/en/agent-sdk/quickstart) to set up the Agent SDK. Rebuild the Day 15 agent with custom tools ([R58](https://code.claude.com/docs/en/agent-sdk/custom-tools)). Add a PreToolUse hook ([R59](https://code.claude.com/docs/en/agent-sdk/hooks)) that blocks any refund above a limit and returns a reason. Add one subagent ([R60](https://code.claude.com/docs/en/agent-sdk/subagents)) that only drafts the customer reply. Compare the code size and behavior with the hand-written loop.

**Mock (45 min).** 15 questions on Days 4 to 17, timed. Review every miss.

**Video, Sunday.** [R87](https://www.youtube.com/watch?v=TqC1qOfiVcQ) Agent SDK workshop, the first 45 minutes. Watch it on Day 19 if the build ran long.

**Write.** One question on a hook versus a prompt instruction for a business rule. One on what a subagent's separate context gives. One on self-hosted versus managed agent deployment.

- [ ] D18: The hook blocks an over-limit refund in a test run, and the mock score is recorded.

## Day 19 · Rest

Sunday 1 November.

## Day 20 · Context engineering

Monday 2 November · Dev D6 context engineering (3.8%), D1 patterns and frameworks (4.9%)

**Goal.** Keep long agent runs inside a useful context.

**Build (45 min).** Make one tool return a large, noisy payload. Run a 10-turn session and watch token use grow. Fix it three ways and compare: prune the tool output to the fields needed, use compaction ([R33](https://platform.claude.com/docs/en/build-with-claude/compaction)), and move a sub-task into a subagent so only its summary returns. Then read the quickstart of one framework (LangGraph, Strands or PydanticAI) for 10 minutes. Note how it names the same ideas.

**Read (35 min).** [R79](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) Effective context engineering. [R12](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations) module 3, first segment.

**Video backup.** [R86](https://www.youtube.com/watch?v=XSZP9GhhuAc) Prompting for Agents.

**Write.** One question on context drift. One on pruning versus compaction. One on context isolation through subagents.

- [ ] D20: Token use per turn, before and after each fix, in `notes.md`.

## Day 21 · Build an MCP server

Tuesday 3 November · Dev D8 MCP server development (2.1%)

**Goal.** Expose a capability once and use it from more than one client.

**Build (45 min).** In `cert-lab/04-mcp/`, build a Python MCP server ([R76](https://modelcontextprotocol.io/docs/develop/build-server)) with two tools (`lookup_order`, `get_policy`), one resource (the refund policy text), and one prompt (a reply template). Run it over stdio. Connect it to Claude Code with a project-scoped `.mcp.json` ([R70](https://code.claude.com/docs/en/mcp)). Put the credential in an environment variable, not in the file. Call each primitive from Claude Code.

**Read (35 min).** [R12](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations) module 3, second segment. [R75](https://modelcontextprotocol.io/docs/getting-started/intro) for the three primitives.

**Video backup.** [R88](https://www.youtube.com/watch?v=kQmXtrmQ5Zg) MCP workshop, the first hour, or [R94](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic). [R17](https://anthropic.skilljar.com/claude-with-the-anthropic-api), section Model Context Protocol.

**Write.** One question on tools versus resources versus prompts. One on stdio versus a network transport. One on keeping secrets out of `.mcp.json`.

- [ ] D21: Claude Code calls both tools and reads the resource through my server.

---

# Week 4 · Configuration, security and evaluation

## Day 22 · Claude Code, Skills and the customization choice

Wednesday 4 November · Dev D3 Claude Code (3.1%), D8 agentic customization (4.1%), D2 configuration management (4.1%)

**Goal.** Pick the right extension type for a need, and configure it for a team.

**Build (45 min).** In `cert-lab`, write a project CLAUDE.md and a personal `CLAUDE.local.md`. Set shared permissions in `.claude/settings.json` and a personal override in `.claude/settings.local.json` ([R65](https://code.claude.com/docs/en/settings)). Write one Skill ([R68](https://code.claude.com/docs/en/skills)) that formats a release note. Run Claude Code headless with `claude -p` and JSON output ([R71](https://code.claude.com/docs/en/headless)). Then fill in a four-row table: built-in tool, custom tool, Skill, MCP server. One row each: what it is for, and one example need.

**Read (40 min).** [R12](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations) module 3, last segment. [R64](https://code.claude.com/docs/en/memory) Memory, the hierarchy section.

**Video backup.** [R91](https://anthropic.skilljar.com/introduction-to-agent-skills) Introduction to Agent Skills, 30 minutes. [R89](https://www.youtube.com/watch?v=gv0WHhKelSE) Claude Code best practices.

**Write.** One question on which settings file a team shares. One on Skill versus MCP server. One on pinning a model and versioning a prompt.

- [ ] D22: The four-row customization table, and a headless run that returns JSON.

## Day 23 · Security

Thursday 5 November · long day, 2 hours · Dev D7 application security (3.2%), guardrails (2.3%), secrets (1.6%)

**Goal.** Make the Day 18 agent survive a hostile input.

**Build (45 min).** Add a tool that fetches a "customer note". Plant an instruction in one note that tells the agent to refund the full order. Run it and record what happens. Fix it with layers: mark fetched content as untrusted data in the prompt, keep `issue_refund` behind the hook and the human checkpoint, and give the note-reading subagent no refund tool. Run again. Check that no key appears in logs or in the repo history.

**Read (70 min).** [R12](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations) module 4, first half. [R51](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) and [R73](https://code.claude.com/docs/en/security) for reference.

**Write.** One question on the most effective injection control. One on least privilege for tools. One on where API keys live in development and in production.

- [ ] D23: Before-and-after log of the injection test, with the planted instruction blocked.

## Day 24 · Evals and debugging

Friday 6 November · long day, 2 hours · Dev D4 debugging (2.6%), D2 application design (8.6%)

**Goal.** Define "done" as a test, and find whether a failure is mine or the model's.

**Build (45 min).** Turn the Day 13 test set into an eval script with a pass threshold. Run it against two models and two prompt versions. Store prompts in versioned files and pin the model version in config. Then break the integration on purpose (drop a field before it reaches the prompt) and use logs to show the fault is in my code, not the model.

**Read (70 min).** [R12](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations) module 4, second half. [R80](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) Demystifying evals, the grader types section.

**Video backup.** [R17](https://anthropic.skilljar.com/claude-with-the-anthropic-api), section Prompt evaluation.

**Write.** One question on code-graded versus model-graded checks. One on isolating integration faults from model faults. One on a regression after a model upgrade.

- [ ] D24: `eval.py` prints a pass rate per model and prompt version, and the traced fault is written up.

## Day 25 · Full timed mock

Saturday 7 November · long day, 2 hours

**Goal.** A full-length rehearsal and an honest gap list.

**Mock (100 min).** 50 questions from my bank and the Drills page, weighted roughly by blueprint: about 16 from D2, 8 from D5, 7 from D1, 6 from D6, 5 from D8, 4 from D7, and 2 each from D3 and D4. Timed. No docs.

**Review (20 min).** Score by domain. List the two weakest domains and the three skill lines behind them.

- [ ] D25: Mock score by domain recorded. Two weakest domains named.

## Day 26 · Rest

Sunday 8 November. Rest is part of the plan.

## Day 27 · Software engineering, platforms and gaps

Monday 9 November · Dev D2 requirements, life cycle, software engineering (13.6% together)

**Goal.** Cover the general engineering lines, then close the gaps from Day 25.

**Build (40 min).** Spend 20 minutes on the weakest domain from Day 25: redo the build step that covers it. Spend 20 minutes on third-party access: read how Claude is called through a cloud platform ([R41](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)) and write three lines on what changes (authentication, model IDs, feature parity).

**Read (50 min).** [R12](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations) module 4, any remaining part. [R12](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations) module 5, the section on choosing where a workload runs. Then skim [R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf) domain 2 skill lines on requirements, life cycle and software engineering. For each, write one sentence on how I already do it at work. These lines test general practice, not Claude features.

- [ ] D27: Weakest domain redone, and one sentence per general engineering skill line.

## Day 28 · Exam

Tuesday 10 November · **Developer Foundations, CCDV-F**

Light recall only: 20 questions from Drills, no new material. Then follow the exam-day checklist on the [Start](start.html) page.

- [ ] D28: Exam taken. Score and domain report recorded in `cert-lab/results.md`.
