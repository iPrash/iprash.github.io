# Frontier Engineer → Principal
## A step-by-step learning path from my own role's Lead and Principal job descriptions

This is my study guide, not a tutorial for anyone else's employer. I built it from my own
company's Lead and Principal Frontier Engineer job descriptions, restructured into skill
areas I can actually learn against. It does not reproduce those job descriptions. It follows
their shape: the same areas of responsibility, in the same order, each broken into what I
need to know, what I need to have built, and where to learn it for free.

I am currently a Lead Frontier Engineer. The target is Principal.

- [ ] Read Part 0 before anything else. It sets the map.
- [ ] Work Parts 1 through 11 roughly in order the first time through. After that, revisit
      whichever part is weakest.
- [ ] Part 12 is the one to keep open permanently. It is the promotion tracker.

Resources for each part live on the [Resources](resources.html) page, numbered to match.

---

# Part 0 — How to use this

## 0.1 The shape of the role

Both Lead and Principal Frontier Engineers sit at the same intersection of engineering,
consulting, and productization. The job is to go into a client environment, work out where
AI can move a real business number, build a working version of that fast, and turn it into
something that survives contact with production. Neither level is a pure research role and
neither is a pure delivery role. The mix is the point.

## 0.2 What actually changes between Lead and Principal

The two role descriptions share almost identical section headings. That is deliberate. A
Principal is not doing different work, they are doing it at a different radius. Reading both
side by side, the delta comes down to five things.

| Dimension | Lead | Principal |
|---|---|---|
| Scope | One client, one engagement, working under a Principal | Multiple clients or industries at once, working directly with CXOs |
| Technical role | Builds and productionizes the solution | Architects the solution and directs the squad building it |
| Strategic role | Feeds insights upward | Sets the AI transformation roadmap and advises leadership on it |
| Reuse | Contributes reusable components | Owns productizing patterns into company-wide platforms and standards |
| External footprint | Internal and client-facing | Publishes, speaks, and builds relationships with vendors and academia |

Principal itself has two sub-levels. L1 operates at portfolio, program, or business-unit
scope. L2 operates at company-wide, multi-business-unit scope, with heavier weight on
external ecosystem influence and on productizing what L1s and Leads build. Part 12 tracks
that L1-to-L2 delta separately, since it is a second, smaller jump after the first one.

## 0.3 A note on "vibing"

My company's job description uses this word for AI-assisted rapid prototyping: building a
working proof of concept by directing an AI coding assistant rather than hand-writing every
line. It is a real, named expectation of the role at Lead level and above, not a shortcut to
apologize for. Part 1 treats it as a skill with its own technique, not just "using Claude
Code."

---

# Part 1 — Foundations

## 1.1 Large language models, without the hand-waving

Before anything else: what a transformer actually does with a prompt, what a context window
is and why it has a cost, what "temperature" and sampling change, and where hallucination
comes from mechanically. It is not a bug being patched. It is the model doing exactly what it
is built to do: predict plausible tokens. This matters because every later part assumes it.
Evaluation, cost control, and prompt design all fall out of this model.

## 1.2 Prompt engineering as an engineering discipline

Treat prompts as versioned, tested artifacts, not one-off text. Few-shot versus zero-shot,
chain-of-thought and when it helps versus when it just burns tokens, structured output
(JSON mode, function calling and tool use), and system-prompt design for a production agent
rather than a chat toy.

## 1.3 Retrieval-augmented generation (RAG)

The default answer to "the model doesn't know my data." Chunking strategy, embeddings and
vector stores, hybrid search combining keyword and vector methods, and the part most
tutorials skip: what breaks in RAG at enterprise scale. Stale indexes, chunk boundaries
cutting a fact in half, and retrieval precision versus recall tradeoffs show up as wrong
answers, not crashes.

## 1.4 AI-assisted rapid prototyping ("vibing")

The skill is not typing a request into an AI coding tool. It is scoping the smallest working
slice before starting, keeping a tight edit-run-check loop, reading every diff before
accepting it, and knowing when to take the wheel back because the assistant is thrashing.
This is the mechanic behind "smallest-viable, end-to-end scope for rapid validation."
Proving something works beats designing the perfect version of it.

