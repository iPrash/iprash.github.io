# Resource Library for the Lead Enterprise Architect
## XYZ Corp AI Consumption, Multi-Model Access and GenAI Landscape engagement

**Compiled:** 17 August 2026

**How to use this list.** It is ordered by when you will need it, not by topic importance. Section 0 is the two-week study sprint to run before and during mobilisation. Sections 1–10 are working references you return to. Section 11 is the background reading that makes you better at the next engagement rather than this one.

**Link discipline.** Where a URL is given it was current at compilation. Where only a domain is given, navigate from there — deep links on these sites change often. Never paste a figure from a secondary source into a client deliverable without opening the primary source and checking the date.

**Source grading used throughout:**
**[P]** primary — vendor documentation, regulation, standard, official research  
**[S]** credible secondary — analyst, practitioner research, established publication  
**[C]** commentary — useful for framing, verify every fact

---

# 0. Two-week study sprint

Run this in parallel with mobilisation. Roughly 25–30 hours.

| Days | Focus | Read / do |
|---|---|---|
| 1–2 | The commercial mechanics you are about to negotiate | OpenAI Admin, Usage and Cost API docs (§1); OpenAI enterprise credits and spend-control help pages (§1); OpenAI Service Credit Terms (§1) |
| 3 | The competitor's mechanics | GitHub Copilot usage-based billing announcement and plans page; Copilot budget and allowance docs (§2) |
| 4 | The alternative access route | AWS Bedrock pricing page and user guide; billing modes; data protection page (§3) |
| 5–6 | The financial discipline | FinOps Framework 2026 overview; FinOps for AI working-group output; FOCUS specification; State of FinOps 2026 (§4) |
| 7 | The regulation that bites now | AI Act text Articles 4, 5 and 50; Digital Omnibus analysis; C2PA overview (§5) |
| 8 | The security control set | OWASP GenAI security material; MITRE ATLAS; agentic threat guidance (§6) |
| 9 | Measuring the thing everyone argues about | DORA research; SPACE framework paper; the 2025–26 AI productivity-paradox analyses (§7) |
| 10 | The architecture you will recommend | AI gateway comparisons; LiteLLM and Portkey docs; reference architectures (§8) |
| 11 | The capability you must build | AI CoE operating-model material; charter and decision-rights patterns (§9) |
| 12 | The client's industry | Fashion and retail GenAI adoption material; provenance and likeness issues (§10) |
| 13–14 | Synthesis | Draft the workload taxonomy, the evaluation criteria and the data request from what you have read |

Set one rule for the sprint: for every claim you plan to use in a client deliverable, note the primary source and the date you checked it. Build that habit now and the credibility of the engagement follows.

---

# 1. OpenAI platform — consumption, administration, commercial

**Do not build the consumption baseline before you have read all of section 1.**

| Resource | Grade | Why |
|---|---|---|
| OpenAI API reference — overview | [P] | https://developers.openai.com/api/reference/overview |
| Admin APIs guide — users, projects, keys, spend limits, audit logs, model permissions | [P] | https://developers.openai.com/api/docs/guides/admin-apis — the mechanics of entitlement analysis and guardrails |
| Costs endpoint reference (`/v1/organization/costs`) | [P] | https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/usage/methods/costs — note grouping by project and line item |
| OpenAI Cookbook — using the Usage and Cost APIs | [P] | https://cookbook.openai.com/examples/completions_usage_api — working code you can adapt in an afternoon |
| Flexible pricing for Enterprise, Edu and Business plans | [P] | https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans — the shared credit pool model that underpins your allocation design |
| Manage usage limits and overages (Enterprise / Edu) | [P] | https://help.openai.com/en/articles/20001001-manage-usage-limits-and-overages-in-chatgpt-enterprise-and-edu — group limits, user overrides, monthly migration |
| Managing credits and spend controls (Business) | [P] | https://help.openai.com/en/articles/20001155-managing-credits-and-spend-controls-in-chatgpt-business |
| Codex rate card | [P] | https://help.openai.com/en/articles/20001106-codex-rate-card — token-aligned credit rates; model retirement notices |
| Using Codex with your ChatGPT plan | [P] | https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan |
| Announcement — enterprise usage analytics and spend controls (June 2026) | [P] | https://openai.com/index/chatgpt-enterprise-spend-controls/ |
| OpenAI Service Credit Terms | [P] | https://openai.com/policies/service-credit-terms/ — read before you negotiate rollover |
| OpenAI enterprise privacy commitments | [P] | https://openai.com/enterprise-privacy/ — the baseline your data redlines start from |
| API pricing | [P] | https://openai.com/api/pricing/ and https://platform.openai.com/docs/pricing |

