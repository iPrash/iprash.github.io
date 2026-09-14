# Frontier Engineer: Lead → Principal
## A two-stage learning path, built from my own role's Lead and Principal job descriptions

This is my study guide, not a tutorial for anyone else's employer. I built it from my own
company's Lead and Principal Frontier Engineer job descriptions, restructured into skill areas
I can learn against. It does not reproduce those job descriptions. It follows their shape: the
same areas of responsibility, in the same order, each broken into what I need to know, what I
need to have built, and where to learn it for free.

The path runs in two stages, in order:

| Stage | Parts | Goal |
|---|---|---|
| Stage 1 | Parts 1 to 11 | Everything the Lead Frontier Engineer role requires, ending in a readiness checklist |
| Stage 2 | Parts 12 to 18 | What Principal adds on top, ending in a second readiness checklist |

Stage 2 assumes Stage 1. A Principal is not doing different work from a Lead, they are doing
it at a wider radius, so the Lead material is the foundation rather than a separate track.

- [ ] Read Part 0 before anything else. It sets the map and calibrates where I'm starting.
- [ ] Work Stage 1 in order. Don't skip ahead to Stage 2 material because it sounds more
      senior; the Principal parts assume the Lead ones.
- [ ] Part 11 and Part 18 are the two checklists. Keep them open permanently.

Resources for each part live on the [Resources](resources.html) page, numbered to match.

---

# Part 0 — Orientation

## 0.1 Two roles, one ladder

Both Lead and Principal Frontier Engineers sit at the same intersection of engineering,
consulting, and productization. The job is to embed in a client environment, work out where AI
moves a real business number, build a working version fast, and turn it into something that
survives contact with production. Neither level is a pure research role and neither is a pure
delivery role. The mix is the point.

The two job descriptions share almost identical section headings. That is deliberate, and it
is why this roadmap is one ladder rather than two separate curricula.

## 0.2 What the Lead role demands

Stage 1 covers this. In the JD's own order: discovery and scoping, co-creation with the
client, technical delivery, validation and iteration, security and compliance, change
management, post-launch ownership, platform engineering, and advanced AI development.

The center of gravity is build capability. A Lead is expected to take a vague business problem
and personally produce a working, production-grade AI solution inside someone else's
enterprise, with the evaluation evidence to prove it worked.

## 0.3 What Principal adds on top

Stage 2 covers this. Five things change, and every one of them is a widening rather than a
replacement.

| Dimension | Lead | Principal |
|---|---|---|
| Scope | One client, one engagement, working under a Principal | Multiple clients or industries at once, working directly with CXOs |
| Technical role | Builds and productionizes the solution | Architects the solution and directs the squad building it |
| Advisory role | Validates a solution against stated requirements | Trusted to tell client leadership the requirements are wrong |
| Reuse | Contributes reusable components | Owns productizing patterns into company-wide platforms and standards |
| External footprint | Internal and client-facing | Publishes, speaks, and builds vendor, hyperscaler and academic relationships |

Principal itself has two sub-levels. L1 operates at portfolio, program, or business-unit scope.
L2 operates at company-wide, multi-business-unit scope, weighted toward external ecosystem
influence and toward productizing what L1s and Leads build. Part 18 treats that as a separate,
later jump.

## 0.4 Where I'm starting from

I'm coming into this from enterprise AI and cloud architecture rather than from a pure ML or
pure delivery background. That changes the sequencing: several Stage 1 parts are recasting
work I already do into the language and evidence this role measures, while others are
genuinely new ground.

Before starting, mark each Stage 1 part as covered, partly covered, or new. My opening
hypothesis, to be corrected rather than trusted:

