---
title: GPT-5.5
date: 2026-05-04T12:09:27-06:00
lastmod: 2026-05-04T12:09:27-06:00
draft: false
description: ""
tags:
  - ai-models
  - llms
categories: []
---
[OpenAI's GPT-5.5](https://openai.com/index/introducing-gpt-5-5/) is the first fully retrained base model since GPT-4.5. Why is OpenAI the literal worst at naming things? Who knows? Maybe a future, more intelligent model will be able to tell us this just after it gives us the answer to life, the universe, and everything.

GPT-5.5 is a pretty exciting model. It's more efficient, better at coding, and offers a huge personality boost over previous versions of the GPT-5 family of models.

## Costs more, but not really?

The sticker price doubles. GPT-5.5 runs at $5/$30 per million input/output tokens versus GPT-5.4's $2.50/$15. But OpenAI claims GPT-5.5 is "more efficient in how it works through problems, often reaching higher-quality outputs with fewer tokens and fewer retries." [BuildFastWithAI's testing](https://www.buildfastwithai.com/blogs/gpt-5-5-review-2026) found GPT-5.5 uses "approximately 40% fewer output tokens to complete the same Codex task as GPT-5.4," putting the real-world cost increase closer to 20%. The [LLM Stats comparison](https://llm-stats.com/blog/research/gpt-5-5-vs-gpt-5-4) backs this up: "my Codex bill on real engineering tasks moved nowhere near 2×."

## The coding debate

A lot of people have been saying GPT-5.5 is a better coder than Opus 4.7. The benchmarks make it complicated to compare, and real-world tests provide a variety of opinions.

GPT-5.5's wins on Terminal-Bench 2.0. It scores 82.7% against Opus 4.7's 69.4%. As [BuildFastWithAI describes it](https://www.buildfastwithai.com/blogs/gpt-5-5-review-2026): "Terminal-Bench 2.0 at 82.7% is GPT-5.5's most decisive win...No publicly available model is close."

For actual bug-fixing and feature work in codebases, it's the opposite. [DataCamp's benchmark analysis](https://www.datacamp.com/blog/gpt-5-5-vs-claude-opus-4-7) finds: "On SWE-bench Pro, Opus 4.7 leads with an impressive 64.3% versus GPT-5.5's 58.6%." DataCamp's conclusion: "Claude Opus 4.7 is the stronger choice for most agentic coding and tool-use workflows."

Where GPT-5.5 is great for long-context work. On the MRCR v2 needle-in-haystack test at 512K–1M token contexts, it jumps to 74.0% from GPT-5.4's 36.6%.

## Still more chatty than you want

One of the worst things about GPT models is how chatty they are. GPT-5.5 improves on this, but still has room to grow. The model still has a tendency to over-explain and add preamble. OpenAI has added a `text.verbosity` API parameter to help manage response length, which is at least an acknowledgment that the problem exists. As the issue with [goblins](https://openai.com/index/where-the-goblins-came-from/) shows us, the fact that you need dedicated instructions or parameters to stop undesirable behaviors says a lot.