**Negotiation-specific (buyer-side, commercially motivated — read critically):**

| Resource | Grade | Note |
|---|---|---|
| Redress Compliance — OpenAI enterprise procurement negotiation playbook | [C] | https://redresscompliance.com/openai-enterprise-procurement-negotiation-playbook — useful on consumption-forecast error and commit structure |
| Redress Compliance — enterprise guide to negotiating OpenAI contracts | [C] | https://redresscompliance.com/the-enterprise-guide-to-negotiating-openai-contracts.html — clause-level checklists |
| Redress Compliance — enterprise AI credits pricing compared (2026) | [C] | https://redresscompliance.com/enterprise-ai-credits-pricing-compared-pillar-2026 — normalising credit currencies across vendors |

These three are advisory-firm marketing. The clause checklists are genuinely useful. The percentages are not evidence. Use the structure, source the numbers yourself.

---

# 2. GitHub Copilot — the Workstream 2 counterparty

| Resource | Grade | Why |
|---|---|---|
| GitHub blog — Copilot moving to usage-based billing (effective 1 June 2026) | [P] | https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/ — the single most important document for the multi-model cost argument |
| Copilot plans and pricing | [P] | https://github.com/features/copilot/plans |
| Copilot billing concepts | [P] | https://docs.github.com/en/copilot/concepts/billing/copilot-requests |
| Managing request allowances and budgets | [P] | https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/manage-and-track-spending/manage-request-allowances |
| Copilot documentation root (metrics, admin, policies) | [P] | https://docs.github.com/en/copilot |
| CloudZero — what teams actually pay for Copilot in 2026 | [S] | https://www.cloudzero.com/blog/github-copilot-cost/ — good on the credit-model transition |

**Action:** export XYZ's historic Copilot billing and metrics data in week 0. See playbook §2.8.

---

# 3. AWS Bedrock and alternative access routes

| Resource | Grade | Why |
|---|---|---|
| Amazon Bedrock pricing | [P] | https://aws.amazon.com/bedrock/pricing/ — on-demand, batch, provisioned throughput; the only rate card you should quote |
| Amazon Bedrock documentation | [P] | https://docs.aws.amazon.com/bedrock/ — model availability by region, cross-region inference, guardrails, knowledge bases, agents |
| Bedrock data protection and privacy | [P] | https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html — the core of the residency argument |
| AWS Well-Architected — generative AI guidance | [P] | https://aws.amazon.com/architecture/well-architected/ — navigate to the generative AI lens |
| Azure OpenAI Service documentation | [P] | https://learn.microsoft.com/azure/ai-services/openai/ — the third access route; check if XYZ has Azure commitments that AI spend could draw down |
| Microsoft Cloud Adoption Framework — AI scenario | [P] | https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/ — operating-model guidance, useful even in a non-Azure estate |
| Anthropic documentation | [P] | https://docs.claude.com — for the secondary-model position |
| CloudZero — Bedrock pricing analysis | [S] | https://www.cloudzero.com/blog/amazon-bedrock-pricing/ — good on adjacent charges that break estimates |
| Artificial Analysis | [S] | https://artificialanalysis.ai/ — independent, continuously updated model comparison on quality, price, latency and throughput. The fastest route to a defensible route-comparison table. |
| LMArena | [S] | https://lmarena.ai/ — comparative preference data; use as one input, never alone |
| Stanford HELM | [P] | https://crfm.stanford.edu/helm/ — rigorous, slower-moving benchmark suite |

---

# 4. FinOps, cost governance and unit economics