| Part | Opening read |
|---|---|
| 1 Foundations | Partly covered. Architecture-level understanding is there. The hands-on build loop and the mechanics of evaluation are the gap. |
| 2 Discovery and scoping | Largely covered. Recast existing discovery practice into the JD's acceptance-criteria and smallest-slice language. |
| 3 Co-creation with the client | Largely covered. The new part is doing it with AI-specific success metrics attached. |
| 4 Technical delivery | Mixed, and the biggest single block. Platform breadth is likely strong; hands-on LLMOps is where to spend real time. |
| 5 Validation and iteration | New in practice. Knowing evaluation exists is different from having run one. |
| 6 Security, compliance, reliability | Largely covered for enterprise and cloud. The AI-specific overlay is new. |
| 7 Change management and enablement | Largely covered. |
| 8 Post-launch ownership | Largely covered. |
| 9 Platform engineering | Partly covered. |
| 10 Advanced AI development | New. Fine-tuning and inference optimization are hands-on skills, not architecture knowledge. |

If that read is wrong, the checklist in Part 11 is the tiebreaker: it asks what I can show, not
what I know.

## 0.5 Practicing the parts that need the job

Some responsibilities in both JDs cannot be practiced without being in the seat. Nobody gives a
non-Lead a CXO to advise. Where that applies, each part ends with a **practice without the
job** line naming the closest honest proxy: a smaller version of the same thing, or an
artifact that proves the capability.

The rule for proxies: produce something a person who does the real job would recognize. A
one-page directional guidance note written for an invented client is a proxy. Reading about
writing one is not.

## 0.6 A note on "vibing"

My company's JD uses this word for AI-assisted rapid prototyping: building a working proof of
concept by directing an AI coding assistant rather than hand-writing every line. It is a named
expectation of the Lead role, not a shortcut to apologize for. Part 1 treats it as a skill with
its own technique.

---

# Lead · Part 1 — Foundations

## 1.1 Large language models, without the hand-waving

What a transformer actually does with a prompt, what a context window is and why it has a
cost, what temperature and sampling change, and where hallucination comes from mechanically.
It is not a bug being patched. It is the model doing exactly what it is built to do: predict
plausible tokens. Every later part assumes this. Evaluation, cost control, and prompt design
all fall out of it.

## 1.2 Prompt engineering as an engineering discipline

Treat prompts as versioned, tested artifacts, not one-off text. Few-shot versus zero-shot,
chain-of-thought and when it helps versus when it just burns tokens, structured output
(JSON mode, function calling and tool use), and system-prompt design for a production agent
rather than a chat toy.

## 1.3 Retrieval-augmented generation

The default answer to "the model doesn't know my data." Chunking strategy, embeddings and
vector stores, hybrid search combining keyword and vector methods, and the part most tutorials
skip: what breaks in RAG at enterprise scale. Stale indexes, chunk boundaries cutting a fact in
half, and retrieval precision versus recall tradeoffs show up as wrong answers, not crashes.

## 1.4 AI-assisted rapid prototyping ("vibing")

The skill is not typing a request into an AI coding tool. It is scoping the smallest working
slice before starting, keeping a tight edit-run-check loop, reading every diff before accepting
it, and knowing when to take the wheel back because the assistant is thrashing. This is the
mechanic behind the JD's "smallest-viable, end-to-end scope for rapid validation." Proving
something works beats designing the perfect version of it.

**Practice without the job:** build one working prototype a week for a month, each in a
different domain, each scoped to finish in a day.

## 1.5 What a proof of value has to prove

A working demo is not a proof of value. A proof of value needs a stated business metric, a
baseline, and a measured delta, even a rough one. Write the success metric down before writing
any code. This single habit separates a Lead's pilot from a hobby project.

---

# Lead · Part 2 — Discovery and scoping

## 2.1 Mapping a business process I don't own

Extracting an accurate process map from people who live inside a process and can't see it from
outside: value stream mapping, swimlane diagrams, and structured discovery interviews. The
failure mode to train against is mapping the process as described in a slide deck instead of
the one people actually run.

## 2.2 Turning a business problem into a technical scope

Decomposing an ambiguous ask such as "make support faster" into acceptance criteria and
guardrails a build can be checked against. The discipline is closer to product management than
engineering: define what done means, numerically, before anyone opens an editor.

## 2.3 Reading a client's technology landscape fast

