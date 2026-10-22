# Drills
## My question bank, by exam and domain

The official practice exam was retired ([R11](https://trainingcamp.com/articles/claude-certifications-explained-all-four-anthropic-exams-costs-and-who-can-take-them/)). This page replaces it. Every question here is my own, written from the public blueprint ([R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf)) and my own builds. None comes from a live exam, and none ever will: the non-disclosure agreement covers all exam content ([R1](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542875%2FClaude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf), section 13), and this repo is public.

**How to use it.** Answer before opening the answer. Each day, add the 3 questions I wrote in the Write block, under the right domain. Match the exam style: one realistic situation, four options, one best answer, and a reason why each wrong option is wrong.

**Seed questions.** The first questions in each domain were written on 14 October 2026 to start the bank. Facts were checked against the docs on that date.

---

# Developer Foundations

## D1 · Agents and workflows

**Q1.1** A team needs to process insurance claims through five fixed steps: extract fields, validate, check policy, calculate payout, draft a letter. The steps never change order. Which design fits best?
A. An autonomous agent with all five capabilities as tools, deciding its own order
B. A fixed workflow that calls the model at each step, with code controlling the order
C. A single prompt that does all five steps at once
D. Five agents that negotiate with each other

<details><summary>Answer</summary>B. When the path is known and fixed, a workflow is cheaper, faster and easier to test than an agent. Agents earn their cost when the steps depend on what is found along the way. A gives up control for no gain. C makes failures hard to locate. D adds coordination cost with no benefit.</details>

**Q1.2** An agent must never issue a refund above $500 without approval. Testing shows that a strong instruction in the system prompt is followed about 98% of the time. What should the team do?
A. Make the instruction more emphatic and repeat it at the end of the prompt
B. Switch to a larger model
C. Enforce the limit in code, with a hook or a check before the refund tool runs, and route larger refunds to a human
D. Log every refund so it can be reviewed later

<details><summary>Answer</summary>C. A business rule that must always hold belongs in deterministic code. A prompt raises the rate but cannot guarantee it. A and B are still probabilistic. D detects the problem after the money has moved.</details>

**Q1.3** A coordinator agent delegates a long codebase search to a subagent. What is the main benefit?
A. The subagent shares the coordinator's full context, so nothing is lost
B. The search runs in its own context, and only a summary returns, which keeps the coordinator's context small
C. Subagents always use a cheaper model
D. Subagents cannot make mistakes

<details><summary>Answer</summary>B. Context isolation is the point. The subagent can read many files without filling the coordinator's window. A is the opposite of how isolation works. C is a choice, not a rule. D is false.</details>

## D2 · Applications and integration

**Q2.1** A developer must process 5,000 support transcripts for a weekly report due in two days. Cost matters most. Which approach fits?
A. Send all requests at once through the Messages API with high concurrency
B. Use the Message Batches API and match results by `custom_id`
C. Stream every response to reduce cost
D. Lower `max_tokens` on each realtime request

<details><summary>Answer</summary>B. Batches are built for latency-tolerant volume at a lower price, and results are matched by `custom_id` because order is not guaranteed. A does not lower the per-token price. C changes delivery, not cost. D may truncate answers without solving the batch-versus-realtime question.</details>

**Q2.2** A batch of 200 requests ends. Twelve results show errors. What is the correct next step?
A. Resubmit the whole batch
B. Use each failed result's `custom_id` to find and resubmit only those requests, after fixing the cause
C. Assume the results are in the same order as the inputs and resubmit items 189 to 200
D. Switch the twelve requests to streaming

<details><summary>Answer</summary>B. `custom_id` is the link between request and result. A wastes money on 188 good results. C relies on an ordering that is not guaranteed. D does not address the failure cause.</details>

**Q2.3** A product moves from a pinned model version to a newer one. Several downstream parsers break. Which practice would have caught this before release?
A. Using the model alias that always points to the latest version
B. Running the eval suite against the new version as a gate before switching, with the model version pinned in config
C. Increasing `max_tokens`
D. Removing the system prompt

<details><summary>Answer</summary>B. Pin the version, and treat a model change like any dependency upgrade: test it against acceptance criteria first. A is what caused the surprise. C and D are unrelated to the regression.</details>

## D3 · Claude Code

**Q3.1** A team wants every developer's Claude Code session to follow the same test conventions. Where should the conventions go?
A. Each developer's user-level CLAUDE.md in their home folder
B. The project CLAUDE.md committed to the repository
C. A personal `CLAUDE.local.md`
D. The system prompt of each developer's chat app

<details><summary>Answer</summary>B. The project file is shared through version control, so everyone gets it. A and C are personal and not shared. D is unrelated to Claude Code.</details>

**Q3.2** A CI job must run Claude Code without a person present and pass the result to the next pipeline step. Which feature fits?
A. Interactive mode with plan mode on
B. Headless mode with `-p` and JSON output
C. A custom slash command typed by the release manager
D. A user-scoped MCP server

<details><summary>Answer</summary>B. Headless mode runs non-interactively, and JSON output gives the next step something it can parse. A and C need a person. D adds a capability but does not make the run non-interactive.</details>

**Q3.3** A developer wants personal permission settings that should not affect teammates. Which file should hold them?
A. `.claude/settings.json`
B. `.claude/settings.local.json`
C. The project CLAUDE.md
D. `.mcp.json`

<details><summary>Answer</summary>B. The local settings file is for personal settings and is not meant to be committed. A is the shared team file. C holds instructions, not permission settings. D configures MCP servers.</details>

## D4 · Eval, testing and debugging

**Q4.1** An extraction feature returns empty values for one field. The model's raw response contains the value. Where is the fault most likely?
A. The model is hallucinating
B. The integration layer: the parsing or mapping code that reads the response
C. The context window is too small
D. The temperature is too high

<details><summary>Answer</summary>B. If the raw output is correct and the stored result is wrong, the fault is after the model. Trace analysis means checking each layer's input and output to find where the value is lost. A, C and D blame the model for a value it produced.</details>

**Q4.2** A service receives intermittent overloaded and rate-limit errors from the API. Which recovery strategy fits?
A. Fail the user request immediately on every error
B. Retry with exponential backoff for these error types, and do not retry invalid-request errors
C. Retry every error type forever
D. Switch to a different API key on each failure

<details><summary>Answer</summary>B. Overload and rate-limit errors are transient, so backoff helps. An invalid request will fail the same way every time, so a retry only wastes calls. A is too brittle. C can loop forever. D may breach usage terms and does not fix overload.</details>

**Q4.3** A team grades a summarizer on "is the tone appropriate for a customer". Which grading method fits best for this criterion?
A. An exact string match against a reference summary
B. A model-based grader with a clear rubric, spot-checked against human ratings
C. Counting words
D. No grading, since tone is subjective

<details><summary>Answer</summary>B. Tone is open-ended, so code checks miss it. A rubric-based model grader scales, and human spot checks keep it honest. A and C measure the wrong thing. D leaves the feature untested.</details>

## D5 · Model selection and optimization

**Q5.1** A routing service must classify 2 million short messages a day into 6 categories with low latency. Accuracy on a test set is equal across the Haiku and Sonnet tiers. Which choice fits?
A. Opus, for safety
B. Haiku, since it meets the quality bar at lower cost and latency
C. Sonnet, since it is the default
D. Alternate between models at random

<details><summary>Answer</summary>B. Pick the smallest model that meets the measured quality bar. At this volume, cost and latency dominate. A and C pay for capability the task does not need. D adds variance for no reason.</details>

**Q5.2** Every request in an application starts with the same 10,000-token policy document, followed by a short question. Which change reduces cost most directly?
A. Put the question before the policy document
B. Cache the stable policy prefix with prompt caching
C. Lower the temperature
D. Split the policy into 10 separate requests

<details><summary>Answer</summary>B. A repeated, stable prefix is exactly what caching is for. A breaks caching, because the varying part must come after the stable part. C has no effect on cost. D multiplies requests.</details>

**Q5.3** The same prompt, sent twice, gives two different but valid answers. What explains this?
A. A bug in the SDK
B. Sampling: the model picks each next token from a probability distribution, so outputs can vary
C. The API key changed
D. The context window was exceeded

<details><summary>Answer</summary>B. Generation is non-deterministic by design. Where consistency matters, constrain the output (structure, examples) and test for it. A, C and D do not explain normal variation.</details>

## D6 · Prompt and context engineering

**Q6.1** A classifier often confuses "billing dispute" with "refund request". Which change is most likely to help?
A. Add 2 to 4 examples that sit on the boundary between the two, with the reason for each label
B. Add more examples of easy, obvious cases
C. Raise `max_tokens`
D. Ask the model to be more careful

<details><summary>Answer</summary>A. Examples teach most where the model is uncertain, and the reasoning helps it generalize. B spends tokens where it already succeeds. C is unrelated. D gives no new information.</details>

**Q6.2** An agent runs for 40 turns. Each tool call returns a large JSON payload, and late answers start to ignore early instructions. What is the best first fix?
A. Move to a model with a larger context window and change nothing else
B. Trim tool results to the fields the task needs, and summarize or compact older turns
C. Repeat all instructions in every user message
D. Restart the conversation every 5 turns and lose the history

<details><summary>Answer</summary>B. Context bloat from verbose tool output is the cause. Remove what is not needed and compact the rest. A delays the problem. C adds more bloat. D throws away state the task needs.</details>

**Q6.3** Code needs a JSON object with fixed fields from every response. Instructions alone give occasional malformed output. What is the most reliable fix?
A. Add "respond only in valid JSON" in capital letters
B. Use structured outputs or strict tool use with a JSON schema, then validate in code
C. Parse with a regular expression and guess missing fields
D. Ask for YAML instead

<details><summary>Answer</summary>B. A schema-constrained feature removes syntax failures, and validation in code still catches wrong values. A is still a request, not a guarantee. C hides errors. D moves the problem to another format.</details>

## D7 · Security and safety

**Q7.1** An agent summarizes customer-uploaded documents and can also send emails. One document contains hidden text telling it to email the full customer list to an outside address. Which control matters most?
A. A system-prompt line asking the model to ignore malicious instructions
B. Treat document content as untrusted data, and remove or gate the email tool so injected text cannot trigger it
C. A higher temperature
D. A larger model

<details><summary>Answer</summary>B. Separate untrusted content from instructions, and apply least privilege so the dangerous action is not available, or needs approval. A is not an enforceable control. C is irrelevant. D does not remove the attack path.</details>

**Q7.2** Where should a production service keep its API key?
A. In the system prompt
B. In the repository, in a config file
C. In a secrets manager or environment injected at runtime, with access limited to the service
D. In the frontend code, so the browser can call the API directly

<details><summary>Answer</summary>C. Secrets belong in a managed store with least-privilege access and rotation. A and D expose the key. B leaks it to everyone with repo access and into history.</details>

**Q7.3** A coding agent may run shell commands. The team wants to stop destructive commands, such as deleting directories, before they run. What fits best?
A. A pre-tool-use hook that inspects the command and denies dangerous patterns
B. A note in CLAUDE.md asking the agent not to delete things
C. A post-run report of commands executed
D. Running the agent only at night

<details><summary>Answer</summary>A. A hook runs deterministically before the action and can block it. B is a request the model may not follow. C detects damage after it happens. D changes nothing about the risk.</details>

## D8 · Tools and MCPs

**Q8.1** Three internal apps all need to query the same inventory service through Claude. The capability should be maintained once. Which approach fits?
A. Copy the tool definition and handler into each app
B. Build an MCP server that exposes the inventory operations, and connect each app to it
C. Paste the inventory data into each prompt
D. Write a Skill that contains the inventory database

<details><summary>Answer</summary>B. An MCP server packages the capability once for many clients. A creates three copies to maintain. C gives stale data and wastes context. D is for reusable instructions and procedures, not live system access.</details>

**Q8.2** In MCP, a server exposes a read-only product catalog that the client application loads as context. Which primitive fits the catalog?
A. A tool
B. A resource
C. A prompt
D. A hook

<details><summary>Answer</summary>B. Resources expose content and data. Tools perform actions the model chooses to invoke. Prompts are reusable templates, usually chosen by the user. Hooks are not an MCP primitive.</details>

**Q8.3** A tool call fails because the order ID does not exist. How should the tool report this to the model?
A. Raise an exception and end the agent loop
B. Return a tool result marked as an error, with a clear message the model can act on
C. Return an empty success result
D. Return a made-up order so the conversation continues

<details><summary>Answer</summary>B. An error result lets the model explain the problem or ask for a correct ID. A ends the task for a recoverable error. C hides the failure. D creates false data.</details>
