---
title: GPT-5.5
date: 2026-04-28T12:09:27-06:00
lastmod: 2026-04-28T12:09:27-06:00
draft: true
description: ""
tags: []
categories: []
---
OpenAI's GPT-5.5 is the first fully retrained base model since GPT-4.5. It's a meaningful release — more efficient, better at terminal and DevOps tasks, and genuinely less annoying to talk to. But whether it's actually a better coder than Claude Opus 4.7 depends on what you're building, and the price hike needs some unpacking.

## A more professional AI

The biggest personality story in modern AI has been sycophancy — models that tell you what you want to hear rather than what you need to know. GPT-4o was a frequent offender. GPT-5.5 makes a deliberate move away from that. [Surge HQ's analysis](https://surgehq.ai/blog/bringing-light-to-the-gpt-4o-vs-gpt-5-personality-controversy) puts it plainly: "GPT-4o is a sycophantic friend; GPT-5 is a polite professional." According to their testing, sycophantic responses dropped from 9% of interactions with GPT-4o down to 2% with GPT-5.

The tradeoff is real. One evaluator in that study noted: "while it didn't satisfy my desire for connection it did satisfy my need for logic." That about sums it up. If you've been frustrated by AI that validates bad ideas instead of pushing back on them, GPT-5.5 is a step in the right direction. If you liked the warmth, it's gone.

GPT-5.5 also ships with configurable preset personas — Cynic, Robot, Listener, Nerd — giving developers more control over tone in their applications. It's a practical acknowledgment that different use cases need different registers.

## Costs more, but not really

The sticker price doubles. GPT-5.5 runs at $5/$30 per million input/output tokens versus GPT-5.4's $2.50/$15. On paper, that's a 2x increase.

In practice, OpenAI claims GPT-5.5 is "more efficient in how it works through problems, often reaching higher-quality outputs with fewer tokens and fewer retries." [BuildFastWithAI's testing](https://www.buildfastwithai.com/blogs/gpt-5-5-review-2026) found GPT-5.5 uses "approximately 40% fewer output tokens to complete the same Codex task as GPT-5.4," putting the real-world cost increase closer to 20%. The [LLM Stats comparison](https://llm-stats.com/blog/research/gpt-5-5-vs-gpt-5-4) backs this up: "my Codex bill on real engineering tasks moved nowhere near 2×."

Batch pricing helps further — Flex and batch tiers run at half the standard rate, landing right at GPT-5.4's per-token cost. For high-volume workloads you can afford to run async, this is a compelling upgrade path at roughly the same price.

## The coding debate

A lot of people have been saying GPT-5.5 is a better coder than Opus 4.7. The benchmarks are more complicated than that.

GPT-5.5's clearest win is terminal and DevOps automation. On Terminal-Bench 2.0, it scores 82.7% against Opus 4.7's 69.4%. As [BuildFastWithAI describes it](https://www.buildfastwithai.com/blogs/gpt-5-5-review-2026): "Terminal-Bench 2.0 at 82.7% is GPT-5.5's most decisive win...No publicly available model is close." For DevOps workflows, shell scripting, and infrastructure tasks, the edge is real.

For software engineering — actual bug-fixing and feature work in codebases — the picture flips. [DataCamp's benchmark analysis](https://www.datacamp.com/blog/gpt-5-5-vs-claude-opus-4-7) finds: "On SWE-bench Pro, Opus 4.7 leads with an impressive 64.3% versus GPT-5.5's 58.6%." That's a meaningful gap on the benchmark most representative of real-world agentic coding. Opus 4.7 also leads on MCP-Atlas multi-tool workflow orchestration at 77.3% vs 75.3%. DataCamp's conclusion: "Claude Opus 4.7 is the stronger choice for most agentic coding and tool-use workflows."

Where GPT-5.5 genuinely shines is long-context work. On the MRCR v2 needle-in-haystack test at 512K–1M token contexts, it jumps to 74.0% from GPT-5.4's 36.6% — a 37-point improvement that's hard to ignore for large-codebase tasks.

## Still more chatty than you want

Despite the personality improvements, verbosity remains a complaint. The model has a tendency to over-explain and add preamble where none was asked for. OpenAI has added a `text.verbosity` API parameter to help manage response length, which is at least an acknowledgment that the problem exists. But the fact that you need a dedicated parameter to stop the model from padding its answers says something.

This is the one area where the "professional" framing falls short. A truly professional response is also a concise one.
## Links

### Personality and steerability
- [A new class of intelligence for real work — OpenAI](https://developers.openai.com/api/docs/guides/prompt-guidance) — moving to an agentic task-runner
- [GPT-5.5 shifts from sycophant to professional — Access Newswire](https://www.accessnewswire.com/newsroom/en/computers-technology-and-internet/chatgpt-5.5-reality-check-why-eduard-klein-calls-openais-new-rele-1161883) — less emotional padding, more direct
- [The new preset personas in GPT-5.5 — Medium](https://medium.com/@meagan_19394/gpt-5-gets-a-personality-upgrade-d72ef08354a1) — Cynic, Robot, Listener, Nerd modes
- [Outcome-first reasoning vs step-by-step — Marketing4eCommerce](https://marketing4ecommerce.net/en/this-is-the-new-gpt-5-5-5-key-points/) — proactive planning over reactive prompting
- [Why GPT-4o's warmth was removed — Surge HQ](https://surgehq.ai/blog/bringing-light-to-the-gpt-4o-vs-gpt-5-personality-controversy) — human evaluators preferred polite professionals

### Coding benchmarks vs Opus 4.7
- [GPT-5.5 vs Claude Opus 4.7 benchmarks — APIYI](https://help.apiyi.com/en/gpt-5-5-vs-claude-opus-4-7-coding-comparison-en.html) — trading leads across SWE-bench variants
- [SWE-bench Verified results for GPT-5.5 — DataCamp](https://www.datacamp.com/blog/gpt-5-5-vs-claude-opus-4-7) — leads at 88.7% verified
- [Terminal-Bench 2.0 and DevOps tasks — MindStudio](https://www.mindstudio.ai/blog/gpt-55-vs-claude-opus-47-coding-comparison) — clear leader for terminal automation
- [Claude Opus 4.7 wins on repository refactoring — LLM Stats](https://llm-stats.com/blog/research/gpt-5-5-vs-claude-opus-4-7) — excels at multi-file architecture changes
- [Token efficiency comparison in coding — BuildFastWithAI](https://www.buildfastwithai.com/blogs/best-ai-models-leaderboard-april-2026-updated) — 72% more token-efficient than GPT-5.4

### Pricing and efficiency
- [GPT-5.5 API pricing doubles to $5/$30 — LLM Stats](https://llm-stats.com/blog/research/gpt-5-5-vs-gpt-5-4) — comparison with GPT-5.4 costs
- [Effective costs are lower due to efficiency — BuildFastWithAI](https://www.buildfastwithai.com/blogs/gpt-5-5-review-2026) — 40% fewer output tokens needed per task
- [New Flex and Priority processing tiers — Framia Pro](https://framia.pro/page/en-US/news/gpt-5-5-pricing-cost) — 50% discount for batch, 2.5x for low latency
- [Opus 4.7 remains cheaper for output — ALM Corp](https://almcorp.com/blog/openai-gpt-5-5-benchmarks-pricing-api-vs-gpt-5-4/) — $25 per 1M output tokens vs GPT-5.5's $30
- [When to stick with GPT-5.4 — Digital Applied](https://www.digitalapplied.com/blog/gpt-5-5-complete-guide-thinking-pro-1m-context) — simple chat and summarization value

### The verbosity debate
- [Is GPT-5.5 too exuberant? — ZDNet](https://www.zdnet.com/article/i-put-openai-gpt-5-5-through-a-10-round-test/) — ignoring single-source instructions in research tasks
- [Concise to a fault in developer workflows — Reddit](https://www.reddit.com/r/codex/comments/1swmpi2/what_types_of_users_are_getting_good_results_from/) — taking the shortest path and skipping reasoning
- [Using text.verbosity to control output — OpenAI](https://developers.openai.com/api/docs/guides/latest-model) — new API parameter to manage response length
- [Occasional challenges in legal parsing — Harvey AI](https://www.harvey.ai/blog/gpt-5-5-research-preview-results) — adds too much detail to simple queries
- [Preamble strategy for latency — OpenAI](https://developers.openai.com/api/docs/guides/prompt-guidance) — managing perceived wait times in long loops
