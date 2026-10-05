---
title: "GitHub - jaredpalmer/kev: Jev-like family of decision models built on top of Qwen3.5/3.8 you can train and run on your own"
date: 2026-10-04T23:57:19-06:00
lastmod: 2026-10-04T23:57:19-06:00
draft: true
description: "Kev is a family of small (0.8B–27B) decision models built on Qwen3.5/3.8 that answer yes/no, multiple-choice, and rating questions in a single request with calibrated probabilities, and it's a drop-in replacement for TypeSafe's Jev API so existing Python SDK code works unchanged. Kev-27B lands within ~1 point of Jev on unseen sources; the 4B and 9B variants are within four points and run on a 32 GB Mac or a single L40S/H100. A coding-agent skill (npx skills add jaredpalmer/kev@kev-finetune) automates the full fine-tune loop on Modal for roughly $1 per 4B run, and a one-command Modal deploy gives you a free-when-idle HTTPS endpoint. The main trade-off: smaller models trail Jev on knowledge-heavy questions (MMLU) and date arithmetic, but fine-tuning on your own labels closes most of the gap for domain-specific routing and classification tasks."
tags: []
categories: []
source_url: https://github.com/jaredpalmer/kev
source_type: article
---

[GitHub - jaredpalmer/kev: Jev-like family of decision models built on top of Qwen3.5/3.8 you can train and run on your own](https://github.com/jaredpalmer/kev)

## 

> 