## 1.5 What a proof of value actually needs to prove

A working demo is not a proof of value. A proof of value needs a stated business metric, a
baseline, and a measured delta, even a rough one, or it is just a demo. Get in the habit of
writing the success metric down before writing any code.

---

# Part 2 — Discovery and Scoping

## 2.1 Mapping a business process you don't own

Techniques for extracting an accurate process map from people who live inside the process
and can't see it from outside: value stream mapping, swimlane diagrams, and structured
discovery interviews. The failure mode to train against is mapping the process as it's
described in a slide deck instead of the one people actually run.

## 2.2 Turning a business problem into a technical scope

Decomposing an ambiguous ask, such as "make support faster," into acceptance criteria and
guardrails a build can be checked against. The discipline here is closer to product
management than engineering: define what "done" means, numerically, before anyone opens an
editor.

## 2.3 Reading a technology landscape fast

Given a client's actual stack, an ERP like SAP or Oracle, a CRM like Salesforce, a data
platform like Snowflake or Databricks, a cloud AI platform like Vertex AI, Bedrock, or
OpenAI's enterprise offering, know enough about each to scope integration work without
becoming a specialist in all of them. Part 4 goes deeper on the platforms themselves. This
section is about scoping speed, not platform mastery.

## 2.4 The smallest viable end-to-end slice

The core discipline of scoping under time pressure: cut a thin vertical slice through the
whole system (data in, model call, output back to a real user) rather than a thick slice of
one layer. A slice that touches every layer, even badly, teaches you more per hour than a
polished layer that touches nothing else.

---

# Part 3 — Client Co-Creation → Client Transformation Advisory

## 3.1 Facilitating a technical workshop with non-technical stakeholders

Running a joint discovery or design session so both a CXO and a platform engineer leave with
the same understanding. Structure the agenda, translate jargon in both directions live, and
close every session with a written-down decision, not just a good conversation.

## 3.2 Model evaluation as a client-facing deliverable

Part 1's evaluation techniques, reframed as something a business stakeholder needs to trust
before signing off: benchmarks tied to a business KPI, not just an accuracy score, presented
so a non-technical sponsor can see why the number is credible.

## 3.3 Domain fluency without a domain degree

A working, not academic, grasp of finance, healthcare, supply chain, retail, or
manufacturing, enough to spot which of a client's stated problems is actually the expensive
one. This is a Principal-weighted skill (their JD names it explicitly), but Leads who build
it early move faster.

## 3.4 From advisor to trusted advisor

The distinction that actually separates the two role levels here: a Lead validates a
solution against requirements; a Principal is trusted to tell a CXO their requirements are
wrong. That trust is earned through a track record, not claimed. But knowing what the
behavior looks like, naming the uncomfortable tradeoff before being asked, lets you start
practicing it now.

---

# Part 4 — Technical Delivery → Solution Architecture

This part is the technical core of the role and the most resource-heavy. It is split into
five sub-areas.

## 4.1 Agentic AI systems

Single-agent versus multi-agent design, the orchestrator/worker pattern, tool use and
function calling, memory (short-term context versus long-term stores), and, critically,
knowing when a plain deterministic workflow beats an agent. Most production "agentic AI"
failures are agents used where a script would have been faster, cheaper, and more reliable.

## 4.2 Enterprise AI platforms

Working fluency, at the build-and-integrate level rather than the vendor-certification
level, across the three platform families the role names: Google Vertex AI, AWS Bedrock, and
enterprise OpenAI or Azure OpenAI. What matters practically: model access and routing,
fine-tuning and grounding options, cost and quota controls, and each platform's native
evaluation and observability tooling.

## 4.3 Data platforms for AI

Snowflake and Databricks are the two data-platform ecosystems named in the role. Focus on the
AI-relevant surface: feature stores, vector search extensions, governed access to data an LLM
pipeline will read, and how each platform's native AI tooling (Cortex, Mosaic AI) plugs into
a broader agent or RAG system.

## 4.4 Business platform literacy

