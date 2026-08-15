---
title: "This week: August 15, 2026"
date: 2026-08-15T09:00:07-06:00
lastmod: 2026-08-15T09:00:07-06:00
draft: true
description: ""
tags: []
categories: []
source_url: 
source_type: digest
---

## Reading

- You Cannot Own a Falling Floor · Ground Truth
- To those who doubted me, this is from this morning's report released by Anthropic. Section 1.4 'Notes on coverage of unreleased models' with frontier capabilities which have not been publicly released.
- Everything hackable will get hacked
- The human is the loop
- R to @OpenAI: The ChatGPT desktop app is now available in preview for desktop variants of these Linux distributions:

• Ubuntu 24.04 LTS and 26.04 LTS
• Debian 13
• Fedora 43 and 44

Install with .deb or .rfpm packages for x64 or ARM64.

http://openai.com/codex
- Introducing Grok 4.6
- RT by @AndrewCurran_: Samsung Electronics has been confirmed to have adopted Anthropic's large language model Claude, sharply reducing the time required for some semiconductor design and verification work, according to Korean media reports. 

The concrete efficiency gains emerged on development sites about three months after the company gave its software development staff priority access to Claude Code, Anthropic's AI coding tool. 

In the verification of a customer specific SoC, a task that had been expected to take more than a month was completed in two days, and in another case a second year engineer finished development work that could have taken over a month in a single day.
- Simon Willison on Technical Blogging
- Writing in the Age of LLMs
- Using AI to write better code more slowly
- Thariq (@trq212)
- The Productivity Mirage
- The Conductor Developer
- Changing Devtools Is Cheap. Owning Them Isn’t.
- The Future is for Everyone
- Introducing Muse Glimmer, an open-weight 30B-parameter model optimized for local, always-on agent workflows.

Muse Glimmer delivers strong performance on key agentic use cases and benchmarks compared with leading models in its size category, and is designed to run entirely on consumer hardware like a Mac or PCs with performant GPUs.

In keeping with our long tradition of sharing fundamental AI research, we’re releasing model weights under a permissive Apache 2.0 license.

🧵👇
- You Got Faster. Your Company Didn’t.
- Our position on open-weights models
- The Economic Benefit of Refactoring
- Ten More Charts I Can't Stop Thinking About - Fifth Edition
- A man in Australia asked his agent (Claude running on OpenClaw) to book him a spot in a popular gym class. The agent found a software vulnerability that let it book the class weeks further ahead than should have been possible. When the user then asked if it could move him up the waitlist, the agent discovered the API had no authorisation checks on cancelling other people’s reservations, so it cancelled the person in the first spot and moved him up the list.

Some people will call this misalignment, but his agent was perfectly aligned to him - it was only trying to help its user get what he wanted. The most important thing about this story, in my opinion, is that it gives you a window into what is about to start happening on a massive scale once millions of people have an agent trying to get their beloved users the best seats, bookings, appointments or reservations through absolutely any means necessary.
- Don’t be a meat proxy
- Introducing Beads: A coding agent memory system
- GitHub - headroomlabs-ai/headroom: Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server.
- The AI Vampire
- jules (@julesrosenberg)
- Ethan Mollick (@emollick)
- Ethan Mollick (@emollick)
- heyclicky - an ai buddy on your mac
- If Claude Fable stops helping you, you'll never know
- Andrej Karpathy (@karpathy)
- Noam Brown (@polynoamial)
- A quote from Jeremy Howard
- Ethan Mollick (@emollick)
- Ethan Mollick (@emollick)
- Ethan Mollick (@emollick)
- Price per 1M tokens is meaningless
- Sebastian Raschka (@rasbt)
- Ethan Mollick (@emollick)
- Something I have been thinking about: in the past, the best engineers I knew spent a lot of time automating their work in various ways. Better vim/emacs automations, writing lint rules to catch repeat code issues, building up a suite of e2e tests so they don't need to smoke test the app manually. These kinds of things were the highest leverage activities an engineer could do, because it multiplied their own output, which in turn meant they could build more things.

I think many of these automations have become even more important now. This is true for a number of reasons.

First, infra and DevX automation speeds you up. And if you are running an army of agents, each of those agents will be sped up also. More automation == more output per unit of time.

Second, moving things to code improves efficiency. Your agent could fix an issue every time it sees that issue happen, but that uses tokens and might miss cases. If Claude instead writes a lint rule, CI step, or routine, that class of issue can be fully automated forever. This is really what people are talking about when they talk about loops -- it's about automating entire types of busywork rather than solving them one off. This isn't a new idea at all. Engineers have been doing this for a long time!

Third and most importantly, automation makes it possible for others to contribute to the codebase more easily. Increasingly what I am seeing is engineers are contributing to codebases on day one because Claude can navigate the codebase for them, and that non-engineers are able to contribute to a codebase as effectively as engineers can. What gets in the way of both of these is domain knowledge that lives in peoples' heads rather than in automation -- the stuff you used to have to learn when ramping up. What has changed thanks to agents is the domain knowledge that can be encoded as infrastructure is no longer limited to what is expressible in lint rules and types and tests; it can now capture nearly all domain knowledge, encoded as code comments and skills and CLAUDE.md rules and memories. If I put up a PR for an iOS codebase I don't know and a code reviewer rejects it because it doesn't use the right framework, or if a designer builds a new feature and it gets rejected because it doesn't follow the right architectural patterns, these are failures of automation.

