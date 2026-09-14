# Resources
## Free reading, video, and hands-on material, numbered to match the Roadmap

Every link here was checked before publishing. Tags: 📖 read, 🎥 watch, 🧪 hands-on.
Where a resource has a paid tier I don't need (a certificate, a graded assignment, extra
compute credits), I say so. The material itself is free either way.

---

# Part 1 — Foundations

## 1.1 – 1.2 Large language models and prompt engineering

- 📖 [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/). Jay Alammar's visual walkthrough of the architecture behind every model in this field. Free, CC-licensed.
- 🎥 [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html). Andrej Karpathy's video series, building up from backpropagation to a working GPT from scratch. All videos free on YouTube.
- 🧪 [Anthropic's Interactive Prompt Engineering Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial). A free, hands-on Jupyter-notebook course, 9 chapters plus appendix, with exercises and an answer key.
- 📖 [Claude prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices). Anthropic's own docs.
- 📖 [dair-ai Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide). The open-source guide behind promptingguide.ai, broader than one vendor. Covers prompting, RAG, and agents.

## 1.3 Retrieval-augmented generation

- 🎥 [RAG Fundamentals and Advanced Techniques](https://www.freecodecamp.org/news/learn-rag-fundamentals-and-advanced-techniques/). Free 2-hour course on the freeCodeCamp YouTube channel.

## 1.4 AI-assisted rapid prototyping ("vibing")

- 📖 [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices). Anthropic's own official guide to the exact skill this section is about: scoping, verification loops, and knowing when to take the wheel back. Read this one closely. It's the most directly applicable resource in the whole roadmap.

---

# Part 2 — Discovery and Scoping

## 2.1 Mapping a business process

- 📖 [Value Stream Mapping Tutorial](https://asq.org/quality-resources/value-stream-mapping). ASQ's free guide to the core technique, with a worked example.

## 2.3 Reading a technology landscape fast

- See Part 4 below for the platform-specific resources (Vertex AI, Bedrock, Snowflake, Databricks, S/4HANA, Salesforce, Oracle). Scoping speed comes from the same material as depth, just read less deep on the first pass.

---

# Part 3 — Client Co-Creation → Client Transformation Advisory

## 3.3 Domain fluency without a domain degree

- 📖 [Umbrex Industry Primers](https://umbrex.com/resources/industry-primers/). Free, consultant-written primers across finance, healthcare, retail, manufacturing, and 18 other sectors. This is the single best starting point for the domain-fluency requirement in both role levels.

## 3.4 Trusted-advisor skills and consulting fundamentals

- 📖 [Introduction to Stakeholder Management (Alison)](https://alison.com/course/introduction-to-stakeholder-management). Genuinely free to take; only an optional certificate costs money. Multi-course Professional Certificates on Coursera are usually subscription-gated even in "audit," so this is the more reliably free option for the underlying skill.

---

# Part 4 — Technical Delivery → Solution Architecture

## 4.1 Agentic AI systems

- 📖 [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents). Anthropic's own engineering guide to agent design patterns and, just as important, when not to use an agent.
- 📖 [LangGraph](https://github.com/langchain-ai/langgraph). Official docs and tutorials for the most widely used agent-orchestration framework. Free, open source.
- 📖 [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/). Official docs, free.
- 📖 [CrewAI](https://docs.crewai.com/en/introduction). Official docs for the role-based multi-agent framework. Free, open-source core.

## 4.2 Enterprise AI platforms

- 🧪 [Introduction to Generative AI (Google Skills)](https://www.skills.google/paths/118). Free course content. Some optional hands-on labs on the platform use paid credits, the core lessons don't.
- 🧪 [Building Generative AI Applications Using Amazon Bedrock (AWS Skill Builder)](https://skillbuilder.aws/generative-ai). Free digital course.
- 🧪 [amazon-bedrock-workshop](https://github.com/aws-samples/amazon-bedrock-workshop). AWS's own free, hands-on notebook workshop covering Bedrock end to end.

## 4.3 Data platforms for AI

- 🧪 [Snowflake University](https://learn.snowflake.com/en/). Official training platform. Not everything here is free: look for the on-demand and "badge" courses, which are; instructor-led and certification-prep courses are paid.
- 🧪 [Databricks Fundamentals](https://www.databricks.com/resources/learn/training/databricks-fundamentals) and [AI Agent Fundamentals](https://www.databricks.com/training/catalog/ai-agent-fundamentals-4482). Databricks' own free training catalog.

## 4.4 Business platform literacy

- 📖 [SAP Learning](https://learning.sap.com/) courses on S/4HANA (openSAP's content moved here). "Implementing SAP S/4HANA Cloud Public Edition" and "Data Migration to SAP S/4HANA" are both listed as free on Class Central; confirm the price shown before enrolling, SAP Learning mixes free and paid content on the same platform.
- 🧪 [Salesforce Trailhead: Einstein AI trail](https://trailhead.salesforce.com/en/einstein-ai-trail). Salesforce's own free, hands-on learning platform.
- 🧪 [Oracle Cloud Infrastructure AI Foundations](https://mylearn.oracle.com/ou/course/oracle-cloud-infrastructure-ai-foundations/147805). Oracle's own foundations course; the course content is free. Oracle has run free-exam promotions for this associate certification before, but that isn't permanent, check the current exam price before registering.

## 4.5 Productionizing AI/LLM workloads (LLMOps)

- 🧪 [Promptfoo](https://www.promptfoo.dev/docs/intro/). Free, open-source, runs locally. The best hands-on way to learn eval-driven prompt development.
- 🧪 [DeepEval](https://deepeval.com/docs/introduction). Free, open-source LLM and RAG evaluation framework with a large library of built-in metrics.
- 🧪 [Ragas](https://docs.ragas.io/en/stable/getstarted/). Free, open-source, RAG-specific evaluation (faithfulness, answer relevance, context precision and recall).

## 4.6 CI/CD and infrastructure-as-code

- 🧪 [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials). HashiCorp's own free, hands-on tutorials, including cloud-specific getting-started paths.

## 4.7 Full-stack delivery and enterprise integration

- 📖 [OpenTelemetry: Getting Started](https://opentelemetry.io/docs/getting-started/). The vendor-neutral, free, open-source standard for the observability half of this section.

---

# Part 5 — Validation and Iteration

- 🧪 Reuse Part 4.5's three evaluation tools (Promptfoo, DeepEval, Ragas). This section is about the practice of writing an evaluation plan, not new tools.
- 📖 [Ragas: Evaluate a simple RAG system](https://docs.ragas.io/en/latest/tutorials/rag/). A concrete worked tutorial that doubles as a template for writing your own evaluation plan.

---

# Part 6 — Security, Compliance, and Reliability

- 📖 [Introduction to Responsible AI (Google Skills)](https://www.skills.google/course_templates/554). Free course.
- 📖 [Embrace Responsible AI Principles and Practices (Microsoft Learn)](https://learn.microsoft.com/en-us/training/modules/embrace-responsible-ai-principles-practices/). Free, official.
- 📖 [EU AI Act, official text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj). Go to the primary source rather than a summary blog for anything you'll rely on. Free.
- 📖 [Google SRE Book](https://sre.google/sre-book/table-of-contents/). The full book, free online, for the observability and SLO half of this section.

---

# Part 7 — Change Management and Enablement

- 📖 [Prosci ADKAR Model](https://www.prosci.com/methodology/adkar). The standard framework, free overview page.
- 🎥 [Introduction to ADKAR (30 minutes)](https://www.prosci.com/resources/webinars/introduction-to-adkar-30-minutes). Free recorded webinar.

---

# Part 8 — Post-Launch Ownership

- 📖 [Google SRE Book](https://sre.google/sre-book/table-of-contents/). Same resource as Part 6. The hyper-care and post-launch chapters are the relevant ones here (see the table of contents for "Monitoring Distributed Systems" and "Managing Incidents").

---

# Part 9 — Platform Engineering and Productization

- 📖 [What is Backstage?](https://backstage.io/docs/overview/what-is-backstage/). Official docs for the open-source reference implementation of an internal developer platform. Free, CNCF project. You don't need to adopt Backstage itself; reading how it's structured is the fastest way to understand what "platform engineering" concretely means.

---

# Part 10 — Advanced AI Development → AI Strategy and Visioning

## 10.1 Fine-tuning and model customization

- 🧪 [Hugging Face: LoRA and PEFT, Efficient Fine-Tuning](https://huggingface.co/learn/smol-course/unit1/3a). Free, hands-on course unit.
- 🧪 [huggingface/peft](https://github.com/huggingface/peft). The official library docs and examples, free and open source.

## 10.3 Translating AI strategy into a roadmap

- 📖 [The AI transformation manifesto](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-ai-transformation-manifesto). Free McKinsey Insights article. Useful for the shape of a multi-horizon transformation roadmap. Read critically rather than as gospel.

---

# Part 11 — Thought Leadership and Ecosystem Collaboration

- No single resource here. This part is about doing the thing (writing, publishing, engaging) more than studying it. Pick one specific, narrow thing you learned building through this roadmap and write it up.

---

# Part 12 — The Lead → Principal gap

- No resources. This is a self-assessment checklist. Revisit it after finishing a pass through Parts 1 through 11, and again every few months.