SAP S/4HANA, Salesforce, and Oracle, not learned as a functional consultant would learn them,
but at the level needed to scope an integration: what data each platform exposes through an
API, what its extension and customization layer looks like, and where an AI feature would
actually sit in it.

## 4.5 Productionizing AI/LLM workloads (LLMOps)

The unglamorous half of the job, and the half that separates a demo from a deployed system:
retrieval pipeline reliability, prompt versioning and regression testing, response caching,
telemetry (what to log, and how to log it without leaking sensitive data), and cost controls
(token budgets, model routing by task complexity, caching hit rate as a cost lever).

## 4.6 CI/CD and infrastructure-as-code for AI systems

Standard software delivery discipline applied to a system with a nondeterministic component.
What's different about testing and rolling out a change to a prompt or a model version versus
a change to plain code, and how IaC (Terraform or equivalent) fits AI infrastructure
specifically: vector databases, GPU-backed endpoints, and model registries.

## 4.7 Full-stack delivery and enterprise integration

Tying the data, API, orchestration, and UI layers together end to end, plus the enterprise
plumbing every real deployment needs regardless of AI content: SSO and identity federation,
ERP/CRM integration patterns, and observability that covers the whole stack, not just the
model call.

---

# Part 5 — Validation and Iteration

## 5.1 Building an evaluation plan before building the system

The habit to instill: write the evaluation plan and acceptance thresholds before the first
line of the pilot, not after it's built and someone asks how you know this works. An
evaluation plan states what's measured, how, against what baseline, and what score counts as
good enough to proceed.

## 5.2 LLM and RAG evaluation in practice

Concrete evaluation techniques: reference-based metrics versus LLM-as-judge, RAG-specific
measures (retrieval precision and recall, faithfulness, answer relevance), and the
open-source tooling that operationalizes these. See Resources; this is one of the most
concretely learnable, hands-on parts of the whole roadmap.

## 5.3 Telemetry that ties technical and business KPIs together

The role's evaluation work isn't just a technical score. It has to connect to a business
number a client cares about. Practice writing telemetry specs that capture both a technical
metric (latency, accuracy) and a linked business metric (tickets deflected, hours saved) from
day one of a pilot.

## 5.4 Running a demo, review, and sign-off

The soft skill wrapped around the hard one: structure a demo so a stakeholder's first
reaction is confidence, not skepticism. Show the metric before the feature, and show a
failure case handled gracefully before someone finds it themselves.

---

# Part 6 — Security, Compliance, and Reliability

## 6.1 Deploying in a regulated enterprise environment

The baseline expectations a client's security and compliance teams will hold any AI system
to: data classification, access controls scoped to least privilege, and audit logging
sufficient to reconstruct what a system did and why.

## 6.2 The regulatory frameworks that actually apply

Working knowledge, not legal expertise, of SOX, HIPAA, and GDPR as they touch an AI system
specifically, plus the EU AI Act, increasingly relevant even for US-based work with European
clients or data. Know which obligations attach to which kind of AI system. A chatbot and a
hiring-decision model are not regulated the same way.

## 6.3 Observability, alerting, and SLOs for AI systems

Extend standard site-reliability practice to a system with a nondeterministic, cost-metered
component: what an SLO means for an LLM-backed service, and what to alert on beyond uptime
(cost spikes, latency percentile drift, evaluation-score regression in production).

## 6.4 Responsible and ethical AI, operationally

Not the philosophy, the checklist: bias testing before deployment, a documented mitigation
plan when bias is found, transparency about AI involvement to end users, and auditability
built in from the start rather than retrofitted after an incident.

---

# Part 7 — Change Management and Enablement

## 7.1 Driving adoption of something you built

The pattern that determines whether a deployed system gets used: identify the people whose
job changes, involve them before launch, and measure adoption explicitly rather than assuming
"it's live" means "it's used."

## 7.2 Knowledge transfer that actually transfers

Structure a handoff to a client's own engineering and operations teams so the system survives
after the engagement ends. Write runbooks for someone who wasn't in the room when the system
was built, not for yourself six months from now.

## 7.3 Building reusable playbooks and templates

The discipline of generalizing a one-off solution into something reusable on the next
engagement, without over-engineering it before there's a second use case to generalize from.

