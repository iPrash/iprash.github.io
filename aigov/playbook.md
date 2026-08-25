# XYZ Corp — Enterprise AI Program
## Analysis, Strategy, Design and Execution Playbook

**Prepared for:** the lead Enterprise Architect  
**Scope:** AI Consumption & Governance · Multi-Model Access Strategy · GenAI Landscape Review  
**Date of market evidence:** 17 August 2026  
**Status:** working playbook — not a client deliverable in this form

> **Currency warning.** Every price, SKU, date and product fact in this playbook was checked in August 2026. This market changes monthly. Re-verify each figure against the primary source before you put it in front of the client. Part 11 lists the primary sources.

---

# Part 0 — How to use this document

This playbook has three uses.

| If you are | Read | Purpose |
|---|---|---|
| Mobilising the engagement | Parts 1, 2, 10 | Framing, plan, cadence |
| Running a workstream | Parts 3, 4 or 5 | Method, data, analysis, deliverable spec |
| Building the durable capability | Parts 6, 7, 8 | Operating model, controls, templates |

Do not send this document to the client. It contains the reasoning behind the engagement design, including the parts of the brief that are wrong. Client-facing artefacts are specified separately in each workstream.

**Language convention.** Deliverables use short sentences, active voice, and one idea per sentence. Define each term once and use it consistently. A tired executive at 22:00 must be able to read the recommendation and act on it.

---

# Part 1 — Read of the brief

## 1.1 What the client asked for

Three workstreams, eleven deliverables. Stated as an analysis exercise.

## 1.2 What the client is actually buying

Read the brief again and note four signals.

1. "Convert that visibility into commercial leverage." The consumption baseline is not a reporting exercise. It is ammunition for a negotiation with a fixed date.
2. "Business impact and stakeholder sentiment created by Copilot's withdrawal — several teams have raised this directly." A decision was taken, it damaged trust, and someone senior now needs cover to revisit it or to defend it.
3. "Initial signal suggests roughly 20–30% ... to be validated against actual usage data rather than assumption." Somebody has already produced a number without evidence. The client knows it and does not trust it.
4. "XYZ is already collating this data." The internal estate data does not exist yet in usable form. Assume it arrives late and dirty.

So the real purchase is: **a defensible evidence base, delivered before the renewal clock runs out, that lets IT leadership make three decisions in public and survive the challenge.**

The three decisions are:

- **D1 — What do we sign at renewal, and on what structure?**
- **D2 — Do we run one model platform or several, and who gets which?**
- **D3 — Where do we build, buy or partner across the GenAI market?**

Everything else is supporting work. Write every deliverable so it visibly serves D1, D2 or D3.

## 1.3 The five traps in this brief

| # | Trap | Why it kills the engagement | Counter-move |
|---|---|---|---|
| T1 | Renewal date not stated | The whole of Workstream 1 is worthless if it lands after the signature | Fix the renewal date in the first 48 hours. Work the plan backwards from it. See 2.3. |
| T2 | Copilot is a political question dressed as a technical one | A clean technical answer that ignores the politics gets rejected | Run a structured sentiment round. Publish what you heard. Then answer with data. See 4.1. |
| T3 | The 20–30% split may be someone's stated position | Validating it looks like auditing a colleague | Frame it as a hypothesis you were asked to test. Test it in public. Report the number the data gives, high or low. |
| T4 | "Landscape review" invites an unbounded market scan | You will spend six weeks producing a poster | Cap the taxonomy at the categories that map to XYZ's value chain. Force category confirmation in scoping. See 5.1. |
| T5 | Consumption data is assumed to be available | Admin API access, identity joins and historic exports each take days of approvals | Raise the data request on day 1, not week 2. See 3.1. |

## 1.4 Operating principles

Adopt these and state them at kickoff. They are also how the firm proves it is a reliable AI partner.

1. **Evidence over assertion.** Every number in every deliverable carries a source, a date and a confidence grade.
2. **Decisions, not documents.** Each deliverable ends with a recommended decision, an owner and a date.
3. **Show the working.** Publish the model, the assumptions and the sensitivity. Let the client change an assumption and see the answer move.
4. **No surprises upward.** Bad news travels immediately, with an option attached.
5. **Leave the capability behind.** Every model, dashboard and register is handed over with a run-book. The client can run the next cycle without you.
6. **Separate the reversible from the irreversible.** Move fast on reversible choices. Slow down only for contract terms, data flows and anything with an exit cost.

## 1.5 Success criteria — agree these at kickoff

| Criterion | Measure | Target |
|---|---|---|
| Renewal readiness | Negotiation brief accepted by procurement and CIO before negotiation opens | ≥ 14 days before first negotiation session |
| Evidence quality | Share of baseline reconciled to invoice | ≥ 98% of spend |
| Decision throughput | Steering decisions taken vs tabled | ≥ 90% closed at first tabling |
| Trust recovery | Developer sentiment score on "I understand why tooling decisions are made" | Improvement vs baseline round |
| Durability | Governance framework operating without the engagement team | 30 days of clean operation before exit |
| Quantified position | Identified addressable saving and identified underused entitlement | Stated with a confidence range, not a point estimate |

---

# Part 2 — Engagement design

## 2.1 The spine

The three workstreams share one data and decision spine. Design them as one program, not three reports.

```
                     ┌──────────────────────────────────────────┐
                     │  CONSUMPTION TRUTH LAYER                 │
                     │  usage · cost · identity · entitlement   │
                     └───────────────┬──────────────────────────┘
                                     │
        ┌────────────────────────────┼────────────────────────────┐
        │                            │                            │
   WS1 Consumption            WS2 Multi-model              WS3 Landscape
   & Governance               access                       review
        │                            │                            │
   segmentation               workload taxonomy            capability taxonomy
   decision matrix            platform evaluation          vendor scorecard
   guardrails                 cost model                   estate cross-check
        │                            │                            │
        └────────────────────────────┼────────────────────────────┘
                                     │
                     ┌───────────────▼──────────────────────────┐
                     │  DECISIONS  D1 renewal · D2 platform     │
                     │             D3 build/buy/partner         │
                     └───────────────┬──────────────────────────┘
                                     │
                     ┌───────────────▼──────────────────────────┐
                     │  OPERATING MODEL — the AI CoE            │
                     │  the thing that runs after you leave     │
                     └──────────────────────────────────────────┘
```

Two shared assets carry across all three workstreams. Build them once.

- **The Workload Taxonomy.** One controlled vocabulary of work classes. WS1 costs them. WS2 maps them to models. WS3 maps them to vendors. If each workstream invents its own list, the deliverables will not reconcile and the client will notice.
- **The Consumption Truth Layer.** One reconciled dataset. Every chart in every deliverable draws from it.

## 2.2 Phases

| Phase | Weeks | Purpose | Exit test |
|---|---|---|---|
| P0 Mobilise | 0–1 | Access, scope, stakeholders, renewal date | Data access granted; taxonomy v0.1 agreed; renewal date fixed |
| P1 Baseline | 1–4 | Consumption truth layer; estate register; sentiment round | Baseline reconciles to invoice within 2%; register covers ≥ 90% of known AI spend |
| P2 Analyse | 4–7 | Segmentation, workload mapping, platform evaluation, market map | Findings pack survives a hostile review by the engineering lead |
| P3 Recommend | 7–10 | Decision matrix, cost model, negotiation brief, blueprint | Steering takes D1, D2, D3 |
| P4 Operationalise | 10–12 | Guardrails live, CoE charter, handover | Governance runs one full monthly cycle without the engagement team |

Twelve weeks is the default. Compress P2 and P3 if the renewal date demands it. Never compress P0 — late data access is the single most common cause of overrun.

## 2.3 The renewal-driven schedule

Fix this in week 0. Work backwards from the renewal date, **R**.

| Milestone | Timing |
|---|---|
| First negotiation session | R − 90 days (target) |
| Negotiation brief approved by CIO and procurement | R − 105 days |
| Draft brief and BATNA costed | R − 120 days |
| Consumption baseline locked | R − 135 days |
| Data access granted | R − 150 days |

If R is closer than 150 days, you are already late. Say so in writing on day 1 and switch to the compressed plan: a two-week baseline on invoice and admin-console data only, deferring identity joins and use-case attribution to a second pass.

## 2.4 Governance and cadence

| Forum | Frequency | Attendees | Decides |
|---|---|---|---|
| Daily stand-up (engagement team) | Daily, 15 min | Team | Blockers |
| Data clinic | 2× weekly, 45 min | EA, data analyst, client platform admin | Data quality, joins, exceptions |
| Workstream review | Weekly, 60 min | EA, workstream leads, client counterparts | Findings, direction |
| Steering | Fortnightly, 60 min | CIO or sponsor, Head of Engineering, Procurement, Security, Data Protection, Finance | D1/D2/D3 and escalations |
| Developer forum | Weeks 2, 6, 10 | Engineering community | Sentiment, validation, adoption |

Two rules. Every steering paper is circulated 48 hours ahead. Every steering meeting ends with the decision log read back aloud.

## 2.5 Stakeholder map and RACI

| Stakeholder | Interest | Risk to you | Handling |
|---|---|---|---|
| CIO / sponsor | Defensible decisions, budget control | Wants a number too early | Give a range with confidence, refuse a point estimate until P2 exit |
| Head of Engineering | Developer productivity, team morale | Owns the Copilot withdrawal decision | Co-author the trial post-mortem. Do not surprise them. |
| Procurement / vendor management | Renewal outcome | May already have a position | Bring them into WS1 from week 1. They own the negotiation, you own the evidence. |
| Finance / FinOps | Forecast accuracy, chargeback | Wants full chargeback immediately | Sell the showback-first ladder (3.6) |
| Security and Data Protection | Data flows, residency, AI Act | Can veto late | Give them the model-access architecture in P2, not P3 |
| Marketing / Digital / Creative | Owns most GenAI spend in a fashion brand | Often outside IT's view | Treat as a first-class stakeholder in WS3. Much of the shadow estate sits here. |
| Developer community | Tooling they actually use | Feels decisions happen to them | Developer forum; publish verbatim feedback |
| OpenAI account team | Renewal value | Will seek to shape your baseline | Do not share the baseline before the brief is approved |