Given a client's actual stack, an ERP like SAP or Oracle, a CRM like Salesforce, a data
platform like Snowflake or Databricks, a cloud AI platform like Vertex AI, Bedrock, or an
enterprise OpenAI deployment, know enough about each to scope integration work without becoming
a specialist in all of them. Part 4 goes deeper. This section is about scoping speed.

## 2.4 The smallest viable end-to-end slice

Cut a thin vertical slice through the whole system (data in, model call, output back to a real
user) rather than a thick slice of one layer. A slice that touches every layer, even badly,
teaches more per hour than a polished layer that touches nothing else.

**Practice without the job:** take a public process description from any industry, write the
one-page scope with acceptance criteria, and have someone in that industry tell me what I got
wrong.

---

# Lead · Part 3 — Co-creation with the client

## 3.1 Facilitating a working session with a mixed audience

Running a joint discovery or design session so a CXO and a platform engineer leave with the
same understanding. Structure the agenda, translate jargon in both directions live, and close
every session with a written decision rather than a good conversation.

## 3.2 Model evaluation as a client-facing deliverable

Part 5's evaluation work, reframed as something a business stakeholder has to trust before
signing off. Benchmarks tied to a business KPI rather than an accuracy score, presented so a
non-technical sponsor can see why the number is credible.

## 3.3 Domain fluency without a domain degree

A working, not academic, grasp of finance, healthcare, supply chain, retail, or manufacturing,
enough to spot which of a client's stated problems is the expensive one. Both role levels name
this. Principal weights it more heavily (Part 12), but a Lead who builds it early moves faster.

## 3.4 Embedding practices that outlast the engagement

The JD calls this shared ownership: putting engineering practices, tools, and reusable
components into the client's own environment so capability stays after the team leaves. The
test is whether the client can run the thing without calling me.

**Practice without the job:** run a design session for any group making a technical decision,
and produce the written decision record afterward.

---

# Lead · Part 4 — Technical delivery

The technical core of the Lead role, and the largest block of work in Stage 1. Seven sub-areas.

## 4.1 Agentic AI systems

Single-agent versus multi-agent design, the orchestrator/worker pattern, tool use and function
calling, memory (short-term context versus long-term stores), and, critically, knowing when a
plain deterministic workflow beats an agent. Most production agentic AI failures are agents used
where a script would have been faster, cheaper, and more reliable.

## 4.2 Enterprise AI platforms

Working fluency at the build-and-integrate level rather than the vendor-certification level,
across the three platform families the JD names: Google Vertex AI, AWS Bedrock, and enterprise
OpenAI or Azure OpenAI. What matters practically: model access and routing, fine-tuning and
grounding options, cost and quota controls, and each platform's native evaluation and
observability tooling.

## 4.3 Data platforms for AI

Snowflake and Databricks are the two ecosystems the JD names. Focus on the AI-relevant surface:
feature stores, vector search extensions, governed access to data an LLM pipeline will read, and
how each platform's native AI tooling (Cortex, Mosaic AI) plugs into a broader agent or RAG
system.

## 4.4 Business platform literacy

SAP S/4HANA, Salesforce, and Oracle, not learned as a functional consultant would learn them,
but at the level needed to scope and build an integration: what data each exposes through an
API, what its extension layer looks like, and where an AI feature would actually sit in it.

## 4.5 Productionizing AI/LLM workloads (LLMOps)

The unglamorous half of the job, and the half that separates a demo from a deployed system:
retrieval pipeline reliability, prompt versioning and regression testing, response caching,
telemetry (what to log, and how without leaking sensitive data), and cost controls (token
budgets, model routing by task complexity, cache hit rate as a cost lever).

This is where to spend the most hands-on time in Stage 1. It is the clearest dividing line
between someone who architects AI systems and someone who ships them.

## 4.6 CI/CD and infrastructure-as-code for AI systems

Standard delivery discipline applied to a system with a nondeterministic component. What's
different about testing and rolling out a change to a prompt or a model version versus a change
to plain code, and how IaC fits AI infrastructure specifically: vector databases, GPU-backed
endpoints, model registries.

