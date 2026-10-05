---
title: "Introducing Strands Decider 2B: a small, open source, decision model"
date: 2026-10-04T23:57:19-06:00
lastmod: 2026-10-04T23:57:19-06:00
draft: true
description: "Strands Decider 2B is a 2B-parameter open-source \"decision model\" that replaces an LLM's text-generation head with a pointer head, so it picks from predefined options and outputs confidence scores instead of free text. It runs locally in ~115ms median latency (RTX 3090) and ranks 3rd of 33 in its size class on JevBench for accuracy/calibration, but it's worse at complex reasoning and can't do coding, chat, or summarization. The architecture is a Qwen3.5-2B torso with a small pointer head and rank-16 LoRA adapter, fully open-sourced with training data on GitHub and Hugging Face. Intended use cases are agentic-workflow glue: model routing, tool-call guardrails, evaluations, memory/context management, and policy classification where you need a fast, cheap, calibrated yes/no or multiple-choice call."
tags: []
categories: []
source_url: https://strandsagents.com/blog/introducing-strands-decider/
source_type: article
---

[Introducing Strands Decider 2B: a small, open source, decision model](https://strandsagents.com/blog/introducing-strands-decider/)

## 

> 