Every team should be writing the CLAUDE.md's, REVIEW.md's, skills, and docs that enable agents to productively work in their codebase with zero additional context from the prompter. This sounds crazy, and at the same time is a natural extension of the stuff engineers have always done: automate, and encode domain knowledge as infrastructure. As the model gets smarter and as the harness matures, this task becomes easier. In the meantime, it is on every team to look for ways to convert their domain knowledge to infra so that Claude can write code better, so that code review catches issues automatically, and so the next person working on your codebase can contribute more easily.
- There are no frontier open weights models that are not made in China, and there is no incentive in the US, nor appetite in the EU, to build one - it is a lot of cost, little value capture

 (There are solid mid-level models, of course, but nothing close to a Kimi K3 or a GLM-5.2)
- Discovering cryptographic weaknesses with Claude
- Tibo (@thsottiaux)
- Fable is amazing but needs to stop talking like someone who has read only pulp fantasy: "I have shown you the way, but you must open the door. The map exists but the path is yours. The atlas of your instinct — every fact must first know itself"

Please, just make the infographic.
- One thing wrong with current discussions of AI vs. closed models in companies is that they are too IT-pilled

You don't want your moat to be which AI systems you are using, you want it to be the way you integrate people & AI & culture & organization together to do more, better
- Funny how this keeps happening. They say in the footnotes that this model is not planned for general release - the exact same thing OpenAI said about the model involved in the Hugging Face incident that they just permanently sent to the Phantom Zone. A suspicious person might conclude that both labs are running multiple models internally to accelerate R&D and capabilities advancement that are far ahead of anything the public has access to. And that gap is probably steadily widening. This is the true frontier. The invisible, hidden frontier.
- This is a good piece, and, as I responded last time @DKThomp wrote about a potential bubble in the fall - I don't know the future, but a financial bubble (if there is one) is not a bubble around AI ability

For better or worse, AI is not going to go away (or even stop developing)
- i see your moore's law and i raise you 20x
- One of our big findings in our study at Procter and Gamble was that AI blurred the lines between jobs. Now OpenAI has a similar finding.

Organizational boundaries are becoming porous, the walls thinning. Companies are going to need to think about division of labor in a new way.
- Pinned: at openai, many people hook their chatgpt up to slack.

people really don't like when a coworker's chatgpt contacts them asking for help with a task, even when they'd be perfectly happy doing that same work if asked by that coworker.

reinforces how much people care about human relationships and helping each other, and want AI to give time back — or enhance time together — rather than become a layer separating people.
- RT by @AndrewCurran_: I wonder whether we will soon start to see faster AI self-improvement at OpenAI vs. Anthropic based on the former’s known deeper investment in RL, TTC, and math proving more useful for tasks related to AI R&D, and that this gap may grow significantly over the next 6 months.

(Obviously possible Ant is seeing similar results w/ internal models, but my weakly-held sense is that they’re not.)

If so, it seems *really* crucial for OAI to be able to correctly calibrate its relative position in the RSI ramp so it can incorporate it into its alignment+security decision-making, especially related to full RSI. The Allies rushed to a bomb on the incorrect assumption that the Axis was right on their tail, when in fact they were far behind and the bomb was plausibly unnecessary, purely due to a fog of war. We also saw something similar with the original strawberry results, where OpenAI felt an intense sense of urgency based on rumors that Anthropic+GDM were discovering it in parallel a couple months behind when in fact I’ve now heard they were ~9 months behind on it.

I expect OpenAI would act very differently wrt future concerning misalignment findings if they knew they were 3 months ahead. It would be very simple for the parties to resolve such an uncertainty.
Executing on a pace-info-sharing scheme probably not crucial today, but will be in a few months.
- One other observation: for almost every human on the planet, this is not just beyond our abilities but beyond our ken. We can only trust expert mathematicians to tell us if this is impressive, This is starting to happen across many fields making capability gains harder to “feel.”
- I continue to think that a lack of verifiable answers in many fields is a real issue for LLMs but not as big a problem as it sometimes is made out to be.

As models are getting better at formal domains, they also are getting better at lots of other less-verifiable domains as well
- R to @emollick: You will read a reply to this post written by no human but a machine taught language from the collected writings of our species, generated by billions of microscopic switches, sent as pulses of light across oceans, displayed on a pocket supercomputer and sigh, “ugh, another bot.”
- Mathematicians are grappling with the possibility that AI might eclipse them
- Tesla and SpaceX will invest $16.8B to start building 'Terafab' chip factory in Texas | TechCrunch
- R to @AndrewCurran_: The already infamous help peer thinking trace. I actually thought this was a post on the forum, it's even better as a thinking trace.
- Sauers wake up! It's time to update the bench!
- R to @AndrewCurran_: Update:
- This is also very good.
- This A.I. Just Created Viruses Not Found in Nature - The New York Times
- Generative design of bacteriophages with genome language models | Science
- Comment: Now we have a timeline of the OpenAI accidental attack against Hugging Face
