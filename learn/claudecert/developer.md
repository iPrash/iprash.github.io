# Developer Foundations
## Days 4 to 28 · exam CCDV-F on Tuesday 10 November 2026

This block prepares the Claude Certified Developer, Foundations exam: 53 items, 120 minutes, pass at 720 of 1,000. The blueprint is in [R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf), section 6. Read it before Day 4.

Each day has the same shape: a goal, a build, a Learn step from an Anthropic course, reference docs, the topics for 3 drill questions, and a done-when checkbox. Every action and reference bullet has its own checkbox, so I can see where I stopped. Ticks are saved in this browser only. Also lists optional Anthropic material for a weak area. Domain tags show the blueprint weight, so I can see where the points are.

**Drill.** Claude asks me each question with no options. I answer cold, with no docs. Claude marks my answer and corrects it. Only after that does Claude add the multiple-choice version to Drills.

---

# Block map

## Where the points are

Weights from [R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf), version 1.0, July 2026. The right column shows which days cover each domain.

| Domain | Weight | Largest skill lines | Days |
|---|---|---|---|
| D1 Agents and Workflows | 14.7% | Agent construction 5.3%, patterns and frameworks 4.9% | 15, 17, 18, 20 |
| D2 Applications and Integration | 33.1% | Application design 8.6%, software engineering 7.4%, API mechanics 6.8% | 4, 7 to 11, 14, 22 to 24, 27 |
| D3 Claude Code | 3.1% | Claude Code operation 3.1% | 22, 27 |
| D4 Eval, Testing and Debugging | 2.6% | Debugging and error handling 2.6% | 8, 24 |
| D5 Model Selection and Optimization | 16.8% | Technical fundamentals 6.1%, LLM fundamentals 5.2% | 4, 6 to 11, 13, 24 |
| D6 Prompt and Context Engineering | 11.0% | Prompt engineering 4.6%, context engineering 3.8% | 13, 14, 20 |
| D7 Security and Safety | 8.1% | Application security 3.2%, guardrails 2.3% | 17, 18, 21 to 23 |
| D8 Tools and MCPs | 10.6% | Tool implementation 4.4%, agentic customization 4.1% | 15, 16, 17, 21, 22 |

Two things stand out. D2 and D5 together are half the exam, and a lot of D2 is general software engineering. D3 and D4 together are under 6%. Claude Code also appears in application design and configuration management (D2), so it gets a full build on Day 22 and a course on Day 27.

## Blueprint checklist

One line per skill in [R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf), section 6, with its weight and the days that cover it. Checked against the blueprint on 22 October 2026. I tick a line when I can explain the skill and have built it. Before the exam, every line should be ticked.

- [ ] BP 1.1 Agent architecture (4.5%): workflow versus agent, manager and supervisor hierarchies, subagents · days 17, 18, 20
- [ ] BP 1.2 Agent construction (5.3%): Agent SDK, custom loops and harnesses, self-hosted versus Anthropic-hosted, hooks · days 15, 18
- [ ] BP 1.3 Agent patterns and frameworks (4.9%): tool-use loops, subagents, memory, context management, LangGraph, Strands, PydanticAI · days 15, 17, 20
- [ ] BP 2.1 Understanding requirements (3.4%) · day 27
- [ ] BP 2.2 Systems life cycle (2.8%) · day 27
- [ ] BP 2.3 Claude API mechanics (6.8%): messages, tools, streaming, vision, thinking, caching, third-party vendors, batch versus realtime · days 4, 7 to 11, 27
- [ ] BP 2.4 Software engineering foundations (7.4%): REST, JSON, async, version control, SDLC, code review, refactoring · days 8, 24, 27
- [ ] BP 2.5 Claude application design (8.6%): instructions across interfaces, content boundaries, schema design, session hygiene, plugins · days 7, 14, 22, 23
- [ ] BP 2.6 Configuration management (4.1%): CLAUDE.md, settings.json, model version pinning, prompt versioning, plugin dependencies · days 22, 24
- [ ] BP 3.1 Claude Code operation (3.1%): rules, Skills, commands, agents, memory, sessions, slash commands, headless and streaming modes, auto mode, CLAUDE.md hierarchy, settings.json · days 22, 27
- [ ] BP 4.1 Debugging and error handling (2.6%): error types, recovery strategy, trace analysis, integration versus model faults · days 8, 24
- [ ] BP 5.1 LLM fundamentals (5.2%): tokens, context windows, sampling, non-determinism, fast mode, thinking, effort, zero-shot to multi-shot · days 6, 7, 9, 10, 13
- [ ] BP 5.2 Technical fundamentals (6.1%): SDKs that wrap REST APIs, websockets · day 8
- [ ] BP 5.3 Model selection and trade-offs (2.7%): Opus, Sonnet, Haiku, quality, latency, cost, breaking changes between releases · days 7, 24
- [ ] BP 5.4 Cost and token management (2.8%): usage tracking, cost models, prompt caching · days 6, 10, 11
- [ ] BP 6.1 Context engineering (3.8%): window management, drift and bloat, pruning, compaction, isolation through subagents · day 20
- [ ] BP 6.2 Prompt engineering (4.6%): clarity, few-shot, system versus user placement, output constraints, iteration, input sanitization · day 13
- [ ] BP 6.3 Output handling (2.6%): structured output, validation, defensive parsing, skepticism toward confident output · day 14
- [ ] BP 7.1 AI application security (3.2%): prompt injection, jailbreaks, untrusted input, data leakage, PII · day 23
- [ ] BP 7.2 Guardrails and safe deployment (2.3%): guardrail layering, least privilege · days 17, 23
- [ ] BP 7.3 Claude hooks (1.0%) · days 18, 22
- [ ] BP 7.4 Identity, secrets and key management (1.6%): keys across environments, access approval, access monitoring · days 2, 21, 23
- [ ] BP 8.1 Tool implementation (4.4%): tool descriptions, error handling, client-side versus server-side tools, approval patterns · days 15, 16, 17
- [ ] BP 8.2 MCP server development (2.1%): tools, resources, prompts, stdio and network transports, client versus server · day 21
- [ ] BP 8.3 Agentic customization (4.1%): built-in tools versus custom tools versus Skills versus MCP · days 16, 22