| Resource | Grade | Why |
|---|---|---|
| FinOps Framework | [P] | https://www.finops.org/framework/ — domains, capabilities, personas, maturity |
| FinOps Framework 2026 update | [P] | https://www.finops.org/insights/2026-finops-framework/ — Scopes, Technology Categories, Executive Strategy Alignment |
| FinOps for AI — working group overview | [P] | https://www.finops.org/wg/finops-for-ai-overview/ — token economics, KPIs, crawl/walk/run, AI scope mapping. Read this before designing the governance framework. |
| State of FinOps 2026 data | [P] | https://data.finops.org/ — 98% of FinOps practices now manage AI spend; use for the "this is standard practice" argument |
| FOCUS — FinOps Open Cost and Usage Specification | [P] | https://focus.finops.org/ — the normalisation schema for multi-provider cost data. Adopt its field names in your truth layer and the client inherits an industry-standard model. |
| FinOps Foundation asset library and KPI list | [P] | https://www.finops.org/ — templates for showback, allocation and unit economics |

**Key idea to carry into the framework design:** the 2026 framework explicitly says an innovation-focused AI scope should tolerate more waste and run at a faster cadence than steady-state scopes. Design two different control regimes, not one.

---

# 5. Regulation, standards and assurance

## 5.1 EU AI Act

| Resource | Grade | Why |
|---|---|---|
| Regulation (EU) 2024/1689 — AI Act, consolidated text | [P] | https://eur-lex.europa.eu/eli/reg/2024/1689/oj — read Articles 4, 5 and 50 in full |
| Regulation (EU) 2026/1744 — Digital Omnibus on AI | [P] | Search EUR-Lex for 2026/1744. Published 24 July 2026, in force 27 July 2026. |
| AI Act Explorer | [S] | https://artificialintelligenceact.eu/ — navigable article-by-article version with timelines |
| European Commission — AI Office and AI Act policy | [P] | https://digital-strategy.ec.europa.eu/en/policies/ai-office |
| Gibson Dunn — Omnibus analysis | [S] | https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ — clear on what moved and what did not |
| Cloud Security Alliance — research note on the high-risk deferral | [S] | https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-high-risk-deadline-omnibus-20260/ |
| CEN-CENELEC JTC 21 | [P] | https://www.cencenelec.eu/areas-of-work/cen-cenelec-topics/artificial-intelligence/ — the harmonised standards that will define conformity |

## 5.2 Management systems and risk frameworks

| Resource | Grade | Why |
|---|---|---|
| ISO/IEC 42001:2023 — AI management systems | [P] | https://www.iso.org — search "ISO/IEC 42001". The certifiable management-system spine for the CoE. Also ask every shortlisted vendor whether they hold it. |
| ISO/IEC 23894 — AI risk management guidance | [P] | https://www.iso.org — complements 42001 |
| NIST AI Risk Management Framework | [P] | https://www.nist.gov/itl/ai-risk-management-framework — Govern, Map, Measure, Manage |
| NIST Generative AI Profile (NIST AI 600-1) | [P] | https://airc.nist.gov/ — GenAI-specific control mapping. The most directly usable control catalogue source for your framework. |
| NIST AI Resource Center — playbook and crosswalks | [P] | https://airc.nist.gov/ — crosswalks between NIST, ISO and EU AI Act save weeks |
| UK ICO — AI and data protection guidance | [P] | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/ — practical on DPIAs and employee monitoring |
| EDPB opinions and guidelines | [P] | https://www.edpb.europa.eu/ — including AI-model-related opinions |
| OECD AI Policy Observatory | [P] | https://oecd.ai/ — multi-jurisdiction tracking for XYZ's operating footprint |

## 5.3 Content provenance and disclosure

| Resource | Grade | Why |
|---|---|---|
| C2PA — Coalition for Content Provenance and Authenticity | [P] | https://c2pa.org/ — the technical standard behind AI content disclosure |
| Content Authenticity Initiative | [P] | https://contentauthenticity.org/ — implementation guidance and tooling |

For a fashion brand generating campaign imagery, sections 5.1 and 5.3 together are the compliance core. Article 50 applies now.

---

# 6. Security for GenAI and agents

| Resource | Grade | Why |
|---|---|---|
| OWASP GenAI Security Project (incl. Top 10 for LLM Applications) | [P] | https://genai.owasp.org/ — the standard engineering checklist; also covers agentic threats and mitigations |
| MITRE ATLAS | [P] | https://atlas.mitre.org/ — adversary tactics and techniques against AI systems |
| Cloud Security Alliance — AI research | [P] | https://cloudsecurityalliance.org/research/topics/artificial-intelligence — AI controls matrix and audit material |
| Model Context Protocol specification | [P] | https://modelcontextprotocol.io/ — read before approving any MCP server; it is a supply-chain surface |
| AI Incident Database | [S] | https://incidentdatabase.ai/ — real failure modes. Use two or three to make risk tiering concrete for executives. |
| NCSC guidance on secure AI system development | [P] | https://www.ncsc.gov.uk/ — search "secure AI system development" |