**RACI extract (full grid in Part 8, T1).**

| Activity | EA | WS lead | Client platform admin | Procurement | Security |
|---|---|---|---|---|---|
| Consumption baseline | A | R | C | I | I |
| Decision matrix | A | R | C | I | C |
| Token governance framework | A | R | R | I | C |
| Negotiation brief | R | C | I | A | C |
| Platform evaluation | A | R | C | C | C |
| Landscape and blueprint | A | R | I | C | C |
| CoE charter | R | C | C | C | C |

## 2.6 Team shape

Minimum viable team for a twelve-week run.

| Role | FTE | Why |
|---|---|---|
| Lead EA (you) | 1.0 | Architecture, decisions, client relationship |
| Data analyst / engineer | 1.0 | Truth layer, segmentation, cost model. Non-negotiable. |
| Platform engineer | 0.5 | Gateway, admin APIs, guardrail implementation |
| Commercial / sourcing analyst | 0.5 | Rate cards, BATNA, negotiation brief |
| Market researcher | 0.5 (WS3 heavy in P2) | Vendor scorecards, reference calls |
| Risk and compliance advisor | 0.2 | AI Act, DPIA, security posture |

If you can fund only one addition to yourself, fund the data analyst. The credibility of all three workstreams rests on the truth layer.

## 2.7 Deliverable specifications and acceptance criteria

| # | Deliverable | WS | Format | Accepted when |
|---|---|---|---|---|
| D1.1 | Consumption baseline and segmentation report | 1 | Deck (20pp) + live dashboard + data dictionary | Reconciles to invoice ≤ 2% variance; every cohort has a named owner |
| D1.2 | Model / tool usage matrix | 1 | One-page matrix + reference guide + machine-readable routing table | Engineering lead and Security both sign; cost per task class stated |
| D1.3 | Token governance framework | 1 | Policy pack + control catalogue + implemented gateway config | One full monthly cycle run by client staff |
| D1.4 | Renewal negotiation brief | 1 | Confidential brief (12pp) + costed BATNA + ask/concede ladder | Procurement confirms it is usable at the table without rework |
| D2.1 | Multi-model comparison and cost model | 2 | Workbook with sensitivity + written method note | A third party can reproduce the numbers from the method note |
| D2.2 | Workload-to-model recommendation | 2 | Deck + routing table | Validated against ≥ 8 weeks of real telemetry, not assumption |
| D2.3 | Directional guidance note | 2 | 4-page note for IT leadership | Contains explicit revisit triggers with thresholds |
| D3.1 | GenAI landscape map | 3 | Category map + vendor scorecards | Categories confirmed in scoping; every score has evidence grade |
| D3.2 | Gap analysis against current estate | 3 | Heat map + register | ≥ 90% of AI spend located and classified |
| D3.3 | Target-state blueprint | 3 | Architecture + build/buy/partner calls + roadmap | Each call has a rule, a cost and a trigger |
| X.1 | AI CoE charter and run-book | Cross | Charter + run-book + metrics pack | Sponsor signs; first intake processed by client staff |

## 2.8 First five days — do these immediately

These are time-critical. Two of them expire.

1. **Fix the renewal date and contract vehicle.** Ask for the order form and the master agreement. Note whether ChatGPT Enterprise and API platform sit on one paper or two.
2. **Request OpenAI admin access** — an Admin API key, plus reader access to the Global Admin Console analytics and the billing invoices. Approvals take days.
3. **Export the Copilot trial data before it is unreachable.** Billing usage reports and metrics history for a cancelled subscription do not stay available indefinitely. If any Copilot entitlement remains, export everything today. If it has lapsed, ask GitHub for a historical export in writing this week. Missing trial data is the single most likely cause of a weak WS2.
4. **Check the model retirement calendar.** OpenAI has scheduled the retirement of GPT-5.4 and GPT-5.4 mini in Codex for ChatGPT-signed-in users on 31 August 2026, with GPT-5.6 Terra and GPT-5.6 Luna as the stated replacements. If XYZ has workspace defaults, saved model settings, managed configs or automations pinned to the retiring models, they break. Raise it in week 1. It is also your first proof of usefulness, and it earns you a contract ask (deprecation notice periods — see 3.7).
5. **Ask whether any ChatGPT Enterprise workspace still uses weekly role-based limits.** OpenAI has been migrating remaining workspaces to monthly usage-limit structures during August 2026. A migration mid-baseline distorts your period comparisons. Record the date it happens.

---

# Part 3 — Workstream 1: AI Consumption & Governance

**Objective restated as a decision:** produce the evidence that lets XYZ decide what to sign, and the controls that make the signature hold.

## 3.1 Data acquisition plan

Raise all of this on day 1 as a single, numbered data request. Track it as a register with an owner and a due date per line.

| # | Source | What it gives you | How to get it | Watch-out |
|---|---|---|---|---|
| 1 | OpenAI **Cost API** (`/v1/organization/costs`) | Daily spend, groupable by project and by invoice line item | Admin API key | Daily buckets only. Cannot be your sole source of user attribution. |
| 2 | OpenAI **Usage API** (`/v1/organization/usage/...`) | Token counts by model, project, API key, user; separate endpoints for completions, embeddings, images, audio, moderations, vector stores, code interpreter | Admin API key | Input, cached input and output tokens are separate meters. Cached input is materially cheaper — count it separately or your unit costs will be wrong. |
| 3 | OpenAI **Global Admin Console** analytics | ChatGPT and Codex credit usage in one view, broken down by user, product and model | Global admin role | Introduced mid-2026. Confirm which workspaces are in scope of the global console versus standalone. |
| 4 | **Codex analytics API** | Codex-specific consumption and adoption | Admin access | Codex credit pricing moved to token-aligned rates in April 2026. Pre-April data is not comparable. Normalise or exclude. |
| 5 | OpenAI **Audit logs** | Who changed limits, keys, projects, model permissions | Admin API | Your evidence for governance maturity claims |
| 6 | OpenAI **Projects / Users / Invites** | Entitlement: seats bought, assigned, pending, never activated | Admin API | Entitlement minus activation is the single most valuable number in the negotiation |
| 7 | **Invoices and order form** | Settled truth; committed spend; overage rate; credit terms | Finance / procurement | Reconcile everything to this. API cost figures are planning estimates, not invoices. |
| 8 | **Azure Cost Management** (if any Azure OpenAI) | Parallel OpenAI consumption on a different paper | Cloud team | Frequently forgotten. Check before you claim a total. |
| 9 | **GitHub billing usage report + Copilot metrics** | The Copilot trial evidence base | GitHub enterprise admin | See 2.8 item 3. Time-critical. |
| 10 | **AWS Cost and Usage Report** (Bedrock lines) | Any existing Bedrock consumption | Cloud team | Often a data-science team experiment nobody logged |
| 11 | **Entra ID / Okta + HR feed** | Team, cost centre, job family, joiner-mover-leaver dates | Identity team | The join key that turns usage into segmentation. Get a DPIA view early. |
| 12 | **Expense system + card statements** | Shadow AI: individual subscriptions to image, video and voice tools | Finance | In a fashion brand, expect meaningful spend inside Marketing and Creative |
| 13 | **CASB / SSE / proxy logs** | Unsanctioned AI domains in use | Security | Aggregate only. Do not produce a named-user surveillance report. |
| 14 | **Contract register** | Every AI-adjacent SaaS renewal date | Vendor management | Feeds WS3 and reveals renewal collisions |

**Privacy guardrail.** You are joining usage telemetry to identity. In most jurisdictions this is employee monitoring. Before you build the join:

- Agree the lawful basis and complete or update a DPIA with Data Protection.
- Report at team level by default. Restrict individual-level views to named administrators with a documented purpose.
- Never publish individual-level league tables. They destroy trust faster than anything else in this engagement and they corrupt the data — people change behaviour when they are ranked.
- Check works-council or employee-representation requirements in each country where XYZ operates.

## 3.2 The consumption truth layer

Build a small dimensional model. Do not analyse in spreadsheets scattered across a shared drive.

**Fact table — `fct_ai_usage`** (grain: day × workspace × project × user × model × meter)

| Column | Notes |
|---|---|
| usage_date | Day bucket |
| platform | openai_api, chatgpt_enterprise, codex, copilot, bedrock, other |
| workspace_id / project_id | Native identifier |
| user_key | Pseudonymised; join to identity dimension |
| model | Exact model string, not a family label |
| meter | input_tokens, cached_input_tokens, output_tokens, credits, requests, images, audio_seconds |
| quantity | Metered quantity |
| list_cost | Quantity × published rate |
| effective_cost | Quantity × contracted rate |
| use_case_id | Nullable at baseline; populated by attribution (3.4) |

**Dimensions:** `dim_user` (team, function, cost centre, country, job family, start date), `dim_model` (family, tier, modality, rate card, status, retirement date), `dim_project`, `dim_use_case`, `dim_entitlement` (seat type, assigned date, activation date, credit allowance).

**Rules that save you later.**

1. Store list cost and effective cost separately. The gap between them is a negotiation exhibit.
2. Store cached input tokens as their own meter. Prompt caching can move a unit cost by an order of magnitude.
3. Never overwrite. Append and version. When a rate card changes mid-period you must be able to restate.
4. Reconcile monthly to the invoice. Publish the variance. A baseline that does not reconcile is an opinion.
5. Keep a `data_quality` flag per row: `reconciled`, `estimated`, `imputed`. Every chart states the mix.

## 3.3 Segmentation model

The brief asks for early adopters, steady-state users and laggards. That three-way split is too coarse to negotiate with. Use five axes and derive seven cohorts.

**Axes**

| Axis | Definition | Source |
|---|---|---|
| Activation | Any usage in the last 30 days | Usage API / console |
| Frequency | Distinct active days per month | Usage |
| Intensity | Credits or effective cost per active user per month | Cost |
| Breadth | Distinct capabilities used (chat, deep research, Codex, voice, image, API) | Usage by endpoint |
| Embeddedness | Usage inside a defined business workflow rather than ad-hoc | Use-case attribution + interviews |

**Cohorts.** Set thresholds from XYZ's own distribution — use deciles, not imported benchmarks. Starting definitions:

| Cohort | Definition | So what |
|---|---|---|
| C1 Never activated | Seat assigned, zero usage since assignment | Direct reclaim. Hard number for the negotiation. |
| C2 Lapsed | Active historically, nothing in 60 days | Reclaim or re-enable. Ask why — often a workflow blocker, not disinterest. |
| C3 Occasional | Active 1–4 days/month, low intensity | Enablement target. Cheap to move. |
| C4 Steady | Active 5–15 days/month, moderate intensity, ≥ 2 capabilities | The core. Protect. |
| C5 Power | Top decile intensity, high breadth, embedded | Your value evidence. Interview them. Their workflows become the reference patterns. |
| C6 Constrained | Hitting limits or requesting increases, high value work | **The most important cohort.** Evidence that entitlement is mis-allocated, not over-bought. |
| C7 Runaway | Top decile intensity, low or unclear value, often automation misconfiguration | The saving. Investigate before you cut. |

**Derived measures for the negotiation.**

| Measure | Formula | Use |
|---|---|---|
| Activation rate | Activated seats ÷ paid seats | Headline underuse |
| Entitlement utilisation | Credits consumed ÷ credits purchased | Credit ask |
| Concentration | Share of total credits used by top 10% of users | Argues for pooled credits, not per-seat caps |
| Zombie cost | C1 + C2 seats × seat price × months | Direct reclaim |
| Constrained value at risk | Estimated value of work blocked in C6 | Argues for a larger pool, not a smaller one |
| Burn trajectory | 3-month rolling growth in effective cost | Commit sizing |
| Peak-to-mean ratio | Peak month ÷ mean month | Argues for rollover and flex, not a flat commit |

**Interpretation discipline.** Low usage is not automatically waste. Test three explanations before you call a seat wasted: no training, no approved use case, or a blocked workflow (data classification, integration gap, latency). The negotiation position is different in each case.

## 3.4 Use-case attribution

Raw telemetry tells you which model was called. It does not tell you what work was done. You need the second one for the decision matrix and the value case.

Three methods, used together.

1. **Tagging at source (best, prospective).** Enforce metadata on every API call through the gateway (3.6): `cost_centre`, `business_unit`, `use_case_id`, `environment`, `data_class`, `initiator` (human or agent). Issue virtual keys per use case. This makes attribution automatic from the date it is switched on.
2. **Project and key archaeology (retrospective).** Map existing projects and API keys to owners and use cases by interview. Expect 60–80% coverage and a long tail of "misc".
3. **Structured interviews and a short survey (qualitative).** 12–20 interviews across cohorts C3–C7, plus a survey to the whole population. Ask what work the tool does, what it replaced, and what it unblocked.

Publish the coverage rate honestly: "78% of spend attributed to a named use case; 22% unattributed, concentrated in three legacy projects."

## 3.5 The model / tool usage matrix

This is the deliverable that changes daily behaviour. Design it as a one-page routing table that a developer or marketer can follow without reading a policy.

**Columns**

| Column | Content |
|---|---|
| Work class | From the shared Workload Taxonomy |
| Typical example | Concrete, from XYZ's own work |
| Data classification permitted | Public / Internal / Confidential / Restricted |
| Default tool | Named product and interface |
| Default model tier | Frontier reasoning / workhorse / fast-cheap / specialist |
| Escalation | When to move up a tier, and who approves |
| Human review | Required / spot check / none |
| Relative unit cost | Indexed, e.g. 1× / 6× / 40× |
| Typical cost per 100 tasks | Modelled, with the assumption stated |
| Prohibited | Explicit anti-patterns |

