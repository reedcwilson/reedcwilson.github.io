---
title: DeepSeek v4
date: 2026-04-28T12:09:18-06:00
lastmod: 2026-04-28T12:09:18-06:00
draft: false
description: ""
tags:
  - open-source
  - ai-rivalry
  - china
  - llms
categories: []
---
The long-awaited DeepSeek v4 was released last week. You'll find all kinds of comments about this from, "[the End of American AI Cost Dominance](https://globalgeopolitics.co.uk/2026/04/27/deepseek-and-the-end-of-american-ai-cost-dominance/)" to "[DeepSeek V4 is Sh!tty](https://medium.com/data-science-in-your-pocket/deepseek-v4-is-shitty-b067af243019)" (both are interesting perspectives, btw). 

As with most things, I think the truth is somewhere between those two extremes.

I think the long gap between DeepSeek releases built anticipation and led some people to hope and expect that v4 could even beat the leading closed-source/closed-weight models.

While it still notably lags behind Opus 4.7 and GPT-5.5, the price-per-performance is where this model becomes most compelling. If the performance nearly matches Opus 4.7 and GPT-5.5 but is $3 instead of $17, do you really care about a few points on the benchmark? And is your use case one that actually even needs SOTA intelligence?

So, in my opinion, it's the same story as it's always been. Chinese models are still 3–6 months behind the best US models, but where they win is by being open and cheaper.

Interesting:
* Adapted for Huawei chips (not good for NVIDIA)
* 1M token context window

Frustrating:
* Still a text-only model.
* Chinese character leakage. This has plagued Chinese models forever, and while it seems to happen less, my own testing of this model is no exception.

[Technical Report](https://huggingface.co/collections/deepseek-ai/deepseek-v4)

{{< youtubeLite id="UV1WDNe4J5w" label="Matthew Berman: DeepSeek v4" >}}
