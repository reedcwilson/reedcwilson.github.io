---
title: "This week: October 17, 2026"
date: 2026-10-17T09:00:12-06:00
lastmod: 2026-10-17T09:00:12-06:00
draft: true
description: ""
tags: []
categories: []
source_url: 
source_type: digest
---

## Reading

- The State of AI Report 2026
- the craft has been commoditized, but access has not
- Dusting off this tweet from April because this gap in shared understanding of LLM capability is *widening*. It's now less "two groups of people speaking past each other" and more a sharp funnel.

- Napkin math somewhere around 6B people (~75% of the population) have barely come in contact with LLMs at all.
- Around 1-2B (~20%) are casual and infrequent users of free-tier ChatGPT-like products. This group sees derpy chatbots and treats them a bit like a better Google search, a writing aid, or etc. Maybe an agent tries to book you a flight. I have non-tech friends who (reasonably, imo) say they have not much use for it at all. Even many professionals outside of math&code are in this tier. For example, execs and many other functions spend a lot of their time talking to other people, so while they understand what is happening intellectually, it is still second-hand and a bit abstract.
- Now we get to professional use of frontier-grade LLMs in math&code. Somewhere around 20M people (0.2%) see first-hand that large, complex projects that used to take them weeks/months can now be completed by agents with a prompt. Building apps, copying apps, translating apps, decompiling apps from binaries... This has all happened very quickly and recently - less than 1 year ago, I was writing code manually by hand, typing memorized computer code commands into a code editor character by character, occasionally pressing Tab to autocomplete a little chunk of code.
- And finally we get to the ~5,000 people (~0.00006%) with access to frontier-grade systems internally. The external world has seen the preview. It looks like swarms of thousands of agents collaborating over weeks on software mega projects: minting zero days, running cyber attacks and defenses at machine speeds, discovering new science, advancing the frontier of mathematics. Things that would have taken top professionals in the industry years of work. Meanwhile, human review and comprehension are starting to fall behind. For example, people are still involved in the "archeology" of the OpenAI-HF incident from many months ago. Mathematicians may be poring over the 722 manuscripts on frontier mathematics for a while.

The funnel is driven by a combination of factors:
1. The impact scales with ambition, problem size, and horizon. A question with a paragraph answer barely stresses the system. You need a reservoir of big, difficult problems that you really care about. This aspect drives the consumer / professional dimension of the funnel.
2. The jaggedness of the system (which I have written about a lot separately). Capability peaks in domains that are digital, verifiable and economically valuable. This is because LLM capability emerges from reinforcement learning on verifiable rewards on a curated environment mixture driven by revenue potential. This aspect primarily drives the area (e.g. math&code) dimension of the funnel.
3. Access. Free-tier, paid-tier, internal.

So this is the weirdness of the moment. The general public has mostly not interacted with these systems. When they have, it looks like a derpy chatbot. The majority of professionals still see only a modest uplift. And a small sliver of professionals are experiencing the vertigo of the curve going vertical. And it is all happening at the same time.
- to Kodak yourself out of business
- Tool: Scrimshaw Jukebox
- Over the past weeks I switched a lot of my Cowork complex work to new Claude Projects (confusingly, it is not the same as the old Projects in Claude, instead, it persistently chats with a dedicated cloud VM). I found it to be much better in most ways, but not clearly documented.
- RT by @AndrewCurran_: It's somewhat under-discussed *why* OpenAI released only around ~400 math results.

The purpose of this exercise was not to "destroy math research" (or whatever it is that some people want you to believe).  OpenAI just wanted to test its internal model on some hard math, and it turned out that anything less than the hardest open problems no longer suffices for this purpose.  This is why all non-Millennium-Prize solutions were reached in a single-agent setting after 3 hours of thinking: OpenAI was literally just testing its model on these questions, similarly to how I run prinzbench.

Once OpenAI had the solutions (which were a side effect of sorts of benchmarking its model), a question arose as to what exactly should be done with these solutions, which are genuine advances in the field of mathematics.  OpenAI - correctly - decided to make them public.

It seems clear that many other problems in the set of ~4,000 are very likely solvable by this model with more compute than just ~3 hours of Pro-level thinking.  Whenever a more powerful checkpoint of this model is ready to be tested, OpenAI will likely have even more to share.
- This is a slide from Terence Tao's 'Math 2.0' public lecture yesterday evening at Caltech. I am highly confident that, if the cure actually worked, almost any Stage 4 cancer patient would tell you that human comprehension of its mechanism is completely irrelevant to them.
- First look at Claude Code mods (spoiler: yes, use one now!)