## 4.7 Full-stack delivery and enterprise integration

Tying data, API, orchestration, and UI layers together end to end, plus the enterprise plumbing
every real deployment needs regardless of AI content: SSO and identity federation, ERP/CRM
integration patterns, and observability covering the whole stack rather than just the model
call.

**Practice without the job:** one end-to-end build that touches all seven sub-areas at small
scale. A single agentic application, on one enterprise AI platform, reading governed data,
evaluated, deployed by pipeline, with SSO in front of it.

---

# Lead · Part 5 — Validation and iteration

## 5.1 Writing the evaluation plan before the system

Write the evaluation plan and acceptance thresholds before the first line of the pilot, not
after it's built and someone asks how we know it works. An evaluation plan states what's
measured, how, against what baseline, and what score is good enough to proceed.

## 5.2 LLM and RAG evaluation in practice

Reference-based metrics versus LLM-as-judge, RAG-specific measures (retrieval precision and
recall, faithfulness, answer relevance), and the open-source tooling that operationalizes them.
This is the most concretely learnable part of Stage 1 and one of the fastest ways to look like
someone who has done this before.

## 5.3 Telemetry that ties technical and business KPIs together

Evaluation work has to connect to a number the client cares about. Practice writing telemetry
specs that capture both a technical metric (latency, accuracy) and a linked business metric
(tickets deflected, hours saved) from day one of a pilot.

## 5.4 Running a demo, review and sign-off

Structure a demo so a stakeholder's first reaction is confidence rather than skepticism. Show
the metric before the feature, and show a failure case handled gracefully before someone finds
it themselves.

**Practice without the job:** build a 30-example evaluation set for something I've already
prototyped, run it across two models, and write up the result as if presenting it for sign-off.

---

# Lead · Part 6 — Security, compliance and reliability

## 6.1 Deploying in a regulated enterprise environment

The baseline any client's security and compliance team will hold an AI system to: data
classification, access controls scoped to least privilege, and audit logging sufficient to
reconstruct what the system did and why.

## 6.2 The regulatory frameworks that actually apply

Working knowledge, not legal expertise, of SOX, HIPAA, and GDPR as they touch an AI system,
plus the EU AI Act. Know which obligations attach to which kind of system. A chatbot and a
hiring-decision model are not regulated the same way.

## 6.3 Observability, alerting and SLOs for AI systems

Standard site-reliability practice extended to a nondeterministic, cost-metered component: what
an SLO means for an LLM-backed service, and what to alert on beyond uptime (cost spikes, latency
percentile drift, evaluation-score regression in production).

## 6.4 Responsible AI, operationally

Not the philosophy, the checklist: bias testing before deployment, a documented mitigation plan
when bias is found, transparency to end users about AI involvement, and auditability built in
from the start rather than retrofitted after an incident.

---

# Lead · Part 7 — Change management and enablement

## 7.1 Driving adoption of something I built

What determines whether a deployed system gets used: identify the people whose job changes,
involve them before launch, and measure adoption explicitly rather than assuming live means
used.

## 7.2 Knowledge transfer that actually transfers

Structure a handoff to the client's own engineering and operations teams so the system survives
after the engagement ends. Write runbooks for someone who wasn't in the room when it was built,
not for myself six months from now.

## 7.3 Playbooks and templates as a deliverable

Generalizing a one-off solution into something reusable on the next engagement, without
over-engineering it before there's a second use case to generalize from.

---

# Lead · Part 8 — Post-launch ownership

## 8.1 Hyper-care and the stabilization window

What the weeks immediately after launch should look like: closer monitoring than steady state,
a fast path for triaging issues, and a defined point at which hyper-care ends and the system
moves to normal operations.

## 8.2 Tracking adoption and impact after handoff

Instrument a system so its ongoing value is visible without having to go ask. Usage dashboards,
and a lightweight repeatable way to re-measure the original success metric months later.

## 8.3 Feeding field learnings back upstream

Turn what broke or surprised me in production into structured feedback that reaches a platform
or product team rather than a note in my own files. The JD measures this directly at both
levels.

