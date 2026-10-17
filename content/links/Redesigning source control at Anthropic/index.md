---
title: "Redesigning source control at Anthropic"
date: 2026-10-17T09:44:50-06:00
lastmod: 2026-10-17T09:44:50-06:00
draft: true
description: "Anthropic replaced Git with a custom centralized system called Scion after their monorepo merge rate exploded from ~2,500/day in May 2026 to 30,000+/day by September, driven largely by AI agents (Claude) generating code at scale. The 7-person team completed the migration in five months; the new \"Antique\" review system overtook traditional pull requests by mid-July. No offline support was built because Claude, the heaviest user, is always online. They also note that adversarial AI code review is effective but can be myopic, requiring human engineers to steer it away from over-engineering."
tags: []
categories: []
source_url: https://simonwillison.net/2026/Oct/13/redesigning-source-control-at-anthropic/
source_type: article
---

[Redesigning source control at Anthropic](https://simonwillison.net/2026/Oct/13/redesigning-source-control-at-anthropic/)

## 

> 