---

# 7. Measuring engineering impact (Workstream 2 evidence base)

| Resource | Grade | Why |
|---|---|---|
| DORA — research and reports | [P] | https://dora.dev/ — the four delivery metrics and the annual research including AI-specific findings |
| SPACE framework — original paper | [P] | https://queue.acm.org/detail.cfm?id=3454124 — Satisfaction, Performance, Activity, Communication, Efficiency. The framework for the developer-experience lens. |
| DX — DORA metrics in the AI era | [S] | https://getdx.com/blog/dora-metrics/ — how the metrics distort under AI adoption |
| Faros AI — the AI productivity paradox | [S] | https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025 — individual output up sharply, organisational delivery flat |
| METR — developer productivity research | [P] | https://metr.org/ — includes the finding that developers systematically misestimate their own AI-assisted speed. Cite this when sentiment and telemetry disagree. |
| Public-sector Copilot pilot using DORA and SPACE | [P] | https://arxiv.org/pdf/2409.17434 — a rare published evaluation design you can adapt directly for the trial post-mortem |

**Use these to protect yourself.** When someone quotes a single productivity percentage at you, this section is why you ask which metric, at which level, over what period.

---

# 8. Model access architecture, gateways, evaluation and observability

## 8.1 Gateways

| Resource | Grade | Why |
|---|---|---|
| LiteLLM documentation | [P] | https://docs.litellm.ai/ — virtual keys, per-team budgets, provider coverage. The open-source reference implementation. |
| LiteLLM repository | [P] | https://github.com/BerriAI/litellm |
| Portkey documentation | [P] | https://portkey.ai/docs — managed gateway with caching and guardrails |
| Kong AI Gateway | [P] | https://konghq.com/products/kong-ai-gateway — if XYZ already runs Kong |
| TrueFoundry — 2026 AI gateway landscape comparison | [C] | https://www.truefoundry.com/blog/a-definitive-guide-to-ai-gateways-in-2026-competitive-landscape-comparison — vendor-authored; useful for the criteria list, not the ranking |

## 8.2 Evaluation

| Resource | Grade | Why |
|---|---|---|
| OpenAI Evals | [P] | https://github.com/openai/evals |
| promptfoo | [P] | https://www.promptfoo.dev/ — the fastest way to stand up a comparison harness across models |
| Ragas | [P] | https://docs.ragas.io/ — retrieval-augmented generation evaluation |
| LangSmith | [P] | https://docs.smith.langchain.com/ — tracing and evaluation |

Build the eval sets during the engagement and hand them over. They are the asset that lets XYZ re-decide when the next model ships.

## 8.3 Observability and cost attribution

| Resource | Grade | Why |
|---|---|---|
| Langfuse | [P] | https://langfuse.com/docs — open-source LLM observability with cost tracking |
| Helicone | [P] | https://www.helicone.ai/ — lightweight proxy-based observability |
| OpenTelemetry GenAI semantic conventions | [P] | https://opentelemetry.io/ — search "gen-ai semantic conventions". Adopt these attribute names so telemetry stays portable. |

---

# 9. Building and running the CoE

| Resource | Grade | Why |
|---|---|---|
| Microsoft Cloud Adoption Framework — AI adoption and governance | [P] | https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/ — the most complete free operating-model reference |
| AWS Cloud Adoption Framework for AI, ML and generative AI | [P] | https://aws.amazon.com/cloud-adoption-framework/ — perspectives, capabilities, maturity |
| Google Cloud AI Adoption Framework | [P] | https://cloud.google.com/ — search "AI adoption framework" |
| MIT Sloan Management Review — AI and business strategy | [S] | https://sloanreview.mit.edu/big-ideas/artificial-intelligence-business-strategy/ — governance and organisational research rather than vendor material |
| McKinsey — State of AI | [S] | https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai — adoption benchmarks for the "are we behind?" question |
| Harvard Program on Negotiation | [S] | https://www.pon.harvard.edu/ — BATNA, anchoring, concession structure. Read before drafting the negotiation brief. |
| ClarityArc — AI CoE design (2026) | [C] | https://www.clarityarc.com/insights/ai-centre-of-excellence-design — practical on the 90/180-day sequencing and the acceleration-versus-blocking tension |
| Trantor — building an AI CoE (2026) | [C] | https://www.trantorinc.com/blog/how-to-build-an-ai-center-of-excellence-team-budget-and-kpis — charter contents and operating-model trade-offs |