**Work classes to start from** (validate against XYZ's telemetry; do not import wholesale):

*Engineering:* inline completion · scoped code change in IDE · multi-file agentic task · code review · test generation · migration/refactor at scale · incident diagnosis · documentation.

*Commercial and corporate:* drafting and editing · summarisation at volume · structured extraction/classification · retrieval Q&A over internal documents · translation and localisation · research synthesis · data analysis · meeting capture.

*Brand and product:* concept imagery · production imagery · video · voice and dubbing · product copy at catalogue scale · design exploration.

**The cost-implication method.** Do not publish unit prices that will be wrong in a month. Publish a formula and an indexed table.

```
cost_per_task = (input_tokens_uncached × rate_in
               + input_tokens_cached  × rate_cached
               + output_tokens        × rate_out
               + tool_calls           × tool_rate)
               × retries_factor
               × (1 + agent_amplification)
```

Then measure `tokens_per_task` from real telemetry for each work class, and express results as an index against the cheapest viable path. Three findings this method reliably produces, all of which are worth money:

- **Agent amplification.** An agentic task consumes many multiples of a single chat turn, because it plans, reads files, retries and self-checks. Teams that budget agentic work at chat rates will overrun. Measure the multiplier for XYZ's own workloads and publish it.
- **Output tokens dominate.** Output is typically priced several times higher than input across frontier models. Verbosity is a cost lever. So is asking for structured output.
- **Caching is the cheapest optimisation nobody enables.** Cached input is priced far below uncached input. Repeated system prompts and repeated document context are the obvious candidates.

**Routing principle to state plainly:** default to the cheapest model that clears the quality bar for the work class, and escalate deliberately. Published buyer-side analyses of enterprise estates put the saving from disciplined task-based routing in the range of tens of percent with no quality loss. Do not quote someone else's percentage to the client. Measure XYZ's own with an A/B on two or three high-volume work classes, then quote that.

**Quality bar, not vibes.** For each work class where routing down saves real money, build a small evaluation set (30–100 real examples with graded expected outcomes). Run the candidate models. Record pass rate, latency and cost. That evaluation set is a durable asset — it is what lets XYZ re-run this decision when the next model ships. Hand it over.

## 3.6 Token and credit governance framework

Seven layers. Deliver a control catalogue with an owner and an implementation state for each control.

**Layer 1 — Policy.** Acceptable use. Data classification rules mapped to approved models and platforms. Prohibited uses. Disclosure rules for AI-generated customer-facing content (see Part 7 — this is now a legal obligation, not a preference). Keep it to two pages. Nobody reads ten.

**Layer 2 — Identity and entitlement.** SSO enforced on every AI platform. Group-based role assignment. Joiner-mover-leaver automation. A seat reclamation SLA: no activation within 30 days of assignment, or 60 days dormant, triggers automatic reclaim with a one-click re-request. Publish the reclaim rule before you enforce it.

**Layer 3 — Allocation.** Move from per-seat caps to a pooled envelope with group limits. Structure:

| Element | Design |
|---|---|
| Enterprise envelope | Monthly credit ceiling aligned to the commit |
| Group allocations | Per business unit or engineering group, sized on the segmentation |
| User overrides | For C5/C6 individuals with documented need |
| Reserve pool | 15–20% held centrally for exceptions and spikes |
| Innovation allowance | A ring-fenced pot with deliberately loose controls (see below) |

Modern platform tooling now supports this directly: ChatGPT Enterprise supports group-level limits with user overrides drawing on a shared workspace pool, and GitHub Copilot moved to credit allowances with organisation-level pooling and user-level budgets in June 2026. Use the native controls first. Add a gateway where native controls cannot reach.

**The innovation exception.** The 2026 FinOps Framework makes an important point that most governance frameworks get wrong: an innovation-focused AI scope should tolerate higher waste, run at a faster cadence, and accept lower maturity. If you apply steady-state efficiency standards to experimentation, you either suppress the experiments or you manufacture the appearance of governance. Ring-fence an explicit innovation budget, cap it, and do not police it at the same granularity as production.

**Layer 4 — Runtime control.** Where the estate spans more than one provider, put an AI gateway in the path. It is the only place where routing, budgets, model allow-lists, caching, redaction and logging can be enforced consistently. See 4.5 for the build/buy assessment.

Controls to implement at the gateway: virtual keys per use case with hard budgets · model allow-list per key · rate limits · prompt and response logging with PII redaction · semantic or exact-prefix caching · automatic failover · mandatory metadata tags.

**Layer 5 — Observability.** Dashboards for three audiences.

| Audience | Cadence | Content |
|---|---|---|
| Platform / FinOps | Daily | Burn vs envelope, anomalies, cache hit rate, failover events, top movers |
| Business unit lead | Weekly | Group consumption vs allocation, cohort mix, adoption trend |
| Executive | Monthly | Cost per unit of work, value delivered, commit utilisation, forecast to renewal |

Set alerts on rate of change, not only on absolute thresholds. The failure mode is a misconfigured automation that burns a month of credits in three days.

**Layer 6 — Accountability.** Use a maturity ladder. Do not start at chargeback.

| Stage | Mechanism | Timing |
|---|---|---|
| 1 Showback | Visible cost by team, no financial transfer | Month 1 |
| 2 Showback with budget | Teams own an allocation and a forecast | Month 3 |
| 3 Soft chargeback | Costs appear in team P&L, not enforced | Month 6 |
| 4 Chargeback | Real transfer, with exception path | Month 9+ |

Jumping straight to chargeback drives usage into shadow tools and destroys the visibility you just built.

**Layer 7 — Exception path.** High-value use cases must be able to exceed guardrails without a two-week wait.

- Request form: use case, value estimate, alternatives tested, data classification, requested increase, duration.
- Decision SLA: two business days for increases under a stated threshold, five days above it.
- Approver: platform owner below threshold, CoE lead above.
- Every exception has an expiry date and a review. No permanent exceptions.
- Publish exception volumes monthly. A rising exception rate means your allocation model is wrong, not that people are misbehaving.

**Deliverable form.** A control catalogue table: control ID · layer · description · owner · implementation state (designed / configured / enforced) · evidence location · review date.

## 3.7 Renewal negotiation brief

This is the highest-value deliverable in the engagement. Procurement owns the negotiation. You own the evidence and the architecture options that create leverage.

### 3.7.1 Structure of the brief

1. Position summary — one page, three asks, one walk-away condition
2. Consumption evidence — baseline, segmentation, trajectory, confidence range
3. Entitlement analysis — what is paid for and not used, what is constrained
4. Forecast scenarios — low / base / high with drivers stated
5. Costed BATNA — the credible alternative, with a migration plan and a switching cost
6. Ask ladder — what to open with, what to trade, what to hold
7. Term sheet redlines — the clauses that matter
8. Choreography — sequence, timing, who says what

### 3.7.2 Build the forecast properly

Vendor-supplied consumption estimates are systematically low. Independent buyer-side reviews of enterprise GenAI deals report first-year vendor estimates running well below actual burn once agentic features are enabled, and committed spend sized to optimistic growth creating shortfall risk. Two implications:

- **Model your own forecast.** Three scenarios, each with explicit drivers: headcount in scope, activation rate, agentic share of workload, average tokens per task, cache hit rate, model mix.
- **Commit at the conservative end.** Then negotiate the right to consume above the commit at the same rate. You want the discount without the shortfall exposure.

Run a sensitivity table. Show the client which single variable moves the annual number most. In most estates it is the agentic share of workload, not headcount.

### 3.7.3 The ask ladder

| Priority | Ask | Rationale from your evidence |
|---|---|---|
| **Hold** | Commit sized at your P50, not the vendor's forecast | Forecast model, scenario table |
| **Hold** | Same negotiated rate applies to consumption above the commit | Removes shortfall risk without capping growth |
| **Hold** | Data terms: no training on XYZ data, defined retention, deletion on exit, export rights | Non-negotiable for a consumer brand |
| **Hold** | Renewal uplift cap in writing (low single digits) and no silent auto-renewal; 90-day notice | Year-two lock-in is where quote-only vendors extract value |
| **Push** | Credit rollover of unused entitlement | Peak-to-mean ratio; C1/C2 unused entitlement |
| **Push** | Pooled credits across seat types rather than per-seat caps | Concentration measure — top decile drives most usage |
| **Push** | Model deprecation notice period and migration support | The 31 August 2026 Codex model retirement is your live example |
| **Push** | Seat flex band (±10–15%) without repricing | Seasonal workforce in fashion retail |
| **Trade** | Multi-year term in exchange for rate lock | Only if data and exit terms are already secured |
| **Trade** | Reference status, case study, logo rights | Costs XYZ little, worth real money to the vendor |
| **Ask** | Free pilot seats (10–25 for 60–90 days) for the next capability | Cheap for the vendor to give |
| **Ask** | Funded solution architect days, enablement workshops, migration credits | Converts directly into your CoE build |
| **Ask** | Contracted overage rate stated on the order form, with alerting thresholds | Estimated dollar values now surface in admin analytics only when a contracted overage rate exists |
| **Ask** | Regional data residency and sub-processor commitments | Feeds the AI Act and GDPR position |

### 3.7.4 Build a real BATNA

A negotiating position without an alternative is a request. Cost the alternative properly, in writing, before the first session.

| BATNA element | What to produce |
|---|---|
| Alternative access route | Bedrock (or equivalent) rate card for the equivalent model mix, including cross-region inference uplift and batch discount where applicable |
| Alternative coding tool | Copilot re-entry cost at current credit-based pricing |
| Alternative frontier model | A second frontier provider quote for the workhorse tier |
| Migration cost | Engineering days to move the top five workloads behind the gateway, with the gateway as the enabling asset |
| Switching timeline | Weeks to move 30% of consumption; weeks to move 80% |
| Residual lock-in | What genuinely cannot move: fine-tuned models, workspace-native features, embedded workflows |

The gateway is what makes the BATNA credible. If XYZ can demonstrate that a portion of traffic can be redirected in days, the negotiation changes character. Build it before the negotiation, not after.

### 3.7.5 Timing and choreography

- Open the conversation early. Do not let the vendor set the calendar.
- Bring one competing quote to the table. It does not have to be a threat to be leverage.
- Vendor quarter-end and year-end create flexibility. Align the closing session where you can.
- Do not share your full baseline with the account team before the brief is approved. Share the conclusions you choose to share.
- Keep the walk-away condition written down and agreed with the CIO in advance. Under pressure, undefined walk-aways move.

### 3.7.6 Where entitlement is being underused — the headline exhibit

Produce one slide with four numbers and their money value:

1. Seats paid for, never activated (C1)
2. Seats dormant beyond 60 days (C2)
3. Credits purchased and unconsumed in the period, and whether they expired
4. Constrained high-value users who were blocked (C6)

Numbers 1–3 are the reclaim argument. Number 4 is the reallocation argument. Presenting all four together is what stops the vendor reframing your underuse finding as "you should buy fewer seats and more credits" on their terms rather than yours.

---

# Part 4 — Workstream 2: Multi-Model Access Strategy

**Objective restated as a decision:** which models, through which route, at what cost — and under what conditions we change our mind.

## 4.0 The context you must hold in your head

Two market facts from 2026 change the shape of this analysis. Verify both before you rely on them.

1. **GitHub Copilot moved to usage-based billing on 1 June 2026.** Premium requests were retired and replaced by GitHub AI Credits, metered on input, output and cached tokens at each model's listed API rate. Seat prices did not change (Business $19/user/month including $19 in monthly credits; Enterprise $39/user/month including $39 in credits). Code completions and next-edit suggestions remain included and do not draw on credits. Organisation-level pooling and user-level budgets are available to admins.
2. **OpenAI Codex moved to token-aligned credit pricing in April 2026**, and enterprise-grade credit analytics and spend controls landed in June 2026.

**Consequence for the recommendation.** Copilot and Codex are no longer a seat-price-versus-consumption comparison. Both are now consumption products with a seat-priced floor. The old argument for consolidating on one platform — "we already pay per seat, so marginal use is free" — no longer holds on either side. The comparison is now genuinely about routing, capability fit and where the free tier sits. That is a materially better argument for a mixed estate than the one the brief assumes, and it is a finding worth leading with.

Note the second-order effect: Copilot's free-completions tier means low-intensity developers can be served at near-zero marginal cost, while high-intensity agentic work is metered on both platforms. That shape supports segmenting developers by intensity, not by team.

## 4.1 Current-state assessment: the Copilot trial post-mortem

Handle this as a trust-repair exercise with an evidence layer, not as an audit.

### 4.1.1 Sequence

1. **Reconstruct the record.** What was the trial's stated hypothesis, population, duration, success criteria and decision rule? In most organisations the answer is that no explicit criteria existed. Record that finding without blame — it is the strongest argument for the evaluation framework you are about to introduce.
2. **Recover the data.** Billing usage reports, seat assignment history, Copilot metrics, repository telemetry for the trial window and a matched pre-trial window.
3. **Run the sentiment round.** Structured, anonymised, published.
4. **Analyse.** Quantitative and qualitative side by side.
5. **Publish a fair account.** Including what the withdrawal cost.

### 4.1.2 Measurement framework

Do not measure with a single metric. Use three lenses together.

| Lens | Metrics | Source |
|---|---|---|
| Delivery (team level) | Deployment frequency, lead time for changes, change failure rate, time to restore | CI/CD, incident system |
| Developer experience (individual level) | Satisfaction, perceived flow, friction points, time-on-task | SPACE-style survey, diary study |
| AI-specific | Utilisation (active users, sessions), acceptance/retention of suggested code, cost per accepted change, review burden, rework rate on AI-touched code at 30/60/90 days | Tool telemetry + repo analysis |

**Three warnings from the 2025–2026 research literature. Put these in the deliverable.**

- **The productivity paradox.** Individual output metrics rise sharply with AI coding assistants while organisational delivery metrics often stay flat. Throughput gains show up later, if the surrounding system can absorb them. Do not accept "PRs merged" as proof of value, and do not accept flat DORA metrics as proof of no value.
- **Speed without a quality counterweight is a false reading.** Pair every speed metric with a quality metric and track AI-touched code over 30–90 days. Defects and rework surface late.
- **Developers are poor estimators of their own productivity.** Use sentiment for direction and diagnosis, telemetry for magnitude. Never use either alone.

**Never use these metrics for individual performance management, and say so in the deliverable.** If developers believe the data will be used against them, the sentiment round returns nothing useful and the telemetry gets gamed.

### 4.1.3 The sentiment round

This is the part the brief is really asking about. Run it properly.

- **Format:** 30-minute structured interviews with 10–15 developers spanning the teams that objected and the teams that did not, plus a short anonymous survey to the whole engineering population.
- **Questions:** What did Copilot do in your workflow that nothing else does? What broke when it was withdrawn? What did you switch to? What did that cost you in time? What would change your mind? How was the decision communicated?
- **Bias control:** interview volunteers *and* a random sample. The loudest voices are not the population.
- **Publish verbatim, anonymised quotes** alongside the numbers. Nothing rebuilds trust faster than people seeing their own words in a leadership deck, unedited.
- **Separate three distinct grievances** in the analysis, because they need different responses: (a) the tool was better for a specific task; (b) the decision was made without consultation; (c) the switch cost time nobody accounted for. Only (a) is a tooling question.

### 4.1.4 Quantify the withdrawal

State the cost of the withdrawal in the deliverable, with a confidence range: switching time, workflow rebuild, any measurable delivery dip in the following quarter, and attrition or engagement signals if HR will share them. Also state the saving it produced. Then let leadership see both sides. A consultant who only reports the cost looks like an advocate. A consultant who reports both looks like an architect.

## 4.2 Workload-to-model mapping

### 4.2.1 Test the 20–30% hypothesis, do not assume it

The brief offers a split of roughly 20–30% of developer workload on Copilot with the balance on Codex. Treat it as a hypothesis, H0, and design a test.

**Method**

1. **Build the developer workload taxonomy** (from 3.5). Nine to twelve classes.
2. **Size each class.** Three independent estimates, triangulated:
    - Telemetry: distribution of session types, agentic task counts, review events, completion acceptance.
    - Diary study: 15–20 developers, one week, time logged against the taxonomy.
    - Repository analysis: change size distribution, file-touch counts, PR characteristics.
3. **Score each class against each platform** on capability fit, cost per task, workflow friction and blast radius.
4. **Derive the split.** The output is a share of *workload*, and separately a share of *developers*, and separately a share of *spend*. These three numbers differ. The brief conflates them. Make the distinction explicit — it is a small piece of rigour that markedly raises the credibility of the whole workstream.

**Likely shape of the finding** (state as a prior to be tested, never as a conclusion): inline completion and small scoped edits favour the always-on, free-tier IDE experience; multi-file agentic tasks, large refactors and long-horizon work favour the dedicated coding agent; code review sits in contention and should be decided on cost per review and defect catch rate. If XYZ's telemetry says otherwise, report what the telemetry says.

### 4.2.2 Present it as a routing table, not a percentage

A percentage is a headline that will be misquoted. A routing table is operable. Deliver both, and lead with the table.

| Work class | Primary | Secondary | Basis | Est. share of workload | Est. share of spend |
|---|---|---|---|---|---|
| Inline completion | | | | | |
| Scoped edit in IDE | | | | | |
| Multi-file agentic task | | | | | |
| Large refactor / migration | | | | | |
| Code review | | | | | |
| Test generation | | | | | |
| Incident diagnosis | | | | | |
| Documentation | | | | | |
| Security remediation | | | | | |

## 4.3 Evaluation framework for access routes

Score every candidate access route on the same criteria, with weights agreed by steering **before** scoring. Agreeing weights after seeing scores is how evaluations lose their authority.

| Criterion | Weight (agree at steering) | Evidence source | Scoring anchors |
|---|---|---|---|
| Capability fit per work class | 25% | Internal eval sets (3.5), benchmark evidence, pilot | 1 = fails bar; 5 = clears bar on all target classes |
| Cost per workload | 20% | Cost model (4.6) | Indexed against cheapest viable route |
| Latency and throughput | 10% | Measured p50/p95, time-to-first-token, tokens/sec, under XYZ's real prompt shapes | Against the work class requirement, not in the abstract |
| Data residency and privacy | 15% | Contract, region availability, sub-processor list, training terms | Binary gates plus gradation |
| Security posture | 10% | Network isolation, key management, audit logging, guardrails, certifications | Against XYZ's control baseline |
| Vendor concentration risk | 10% | Share of AI spend, substitutability, exit cost | Portfolio-level, not per-route |
| Operational burden | 5% | FTE to run, integration effort, skills available | Honest estimate from platform engineering |
| Commercial flexibility | 5% | Commit structure, rollover, overage, exit | From the contract, not the website |

Gates that override the score: any route that fails a mandatory data residency, security certification or contractual data-use requirement is excluded regardless of total score. Say this before scoring.

## 4.4 Bedrock (or equivalent) evaluation

### 4.4.1 What to assess

| Dimension | What to check in 2026 | Why it matters here |
|---|---|---|
| Model families available | First-party Amazon models plus multiple third-party families (Anthropic, Meta, Mistral, Cohere, Stability and others), with OpenAI frontier models added to the platform during 2026 | Determines whether Bedrock is a genuine diversification route or just a second door to the same models |
| Billing modes | On-demand per token; batch at a substantial discount (commonly ~50%) with asynchronous turnaround; provisioned throughput in model units on 1- or 6-month commitments | Batch is the most under-used lever for catalogue-scale fashion workloads |
| Break-even for provisioned throughput | Provisioned only wins at high, sustained utilisation. Below roughly 60–85% sustained utilisation, on-demand or batch usually wins | Prevents an expensive mistake |
| Prompt caching | Large reductions on repeated input context where supported | The single biggest lever on RAG and long-system-prompt workloads |
| Adjacent charges | Knowledge base vector storage, agent orchestration, guardrails, data transfer, embeddings | Where Bedrock estimates typically under-read actual bills |
| Data residency | Region availability per model; behaviour of cross-region inference and where inference may execute | Central to the EU position for a fashion brand with EU customers |
| Security posture | VPC and private connectivity, KMS-managed keys, CloudTrail logging, IAM integration, native guardrails | Bedrock's strongest argument: it inherits controls XYZ already operates |
| Latency | Measured, per model, per region, under XYZ's prompt shapes | Vendor-quoted latency is not evidence |

### 4.4.2 The concentration-risk subtlety worth writing down

Adding Bedrock as an access route does not automatically reduce vendor concentration. Two reasons.

- If XYZ routes the *same* model family through a different platform, the model dependency is unchanged. Only the commercial and infrastructure dependency changes.
- The provider landscape in 2026 includes cross-holdings and distribution arrangements between the major cloud platforms and the major model labs, including an AWS–OpenAI distribution arrangement announced in February 2026. Verify the current position before writing a concentration-risk paragraph.

**Therefore:** define concentration risk on two axes and report both.

| Axis | Question | Mitigation |
|---|---|---|
| Model dependency | Would a quality regression, retirement or price change in one model family break a critical workflow? | Maintain a validated secondary model per tier, with an eval set proving it clears the bar |
| Commercial dependency | What share of AI spend sits with one commercial counterparty? | Access route diversity, gateway abstraction, contractual exit terms |

The honest recommendation is usually: use the gateway to make substitution *possible* and cheap, then concentrate consumption where the economics are best, and re-test substitution quarterly. Diversification bought by permanently splitting traffic is expensive. Diversification bought by maintaining a tested exit is cheap.

## 4.5 The access architecture

The architectural decision underneath all of this is whether to put an AI gateway between applications and providers.

**Recommend one.** Once XYZ calls more than one provider, or spends meaningfully on tokens, the gateway is where cost attribution, routing, model allow-listing, budgets, caching, redaction and audit logging are actually enforced. Without it, each of those controls has to be re-implemented in every application.

**Options to assess** (all active in 2026; verify current capability):

| Option | Shape | Fits when |
|---|---|---|
| Open-source proxy (e.g. LiteLLM) | Self-hosted, very broad provider coverage, virtual keys with budgets | XYZ wants portability, has platform engineering capacity, may run self-hosted models |
| Managed AI-native gateway (e.g. Portkey and peers) | SaaS control plane, semantic caching, guardrails, observability out of the box | XYZ wants speed over control and accepts a SaaS dependency in the request path |
| API-management extension (e.g. Kong AI Gateway, Azure API Management) | AI plugins on an existing gateway estate | XYZ already runs that gateway and wants governance continuity |
| Cloud-native (Bedrock as the abstraction, or a cloud AI gateway) | Fewest moving parts inside one cloud | XYZ is decisively single-cloud and accepts that as the boundary |
| Build | Internal service | Almost never justified. Assess it so you can rule it out with a number. |

**Selection criteria:** latency overhead added at p95 · provider coverage · budget and key granularity · caching mechanics · guardrail and redaction capability · self-hosting option · audit and compliance features · failure behaviour when the gateway is down · operational cost in FTE.

**Non-negotiable design points.**

1. The gateway must not be a single point of failure. Design the fallback path and test it.
2. Enforce metadata tagging at the gateway. This is what makes 3.4 automatic.
3. Log prompts and responses with redaction, with a retention period agreed with Data Protection.
4. Keep the request path simple. A gateway that adds meaningful p95 latency to interactive workloads will be bypassed.

**Reference architecture (target state)**

```
 Users / Apps / Agents
        │
   Identity (SSO, groups, RBAC)
        │
   ┌────▼─────────────────────────────────────────┐
   │  AI GATEWAY                                   │
   │  virtual keys · budgets · model allow-list    │
   │  routing & failover · cache · redaction       │
   │  metadata tagging · logging                   │
   └────┬──────────────┬──────────────┬────────────┘
        │              │              │
   OpenAI API     Bedrock        Other providers
   ChatGPT Ent.   (Anthropic,    (specialist:
   Codex          Amazon, Meta,   voice, video,
                  Mistral…)       image)
        │              │              │
   ┌────▼──────────────▼──────────────▼────────────┐
   │  OBSERVABILITY & FINOPS                        │
   │  usage · cost · quality evals · anomalies      │
   └────────────────────────────────────────────────┘
```

Note that seat-based products (ChatGPT Enterprise, Copilot IDE, Codex in the IDE) do not route through the gateway. Govern those with native admin controls. Be explicit in the deliverable about which controls apply where — this is a common and embarrassing gap in AI governance frameworks.

## 4.6 The cost model

Build one workbook. It serves WS1 and WS2 and it is the artefact procurement will keep.

**Sheets**

| Sheet | Content |
|---|---|
| `Assumptions` | Every input, one place, colour-coded as measured / estimated / vendor-quoted |
| `Rate cards` | Per model per route, with source URL and date checked |
| `Workload` | Work classes, volumes, tokens per task, agent amplification, retry rate, cache hit rate |
| `Scenarios` | Low / base / high, with drivers |
| `Route comparison` | Cost per 1,000 tasks per work class per route |
| `TCO` | Adds platform, gateway, engineering, enablement and run costs |
| `Sensitivity` | Tornado chart on the five biggest drivers |
| `Output` | The three or four numbers leadership will quote |

**Rules.** No hard-coded numbers in formulas. Every rate card cell carries a source and a date. Include a "what would have to be true" section: state the assumption values at which the recommendation flips.

**TCO components teams routinely forget:** gateway run cost · observability and eval tooling · vector storage and retrieval infrastructure · data preparation · human review time · enablement and training · seat cost for people whose usage is below the free tier · the cost of running two platforms in parallel during migration.

## 4.7 Directional guidance note

Four pages for IT leadership. No appendices.

**Structure**

1. **Position** — one paragraph. The target portfolio and the access route for each tier.
2. **Why** — the three findings that drive it, each with a number.
3. **What changes** — for developers, for marketing, for platform engineering.
4. **What it costs** — the number, the range, and the biggest uncertainty.
5. **Revisit triggers** — the conditions under which this position must be reopened.

**Target portfolio, expressed by tier**

| Tier | Purpose | Primary | Secondary (validated) | Access route |
|---|---|---|---|---|
| Frontier reasoning | Hard analysis, complex agentic work | | | |
| Workhorse | Most drafting, summarisation, RAG | | | |
| Fast / low cost | High-volume classification, extraction, routing | | | |
| Coding agent | Multi-file autonomous engineering work | | | |
| IDE assistant | Inline completion, scoped edits | | | |
| Embeddings | Retrieval | | | |
| Image | Concept and production imagery | | | |
| Video | Campaign and product video | | | |
| Voice | Contact centre, localisation, dubbing | | | |

For each tier: name the primary, name a secondary that has been *tested against the eval set*, and state the access route. A secondary that has never been tested is not a secondary.

**Revisit triggers — state thresholds, not sentiments**

| Trigger | Threshold | Action |
|---|---|---|
| Price change | Any effective rate change > 15% on a tier | Re-run route comparison within 10 working days |
| Model retirement notice | Any notice affecting a primary or secondary | Run migration assessment; invoke contractual notice terms |
| Quality regression | Eval set pass rate falls > 5 points | Fail over to secondary; open vendor ticket |
| Latency breach | p95 exceeds work-class requirement for 3 consecutive days | Route-level failover |
| Concentration | One commercial counterparty exceeds 70% of AI spend | Report to steering; test substitution |
| Commit utilisation | Below 70% or above 95% of committed spend at mid-term | Re-forecast; open commercial conversation |
| Regulatory change | New obligation affecting model use or disclosure | Compliance review before further rollout |
| New capability tier | A materially new modality reaches enterprise readiness | Landscape refresh (WS3 cadence) |

Set the standing review cadence at quarterly, with the triggers able to force an out-of-cycle review. State who owns the review: the CoE lead, not the engagement team.

---

# Part 5 — Workstream 3: GenAI Landscape Review

**Objective restated as a decision:** where does XYZ build, where does it buy, where does it partner — and what should it stop doing.

## 5.1 Bound the scope first

The brief names voice and video and leaves further categories "to be confirmed in scoping". Do not let that stay open. Bring a proposed taxonomy to the scoping session and force a decision on it in week 1.

**Proposed capability taxonomy for a fashion brand.** Twelve domains, mapped to the value chain. Ask steering to confirm, add or strike.

| # | Domain | Representative capability | Typical owner |
|---|---|---|---|
| 1 | Brand and campaign content | Image generation, editing, variation at scale | Marketing / Creative |
| 2 | Video | Campaign video, product video, social cutdowns, localisation | Marketing |
| 3 | Voice | Contact centre agents, IVR, dubbing, brand voice | Customer Service |
| 4 | Product content | Copy at catalogue scale, attribution, PIM enrichment, translation | E-commerce |
| 5 | Discovery | Visual and semantic search, recommendation, virtual try-on, sizing | E-commerce |
| 6 | Conversational and agentic commerce | Shopping assistants, agent-readable storefronts, service resolution | Digital |
| 7 | Design and product development | Concept exploration, colourways, 3D and sample reduction | Design |
| 8 | Merchandising and planning | Demand forecast, allocation, markdown, assortment | Merchandising |
| 9 | Supply chain and sourcing | Supplier communication, document processing, compliance data | Supply Chain |
| 10 | Store and workforce | Scheduling, clienteling, in-store assistance, loss prevention | Retail Ops |
| 11 | Corporate functions | Finance, legal, HR, procurement assistance | Functions |
| 12 | Engineering and platform | Coding agents, gateway, RAG, evals, observability, agent infrastructure | IT |

**Cross-cutting themes** to assess separately, because they cut across every domain and are where a fashion brand carries specific exposure: content provenance and disclosure · likeness and model rights · IP and training-data posture · sustainability claim accuracy · accessibility.

**Prioritisation rule for the scan.** Rank domains on (a) share of current or planned spend, (b) proximity to revenue, (c) regulatory exposure, (d) rate of market change. Do deep vendor work on the top five or six. Give the rest a one-page market summary. A shallow scan across twelve domains is worth less than a deep scan across five.

## 5.2 Vendor scorecard

Nine criteria. Score 1–5. Every score carries an evidence grade.

| Criterion | What good looks like |
|---|---|
| Capability depth | Solves the specific work class, not the category |
| Retail / fashion proof | Named comparable customers at comparable scale; verifiable outcomes |
| Enterprise readiness | SSO, RBAC, audit logs, DPA, sub-processor transparency, security certifications, an articulated AI Act position |
| Data posture | Training on customer data, retention, residency, deletion, export |
| Integration fit | Works with XYZ's commerce, PIM, DAM, CDP and identity stack |
| Commercial model | Predictable, aligned to value, no punitive overage cliff, exit terms |
| Viability | Funding, ownership, revenue signal, customer concentration, roadmap credibility |
| Lock-in and substitutability | How much would it cost to leave in 18 months |
| Model dependency | Which foundation models sit underneath, and what happens if those change |

**The last criterion matters more than it looks.** A large share of application-layer GenAI vendors are thin layers over the same handful of foundation models. Two consequences for XYZ: (a) an apparently diversified vendor portfolio may sit on a single model dependency; (b) the vendor's margin depends on model prices they do not control. Ask every vendor which models they use and what their price-change policy is. Record the answers.

**Evidence grading.** Apply to every claim in the scorecard.

| Grade | Meaning |
|---|---|
| A | Primary source: contract, documentation, measured test, reference call with a comparable customer |
| B | Credible secondary: independent analyst, peer review at scale, verified case study |
| C | Vendor claim, unverified |

Publish the grade distribution. A landscape map built entirely on grade C is marketing.

## 5.3 Research protocol

**Primary research (do this — it is what distinguishes the work).**

- Reference calls: three per shortlisted vendor, at least one sourced by you rather than by the vendor.
- Analyst inquiry calls if XYZ holds a subscription. Use the inquiry hours; they are usually unused.
- A short RFI to shortlisted vendors: 15 questions, standard format, comparable answers.
- Hands-on test against XYZ's own eval sets where the vendor allows a trial.
- Peer network: other retail and consumer brands, industry bodies, CIO networks.

**Secondary research.**

- Analyst market maps for structure, not for conclusions.
- Vendor documentation, changelogs, status pages, trust centres, security portals.
- Public financial disclosure and earnings commentary for viability signals.
- Job postings as a leading indicator of roadmap direction.
- Practitioner communities for failure modes that never appear in case studies.

**Bias controls.** State them in the method note.

1. Score against the same criteria in the same order for every vendor.
2. Two assessors score independently on the shortlist; reconcile differences in writing.
3. Disclose any commercial relationship between your firm and any assessed vendor. If one exists, say so on the page where that vendor is scored.
4. Include at least one vendor per category that the client has not heard of. If your map only contains the incumbents, you have not done research.
5. Record what you could not find out. Absence of evidence is a finding.

## 5.4 Internal cross-check

The brief notes XYZ is collating this data. Assume it is incomplete. Build the register yourself in parallel.

**Estate register — one row per AI tool or initiative**

| Field | Notes |
|---|---|
| Tool / initiative | Name |
| Domain | From 5.1 taxonomy |
| Status | Pilot / production / committed but unstarted / dormant |
| Business owner | A person, not a department |
| Technical owner | A person |
| Contract value and renewal date | From vendor management |
| Users: entitled vs active | From WS1 method |
| Data classification processed | Highest class |
| Underlying model(s) | Ask the vendor |
| Overlapping capability | Cross-reference to other rows |
| Value evidence | Grade A/B/C |
| Disposition | Keep / consolidate / renegotiate / retire / escalate |

**Shadow estate discovery.** Four sources, triangulated: expense and card data · SSO and identity provider application logs · network or CASB telemetry (aggregate only) · a no-blame amnesty survey. In a fashion brand, expect the largest shadow concentration in Marketing, Creative and E-commerce, not in IT. Announce the amnesty. Punishing disclosure guarantees you never see the real estate.

**Three analyses to produce**

1. **Gap.** Domains with material business value and no capability. Rank by value at stake.
2. **Duplication.** Two or more tools serving the same work class. **Deduplicate on capability, not on brand** — three tools with different names may all be doing catalogue copy generation on the same underlying model.
3. **Over-investment.** Committed spend materially above realised usage or value. Cross-reference to the WS1 cohorts. This is where the money is.

**Heat map.** Domains on one axis, four measures on the other: current spend · realised value (graded) · capability coverage · risk exposure. One page. It is the slide the executive team will remember.

## 5.5 Target-state blueprint

### 5.5.1 The decision rule for build / buy / partner / consume

Use four options, not three. The brief's omission of "consume" is worth correcting — most thin use cases need a model call behind a gateway, not a product.

| Option | Use when | Test |
|---|---|---|
| **Consume** | Thin capability, no proprietary data, no specialised UX | Could a competent engineer build this in under two weeks on top of the gateway? |
| **Buy** | Commodity capability, mature vendor market, not differentiating | Would XYZ's customers notice if this were identical to a competitor's? If no, buy. |
| **Partner** | Requires vendor IP plus XYZ's proprietary data or brand context | Is there a specific vendor whose capability plus XYZ's data creates something neither has alone? |
| **Build** | Touches proprietary data, expresses brand differentiation, and is reusable across domains | Three conditions, all required. Two out of three is a "buy". |

Add two constraints on top of the rule:

- **Build capacity is finite.** Rank build candidates and fund the top two or three. A blueprint with nine "build" calls is a wish list.
- **Every build call carries a run cost.** State it. Most build decisions are made on construction cost and regretted on run cost.

### 5.5.2 Blueprint layers

Present the target state as layers, with the build/buy/partner/consume call marked on each component.

| Layer | Components |
|---|---|
| Experience | Storefront, app, store tools, contact centre, internal assistants |
| Agent and orchestration | Agent runtime, tool registry, workflow orchestration, human-in-the-loop |
| Capability services | Content generation, product enrichment, search and discovery, forecasting, service resolution |
| Model access | Gateway, model portfolio, routing, caching, failover |
| Data and retrieval | Product data, customer data, brand and asset data, vector stores, feature store, lineage |
| Governance and quality | Eval harness, guardrails, observability, cost attribution, incident management |
| Security and identity | SSO, RBAC, secrets, DLP, network isolation, audit |

Mark each component with: current state · target state · disposition · owner · sequence (now / next / later).

### 5.5.3 Roadmap

Three horizons, each with named owners and a stated funding source.

| Horizon | Timeframe | Content |
|---|---|---|
| Now | 0–3 months | Retire duplicates, reclaim entitlement, stand up gateway and observability, publish routing matrix, close the highest-exposure compliance gaps |
| Next | 3–9 months | Consolidate onto the target portfolio, deliver top two build candidates, formalise the CoE, first chargeback stage |
| Later | 9–18 months | Domain expansion, agentic workflows in production, second landscape refresh |

---

# Part 6 — Building the AI Centre of Excellence

You have strong theory and no CoE build behind you. This part is the practical scaffolding. Everything here is designed so a first-time builder can execute it without improvising.

## 6.1 Choose the archetype deliberately

| Archetype | Hub owns | Spokes own | Fails when |
|---|---|---|---|
| Centralised | Everything | Nothing | Demand exceeds hub capacity; hub becomes a queue |
| Federated | Standards only | Delivery, platform choices | Fragmentation; duplicate spend; governance gaps |
| Hub-and-spoke | Platform, standards, governance, enablement, commercial | Use cases, domain data, adoption, value | Hub takes delivery work and becomes a bottleneck |

**Recommendation for XYZ: hub-and-spoke.** Two reasons specific to this client. First, the Copilot withdrawal has already created a perception that tooling decisions happen centrally and without consultation; a visible federation of decision rights is part of the remedy. Second, in a fashion brand the highest-value GenAI use cases sit in Marketing, Creative, E-commerce and Merchandising — functions that will not accept an IT-owned delivery queue.

Hub-and-spoke is the dominant enterprise pattern in 2026 practitioner literature, but the pattern is not the point. The decision rights are. Write them down.

## 6.2 Charter — define these six things or do not launch

1. **Purpose and mandate.** Why the CoE exists. What it owns. What it explicitly does *not* own.
2. **Scope.** Which technologies and which use-case classes are in scope. Where the boundary with data, security and architecture sits.
3. **Decision rights.** What the CoE approves, what it recommends, what it can veto, and what it merely observes. Be specific. Ambiguity here is what turns CoEs into bureaucracy.
4. **Funding model.** Who pays for the platform, who pays for consumption, and how the innovation pot is funded.
5. **Service catalogue.** What a business unit actually gets: intake, architecture review, model access, eval support, enablement, risk review, cost visibility.
6. **Metrics.** How the CoE itself is measured, and by whom.

Keep the charter to four pages. Get it signed by a sponsor with budget authority and the standing to resolve cross-functional disputes.

## 6.3 Decision rights table — the anti-bureaucracy device

| Decision | CoE approves | CoE advises | Business unit decides | Steering decides |
|---|---|---|---|---|
| Which model tier for a work class | ✔ | | | |
| New foundation model provider | | ✔ | | ✔ |
| Use case in a pre-approved pattern | | ✔ | ✔ | |
| Use case with Restricted data | ✔ | | | |
| Customer-facing autonomous agent | | ✔ | | ✔ |
| Vendor purchase under threshold | | ✔ | ✔ | |
| Vendor purchase over threshold | | ✔ | | ✔ |
| Budget increase within allocation | | | ✔ | |
| Budget increase beyond allocation | ✔ | | | |
| Production release of a Tier 1 risk system | ✔ | | | ✔ |

**Design principle: default-allow lanes.** Publish two or three pre-approved patterns (for example: internal RAG over Internal-class documents, using approved models through the gateway, with logging on). Anything matching a pattern needs registration, not approval. Everything else enters the gate process. Without default-allow lanes, the CoE becomes the bottleneck the brief is trying to avoid.

## 6.4 Roles

| Role | FTE at launch | Sourcing | Accountability |
|---|---|---|---|
| Executive sponsor | 0.1 | Existing exec | Budget, escalation, air cover |
| CoE lead | 1.0 | Hire or promote | Charter, portfolio, decisions |
| AI platform engineer | 1.0–2.0 | Existing platform team | Gateway, model access, observability |
| AI architect | 1.0 | Existing EA function | Patterns, reference architectures, reviews |
| Evaluation / quality lead | 0.5 | Data science or QA | Eval sets, quality gates, regression testing |
| AI FinOps analyst | 0.5 | Finance / FinOps | Truth layer, showback, forecast, commit management |
| Risk and compliance partner | 0.3 | Legal / Data Protection | Risk tiering, DPIAs, AI Act posture |
| Enablement lead | 0.5 | L&D or internal comms | Training, champions, adoption |
| Domain champions (spokes) | 0.2 × N | Business units | Use case ownership, adoption, value tracking |

A minimum viable CoE is four to six people at the hub plus named champions in the spokes. Larger than that at launch and you build an institution before you have proved a service.

## 6.5 Intake and stage gates

| Gate | Name | Entry criteria | Decision |
|---|---|---|---|
| G0 | Idea | One-paragraph description, named business owner | Register or decline |
| G1 | Qualified | Value hypothesis with a number, data classification, feasibility view, risk tier | Fund discovery or decline |
| G2 | Pilot approved | Success criteria, eval set defined, cost envelope, guardrails, DPIA if required | Approve pilot with expiry date |
| G3 | Production approved | Eval results, security review, cost per unit of work, run model, human-in-loop design, rollback plan | Approve production |
| G4 | Scaled | Adoption and value evidence, unit economics stable | Fund scaling |
| G5 | Review or retire | Quarterly value review | Continue, remediate or retire |

Two rules that keep the portfolio honest. Every pilot has an expiry date at G2 — pilots that neither fail nor scale are the most expensive thing in an AI portfolio. And G5 must be capable of retiring things; if nothing is ever retired, the gate is decorative.

## 6.6 Risk tiering

| Tier | Definition | Controls |
|---|---|---|
| T1 | Autonomous action affecting customers, money, safety or legal rights | Full review, DPIA, eval gate, human oversight design, incident runbook, steering approval, logging and monitoring, periodic re-validation |
| T2 | Customer-facing content or recommendations with human review | Eval gate, disclosure controls, brand review, monitoring, spot audit |
| T3 | Internal decision support | Registration, standard guardrails, sample review |
| T4 | Individual productivity within approved tools and data classes | Policy and training only |

Map the tiers to the regulatory obligations in Part 7. Most of a fashion brand's GenAI portfolio sits in T2–T4. The T1 cases are usually recruitment tools, credit or fraud decisions, and autonomous customer-facing agents.

## 6.7 Metrics for the CoE

| Category | Metric | Warning |
|---|---|---|
| Adoption | Activation rate, steady-user share, breadth of capability use | Do not report raw seat counts |
| Unit economics | Cost per unit of work by work class; trend | The number that proves governance works |
| Value | Realised benefit per production use case, graded by evidence quality | Force an evidence grade or this becomes fiction |
| Portfolio | Use cases by gate; time in gate; retirement rate | Time-in-gate is your bureaucracy detector |
| Quality | Eval pass rates, regression incidents, human-override rate | |
| Risk | Open findings by tier, exception count and ageing, incidents | Rising exception count means allocation is mis-sized |
| Platform | Availability, p95 latency, cache hit rate, failover events | |

## 6.8 First 90 / 180 / 365 days

**Days 0–90 — decide, do not build.** Charter, mandate, operating model, decision rights, sponsor, funding, initial risk tiering, first intake process, consumption truth layer live, seat reclamation running. Executive attention is at its maximum now and will never be this available again. Spend it on the organisational decisions, not the technology.

**Days 90–180 — platform and process.** Gateway in production. Observability and showback live. Routing matrix published and adopted. Eval harness operating for the top three work classes. First cohort of use cases through G2 and G3. Enablement programme running. Minimum viable governance, not complete governance.

**Days 180–365 — scale and prove.** Chargeback stage 3. Second landscape refresh. Agentic patterns in production with T1 controls. Value reporting to the executive team with graded evidence. CoE running its own quarterly review of the model portfolio using the triggers in 4.7.

Expect 12–18 months to a fully mature capability. Say that to the sponsor at the start. A CoE sold as a 90-day fix will be judged a failure at day 91.

---

# Part 7 — Risk, compliance and the fashion-specific overlay

This is where a generic AI strategy becomes an XYZ strategy. A consumer fashion brand carries exposures that a B2B software company does not.

## 7.1 The EU AI Act position as at August 2026 — verify before use

The timeline moved in 2026, and most compliance calendars are now wrong in both directions. Get this right in front of the client; it is a fast credibility win.

Regulation (EU) 2026/1744 — the "Digital Omnibus on AI" — was published in the Official Journal on 24 July 2026 and entered into force on 27 July 2026, days before the AI Act's original high-risk deadline.

| Date | Obligation | Status |
|---|---|---|
| Already in force | Prohibited practices; general-purpose AI model obligations; AI literacy duty (Art. 4) | Applies now |
| **2 August 2026** | **Article 50 transparency obligations** — disclose that users are interacting with an AI system; disclose AI-generated or manipulated content | **Applies now.** Not deferred. |
| 2 December 2026 | Article 50(2) marking requirements extended to systems already on the market at 2 Aug 2026; new prohibitions (including AI-generated non-consensual intimate imagery and CSAM) | Imminent |
| 2 December 2027 | High-risk obligations for standalone Annex III systems (recruitment, credit scoring, biometrics, education and similar) | Deferred from Aug 2026 |
| 2 August 2028 | High-risk obligations for AI embedded in regulated products (Annex I) | Deferred |

**What this means for XYZ specifically.**

1. **AI-generated marketing content must be disclosed.** A fashion brand generating campaign imagery, product imagery, video or synthetic models is squarely inside Article 50. Build the disclosure and provenance capability now, not in 2027. Content Credentials (C2PA) is the practical mechanism — it is embedded in the major creative tools and gives a machine-readable provenance trail.
2. **Customer-facing chat and voice agents must disclose they are AI.** Check every deployed assistant this quarter.
3. **Recruitment tooling is the likely Annex III exposure.** If HR uses AI screening, that is high-risk and the December 2027 clock is running. Start now; conformity work takes longer than people expect.
4. **The AI literacy duty already applies.** It is cheap to satisfy and easy to evidence. Fold it into the CoE enablement programme and record completion.
5. **The deferral is not a reason to slow down.** The obligations that create the most day-to-day work for a consumer brand — transparency, disclosure, provenance — were not deferred.

## 7.2 The wider regulatory and legal surface for a fashion brand

| Area | Exposure | Action |
|---|---|---|
| Data protection (GDPR and equivalents) | Customer data in prompts; employee monitoring via usage telemetry; automated decision-making | DPIAs; lawful basis for the WS1 identity join; data-flow map per model route |
| Likeness and model rights | Synthetic or digitally altered models; digital twins of real models | Explicit consent, scope, duration and compensation terms; check union and agency agreements |
| Advertising standards | AI-generated imagery that misrepresents fit, colour, material or body shape | Review process before publication; disclosure |
| Sustainability claims | Generated product copy asserting material or environmental claims | Claims must be traceable to source data. Generative copy is a greenwashing risk vector. |
| IP | Training-data provenance of image and video tools; ownership of outputs; brand asset leakage into third-party training | Contractual warranties and indemnities; check every creative tool's training terms |
| Product data | Digital product passport and equivalent regimes | Accuracy of generated product attributes matters legally, not just commercially |
| US state and sectoral law | Varies by state; hiring-tool audit rules in some jurisdictions | Map by operating footprint |
| Accessibility | AI-generated alt text, captions, voice interfaces | Quality gate, not an afterthought |

## 7.3 Security controls specific to GenAI

Fold these into the CoE control catalogue. Use OWASP's LLM and agentic-security material as the source checklist.

| Threat | Control |
|---|---|
| Prompt injection, direct and indirect | Input and output filtering; least-privilege tools; no implicit trust in retrieved content; human confirmation for consequential actions |
| Data exfiltration through agents | Egress controls; tool allow-lists; output scanning; blast-radius limits per agent |
| Secrets in prompts and logs | Redaction at the gateway; secret scanning; retention limits |
| Model or plugin supply chain (including MCP servers) | Registry of approved tools and servers; provenance checks; change review |
| Insecure AI-generated code reaching production | Mandatory review for AI-touched code; SAST/DAST in the pipeline; 30/60/90-day defect tracking on AI-touched changes |
| Over-permissioned service accounts | Scoped credentials per use case; virtual keys with budgets; rotation |
| Excessive agency | Explicit authority limits per agent; approval steps for irreversible actions |
| Shadow AI | Discovery (5.4); sanctioned easy path; amnesty rather than punishment |

## 7.4 Third-party and model risk

Add these to the vendor scorecard as gates, not scores: training on customer data · data residency and sub-processors · retention and deletion · model change and deprecation notice periods · incident notification terms · audit rights · exit and data export · indemnities for IP and output.

**Model change management is the underrated one.** Models are retired and replaced on vendor timetables. The 31 August 2026 Codex model retirement is a live example. Build a standing process: a register of every model in production use, the pinned version, the workflows that depend on it, and the owner who must act on a retirement notice.

---

# Part 8 — Templates

Short, usable versions. Expand in the working files.

## T1 — Data request register

| # | Item | Source system | Owner (client) | Requested | Due | Received | Quality | Blocker |
|---|---|---|---|---|---|---|---|---|

## T2 — Interview guide (consumption and use case)

1. What do you use AI tools for in a typical week? Walk me through one real example.
2. What did that work look like before?
3. What stops you using it more?
4. Have you ever hit a limit? What did you do?
5. What would you lose if it were withdrawn tomorrow?
6. What do you use that IT does not know about? *(ask late, no consequences)*
7. What would you tell leadership if they had to choose one tool?

Record verbatim. Code against the workload taxonomy. Ten to twenty interviews is enough for saturation in most organisations.

## T3 — Survey instrument (keep to 10 questions)

Frequency of use · capabilities used · work classes supported · perceived time saved (banded) · confidence in output quality · limits encountered · training received · tools used outside the sanctioned set (anonymous) · one thing that would help most (free text) · role and team (for segmentation only).

## T4 — Decision log

| ID | Date | Decision | Options considered | Rationale | Owner | Reversible? | Review date |
|---|---|---|---|---|---|---|---|

## T5 — Risk register

| ID | Risk | Category | Likelihood | Impact | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|

Seed it with these eight, which recur on every engagement of this type:

1. Renewal date arrives before the evidence base is complete.
2. Data access is granted late or partially.
3. Copilot trial data is unrecoverable.
4. Consumption data cannot be joined to identity for privacy or works-council reasons.
5. The 20–30% hypothesis is contradicted by data and its author objects.
6. Internal estate data from the client arrives late or incomplete.
7. A model retirement or pricing change invalidates part of the cost model mid-engagement.
8. Governance controls are perceived as surveillance and drive usage into shadow tools.

## T6 — Exception request form

Use case · requester and business owner · value estimate and basis · data classification · current allocation and requested increase · alternatives tested (including cheaper models) · guardrails in place · duration requested · approver · expiry date · review outcome.

## T7 — Steering paper format (two pages, always the same shape)

1. Decision required — one sentence
2. Recommendation — one paragraph
3. Evidence — three exhibits maximum
4. Options considered and why rejected
5. Risks and mitigations
6. What happens if we do nothing
7. Owner and date

## T8 — Weekly status (one page)

Progress against plan · decisions taken · decisions needed · risks changed this week · data blockers · next week's focus. Same shape every week. Never longer.

## T9 — Handover run-book contents

Data pipeline and refresh schedule · dashboard definitions and owners · rate card update procedure · monthly governance cycle checklist · exception process · eval set locations and re-run instructions · vendor contacts and contract dates · model retirement watch process · escalation paths · the decision log.

---

# Part 9 — Anti-patterns

Twelve ways this engagement fails. Read this list at the start of each phase.

1. **Boiling the ocean on the landscape.** Twelve domains scanned shallowly. Cap it at five deep.
2. **Reporting a baseline that does not reconcile to the invoice.** One challenged number destroys the credibility of all of them.
3. **Publishing individual usage league tables.** Corrupts the data and the relationship.
4. **Treating low usage as waste without diagnosis.** Three explanations, one conclusion. Test all three.
5. **Letting the vendor's forecast become your forecast.** Build your own.
6. **Recommending a platform position without a tested secondary.** An untested alternative is not an alternative.
7. **Quoting someone else's savings percentage as XYZ's.** Measure XYZ's own with a controlled comparison.
8. **Governance without an exception path.** Guarantees shadow usage.
9. **Jumping to chargeback in month one.** Drives spend out of sight.
10. **Answering the Copilot question with data only.** Half the problem was how the decision was made. Address that half explicitly.
11. **A CoE that approves everything.** Build default-allow lanes on day one, or the CoE becomes the queue it was created to remove.
12. **Leaving no run-book.** The engagement's value evaporates 60 days after you leave.

Add a thirteenth for this specific client: **conflating share of workload, share of developers and share of spend.** The 20–30% figure will be quoted back at you. Define which one you mean, every time.

---

# Part 10 — Twelve-week execution calendar

| Week | Workstream 1 | Workstream 2 | Workstream 3 | Cross |
|---|---|---|---|---|
| 0 | Data request issued; renewal date fixed; admin access requested | Copilot data export requested (urgent) | Taxonomy proposal drafted | Kickoff; principles agreed; RACI signed |
| 1 | Admin API connected; invoice reconciliation started | Trial record reconstructed | Scoping session: taxonomy confirmed | Steering 1: scope, criteria, weights |
| 2 | Truth layer v1; entitlement extract | Sentiment round launched | Estate register started; shadow discovery | Developer forum 1 |
| 3 | Segmentation v1; cohort thresholds calibrated | Workload taxonomy sized; diary study runs | Vendor longlist; RFI issued | Data clinic cadence established |
| 4 | **Baseline locked**; reconciliation published | Telemetry analysis; measurement framework applied | Shortlist; reference calls booked | Steering 2: baseline accepted |
| 5 | Use-case attribution; matrix drafted | Platform evaluation scoring; latency tests | Scorecards in progress | Security review of access architecture |
| 6 | Governance framework designed; gateway design agreed | Cost model built | Gap and duplication analysis | Developer forum 2: findings tested |
| 7 | Guardrails configured in a test workspace | Routing table drafted; 20–30% hypothesis result | Heat map drafted | Steering 3: D2 direction agreed |
| 8 | Forecast scenarios; BATNA costed | Directional note drafted | Blueprint drafted | Procurement working session |
| 9 | **Negotiation brief drafted** | Recommendation finalised | Build/buy/partner calls made | Legal and Data Protection review |
| 10 | Brief approved; guardrails enforced in production | Directional note issued | Blueprint issued | Steering 4: D1 and D3 taken |
| 11 | First monthly governance cycle run by client staff | Eval sets handed over | Roadmap sequenced and funded | CoE charter signed |
| 12 | Run-book handover; showback live | Model watch process live | Refresh cadence set | Closeout; lessons learned; value statement |

Adjust the calendar to the renewal date, not the other way round. If the renewal is inside 12 weeks, run WS1 at double pace and defer WS3 depth to a second phase — but tell the client that trade-off explicitly, in writing, in week 0.

---

# Part 11 — Making this a reference engagement

The brief says this is an opportunity to prove the firm as a reliable partner in AI projects. Reliability is demonstrated by specific, checkable behaviours. These are the ones that register with clients.

1. **Reconcile to the invoice and say so.** Most consumption analyses do not. Publishing a 1.4% variance and explaining it buys more credibility than any slide.
2. **Publish confidence, not just numbers.** Ranges, evidence grades, and a stated list of what you could not find out.
3. **Hand over reproducible artefacts.** The cost model with no hard-coded numbers. The eval sets. The dashboard definitions. The run-book. A client who can re-run your analysis in six months will call you back.
4. **Report the finding that costs you scope.** If the data says the Copilot hypothesis was wrong, or that governance tooling XYZ already owns is sufficient, say it. This is the single strongest trust signal available in a consulting engagement.
5. **Deliver something in week 1.** The model retirement warning in 2.8 is a live example. Small, unasked-for, immediately useful.
6. **Design for your own absence.** Every control has a named client owner before you leave, and 30 days of the client running it while you are still there to watch.
7. **Write for the reader, not for the record.** Short sentences. One idea each. The recommendation in the first paragraph.

## Closing note to the EA

Three things will determine whether this engagement succeeds, and none of them is analytical sophistication.

**Get the data early.** Every week of delayed access compresses analysis at the far end, where the thinking is worth most.

**Handle the Copilot question with more care than it appears to deserve.** It is presented as one input to a technical recommendation. It is actually the trust context in which every other recommendation will be received. Get it right and the rest of the engagement is easier. Get it wrong and correct analysis will be rejected on political grounds.

**Do not confuse the deliverables with the outcome.** Eleven artefacts is the contract. Three decisions, defensibly made and durably operated, is the job.
