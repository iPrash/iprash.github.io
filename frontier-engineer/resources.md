# Resources
## Free reading, video, and hands-on material, numbered to match the Roadmap

Every link here was checked before publishing: opened and read, not just found in a search
result. Tags: 📖 read, 🎥 watch, 🧪 hands-on.

Where a platform mixes free and paid content, the entry says so. Anything that turned out to be
metered or subscription-gated was dropped rather than listed as free.

Parts 1 to 11 are Stage 1 (Lead). Parts 12 to 18 are Stage 2 (Principal). Parts 11 and 18 are
checklists and have no resources.

---

# Stage 1 · Part 1 — Foundations

## 1.1 – 1.2 Large language models and prompt engineering

- 📖 [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/). Jay Alammar's visual walkthrough of the architecture behind every model in this field. Free, CC-licensed.
- 🎥 [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html). Andrej Karpathy's video series, building from backpropagation to a working GPT from scratch. All videos free on YouTube.
- 🧪 [Anthropic's Interactive Prompt Engineering Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial). Free hands-on Jupyter-notebook course, 9 chapters plus appendix, with exercises and an answer key.
- 📖 [Claude prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices). Anthropic's own docs.
- 📖 [dair-ai Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide). The open-source guide behind promptingguide.ai. Broader than one vendor: prompting, RAG, and agents.

## 1.3 Retrieval-augmented generation

- 🎥 [RAG Fundamentals and Advanced Techniques](https://www.freecodecamp.org/news/learn-rag-fundamentals-and-advanced-techniques/). Free 2-hour course on the freeCodeCamp YouTube channel.

## 1.4 AI-assisted rapid prototyping ("vibing")

- 📖 [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices). Anthropic's official guide to exactly this skill: scoping, verification loops, and knowing when to take the wheel back. The most directly applicable resource in Stage 1.

---

# Stage 1 · Part 2 — Discovery and scoping

## 2.1 Mapping a business process

- 📖 [Value Stream Mapping Tutorial](https://asq.org/quality-resources/value-stream-mapping). ASQ's free guide to the core technique, with worked improvement examples.

## 2.3 Reading a technology landscape fast

- The platform resources in Part 4 serve this too. Scoping speed comes from the same material, read less deep on the first pass.

---

# Stage 1 · Part 3 — Co-creation with the client

## 3.1 Facilitation and stakeholder work

- 📖 [Introduction to Stakeholder Management (Alison)](https://alison.com/course/introduction-to-stakeholder-management). Genuinely free to take; only an optional certificate costs money.

## 3.3 Domain fluency without a domain degree

- 📖 [Umbrex Industry Primers](https://umbrex.com/resources/industry-primers/). Free consultant-written primers across finance, healthcare, retail, manufacturing, and 18 other sectors. The single best starting point for the domain-fluency requirement, and it serves Part 12 again at greater depth.

---

# Stage 1 · Part 4 — Technical delivery

## 4.1 Agentic AI systems

- 📖 [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents). Anthropic's engineering guide to agent design patterns and, just as important, when not to use an agent.
- 📖 [LangGraph](https://github.com/langchain-ai/langgraph). Official docs and tutorials for the most widely used agent-orchestration framework. Free, MIT-licensed.
- 📖 [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/). Official docs, free.
- 📖 [CrewAI](https://docs.crewai.com/en/introduction). Official docs for the role-based multi-agent framework. Free, open-source core.

## 4.2 Enterprise AI platforms

- 🧪 [Introduction to Generative AI (Google Skills)](https://www.skills.google/paths/118). Free course content. Some optional hands-on labs on the platform use paid credits; the core lessons don't.
- 🧪 [Building Generative AI Applications Using Amazon Bedrock (AWS Skill Builder)](https://skillbuilder.aws/generative-ai). Free digital course.
- 🧪 [amazon-bedrock-workshop](https://github.com/aws-samples/amazon-bedrock-workshop). AWS's own free hands-on notebook workshop covering Bedrock end to end: text generation, RAG, customization, agents.

## 4.3 Data platforms for AI

- 🧪 [Snowflake University](https://learn.snowflake.com/en/). Official training platform. Not everything here is free: the on-demand and badge courses are; instructor-led and certification-prep courses are paid.
- 🧪 [Databricks Fundamentals](https://www.databricks.com/resources/learn/training/databricks-fundamentals) and [AI Agent Fundamentals](https://www.databricks.com/training/catalog/ai-agent-fundamentals-4482). Databricks' own free training.

## 4.4 Business platform literacy

- 📖 [SAP Learning](https://learning.sap.com/) courses on S/4HANA (openSAP's content moved here). "Implementing SAP S/4HANA Cloud Public Edition" and "Data Migration to SAP S/4HANA" are both listed as free on Class Central; confirm the price shown before enrolling, since SAP Learning mixes free and paid content.
- 🧪 [Salesforce Trailhead: Einstein AI trail](https://trailhead.salesforce.com/en/einstein-ai-trail). Salesforce's own free hands-on learning platform.
- 🧪 [Oracle Cloud Infrastructure AI Foundations](https://mylearn.oracle.com/ou/course/oracle-cloud-infrastructure-ai-foundations/147805). Course content is free. Oracle has run free-exam promotions for this associate certification before, but that isn't permanent; check the current exam price before registering.

## 4.5 Productionizing AI/LLM workloads (LLMOps)

The highest-value hands-on block in Stage 1.

- 🧪 [Promptfoo](https://www.promptfoo.dev/docs/intro/). Free, open source, runs locally. The best hands-on way to learn eval-driven prompt development.
- 🧪 [DeepEval](https://deepeval.com/docs/introduction). Free, open-source LLM and RAG evaluation framework, 50+ built-in metrics, Apache 2.0.
- 🧪 [Ragas](https://docs.ragas.io/en/stable/getstarted/). Free, open source, RAG-specific evaluation: faithfulness, answer relevance, context precision and recall.

## 4.6 CI/CD and infrastructure-as-code

- 🧪 [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials). HashiCorp's own free hands-on tutorials, including cloud-specific getting-started paths.

## 4.7 Full-stack delivery and enterprise integration

- 📖 [OpenTelemetry: Getting Started](https://opentelemetry.io/docs/getting-started/). The vendor-neutral, free, open-source standard for the observability half of this section.

---

# Stage 1 · Part 5 — Validation and iteration

- 🧪 The three evaluation tools in Part 4.5 are the tooling for this part. What's new here is the practice of writing the plan first.
- 📖 [Ragas: Evaluate a simple RAG system](https://docs.ragas.io/en/latest/tutorials/rag/). A worked tutorial that doubles as a template for writing an evaluation plan.

---

# Stage 1 · Part 6 — Security, compliance and reliability

- 📖 [Introduction to Responsible AI (Google Skills)](https://www.skills.google/course_templates/554). Free course.
- 📖 [Embrace Responsible AI Principles and Practices (Microsoft Learn)](https://learn.microsoft.com/en-us/training/modules/embrace-responsible-ai-principles-practices/). Free, official.
- 📖 [EU AI Act, official text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj). Go to the primary source rather than a summary blog for anything I'll rely on. Free.
- 📖 [Google SRE Book](https://sre.google/sre-book/table-of-contents/). The full book, free online under CC BY-NC-ND, for the observability and SLO half of this part.

---

# Stage 1 · Part 7 — Change management and enablement

- 📖 [Prosci ADKAR Model](https://www.prosci.com/methodology/adkar). The standard framework, free overview.
- 🎥 [Introduction to ADKAR (30 minutes)](https://www.prosci.com/resources/webinars/introduction-to-adkar-30-minutes). Free recorded webinar.

---

# Stage 1 · Part 8 — Post-launch ownership

- 📖 [Google SRE Book](https://sre.google/sre-book/table-of-contents/), specifically chapter 6 (Monitoring Distributed Systems), chapter 14 (Managing Incidents) and chapter 15 (Postmortem Culture). Free.

---

# Stage 1 · Part 9 — Platform engineering

- 📖 [What is Backstage?](https://backstage.io/docs/overview/what-is-backstage/). Official docs for the open-source reference implementation of an internal developer portal. Free, CNCF project. No need to adopt Backstage itself; reading how it's structured is the fastest way to see what platform engineering concretely means.

---

# Stage 1 · Part 10 — Advanced AI development

## 10.1 Fine-tuning and model customization

- 🧪 [Hugging Face: LoRA and PEFT, Efficient Fine-Tuning](https://huggingface.co/learn/smol-course/unit1/3a). Free hands-on course unit.
- 🧪 [huggingface/peft](https://github.com/huggingface/peft). Official library docs and examples. Free, Apache 2.0.

## 10.3 Inference optimization and cost control

- 🧪 [vLLM documentation](https://docs.vllm.ai/en/latest/). Free, open source. Covers serving, batching, and the full range of quantization approaches, which is where the model-level cost levers actually live.

---

# Stage 2 · Part 12 — Client transformation advisory

- 📖 [Umbrex Industry Primers](https://umbrex.com/resources/industry-primers/) again, read at advisory depth this time: value chains, economics, and regulatory context rather than just vocabulary.

---

# Stage 2 · Part 13 — Solution architecture and leading a squad

- 📖 [Architectural Decision Records](https://adr.github.io/). Free, open resource: templates, tooling, and the background literature including Michael Nygard's original piece.
- 📖 [StaffEng guides](https://staffeng.com/guides/). Free and directly on point for the Principal role's shape: operating at staff-plus level, leading without managing, writing strategy, and executive communication. The associated book is a separate paid product; the guides themselves are free.

---

# Stage 2 · Part 14 — AI strategy and visioning

- 📖 [The AI transformation manifesto](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-ai-transformation-manifesto). Free McKinsey Insights article, useful for the shape of a multi-horizon transformation roadmap. Read critically rather than as gospel.

---

# Stage 2 · Part 15 — Productization

- 📖 [StaffEng guides](https://staffeng.com/guides/), the "operating at staff" section, for how a technical proposal becomes something an organization formally adopts.
- No strong free resource exists for productization specifically. This part is learned by doing it and by watching how the platform teams around me package their own work.

---

# Stage 2 · Part 16 — Thought leadership and ecosystem

- No single resource. This part is doing the thing rather than studying it. The Stage 1 builds from Parts 4, 5 and 9 are the raw material for the first piece.

---

# Stage 2 · Part 17 — Mentoring and capability building

- 📖 [Google re:Work guides](https://rework.withgoogle.com/intl/en/guides/). Free. Relevant guides: "Coach managers to coach," "Coaching for everyone: the amplified impact of peer coaching," and "Understand team effectiveness."

---

# Checked and rejected

Listed so I don't re-find them and assume they're free:

- **IBM Management Consultant Professional Certificate (Coursera).** Multi-course Professional Certificates are subscription-gated even in audit mode, unlike standalone Coursera courses. Replaced with the Alison course in Part 3.1.
- **LeadDev articles on leading without authority.** Metered paywall: one article per month before registration is required. StaffEng covers the same ground with no meter.