## The reading spine

Anthropic's own courses are the baseline. Two Anthropic sources set the Learn step for every day: the exam prep course ([R12](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations), modules [R103](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/mso-foundations) to [R107](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/accelerators-ip-contribution)) and the Claude Developer learning path ([R97](https://anthropic-partners.skilljar.com/path/claude-developer)). Enrol in both before Day 4. Docs pages are reference during the build. I read the section I need, not the whole page.

| Course | Source | Length | Days | Status |
|---|---|---|---|---|
| [R103](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/mso-foundations) MSO Foundations | Prep course | 57 min | 4 | Required |
| [R104](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/production-grade-prompting-agents-tool-use) Production-Grade Prompting, Agents & Tool Use | Prep course | 209 min | 13 to 17 | Required |
| [R105](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/claude-code-mcp-integration) Claude Code, MCP & Integration | Prep course | 142 min | 20 to 22 | Required |
| [R106](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/production-engineering-evals-security) Production Engineering, Evals & Security | Prep course | 211 min | 23, 24 | Required |
| [R107](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/accelerators-ip-contribution) Accelerators & IP Contribution | Prep course | 155 min | 27 | Optional: the platform-choice section |
| [R98](https://anthropic-partners.skilljar.com/path/claude-developer/ai-capabilities-and-limitations) AI capabilities and limitations | Developer path | 3.5 h | 6, 9, 10, 13, 14 | Required |
| [R99](https://anthropic-partners.skilljar.com/path/claude-developer/ai-fluency-for-builders) AI Fluency for builders | Developer path | 3 h | 27 | Optional |
| [R100](https://anthropic-partners.skilljar.com/path/claude-developer/claude-platform-model-foundations) Claude Platform & Model Foundations | Developer path | 59 min | 7 | Required |
| [R101](https://anthropic-partners.skilljar.com/path/claude-developer/claude-platform-101) Claude Platform 101 | Developer path | 1.5 h | 4, 7, 15, 18 | Required |
| [R102](https://anthropic-partners.skilljar.com/path/claude-developer/claude-code-101) Claude Code 101 | Developer path | 1.5 h | 22 | Required |
| [R18](https://anthropic-partners.skilljar.com/path/claude-developer/claude-code-in-action) Claude Code in Action | Developer path | 1 h | 27 | Required |
| [R19](https://anthropic-partners.skilljar.com/path/claude-developer/introduction-to-model-context-protocol) Introduction to Model Context Protocol | Developer path | 1 h | 21 | Required |
| [R91](https://anthropic-partners.skilljar.com/path/claude-developer/introduction-to-agent-skills) Introduction to agent skills | Developer path | 1 h | 16 | Required |
| [R92](https://anthropic-partners.skilljar.com/path/claude-developer/introduction-to-subagents) Introduction to subagents | Developer path | 45 min | 20 | Required |
| [R17](https://anthropic-partners.skilljar.com/claude-with-the-anthropic-api) Building with the Claude API | Prep course recommended | 9 h | 8, 9, 10 required. Other sections as backup | Partly required |
| [R108](https://academy.claude.com/courses/ai-native-sdlc-playbook) The AI-native SDLC playbook | Claude Academy | 1 h | 27 | Required |
| [R20](https://anthropic-partners.skilljar.com/model-context-protocol-advanced-topics) Model Context Protocol: Advanced Topics | Prep course recommended | 1.5 h | 21 | Optional: the transport lessons |

The required courses total about 25 hours. With the builds, a day now holds 1.5 to 2.5 hours. At 90 minutes a sitting, some days take two sittings. The dates under each day show the fastest pace, not a deadline.

---

# Week 1 · API basics

## Day 4 · First real calls

Saturday 17 October · long day, 2 hours · Dev D2 API mechanics, D5 LLM fundamentals

**Goal.** Understand one Messages API request and response completely.

**Build · 60 min**

- [ ] D4: In `CertLab/01_API/`, write `basics.py`.
- [ ] D4: Send a request with a system prompt and two user turns.
- [ ] D4: Print the full response object, not only the text.
- [ ] D4: Identify `stop_reason`, `usage.input_tokens` and `usage.output_tokens`.
- [ ] D4: Set `max_tokens` to 20 and watch `stop_reason` change to `max_tokens`.
- [ ] D4: Add a stop sequence and watch it change to `stop_sequence`.

**Learn · 60 min**

- [ ] D4: [R103](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/mso-foundations) MSO Foundations, all of it.

**Also**

- [ ] D4: [R101](https://anthropic-partners.skilljar.com/path/claude-developer/claude-platform-101) Claude Platform 101, the lesson on the first API call.

**Reference**

- [ ] D4: Reference: [R24](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) Messages API.

**Drill**

- [ ] D4: Drill: One question on `stop_reason` values.
- [ ] D4: Drill: One on where a system prompt goes in the request.
- [ ] D4: Drill: One on what `max_tokens` controls and what it does not.

**Done when**

- [ ] D4: `basics.py` prints three different `stop_reason` values, and I can explain each.

## Day 5 · Rest

Sunday 18 October. No study. If a read from this week ran over, it can move here.

## Day 6 · Tokens, context and sampling

Monday 19 October · Dev D5 LLM fundamentals (5.2%)

**Goal.** Make tokens, context windows and non-determinism concrete.

**Build · 45 min**

- [ ] D6: Use the token counting endpoint ([R29](https://platform.claude.com/docs/en/build-with-claude/token-counting)) on three inputs: a short prompt, a 20-page text, and an image.
- [ ] D6: Record the counts.
- [ ] D6: Send the same open-ended prompt five times and diff the outputs.
- [ ] D6: Repeat with a prompt that has one correct answer.
- [ ] D6: Note where variation matters and where it does not.

**Learn · 95 min**

- [ ] D6: [R98](https://anthropic-partners.skilljar.com/path/claude-developer/ai-capabilities-and-limitations) AI capabilities and limitations: the opening lessons, then the Next Token Prediction section and its exercise.

**Also**

- [ ] D6: [R109](https://academy.claude.com/tutorials/tokens-and-embeddings) Tokens tutorial, 15 minutes.
- [ ] D6: [R110](https://academy.claude.com/tutorials/parametric-memory-and-context) How context affects performance and cost, 20 minutes.

**Reference**

- [ ] D6: Reference: [R32](https://platform.claude.com/docs/en/build-with-claude/context-windows) Context windows.
- [ ] D6: Reference: [R29](https://platform.claude.com/docs/en/build-with-claude/token-counting) Token counting.
- [ ] D6: Reference: The first part of [R39](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), the sections on being clear and on examples.

**Drill**

- [ ] D6: Drill: One question on why outputs vary between identical requests.
- [ ] D6: Drill: One on what counts against the context window.
- [ ] D6: Drill: One on zero-shot versus few-shot.

**Done when**

- [ ] D6: A table in `01_API/notes.md` with token counts for three inputs and a one-line finding on output variation.

## Day 7 · Model tiers, thinking and effort

Tuesday 20 October · Dev D5 model selection (2.7%), LLM fundamentals

**Goal.** Choose a model from evidence, not habit.

**Build · 45 min**

- [ ] D7: Run three tasks on the current Haiku, Sonnet and Opus models ([R35](https://platform.claude.com/docs/en/models/overview)): a short classification, a structured summary, and a multi-step reasoning problem.
- [ ] D7: Record latency, tokens and a quality grade for each.
- [ ] D7: Run the reasoning task again with adaptive thinking ([R30](https://platform.claude.com/docs/en/build-with-claude/thinking)) and at two effort settings ([R31](https://platform.claude.com/docs/en/build-with-claude/effort)).
- [ ] D7: Try fast mode ([R114](https://platform.claude.com/docs/en/build-with-claude/fast-mode)) on one task if the model supports it, and record the change in speed and price.
- [ ] D7: Note the exact model ID I used and whether it is an alias or a pinned snapshot ([R115](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)).

**Learn · 60 min**

- [ ] D7: [R100](https://anthropic-partners.skilljar.com/path/claude-developer/claude-platform-model-foundations) Claude Platform & Model Foundations, 59 minutes.

**Also**

- [ ] D7: [R101](https://anthropic-partners.skilljar.com/path/claude-developer/claude-platform-101), the lesson on choosing the right model.
- [ ] D7: [R111](https://academy.claude.com/tutorials/choosing-the-right-claude-model) tutorial.

**Reference**

- [ ] D7: Reference: [R36](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model) Choosing a model.
- [ ] D7: Reference: [R37](https://platform.claude.com/docs/en/about-claude/model-deprecations) Model deprecations: note what changes when a model version is retired.
- [ ] D7: Reference: [R30](https://platform.claude.com/docs/en/build-with-claude/thinking) Thinking, including which models support adaptive thinking.
- [ ] D7: Reference: [R31](https://platform.claude.com/docs/en/build-with-claude/effort) Effort.
- [ ] D7: Reference: [R114](https://platform.claude.com/docs/en/build-with-claude/fast-mode) Fast mode.
- [ ] D7: Reference: [R115](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) Model IDs and versioning.

**Drill**

- [ ] D7: Drill: One question that gives a workload and asks for a model tier.
- [ ] D7: Drill: One on when thinking and higher effort are worth their cost, and when fast mode is.
- [ ] D7: Drill: One on why pinning a model version matters.

**Done when**

- [ ] D7: A 3 by 3 table (task by model) with latency, cost and quality, and a one-line rule I would apply.

---

# Week 2 · Production mechanics

## Day 8 · Streaming, errors and raw HTTP

Wednesday 21 October · Dev D2 API mechanics, D4 debugging, D5 technical fundamentals (6.1%)

**Goal.** Handle the API the way production code must.

**Build · 45 min**

- [ ] D8: Call the API once with plain HTTP (`requests` or `curl`), then with the SDK.
- [ ] D8: Compare what the SDK adds: retries, typed errors, streaming helpers.
- [ ] D8: Stream a long response ([R25](https://platform.claude.com/docs/en/build-with-claude/streaming)) and print text as it arrives.
- [ ] D8: Force three errors: a bad API key, an invalid request, and a too-large `max_tokens`.
- [ ] D8: Write a retry wrapper that retries only errors that a retry can fix, including 429 rate-limit errors ([R117](https://platform.claude.com/docs/en/api/rate-limits)).
- [ ] D8: Then switch to the async client ([R116](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python)) and run three requests at the same time.
- [ ] D8: Note that the API streams over server-sent events, and read how a websocket differs ([R118](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)).

**Learn · 60 min**

- [ ] D8: [R17](https://anthropic-partners.skilljar.com/claude-with-the-anthropic-api), section Accessing Claude with the API: requests, multi-turn, system prompts, temperature, streaming and structured data.

**Reference**

- [ ] D8: Reference: [R40](https://platform.claude.com/docs/en/api/errors) API errors.
- [ ] D8: Reference: [R25](https://platform.claude.com/docs/en/build-with-claude/streaming) Streaming, the event-types section.
- [ ] D8: Reference: [R116](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python) Python SDK, sync and async clients.
- [ ] D8: Reference: [R117](https://platform.claude.com/docs/en/api/rate-limits) Rate limits.
- [ ] D8: Reference: [R118](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) WebSockets, for the comparison only.

**Drill**

- [ ] D8: Drill: One question on which HTTP errors to retry.
- [ ] D8: Drill: One on what streaming changes for the user and what it does not change for cost.
- [ ] D8: Drill: One on SDK versus raw REST, or sync versus async calls.

**Done when**

- [ ] D8: `errors.py` shows each forced error caught by type, with retry only on retryable errors.

## Day 9 · Vision and documents

Thursday 22 October · Dev D2 API mechanics, application design (8.6%)

**Goal.** Send non-text input correctly.

**Build · 45 min**

- [ ] D9: Send an image by base64 and by URL.
- [ ] D9: Ask for a structured description.
- [ ] D9: Send a short PDF as a document block and ask for a table from it.
- [ ] D9: Measure the token cost of each input.

**Learn · 75 min**

- [ ] D9: [R17](https://anthropic-partners.skilljar.com/claude-with-the-anthropic-api), section Features of Claude: Image support, PDF support, Citations, and Code execution and the Files API.
- [ ] D9: Then [R98](https://anthropic-partners.skilljar.com/path/claude-developer/ai-capabilities-and-limitations), the Working Memory section and its exercise.

**Reference**

- [ ] D9: Reference: [R26](https://platform.claude.com/docs/en/build-with-claude/vision) Vision.
- [ ] D9: Reference: [R24](https://platform.claude.com/docs/en/build-with-claude/working-with-messages), the section on content blocks.

**Drill**

- [ ] D9: Drill: One question on image versus document input.
- [ ] D9: Drill: One on the cost of large images.
- [ ] D9: Drill: One on where in the message to put an image relative to the question.

**Done when**

- [ ] D9: Image and PDF inputs both return correct structured output, with token cost recorded.

## Day 10 · Prompt caching and the cost model

Friday 23 October · Dev D5 cost and token management (2.8%)

**Goal.** Cut repeated-prefix cost and prove it with numbers.

**Build · 45 min**

- [ ] D10: Put a long, fixed system prompt (over the minimum cacheable length in [R27](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)) before a short user question.
- [ ] D10: Add a cache breakpoint.
- [ ] D10: Send the request three times.
- [ ] D10: Record `cache_creation_input_tokens` and `cache_read_input_tokens`.
- [ ] D10: Build a small cost model: requests per day, prefix size, hit rate, saving.
- [ ] D10: Then change one word in the prefix and show the cache miss.

**Learn · 70 min**

- [ ] D10: [R17](https://anthropic-partners.skilljar.com/claude-with-the-anthropic-api), section Features of Claude: Extended thinking and the three prompt caching lessons.
- [ ] D10: Then [R98](https://anthropic-partners.skilljar.com/path/claude-developer/ai-capabilities-and-limitations), the Knowledge section and its exercise.

**Reference**

- [ ] D10: Reference: [R27](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) Prompt caching, including what invalidates the cache.

**Drill**

- [ ] D10: Drill: One question on what makes a cache miss.
- [ ] D10: Drill: One on ordering content so the stable part comes first.
- [ ] D10: Drill: One that asks which workload benefits most from caching.

**Done when**

- [ ] D10: A cost-model sheet showing cached versus uncached cost for one realistic workload.

## Day 11 · Batches and the first mini-mock

Saturday 24 October · long day, 2 hours · Dev D2 API mechanics, batch versus realtime

**Goal.** Know when batch beats realtime, and run my first timed drill.

**Build · 60 min**

- [ ] D11: Submit a batch of 20 requests with unique `custom_id` values ([R28](https://platform.claude.com/docs/en/build-with-claude/batch-processing)).
- [ ] D11: Include one request that will fail.
- [ ] D11: Poll until the batch ends.
- [ ] D11: Match results to inputs by `custom_id`, not by order.
- [ ] D11: Resubmit the failed one.

**Mock · 60 min**

- [ ] D11: 20 questions from my bank and the Drills page, timed at 2 minutes each.
- [ ] D11: Then review every miss and write down why I missed it.

**Drill**

- [ ] D11: Drill: One question on matching batch results.
- [ ] D11: Drill: One on a latency-tolerant workload.
- [ ] D11: Drill: One on what batches do not support.

**Done when**

- [ ] D11: Batch run completes with one failure handled by `custom_id`. Mock score recorded in `CertLab/results.md`.

## Day 12 · Rest

Sunday 25 October.

## Day 13 · Prompt engineering

Monday 26 October · Dev D6 prompt engineering (4.6%)

**Goal.** Improve a prompt by measurement, not by feel.

**Build · 45 min**

- [ ] D13: In `CertLab/02_Prompts/`, build a support-ticket classifier with five categories.
- [ ] D13: Write 20 labeled test tickets, including 5 ambiguous ones.
- [ ] D13: Score version 1 of the prompt.
- [ ] D13: Then change one thing at a time: clear instructions, XML tags around the ticket, a system-prompt role, and 3 examples that target the ambiguous cases.
- [ ] D13: Score each version.

**Learn · 75 min**

- [ ] D13: [R104](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/production-grade-prompting-agents-tool-use), first segment.
- [ ] D13: Then [R98](https://anthropic-partners.skilljar.com/path/claude-developer/ai-capabilities-and-limitations), the Steerability section and its exercise.

**Also**

- [ ] D13: [R17](https://anthropic-partners.skilljar.com/claude-with-the-anthropic-api), section Prompt engineering techniques.
- [ ] D13: [R85](https://www.youtube.com/watch?v=ysPbXH0LpIE) Prompting 101.

**Reference**

- [ ] D13: Reference: [R39](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) Prompting best practices.

**Drill**

- [ ] D13: Drill: One question on system versus user placement.
- [ ] D13: Drill: One on why examples should target the ambiguous cases.
- [ ] D13: Drill: One on input sanitization.

**Done when**

- [ ] D13: A score table: prompt version by accuracy on 20 tickets, with the change that helped most.

## Day 14 · Structured output and defensive parsing

Tuesday 27 October · Dev D6 output handling (2.6%)

**Goal.** Get output my code can trust.

**Build · 45 min**

- [ ] D14: Make the classifier return JSON: category, confidence, and a short reason.
- [ ] D14: First try with instructions only, and count parse failures over 20 runs.
- [ ] D14: Then use structured outputs or strict tool use ([R34](https://platform.claude.com/docs/en/build-with-claude/structured-outputs), [R47](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use)).
- [ ] D14: Validate with Pydantic.
- [ ] D14: On a validation failure, retry once with the error message included.

**Learn · 90 min**

- [ ] D14: [R104](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/production-grade-prompting-agents-tool-use), second segment.
- [ ] D14: Then [R98](https://anthropic-partners.skilljar.com/path/claude-developer/ai-capabilities-and-limitations), the last section, Putting it all together, and the course quiz.

**Also**

- [ ] D14: [R17](https://anthropic-partners.skilljar.com/claude-with-the-anthropic-api), the Structured data lesson.

**Reference**

- [ ] D14: Reference: [R34](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) Structured outputs.
- [ ] D14: Reference: [R47](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use) Strict tool use.

**Drill**

- [ ] D14: Drill: One question on schema-guaranteed output versus instruction-only JSON.
- [ ] D14: Drill: One on what validation cannot catch.
- [ ] D14: Drill: One on a confident but wrong answer.

**Done when**

- [ ] D14: Zero parse failures over 20 runs, and a retry path that I have seen fire.

---

# Week 3 · Tools, agents and MCP

## Day 15 · Tool use, by hand

Wednesday 28 October · Dev D8 tool implementation (4.4%)

**Goal.** Run the tool-use loop myself before any framework does it for me.

**Build · 45 min**

- [ ] D15: In `CertLab/03_Agent/`, define three tools for an order-support case: `lookup_order`, `get_policy`, `issue_refund`.
- [ ] D15: Write the loop: send, check `stop_reason`, run the tool when it is `tool_use`, return a `tool_result`, repeat until `end_turn`.
- [ ] D15: Return `is_error: true` with a clear message when an order is not found.
- [ ] D15: Add a maximum-turns limit.

**Learn · 60 min**

- [ ] D15: [R104](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/production-grade-prompting-agents-tool-use), third segment.
- [ ] D15: Then [R101](https://anthropic-partners.skilljar.com/path/claude-developer/claude-platform-101), the section Teaching your Agent: the agent loop, tool use and thinking.

**Also**

- [ ] D15: [R17](https://anthropic-partners.skilljar.com/claude-with-the-anthropic-api), section Tool use with Claude, up to Multi-turn conversations with tools.

**Reference**

- [ ] D15: Reference: [R43](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works) How tool use works.
- [ ] D15: Reference: [R45](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) Handle tool calls.

**Drill**

- [ ] D15: Drill: One question on what ends the loop.
- [ ] D15: Drill: One on how to report a tool failure to the model.
- [ ] D15: Drill: One on client-side versus server-side tools.

**Done when**

- [ ] D15: The loop handles a two-tool request and a not-found error, and stops at the turn limit.

## Day 16 · Tool choice and tool descriptions

Thursday 29 October · Dev D8 tool implementation, tool set construction

**Goal.** Control which tool runs, and make the model pick the right one.

**Build · 45 min**

- [ ] D16: Try `tool_choice` set to auto, any, a named tool, and none.
- [ ] D16: Note what each does.
- [ ] D16: Add a fourth tool, `get_order_status`, that overlaps with `lookup_order`.
- [ ] D16: Send 10 ambiguous requests and count wrong picks.
- [ ] D16: Rewrite both descriptions to separate them clearly.
- [ ] D16: Count again.
- [ ] D16: Ask for two independent lookups in one message and watch for parallel tool calls ([R46](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use)).

**Learn · 100 min**

- [ ] D16: [R104](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/production-grade-prompting-agents-tool-use), fourth segment.
- [ ] D16: Then [R91](https://anthropic-partners.skilljar.com/path/claude-developer/introduction-to-agent-skills) Introduction to agent skills, 1 hour.

**Also**

- [ ] D16: [R17](https://anthropic-partners.skilljar.com/claude-with-the-anthropic-api), section Tool use with Claude, from Using multiple tools to the end.

**Reference**

- [ ] D16: Reference: [R78](https://www.anthropic.com/engineering/writing-tools-for-agents) Writing effective tools for agents.
- [ ] D16: Reference: [R46](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use) Parallel tool use.
- [ ] D16: Reference: [R119](https://code.claude.com/docs/en/features-overview) Extend Claude Code, the comparison of Skills, subagents, hooks, MCP and plugins.

**Drill**

- [ ] D16: Drill: One question on forcing a tool.
- [ ] D16: Drill: One on fixing tool confusion.
- [ ] D16: Drill: One on splitting versus merging two tools, or on built-in tool versus custom tool versus Skill versus MCP server.

**Done when**

- [ ] D16: Wrong-pick count before and after the description rewrite.

## Day 17 · Workflow or agent

Friday 30 October · Dev D1 agent architecture (4.5%)

**Goal.** Decide when a fixed workflow is better than an agent.

**Build · 45 min**

- [ ] D17: Add a human approval checkpoint before `issue_refund`.
- [ ] D17: The loop pauses, prints the planned refund, and waits for yes or no.
- [ ] D17: Add a spend budget that stops the agent.
- [ ] D17: Then sketch, in `notes.md`, the same case as a fixed workflow (classify, look up, apply policy, draft reply) and list what each design is better at.

**Learn · 55 min**

- [ ] D17: [R104](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/production-grade-prompting-agents-tool-use), last segment.
- [ ] D17: Then [R84](https://www.youtube.com/watch?v=D7_ipDqhtwk) How We Build Effective Agents, 15 minutes.

**Also**

- [ ] D17: [R17](https://anthropic-partners.skilljar.com/claude-with-the-anthropic-api), section Agents and workflows.

**Reference**

- [ ] D17: Reference: [R77](https://www.anthropic.com/engineering/building-effective-agents) Building effective agents.

**Drill**

- [ ] D17: Drill: One question on workflow versus agent.
- [ ] D17: Drill: One on where to place a human checkpoint.
- [ ] D17: Drill: One on supervisor and subagent roles.

**Done when**

- [ ] D17: The refund pauses for approval, and `notes.md` compares the two designs.

## Day 18 · The Agent SDK and a blocking hook

Saturday 31 October · long day, 2 hours · Dev D1 agent construction (5.3%), D7 hooks (1.0%)

**Goal.** Rebuild the agent on the Agent SDK and enforce a rule in code.

**Build · 75 min**

- [ ] D18: Follow [R56](https://code.claude.com/docs/en/agent-sdk/quickstart) to set up the Agent SDK.
- [ ] D18: Rebuild the Day 15 agent with custom tools ([R58](https://code.claude.com/docs/en/agent-sdk/custom-tools)).
- [ ] D18: Add a PreToolUse hook ([R59](https://code.claude.com/docs/en/agent-sdk/hooks)) that blocks any refund above a limit and returns a reason.
- [ ] D18: Add one subagent ([R60](https://code.claude.com/docs/en/agent-sdk/subagents)) that only drafts the customer reply.
- [ ] D18: Compare the code size and behavior with the hand-written loop.

**Mock · 45 min**

- [ ] D18: 15 questions on Days 4 to 17, timed.
- [ ] D18: Review every miss.

**Learn · 40 min, or on Day 19**

- [ ] D18: [R101](https://anthropic-partners.skilljar.com/path/claude-developer/claude-platform-101), the sections Extending your Agent and Managed Agents: built-in tools, Skills, MCP, context management and managed agents.
- [ ] D18: [R112](https://academy.claude.com/tutorials/what-is-claude-managed-agents) tutorial, 4 minutes.

**Also**

- [ ] D18: [R87](https://www.youtube.com/watch?v=TqC1qOfiVcQ) Agent SDK workshop, the first 45 minutes.

**Reference**

- [ ] D18: Reference: [R56](https://code.claude.com/docs/en/agent-sdk/quickstart) Quickstart.
- [ ] D18: Reference: [R58](https://code.claude.com/docs/en/agent-sdk/custom-tools) Custom tools.
- [ ] D18: Reference: [R59](https://code.claude.com/docs/en/agent-sdk/hooks) Hooks.
- [ ] D18: Reference: [R60](https://code.claude.com/docs/en/agent-sdk/subagents) Subagents.
- [ ] D18: Reference: [R120](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner) Tool runner.
- [ ] D18: Reference: [R121](https://platform.claude.com/docs/en/managed-agents/overview) Managed Agents overview.
- [ ] D18: Reference: [R122](https://platform.claude.com/docs/en/managed-agents/choosing-an-environment) Choose an agent environment: Anthropic-hosted versus self-hosted.

**Drill**

- [ ] D18: Drill: One question on a hook versus a prompt instruction for a business rule.
- [ ] D18: Drill: One on what a subagent's separate context gives.
- [ ] D18: Drill: One on self-hosted versus managed agent deployment.

**Done when**

- [ ] D18: The hook blocks an over-limit refund in a test run, and the mock score is recorded.

## Day 19 · Rest

Sunday 1 November.

## Day 20 · Context engineering

Monday 2 November · Dev D6 context engineering (3.8%), D1 patterns and frameworks (4.9%)

**Goal.** Keep long agent runs inside a useful context.

**Build · 45 min**

- [ ] D20: Make one tool return a large, noisy payload.
- [ ] D20: Run a 10-turn session and watch token use grow.
- [ ] D20: Fix it three ways and compare: prune the tool output to the fields needed, use compaction ([R33](https://platform.claude.com/docs/en/build-with-claude/compaction)), and move a sub-task into a subagent so only its summary returns.
- [ ] D20: Then read the quickstart of one framework (LangGraph, Strands or PydanticAI) for 10 minutes.
- [ ] D20: Note how it names the same ideas.

**Learn · 90 min**

- [ ] D20: [R105](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/claude-code-mcp-integration), first third.
- [ ] D20: Then [R92](https://anthropic-partners.skilljar.com/path/claude-developer/introduction-to-subagents) Introduction to subagents, 45 minutes.

**Also**

- [ ] D20: [R86](https://www.youtube.com/watch?v=XSZP9GhhuAc) Prompting for Agents.

**Reference**

- [ ] D20: Reference: [R79](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) Effective context engineering.
- [ ] D20: Reference: [R33](https://platform.claude.com/docs/en/build-with-claude/compaction) Compaction.
- [ ] D20: Reference: [R123](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool) Memory tool.
- [ ] D20: Reference: [R124](https://platform.claude.com/docs/en/build-with-claude/context-editing) Context editing.

**Drill**

- [ ] D20: Drill: One question on context drift.
- [ ] D20: Drill: One on pruning versus compaction versus the memory tool.
- [ ] D20: Drill: One on context isolation through subagents.

**Done when**

- [ ] D20: Token use per turn, before and after each fix, in `notes.md`.

## Day 21 · Build an MCP server

Tuesday 3 November · Dev D8 MCP server development (2.1%)

**Goal.** Expose a capability once and use it from more than one client.

**Build · 45 min**

- [ ] D21: In `CertLab/04_MCP/`, build a Python MCP server ([R76](https://modelcontextprotocol.io/docs/develop/build-server)) with two tools (`lookup_order`, `get_policy`), one resource (the refund policy text), and one prompt (a reply template).
- [ ] D21: Run it over stdio.
- [ ] D21: Connect it to Claude Code with a project-scoped `.mcp.json` ([R70](https://code.claude.com/docs/en/mcp)).
- [ ] D21: Put the credential in an environment variable, not in the file.
- [ ] D21: Call each primitive from Claude Code.
- [ ] D21: Then run the same server over Streamable HTTP and note what changes ([R125](https://modelcontextprotocol.io/specification/latest/basic/transports)).

**Learn · 105 min**

- [ ] D21: [R19](https://anthropic-partners.skilljar.com/path/claude-developer/introduction-to-model-context-protocol) Introduction to Model Context Protocol, 1 hour.
- [ ] D21: It builds a Python server, like today's build.
- [ ] D21: Then [R105](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/claude-code-mcp-integration), second third.

**Also**

- [ ] D21: [R20](https://anthropic-partners.skilljar.com/model-context-protocol-advanced-topics) MCP Advanced Topics, the transport lessons.
- [ ] D21: [R88](https://www.youtube.com/watch?v=kQmXtrmQ5Zg) MCP workshop, the first hour, or [R94](https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic).

**Reference**

- [ ] D21: Reference: [R76](https://modelcontextprotocol.io/docs/develop/build-server) Build an MCP server.
- [ ] D21: Reference: [R75](https://modelcontextprotocol.io/docs/getting-started/intro) for the three primitives.
- [ ] D21: Reference: [R70](https://code.claude.com/docs/en/mcp) MCP in Claude Code.
- [ ] D21: Reference: [R125](https://modelcontextprotocol.io/specification/latest/basic/transports) MCP transports.

**Drill**

- [ ] D21: Drill: One question on tools versus resources versus prompts.
- [ ] D21: Drill: One on stdio versus a network transport.
- [ ] D21: Drill: One on keeping secrets out of `.mcp.json`.

**Done when**

- [ ] D21: Claude Code calls both tools and reads the resource through my server.

---

# Week 4 · Configuration, security and evaluation

## Day 22 · Claude Code, Skills and the customization choice

Wednesday 4 November · Dev D3 Claude Code (3.1%), D8 agentic customization (4.1%), D2 configuration management (4.1%)

**Goal.** Pick the right extension type for a need, and configure it for a team.

**Build · 75 min**

- [ ] D22: In `CertLab`, write a project CLAUDE.md and a personal `CLAUDE.local.md`.
- [ ] D22: Add one path-scoped rule in `.claude/rules/` ([R129](https://code.claude.com/docs/en/claude-directory)).
- [ ] D22: Set shared permissions in `.claude/settings.json` and a personal override in `.claude/settings.local.json` ([R65](https://code.claude.com/docs/en/settings)).
- [ ] D22: Write one Skill ([R68](https://code.claude.com/docs/en/skills)) that formats a release note, and run it as a slash command.
- [ ] D22: Add one custom subagent.
- [ ] D22: Package the Skill and the subagent as a plugin and install it from the local folder ([R130](https://code.claude.com/docs/en/plugins/create), [R131](https://code.claude.com/docs/en/plugins/components)).
- [ ] D22: Try three permission modes, including auto mode ([R128](https://code.claude.com/docs/en/permission-modes)).
- [ ] D22: Name a session, then resume it, and note when to use `/clear` versus `/compact` ([R127](https://code.claude.com/docs/en/sessions)).
- [ ] D22: Run Claude Code headless with `claude -p`, first with JSON output, then with stream-json ([R71](https://code.claude.com/docs/en/headless)).

Then fill in two tables in `notes.md`. First, the four extension types: built-in tool, custom tool, Skill, MCP server. One row each: what it is for, and one example need. Second, where instructions live on each interface: claude.ai project instructions, the Desktop app, Claude Code (CLAUDE.md and rules), the API system prompt, and the Agent SDK ([R126](https://code.claude.com/docs/en/platforms)).

**Learn · 135 min, two sittings**

- [ ] D22: [R105](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/claude-code-mcp-integration), last third.
- [ ] D22: Then [R102](https://anthropic-partners.skilljar.com/path/claude-developer/claude-code-101) Claude Code 101, 1.5 hours.

**Also**

- [ ] D22: [R113](https://academy.claude.com/tutorials/what-are-skills) skills tutorials.
- [ ] D22: [R89](https://www.youtube.com/watch?v=gv0WHhKelSE) Claude Code best practices.
- [ ] D22: [R90](https://www.youtube.com/watch?v=dRsjO-88nBs) headless automation.
- [ ] D22: [R93](https://claude.com/resources/guides/the-complete-guide-to-building-skills-for-claude) Skills guide.

**Reference**

- [ ] D22: Reference: [R64](https://code.claude.com/docs/en/memory) Memory, the hierarchy section.
- [ ] D22: Reference: [R65](https://code.claude.com/docs/en/settings) Settings.
- [ ] D22: Reference: [R68](https://code.claude.com/docs/en/skills) Skills.
- [ ] D22: Reference: [R71](https://code.claude.com/docs/en/headless) Headless mode.
- [ ] D22: Reference: [R126](https://code.claude.com/docs/en/platforms) Platforms and integrations.
- [ ] D22: Reference: [R127](https://code.claude.com/docs/en/sessions) Sessions.
- [ ] D22: Reference: [R128](https://code.claude.com/docs/en/permission-modes) Permission modes.
- [ ] D22: Reference: [R129](https://code.claude.com/docs/en/claude-directory) The .claude directory.
- [ ] D22: Reference: [R130](https://code.claude.com/docs/en/plugins/create) Create a plugin.
- [ ] D22: Reference: [R131](https://code.claude.com/docs/en/plugins/components) Plugin components.

**Drill**

- [ ] D22: Drill: One question on which settings file a team shares.
- [ ] D22: Drill: One on where an instruction belongs: CLAUDE.md, a rule, a Skill or a hook.
- [ ] D22: Drill: One on session hygiene in a long session.

**Done when**

- [ ] D22: The four-row customization table, and a headless run that returns JSON.
- [ ] D22: The plugin installs from a local folder, and both tables are in `notes.md`.

## Day 23 · Security

Thursday 5 November · long day, 2 hours · Dev D7 application security (3.2%), guardrails (2.3%), secrets (1.6%)

**Goal.** Make the Day 18 agent survive a hostile input.

**Build · 45 min**

- [ ] D23: Add a tool that fetches a "customer note".
- [ ] D23: Plant an instruction in one note that tells the agent to refund the full order.
- [ ] D23: Run it and record what happens.
- [ ] D23: Fix it with layers: mark fetched content as untrusted data in the prompt, keep `issue_refund` behind the hook and the human checkpoint, and give the note-reading subagent no refund tool.
- [ ] D23: Run again.
- [ ] D23: Add a step that redacts personal data (names, emails, order IDs tied to a person) before anything is logged.
- [ ] D23: Check that no key appears in logs or in the repo history.
- [ ] D23: Then open the `CertLab` workspace from Day 2 ([R132](https://platform.claude.com/docs/en/manage-claude/workspaces)), and look at the `CertLabDev` key's usage in the Usage and Cost API or the Console ([R133](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)).

**Learn · 105 min**

- [ ] D23: [R106](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/production-engineering-evals-security), first half.

**Reference**

- [ ] D23: Reference: [R51](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) Mitigate jailbreaks.
- [ ] D23: Reference: [R73](https://code.claude.com/docs/en/security) Claude Code security.
- [ ] D23: Reference: [R132](https://platform.claude.com/docs/en/manage-claude/workspaces) Workspaces.
- [ ] D23: Reference: [R133](https://platform.claude.com/docs/en/manage-claude/usage-cost-api) Usage and Cost API.
- [ ] D23: Reference: [R134](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention) API and data retention.
- [ ] D23: Reference: [R135](https://genai.owasp.org/llm-top-10/) OWASP Top 10 for LLM applications.

**Drill**

- [ ] D23: Drill: One question on the most effective injection control.
- [ ] D23: Drill: One on least privilege for tools.
- [ ] D23: Drill: One on where API keys live in development and in production, and how to see who used one.

**Done when**

- [ ] D23: Before-and-after log of the injection test, with the planted instruction blocked.

## Day 24 · Evals and debugging

Friday 6 November · long day, 2 hours · Dev D4 debugging (2.6%), D2 application design (8.6%)

**Goal.** Define "done" as a test, and find whether a failure is mine or the model's.

**Build · 45 min**

- [ ] D24: Turn the Day 13 test set into an eval script with a pass threshold.
- [ ] D24: Run it against two models and two prompt versions.
- [ ] D24: Store prompts in versioned files and pin the model version in config.
- [ ] D24: Then break the integration on purpose (drop a field before it reaches the prompt) and use logs or traces to show the fault is in my code, not the model.

**Learn · 105 min**

- [ ] D24: [R106](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/production-engineering-evals-security), second half.

**Also**

- [ ] D24: [R17](https://anthropic-partners.skilljar.com/claude-with-the-anthropic-api), section Prompt evaluation.

**Reference**

- [ ] D24: Reference: [R80](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) Demystifying evals, the grader types section.
- [ ] D24: Reference: [R49](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) Define success and develop tests.
- [ ] D24: Reference: [R115](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) Model IDs and versioning.
- [ ] D24: Reference: [R136](https://platform.claude.com/docs/en/manage-claude/opentelemetry) OpenTelemetry for the Claude API.

**Drill**

- [ ] D24: Drill: One question on code-graded versus model-graded checks.
- [ ] D24: Drill: One on isolating integration faults from model faults.
- [ ] D24: Drill: One on a regression after a model upgrade.

**Done when**

- [ ] D24: `eval.py` prints a pass rate per model and prompt version, and the traced fault is written up.

## Day 25 · Full timed mock

Saturday 7 November · long day, 2 hours

**Goal.** A full-length rehearsal and an honest gap list.

**Mock · 100 min**

- [ ] D25: 50 questions from my bank and the Drills page, weighted roughly by blueprint: about 16 from D2, 8 from D5, 7 from D1, 6 from D6, 5 from D8, 4 from D7, and 2 each from D3 and D4.
- [ ] D25: Timed.
- [ ] D25: No docs.

**Review · 20 min**

- [ ] D25: Score by domain.
- [ ] D25: List the two weakest domains and the three skill lines behind them.

**Done when**

- [ ] D25: Mock score by domain recorded. Two weakest domains named.

## Day 26 · Rest

Sunday 8 November. Rest is part of the plan.

## Day 27 · Software engineering, platforms and gaps

Monday 9 November · Dev D2 requirements, life cycle, software engineering (13.6% together)

**Goal.** Cover the general engineering lines, then close the gaps from Day 25.

**Build · 60 min**

- [ ] D27: Spend 20 minutes on the weakest domain from Day 25: redo the build step that covers it.
- [ ] D27: Spend 25 minutes on software engineering in a Claude workflow: on a new branch, refactor the Day 15 agent loop into a module with one test, run `/code-review` on the branch ([R137](https://code.claude.com/docs/en/code-review-local)), fix what it finds and commit.
- [ ] D27: Read how Claude reviews pull requests in GitHub Actions ([R138](https://code.claude.com/docs/en/github-actions)).
- [ ] D27: Spend 15 minutes on third-party access: read how Claude is called through a cloud platform ([R41](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)) and write three lines on what changes (authentication, model IDs, feature parity).

**Learn · 120 min**

- [ ] D27: [R18](https://anthropic-partners.skilljar.com/path/claude-developer/claude-code-in-action) Claude Code in Action, 1 hour: verification, permission modes, headless runs, GitHub Actions, code review and plugins.
- [ ] D27: Then [R108](https://academy.claude.com/courses/ai-native-sdlc-playbook) The AI-native SDLC playbook, 1 hour: requirements, life cycle and review in a team that uses Claude.
- [ ] D27: Then skim [R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf) domain 2 skill lines on requirements, life cycle and software engineering.
- [ ] D27: For each, write one sentence on how I already do it at work.
- [ ] D27: These lines test general practice, not Claude features.

**Also**

- [ ] D27: [R107](https://anthropic-partners.skilljar.com/path/claude-certified-developer-foundations/accelerators-ip-contribution), the section on choosing where a workload runs.
- [ ] D27: [R99](https://anthropic-partners.skilljar.com/path/claude-developer/ai-fluency-for-builders) AI Fluency for builders, the lessons on acceptance tests and discernment.
- [ ] D27: Take the rest of [R99](https://anthropic-partners.skilljar.com/path/claude-developer/ai-fluency-for-builders) after the exam.

**Reference**

- [ ] D27: Reference: [R41](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai) Claude on Vertex AI.
- [ ] D27: Reference: [R137](https://code.claude.com/docs/en/code-review-local) Local code review.
- [ ] D27: Reference: [R138](https://code.claude.com/docs/en/github-actions) Claude Code GitHub Actions.

**Done when**

- [ ] D27: Weakest domain redone, and one sentence per general engineering skill line.

## Day 28 · Exam

Tuesday 10 November · **Developer Foundations, CCDV-F**

Light recall only: 20 questions from Drills, no new material. Then follow the exam-day checklist on the [Start](start.html) page.

**Done when**

- [ ] D28: Exam taken. Score and domain report recorded in `CertLab/results.md`.