---

# Lead · Part 9 — Platform engineering

## 9.1 From one-off solution to reusable component

Recognize the pattern that shows up across engagements and extract it into something with a
stable interface, a library, a scaffold, a template, before building it three separate times by
hand.

## 9.2 Designing for reuse without overbuilding

The tension at the center of platform engineering: a component built for one client is brittle
everywhere else, and a component built for every hypothetical client never ships. Abstract from
two real cases, not zero.

## 9.3 Internal tooling other engineers actually adopt

Usability, maintainability, and automation as first-order concerns rather than afterthoughts.
An internal framework nobody adopts is a cost, not an asset, and adoption is the measure the JD
names.

**Practice without the job:** take two things I've built and extract the shared part into a
scaffold someone else could use without me explaining it.

---

# Lead · Part 10 — Advanced AI development

## 10.1 Fine-tuning and model customization

When fine-tuning is the right tool versus prompt engineering or RAG, and the mechanics: dataset
preparation, parameter-efficient fine-tuning (LoRA and similar), and evaluating a fine-tuned
model against the baseline it's meant to beat.

## 10.2 Multi-modal AI

Working knowledge across text, image, and code generation, the modalities the Lead JD names.
Enough to know what is production-ready today versus still research-grade.

## 10.3 Inference optimization and cost control

Model-level levers rather than pipeline-level ones: quantization, batching, routing by task
complexity, and knowing which of these actually moves the bill for a given workload.

---

# Lead · Part 11 — Lead readiness

## 11.1 The evidence a Lead role actually requires

Not a knowledge checklist. Parts 1 to 10 cover knowledge. This is what I should be able to point
at, built from the shape of the Lead performance measures:

- [ ] One end-to-end AI solution I built and put in front of real users, not a notebook demo
- [ ] A stated business metric, a baseline, and a measured delta for that solution
- [ ] An evaluation suite I wrote, with results I can explain to a non-technical sponsor
- [ ] Evidence that solution ran securely in a regulated or governed environment
- [ ] One reusable component, template, or scaffold extracted from real work
- [ ] A runbook or handoff artifact someone else has successfully used
- [ ] A documented case of field feedback I passed to a product or platform team
- [ ] A working process map and scope document produced from a real discovery conversation

## 11.2 Turning the gaps into builds

For each unchecked box, name the smallest artifact that would check it, and put a date on it.
The checklist is worth more as a build queue than as a self-assessment.

---

# Principal · Part 12 — Client transformation advisory

Stage 2 starts here. Everything below assumes Stage 1.

## 12.1 From validating requirements to challenging them

The distinction that separates the levels: a Lead validates a solution against stated
requirements; a Principal is trusted to tell client leadership their requirements are wrong.
That trust is earned through a track record rather than claimed, but the behavior is learnable:
name the uncomfortable tradeoff before being asked, and bring an option with it.

## 12.2 Domain expertise at advisory depth

Part 3.3 at a different level. A Lead needs enough domain fluency to build the right thing. A
Principal needs enough to reshape a client's process and defend the reshaping to the people who
own it.

## 12.3 AI adoption roadmaps and organizational readiness

Advising on sequencing, organizational readiness, and change capacity rather than on technology
alone. The common failure this guards against is a technically correct roadmap the organization
has no capacity to absorb.

**Practice without the job:** write the four-page directional guidance note for a real or
invented organization, covering where AI should and should not be applied, in what order, and
what has to be true first.

---

# Principal · Part 13 — Solution architecture and leading a squad

## 13.1 Architecting what others will build

Designing systems I will not personally implement, which changes what the design has to
contain: explicit interfaces, stated constraints, and the reasoning behind choices, so a squad
can build without guessing what I meant.

## 13.2 Documenting decisions so they survive me

Architecture decision records as a practice. Each captures one decision, its context, the
options, and the consequence. This is what makes a Principal's architecture auditable and
teachable rather than folklore.

## 13.3 Directing a cross-functional squad without managing it