The last two are consultancy content. Use them for structure and checklists. The charter you write should be XYZ's, built from Part 6 of the playbook.

---

# 10. Retail, fashion and the client's market

| Resource | Grade | Why |
|---|---|---|
| McKinsey — State of Fashion (with Business of Fashion) | [S] | https://www.mckinsey.com/industries/retail/our-insights/state-of-fashion — the annual reference every fashion executive has read. Know what it says about AI this year. |
| Business of Fashion — technology coverage | [S] | https://www.businessoffashion.com/ |
| Vogue Business — technology | [S] | https://www.voguebusiness.com/technology — practical coverage of brand-side AI deployments including synthetic imagery and model likeness |
| National Retail Federation | [S] | https://nrf.com/ — retail technology adoption research and the annual Big Show agenda as a landscape signal |
| Adobe / Salesforce / Shopify commerce insight reports | [S] | Vendor research, but the traffic and conversion data on AI-referred shopping is not available elsewhere |
| EU Ecodesign for Sustainable Products Regulation and Digital Product Passport | [P] | https://commission.europa.eu/ — search "ecodesign sustainable products regulation". Relevant because generated product data becomes regulated product data. |

**Watch-out for the landscape map:** the fashion GenAI vendor space contains many thin application layers over a small number of foundation models. Apply the model-dependency criterion in playbook §5.2 to every vendor you score.

---

# 11. Deeper background — makes you better at the next one

**Books**

| Title | Author | Why |
|---|---|---|
| *Accelerate* | Forsgren, Humble, Kim | The research basis for DORA. Read it before you argue about developer productivity. |
| *Team Topologies* | Skelton, Pais | The vocabulary for hub-and-spoke, platform teams and cognitive load — directly applicable to CoE design |
| *Cloud FinOps* | Storment, Fuller | The discipline your token governance framework is an instance of |
| *Getting to Yes* | Fisher, Ury, Patton | BATNA and principled negotiation, in the original |
| *Good Strategy / Bad Strategy* | Rumelt | The test for whether your directional guidance note is a strategy or a list of aspirations |
| *The Goal* / *The Phoenix Project* | Goldratt / Kim et al. | Constraint thinking — why individual AI speedups do not become organisational throughput |
| *On Writing Well* | Zinsser | Simplicity, brevity, clarity, humanity. Your deliverables are read by tired people. |

**Standing sources to follow during the engagement**

- OpenAI, Anthropic, Google and AWS changelogs and release notes — subscribe to all of them; model retirements arrive here first
- The FinOps Foundation blog and community calls
- DORA and DX research publications
- EU AI Act implementation trackers
- Gartner and Forrester, if XYZ holds subscriptions — use the inquiry hours, they are usually unspent

**Certifications worth holding (not required for this engagement)**

- FinOps Certified Practitioner — https://learn.finops.org/
- ISO/IEC 42001 lead implementer or auditor — for CoE assurance credibility
- Cloud provider AI practitioner or specialty certifications — for the access-route conversations

---

# 12. Fast-reference checklist

Before each major deliverable ships, confirm:

- [ ] Every figure has a primary source and a date checked
- [ ] The baseline reconciles to the invoice and the variance is stated
- [ ] Evidence grades are shown, and the grade distribution is visible
- [ ] Confidence ranges replace point estimates wherever the data does not support precision
- [ ] What you could not find out is stated explicitly
- [ ] Every recommendation has an owner, a date and a revisit trigger
- [ ] No individual-level usage data appears in any published artefact
- [ ] Legal and Data Protection have seen anything touching disclosure, residency or employee monitoring
- [ ] The recommendation appears in the first paragraph
- [ ] A client staff member can re-run the analysis from the run-book