---

# Part 8 — Post-Launch Ownership

## 8.1 Hyper-care and the stabilization window

What the weeks immediately after launch should look like: closer monitoring than steady
state, a fast path for triaging and fixing issues, and a defined point at which hyper-care
ends and the system moves to normal operations.

## 8.2 Tracking adoption and business impact after handoff

Instrument a system so its ongoing value is visible without having to go ask. Build usage
dashboards, and a lightweight, repeatable way to re-measure the original success metric weeks
or months later.

## 8.3 Feeding field learnings back upstream

Turn what broke or surprised you in production into structured feedback that actually reaches
a platform or product team, not just a note in your own files.

---

# Part 9 — Platform Engineering and Productization

## 9.1 From one-off solution to reusable platform component

Recognize the pattern that shows up across engagements and extract it into something with a
stable interface (a library, a scaffold, a template) before building it three separate times
by hand.

## 9.2 Designing for reuse without overbuilding

The tension at the center of platform engineering: a component built for one client is
brittle everywhere else, and a component built for every hypothetical client never ships.
Learn to abstract from two real cases, not zero.

## 9.3 Productization as a Principal-level skill

The step beyond building reusable components: turning a proven pattern into something a
company formally adopts, supports, and scales, a named accelerator or platform capability
with an owner, not just a shared folder of code.

---

# Part 10 — Advanced AI Development → AI Strategy and Visioning

## 10.1 Fine-tuning and model customization

When fine-tuning is the right tool versus prompt engineering or RAG, and the practical
mechanics of it: dataset preparation, parameter-efficient fine-tuning (LoRA and similar), and
evaluating a fine-tuned model against the baseline it's meant to beat.

## 10.2 Multi-modal AI

Working knowledge across text, image, and code generation (the modalities the Lead role
names), extending toward video and 3D generation (which the Principal role adds), enough to
know what's genuinely production-ready today versus still research-grade.

## 10.3 Translating AI strategy into an architecture roadmap

The Principal-level version of scoping is not "what do we build this quarter" but "what
sequence of builds, over 12 to 18 months, gets an enterprise from where it is to where its AI
strategy says it should be." Short, mid, and long-horizon roadmapping is a distinct planning
skill from sprint-level scoping.

---

# Part 11 — Thought Leadership and Ecosystem Collaboration
### Principal-only in the source role, worth starting into as a Lead

## 11.1 Writing and publishing applied AI insight

Turn what you learn on engagements into a publishable point of view: pick a topic narrow
enough to say something real about, and a format (post, whitepaper, talk) that fits the
insight rather than padding it out.

## 11.2 Building relationships with the wider ecosystem

Hyperscalers, platform vendors, and the research and academic side of the field. Practical
entry points at Lead level: contribute to open-source tools you actually use, engage in a
platform vendor's technical community, and follow, not just skim, a small number of research
labs and practitioner voices closely.

---

# Part 12 — The Lead → Principal gap

## 12.1 What "ready for Principal" looks like against the performance measures

Not a technical skill checklist; that's Parts 1 through 11. This is the evidence checklist a
promotion case actually needs, built from the shape of the Principal performance measures:

- [ ] A quantified business outcome I can point to from a real engagement (efficiency,
      cost, accuracy, or a new capability)
- [ ] At least one reusable asset (template, accelerator, framework) I built that someone
      else has adopted
- [ ] A case where I advised a client on strategy or direction, not just delivery
- [ ] A multi-client or multi-domain engagement, or a credible plan for getting one
- [ ] At least one person I've mentored toward field readiness
- [ ] One published or presented piece of thought leadership
- [ ] A relationship with at least one platform vendor or hyperscaler beyond a vendor rep
      contact

## 12.2 The L1 → L2 delta, for later

Once Principal L1 is reached, the next jump is company-wide, multi-business-unit scope
instead of portfolio or program scope, strategic CXO relationships instead of engagement-level
stakeholder management, and measurable contributions to productizing and standardizing
company-wide AI platforms rather than one engagement's accelerators. It's worth knowing the
shape of this now, even years out. It changes what "reusable" should mean in 12.1.
