---
title: "Jared Palmer"
date: 2026-10-04T23:57:19-06:00
lastmod: 2026-10-04T23:57:19-06:00
draft: true
description: "Jared Palmer released Kev 1.0, four Apache-2.0 open-source decision models (0.8B–27B params) that score multiple-choice answers via a pointer head instead of generating tokens, making them a drop-in replacement for TypeSafe's Jev API. The document is read once and cached; every question branches off that single pass, so asking 30 questions costs the same as asking 3. Kev-27B leads his own evals (75.7% generalization, 91.8% policy reasoning); Kev-9B and Kev-4B trail by 1–6 points on most tasks but run on a 32 GB Mac via MLX. Smaller models use Qwen3.5 backbones with LoRA adapters; the 27B is a full fine-tune of Qwen3.8-27B on ~146K examples / 337K questions, trained in ~16 hours on 8 H200s (~$650)."
tags: []
categories: []
source_url: https://jaredpalmer.com/blog/introducing-kev
source_type: article
---

[Jared Palmer](https://jaredpalmer.com/blog/introducing-kev)

## 

> 