The Principal role directs squads, including Frontier Engineers and partner teams, without
being their manager. Influence, technical credibility, and clear written direction do the work
that authority would otherwise do. This is a well-documented skill in the staff-plus
engineering literature and worth studying directly rather than learning by accident.

---

# Principal · Part 14 — AI strategy and visioning

## 14.1 Short, mid and long-horizon roadmapping

Not "what do we build this quarter" but "what sequence of builds, over 12 to 18 months, moves
an enterprise from where it is to where its AI strategy says it should be." Distinct from
sprint-level scoping, and a genuinely different planning skill.

## 14.2 Piloting genuinely novel solutions

The Principal JD extends the modality list to video and 3D and asks for conceptualization of
novel AI-powered experiences. The skill is judging which emerging capability is ready to build
a client commitment on, and which is a demo that will embarrass everyone in six months.

## 14.3 Domain-aware AI architecture

Combining AI capability mapping with functional process redesign, so the architecture reflects
how the business actually works rather than a generic reference diagram with the client's logo
on it.

---

# Principal · Part 15 — Productization

## 15.1 From reusable asset to supported offering

The step beyond Part 9. A reusable component is code someone else can use. An offering is
something the company formally adopts, supports, versions, and sells, with an owner. Knowing
what that transition requires is a Principal-level skill the JD measures directly.

## 15.2 Reference architectures and blueprints

Codifying a pattern so it can be applied across clients, geographies, or sectors without being
rebuilt each time. This is the L2 weighting in particular, and worth understanding early.

## 15.3 Influencing a platform roadmap from the field

Turning deployment experience into product direction that a platform team acts on. The
mechanics matter: a structured, evidenced case lands, an anecdote does not.

---

# Principal · Part 16 — Thought leadership and ecosystem

## 16.1 Writing and publishing applied AI insight

Turn engagement learning into a publishable point of view. Pick a topic narrow enough to say
something real about, and a format that fits the insight rather than padding it out.

## 16.2 Speaking and industry forums

Representing the firm in panels and forums. Start smaller than a conference keynote: internal
sessions, user groups, and meetups build the same muscle with a lower cost of failure.

## 16.3 Vendor, hyperscaler and academic relationships

Practical entry points that don't require a title: contribute to open-source tools I actually
use, engage in a platform vendor's technical community, and follow a small number of research
labs closely rather than skimming many.

**Practice without the job:** publish one written piece per quarter. The Lead-stage builds from
Parts 4, 5 and 9 are the raw material.

---

# Principal · Part 17 — Mentoring and capability building

## 17.1 Mentoring Frontier Engineers toward field readiness

The Principal performance measures count people developed. Mentoring is a skill with its own
technique: coaching questions rather than answers, and calibrating against the readiness bar
rather than against my own preferences.

## 17.2 Enablement at team and organization scale

Moving from mentoring individuals to building capability across client and internal engineering
teams. Playbooks from Part 7 are the artifact; the new skill is designing the enablement itself.

---

# Principal · Part 18 — Principal readiness

## 18.1 The evidence checklist

Built from the shape of the Principal performance measures. Stage 1's checklist asks what I've
built. This one asks what I've influenced.

- [ ] A quantified business outcome from a real engagement, at a scale leadership cares about
- [ ] A reusable asset I built that another team or engagement has adopted
- [ ] A case where I advised a client on direction or strategy, not just delivery
- [ ] A multi-client or multi-domain engagement, or a credible plan to get one
- [ ] At least one person I've mentored toward field readiness
- [ ] One published or presented piece of thought leadership
- [ ] A working relationship with a platform vendor or hyperscaler beyond a sales contact
- [ ] Evidence I've influenced a product or platform roadmap with field insight

## 18.2 The L1 → L2 delta, for later

Once Principal L1 is reached, the next jump is company-wide, multi-business-unit scope instead
of portfolio or program scope, strategic CXO relationships instead of engagement-level
stakeholder management, reusable frameworks adopted across geographies or sectors, and
industry-level influence rather than firm-level. Worth knowing the shape now, years out,
because it changes what reusable should mean in 18.1.
