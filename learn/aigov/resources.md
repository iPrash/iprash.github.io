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

| Resource | Grade | Note |
|---|---|---|
| [OpenAI API reference — overview](<https://developers.openai.com/api/reference/overview>) | [P] |  |
| [Admin APIs guide — users, projects, keys, spend limits, audit logs, model permissions](<https://developers.openai.com/api/docs/guides/admin-apis>) | [P] | the mechanics of entitlement analysis and guardrails |
| [Costs endpoint reference (`/v1/organization/costs`)](<https://developers.openai.com/api/reference/resources/admin/subresources/organization/subresources/usage/methods/costs>) | [P] | note grouping by project and line item |
| [OpenAI Cookbook — using the Usage and Cost APIs](<https://cookbook.openai.com/examples/completions_usage_api>) | [P] | working code you can adapt in an afternoon |
| [Flexible pricing for Enterprise, Edu and Business plans](<https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans>) | [P] | the shared credit pool model that underpins your allocation design |
| [Manage usage limits and overages (Enterprise / Edu)](<https://help.openai.com/en/articles/20001001-manage-usage-limits-and-overages-in-chatgpt-enterprise-and-edu>) | [P] | group limits, user overrides, monthly migration |
| [Managing credits and spend controls (Business)](<https://help.openai.com/en/articles/20001155-managing-credits-and-spend-controls-in-chatgpt-business>) | [P] |  |
| [Codex rate card](<https://help.openai.com/en/articles/20001106-codex-rate-card>) | [P] | token-aligned credit rates; model retirement notices |
| [Using Codex with your ChatGPT plan](<https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan>) | [P] |  |
| [Announcement — enterprise usage analytics and spend controls (June 2026)](<https://openai.com/index/chatgpt-enterprise-spend-controls/>) | [P] |  |
| [OpenAI Service Credit Terms](<https://openai.com/policies/service-credit-terms/>) | [P] | read before you negotiate rollover |
| [OpenAI enterprise privacy commitments](<https://openai.com/enterprise-privacy/>) | [P] | the baseline your data redlines start from |
| [API pricing](<https://openai.com/api/pricing/>) | [P] | Also the [platform pricing docs](<https://platform.openai.com/docs/pricing>) |

**Negotiation-specific (buyer-side, commercially motivated — read critically):**

| Resource | Grade | Note |
|---|---|---|
| [Redress Compliance — OpenAI enterprise procurement negotiation playbook](<https://redresscompliance.com/openai-enterprise-procurement-negotiation-playbook>) | [C] | useful on consumption-forecast error and commit structure |
| [Redress Compliance — enterprise guide to negotiating OpenAI contracts](<https://redresscompliance.com/the-enterprise-guide-to-negotiating-openai-contracts.html>) | [C] | clause-level checklists |
| [Redress Compliance — enterprise AI credits pricing compared (2026)](<https://redresscompliance.com/enterprise-ai-credits-pricing-compared-pillar-2026>) | [C] | normalising credit currencies across vendors |

These three are advisory-firm marketing. The clause checklists are genuinely useful. The percentages are not evidence. Use the structure, source the numbers yourself.

---

# 2. GitHub Copilot — the Workstream 2 counterparty

| Resource | Grade | Note |
|---|---|---|
| [GitHub blog — Copilot moving to usage-based billing (effective 1 June 2026)](<https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/>) | [P] | the single most important document for the multi-model cost argument |
| [Copilot plans and pricing](<https://github.com/features/copilot/plans>) | [P] |  |
| [Copilot billing concepts](<https://docs.github.com/en/copilot/concepts/billing/copilot-requests>) | [P] |  |
| [Managing request allowances and budgets](<https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/manage-and-track-spending/manage-request-allowances>) | [P] |  |
| [Copilot documentation root (metrics, admin, policies)](<https://docs.github.com/en/copilot>) | [P] |  |
| [CloudZero — what teams actually pay for Copilot in 2026](<https://www.cloudzero.com/blog/github-copilot-cost/>) | [S] | good on the credit-model transition |

**Action:** export XYZ's historic Copilot billing and metrics data in week 0. See playbook §2.8.

---

# 3. AWS Bedrock and alternative access routes

| Resource | Grade | Note |
|---|---|---|
| [Amazon Bedrock pricing](<https://aws.amazon.com/bedrock/pricing/>) | [P] | on-demand, batch, provisioned throughput; the only rate card you should quote |
| [Amazon Bedrock documentation](<https://docs.aws.amazon.com/bedrock/>) | [P] | model availability by region, cross-region inference, guardrails, knowledge bases, agents |
| [Bedrock data protection and privacy](<https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html>) | [P] | the core of the residency argument |
| [AWS Well-Architected — generative AI guidance](<https://aws.amazon.com/architecture/well-architected/>) | [P] | navigate to the generative AI lens |
| [Azure OpenAI Service documentation](<https://learn.microsoft.com/azure/ai-services/openai/>) | [P] | the third access route; check if XYZ has Azure commitments that AI spend could draw down |
| [Microsoft Cloud Adoption Framework — AI scenario](<https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/>) | [P] | operating-model guidance, useful even in a non-Azure estate |
| [Anthropic documentation](<https://docs.claude.com>) | [P] | for the secondary-model position |
| [CloudZero — Bedrock pricing analysis](<https://www.cloudzero.com/blog/amazon-bedrock-pricing/>) | [S] | good on adjacent charges that break estimates |
| [Artificial Analysis](<https://artificialanalysis.ai/>) | [S] | independent, continuously updated model comparison on quality, price, latency and throughput. The fastest route to a defensible route-comparison table. |
| [LMArena](<https://lmarena.ai/>) | [S] | comparative preference data; use as one input, never alone |
| [Stanford HELM](<https://crfm.stanford.edu/helm/>) | [P] | rigorous, slower-moving benchmark suite |

---

# 4. FinOps, cost governance and unit economics

| Resource | Grade | Note |
|---|---|---|
| [FinOps Framework](<https://www.finops.org/framework/>) | [P] | domains, capabilities, personas, maturity |
| [FinOps Framework 2026 update](<https://www.finops.org/insights/2026-finops-framework/>) | [P] | Scopes, Technology Categories, Executive Strategy Alignment |
| [FinOps for AI — working group overview](<https://www.finops.org/wg/finops-for-ai-overview/>) | [P] | token economics, KPIs, crawl/walk/run, AI scope mapping. Read this before designing the governance framework. |
| [State of FinOps 2026 data](<https://data.finops.org/>) | [P] | 98% of FinOps practices now manage AI spend; use for the "this is standard practice" argument |
| [FOCUS — FinOps Open Cost and Usage Specification](<https://focus.finops.org/>) | [P] | the normalisation schema for multi-provider cost data. Adopt its field names in your truth layer and the client inherits an industry-standard model. |
| [FinOps Foundation asset library and KPI list](<https://www.finops.org/>) | [P] | templates for showback, allocation and unit economics |

**Key idea to carry into the framework design:** the 2026 framework explicitly says an innovation-focused AI scope should tolerate more waste and run at a faster cadence than steady-state scopes. Design two different control regimes, not one.

---

# 5. Regulation, standards and assurance

## 5.1 EU AI Act

| Resource | Grade | Note |
|---|---|---|
| [Regulation (EU) 2024/1689 — AI Act, consolidated text](<https://eur-lex.europa.eu/eli/reg/2024/1689/oj>) | [P] | read Articles 4, 5 and 50 in full |
| Regulation (EU) 2026/1744 — Digital Omnibus on AI | [P] | Search EUR-Lex for 2026/1744. Published 24 July 2026, in force 27 July 2026. |
| [AI Act Explorer](<https://artificialintelligenceact.eu/>) | [S] | navigable article-by-article version with timelines |
| [European Commission — AI Office and AI Act policy](<https://digital-strategy.ec.europa.eu/en/policies/ai-office>) | [P] |  |
| [Gibson Dunn — Omnibus analysis](<https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/>) | [S] | clear on what moved and what did not |
| [Cloud Security Alliance — research note on the high-risk deferral](<https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-high-risk-deadline-omnibus-20260/>) | [S] |  |
| [CEN-CENELEC JTC 21](<https://www.cencenelec.eu/areas-of-work/cen-cenelec-topics/artificial-intelligence/>) | [P] | the harmonised standards that will define conformity |

## 5.2 Management systems and risk frameworks

| Resource | Grade | Note |
|---|---|---|
| [ISO/IEC 42001:2023 — AI management systems](<https://www.iso.org>) | [P] | search "ISO/IEC 42001". The certifiable management-system spine for the CoE. Also ask every shortlisted vendor whether they hold it. |
| [ISO/IEC 23894 — AI risk management guidance](<https://www.iso.org>) | [P] | complements 42001 |
| [NIST AI Risk Management Framework](<https://www.nist.gov/itl/ai-risk-management-framework>) | [P] | Govern, Map, Measure, Manage |
| [NIST Generative AI Profile (NIST AI 600-1)](<https://airc.nist.gov/>) | [P] | GenAI-specific control mapping. The most directly usable control catalogue source for your framework. |
| [NIST AI Resource Center — playbook and crosswalks](<https://airc.nist.gov/>) | [P] | crosswalks between NIST, ISO and EU AI Act save weeks |
| [UK ICO — AI and data protection guidance](<https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/>) | [P] | practical on DPIAs and employee monitoring |
| [EDPB opinions and guidelines](<https://www.edpb.europa.eu/>) | [P] | including AI-model-related opinions |
| [OECD AI Policy Observatory](<https://oecd.ai/>) | [P] | multi-jurisdiction tracking for XYZ's operating footprint |

## 5.3 Content provenance and disclosure

| Resource | Grade | Note |
|---|---|---|
| [C2PA — Coalition for Content Provenance and Authenticity](<https://c2pa.org/>) | [P] | the technical standard behind AI content disclosure |
| [Content Authenticity Initiative](<https://contentauthenticity.org/>) | [P] | implementation guidance and tooling |

For a fashion brand generating campaign imagery, sections 5.1 and 5.3 together are the compliance core. Article 50 applies now.

---

# 6. Security for GenAI and agents

| Resource | Grade | Note |
|---|---|---|
| [OWASP GenAI Security Project (incl. Top 10 for LLM Applications)](<https://genai.owasp.org/>) | [P] | the standard engineering checklist; also covers agentic threats and mitigations |
| [MITRE ATLAS](<https://atlas.mitre.org/>) | [P] | adversary tactics and techniques against AI systems |
| [Cloud Security Alliance — AI research](<https://cloudsecurityalliance.org/research/topics/artificial-intelligence>) | [P] | AI controls matrix and audit material |
| [Model Context Protocol specification](<https://modelcontextprotocol.io/>) | [P] | read before approving any MCP server; it is a supply-chain surface |
| [AI Incident Database](<https://incidentdatabase.ai/>) | [S] | real failure modes. Use two or three to make risk tiering concrete for executives. |
| [NCSC guidance on secure AI system development](<https://www.ncsc.gov.uk/>) | [P] | search "secure AI system development" |

---

# 7. Measuring engineering impact (Workstream 2 evidence base)

| Resource | Grade | Note |
|---|---|---|
| [DORA — research and reports](<https://dora.dev/>) | [P] | the four delivery metrics and the annual research including AI-specific findings |
| [SPACE framework — original paper](<https://queue.acm.org/detail.cfm?id=3454124>) | [P] | Satisfaction, Performance, Activity, Communication, Efficiency. The framework for the developer-experience lens. |
| [DX — DORA metrics in the AI era](<https://getdx.com/blog/dora-metrics/>) | [S] | how the metrics distort under AI adoption |
| [Faros AI — the AI productivity paradox](<https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025>) | [S] | individual output up sharply, organisational delivery flat |
| [METR — developer productivity research](<https://metr.org/>) | [P] | includes the finding that developers systematically misestimate their own AI-assisted speed. Cite this when sentiment and telemetry disagree. |
| [Public-sector Copilot pilot using DORA and SPACE](<https://arxiv.org/pdf/2409.17434>) | [P] | a rare published evaluation design you can adapt directly for the trial post-mortem |

**Use these to protect yourself.** When someone quotes a single productivity percentage at you, this section is why you ask which metric, at which level, over what period.

---

# 8. Model access architecture, gateways, evaluation and observability

## 8.1 Gateways

| Resource | Grade | Note |
|---|---|---|
| [LiteLLM documentation](<https://docs.litellm.ai/>) | [P] | virtual keys, per-team budgets, provider coverage. The open-source reference implementation. |
| [LiteLLM repository](<https://github.com/BerriAI/litellm>) | [P] |  |
| [Portkey documentation](<https://portkey.ai/docs>) | [P] | managed gateway with caching and guardrails |
| [Kong AI Gateway](<https://konghq.com/products/kong-ai-gateway>) | [P] | if XYZ already runs Kong |
| [TrueFoundry — 2026 AI gateway landscape comparison](<https://www.truefoundry.com/blog/a-definitive-guide-to-ai-gateways-in-2026-competitive-landscape-comparison>) | [C] | vendor-authored; useful for the criteria list, not the ranking |

## 8.2 Evaluation

| Resource | Grade | Note |
|---|---|---|
| [OpenAI Evals](<https://github.com/openai/evals>) | [P] |  |
| [promptfoo](<https://www.promptfoo.dev/>) | [P] | the fastest way to stand up a comparison harness across models |
| [Ragas](<https://docs.ragas.io/>) | [P] | retrieval-augmented generation evaluation |
| [LangSmith](<https://docs.smith.langchain.com/>) | [P] | tracing and evaluation |

Build the eval sets during the engagement and hand them over. They are the asset that lets XYZ re-decide when the next model ships.

## 8.3 Observability and cost attribution

| Resource | Grade | Note |
|---|---|---|
| [Langfuse](<https://langfuse.com/docs>) | [P] | open-source LLM observability with cost tracking |
| [Helicone](<https://www.helicone.ai/>) | [P] | lightweight proxy-based observability |
| [OpenTelemetry GenAI semantic conventions](<https://opentelemetry.io/>) | [P] | search "gen-ai semantic conventions". Adopt these attribute names so telemetry stays portable. |

---

# 9. Building and running the CoE

| Resource | Grade | Note |
|---|---|---|
| [Microsoft Cloud Adoption Framework — AI adoption and governance](<https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/>) | [P] | the most complete free operating-model reference |
| [AWS Cloud Adoption Framework for AI, ML and generative AI](<https://aws.amazon.com/cloud-adoption-framework/>) | [P] | perspectives, capabilities, maturity |
| [Google Cloud AI Adoption Framework](<https://cloud.google.com/>) | [P] | search "AI adoption framework" |
| [MIT Sloan Management Review — AI and business strategy](<https://sloanreview.mit.edu/big-ideas/artificial-intelligence-business-strategy/>) | [S] | governance and organisational research rather than vendor material |
| [McKinsey — State of AI](<https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai>) | [S] | adoption benchmarks for the "are we behind?" question |
| [Harvard Program on Negotiation](<https://www.pon.harvard.edu/>) | [S] | BATNA, anchoring, concession structure. Read before drafting the negotiation brief. |
| [ClarityArc — AI CoE design (2026)](<https://www.clarityarc.com/insights/ai-centre-of-excellence-design>) | [C] | practical on the 90/180-day sequencing and the acceleration-versus-blocking tension |
| [Trantor — building an AI CoE (2026)](<https://www.trantorinc.com/blog/how-to-build-an-ai-center-of-excellence-team-budget-and-kpis>) | [C] | charter contents and operating-model trade-offs |

The last two are consultancy content. Use them for structure and checklists. The charter you write should be XYZ's, built from Part 6 of the playbook.

---

# 10. Retail, fashion and the client's market

| Resource | Grade | Note |
|---|---|---|
| [McKinsey — State of Fashion (with Business of Fashion)](<https://www.mckinsey.com/industries/retail/our-insights/state-of-fashion>) | [S] | the annual reference every fashion executive has read. Know what it says about AI this year. |
| [Business of Fashion — technology coverage](<https://www.businessoffashion.com/>) | [S] |  |
| [Vogue Business — technology](<https://www.voguebusiness.com/technology>) | [S] | practical coverage of brand-side AI deployments including synthetic imagery and model likeness |
| [National Retail Federation](<https://nrf.com/>) | [S] | retail technology adoption research and the annual Big Show agenda as a landscape signal |
| Adobe / Salesforce / Shopify commerce insight reports | [S] | Vendor research, but the traffic and conversion data on AI-referred shopping is not available elsewhere |
| [EU Ecodesign for Sustainable Products Regulation and Digital Product Passport](<https://commission.europa.eu/>) | [P] | search "ecodesign sustainable products regulation". Relevant because generated product data becomes regulated product data. |

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
