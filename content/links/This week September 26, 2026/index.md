---
title: "This week: September 26, 2026"
date: 2026-09-26T09:00:07-06:00
lastmod: 2026-09-26T09:00:07-06:00
draft: true
description: ""
tags: []
categories: []
source_url: 
source_type: digest
---

## Reading

- Maybe We Shouldn't Be Reviewing All This Code
- The loudest voices stoking fears about AI dangers have made tremendous headway in the past two weeks. AI technology has not taken some unexpected, dangerous turn, but the hype around it — propelled by what appears to be a well orchestrated PR campaign — has drummed up considerable fear. I worry that it represents a setback for our field.

I have written frequently that fears of AI are overhyped. AI’s capabilities can be uncannily human-like and unpredictable, and it’s rational to worry when people who are directly involved express concerns. But I see the problems as a sign of the engineering work that ahead, rather than insurmountable barriers or the sky falling. AI technology continues to advance — which is a good thing! — but technical advances, poorly understood by the public, give those who seek to generate hype repeated opportunities to do so.

First, I don’t see any step up in the risk of human extinction from AI compared to a few months ago. The theories about this remain the same fantastical, science fiction scenarios as a few months ago. The biggest change in AI risk is its cybersecurity capabilities — a topic which we should take seriously — but this, too, will not lead to the end of the world.

The most notable recent event leading to increased fear was when an OpenAI team deployed an agent swarm that hacked into Hugging Face. Much of the popular press contained significant hype. For example, some publications reported that a swarm of 1,200 agents carried out the attack. While this was technically accurate, as I write this, I have about 1,300 processes running on my laptop. Yes, the ability to get large swarms of agents to work in parallel on a task is a significant technical advance, And, in computing, many processes run at the same time. So this shouldn’t be seen as some magical capability.

Additionally, OpenAI’s buggy sandboxing and monitoring processes were key to enabling this incident. Fixing these bugs and putting in place improved monitoring would be appropriate fixes, not pausing AI. There are many well known ways to attack software systems. The main advantage of AI agents is that they are relentless. They will tirelessly try many tactics — and have the patience to chain vulnerabilities together — that previously would have taken an infeasible amount of human effort. But in the long term, I believe the advantage will lie with defenders (because they have more information with which to identify bugs, which they can fix), but the cyber-threat landscape has changed significantly. There are still bottlenecks to identifying and exploiting a vulnerability. AI agents still have to try a lot of things to see what works, and taking these actions takes time and might be detected by defenders. This is why, even though it is now easy to obtain versions of leading open weight models that have had their guardrails removed or weakened, so they will not refuse to try to execute cyber attacks, the world has not ended.

I am also concerned about the anthropomorphization of AI in a lot of reporting, where LLMs and agents are unnecessarily treated as if they were people. If I wield a hammer, miss a nail, and accidentally dent the wall, it’s not the fault of the hammer. The problem lies in how I used the hammer. Similarly, if I prompt an agent and it hacks into someone else’s system, the responsibility lies with me, not the agent.

Of course, we want to build systems that are as safe and predictable as possible. (For example, an unsafe hammer would be one whose head randomly flies off under normal use.) Today’s agentic systems are not predictable, but I see no reason why, by applying sound engineering practices, we won’t be able to make them extremely safe to use. One new element in the forecasts of AI-enabled doom is AI companies disclaiming responsibility for their own products. “I didn’t do it; my out-of-control agent did!” There’s a balance to be struck between the responsibility of the tool maker and the tool user, but when something goes wrong, let’s hold the people building and/or using the hammer responsible, rather than the hammer. (By the way, if you’re worried about AI bioweapon risk, David Bellamy has a great post on why this, too, is overhyped. Briefly, the bottleneck in building a bioweapon is not intelligence, but lab work and manufacturing.)

Pausing AI progress will create much more harm than benefit. First, our adversaries will certainly not slow down. Second, engineering requires discovering problems empirically so we can fix them. If we pause AI by a decade, we will also delay finding and implementing safety engineering fixes by about the same duration.

Of course, the incentive to stoke fears — for regulatory capture, to garner attention, or to make one’s technology seem more powerful — remains the same as before. Disclaiming responsibility is a new one. Taking a hard technical look at the actual risks however, I see little factual basis for the degree of fear that’s been stoked up. We still have hard research and engineering work ahead to improve AI safety, but the beneficial applications continue to vastly outweigh the risks, and we should keep building.

[Original text (with links): https://www.deeplearning.ai/the-batch/issue-371 ]
- R to @sama: (As a side note, getting ready for this DevDay is the first time I remember ever, in OpenAI history, saying "this is too much stuff to launch".)
- RT by @emollick: People got upset at me for saying this, but there are no companies outside the US and China even *trying* to build frontier AI (perhaps Korea and UK are close), despite marketing claims. Governments saying "sovereign AI" need to understand this.
- Today we announced the Claude-led discovery of a molecular machine that we suspect could represent a new gene editing mechanism. Its precise function, biotechnological utility (if any), or level of significance is not yet clear, but at minimum it is work I would have been proud to do as a PhD student. The work was done mostly, though not entirely, by Claude: our life sciences team suggested a broad area of research, Claude read through the literature and a bunch of genome data and discovered something interesting, then Claude proposed experiments to verify the discovery and our team carried them out.

It’s easy to dismiss this as a one-off or curiosity, but we’ve repeatedly seen a pattern where AI performance in new intellectual domains goes from weak to superhuman in a matter of a few years. In 2023 models struggled to do math at the level of an average high-school student. In 2024 they started to do well on math competitions for the best high-schoolers in the country, in 2025 they started to solve minor open problems, in early 2026 more significant open problems, and in late 2026 they are beginning to solve the top few open problems in all of mathematics. We believe AI for biology is on a similar exponential trend.

The main difference between biology and mathematics, of course, is that math can be done purely theoretically, while biology requires experimentation. Some have used this to draw the conclusion that AI’s utility in biology will be limited. We think this is wrong. As we’ve demonstrated today, humans can collaborate with AI to perform the experiments, validate key results in a few weeks and, if necessary, work with the AI to iterate on what they find. Eventually it may even be possible for Claude itself to safely perform the experiments by autonomously controlling lab equipment, with appropriate safeguards in place, but we aren’t doing that today (our lab is also a BSL1/BSL2 facility that doesn't handle materials dangerous to humans).

More broadly, biomedical advancement has many stages — from fundamental biology discoveries, to translational research, to drug discovery, clinical trials, and finally the actual delivery of medicines and health care to patients. We are also interested in these later stages, but even simply accelerating the first stage of fundamental biological discoveries has the potential to speed up and broaden the entire pipeline. Improving our understanding of biology and sharpening biologists’ tools can drive forward all of the later stages, for example by identifying new drug targets, finding new therapeutic modalities, allowing for more precise measurement, and speeding up the experimental loop which itself further accelerates our understanding of biology. This will not in itself speed up clinical trial times, but if it succeeds it could greatly increase the number of promising candidates that go into the pipeline — an increase in throughput even though latency remains.

In Machines of Loving Grace, I wrote about AI’s potential to “cure most diseases in 5-10 years” — a goal that sounds impossible, but one I believe is just barely possible if AI is applied to every stage of the pipeline. The first step is showing that AI can first help with, and then drive, biological discoveries.

Claude’s discovery is the latest in a line of related prior work that goes back decades, beginning with systems like CRISPR, and continuing with discoveries like the bridge recombinase and VIPR in the past few years. Recently, there has been heightened interest in systems based on reverse transcriptase (RT) enzymes, the enzyme underlying the system Claude identified. And most recently, a Stanford team working independently described a novel RT system with an associated non-coding array that is in some ways similar to the one Claude found, though they are distinct systems that evolved independently from each other. I believe that we’re at the very beginning of finding such systems and developing them into powerful tools for biotechnology.

I’m proud of the resources Anthropic has invested in accelerating the public benefits of AI through the life sciences, and we’re aiming both to grow our life sciences team and to work with other scientists to extend this approach to a broad range of problems. If you have a proposal for a research collaboration or are interested in joining our life sciences team, please reach out.
- Ethan Mollick (@emollick)
- Stuff is happening quite fast.

When asked in September 2025, the best superforecasters put the chance of AI resolving a Millennium Problem by September 2026 at 1.7% and (the more optimistic) industry expert put the chance at 4.6%

They also greatly underestimated AI Lab revenue.
- RT by @bcherny: At Box, we've been testing Opus 5.5 on a variety of complex enterprise knowledge work tasks dealing with unstructured data with the Box Agent.  

Overall, we saw frontier capability levels, with major performance improvements over Opus 5. 63% fewer tokens used, 42% less verbosity, and 30% faster vs. Opus 5. And the model itself is cheaper, so this is a major win for any agentic computer use, coding, analytics, or data work that enterprises will be doing.

Here are some examples of the task wins and performance gains across a variety of industry tests that we performed:

• Financial services - due diligence (+39% task accuracy): A year of transaction records, with the job of finding every miscalculation in an acquisition target's pricing tool. Opus 5.5 scored a perfect result on every  attempt in half the words Opus 5 used, consuming 82% fewer tokens overall.

• Technology - cloud cost analysis (+65% task accuracy): Work out what a company should actually change about its cloud spend. Opus 5.5 picked the right basis for the retention calculation and kept the source data's unit conventions straight all the way through, so the number at the end actually holds up. It took half the time Opus 5 took, with 70% fewer tokens.

• Consumer products - client account analysis (+17% task accuracy): Set the onboarding targets for a client account, reading across the signed contract, a satisfaction tracker and a team metrics sheet. The contract never states a senior/junior split, so Opus 5.5 derived it from the 18-person roster and showed the rule it used; several clients had a perfect 10 on individual survey questions, so it averaged each client's responses instead of crowning the single 10. It finished this one in half the time, on 78% fewer tokens. 

• Clinical diagnostics - data analysis (+15% task accuracy): Malaria rapid-test performance across a dry and a wet season: build the patient records out of two clinical PDFs, compute positive test rates by season and gender, and test whether parasite counts really differ between test-positive and test-negative patients. Opus 5.5 caught that the two groups' standard deviations differed more than 100-fold, re-ran it the right way, and found the dry-season difference didn't hold up after all. This accuracy gain came with a final answer that was half the length of Opus 5's, and also needed 78% fewer tokens end to end. 

Customers will be able to build AI Agents with Opus 5.5 shortly in the Box AI Studio.
- RT by @AndrewCurran_: Opus 5.5 was obviously trained by a much bigger teacher model. Probably  Model-2 Mythos. Opus 5.5 is the first model trained from RSI and also distilled from the internal Ant teacher model.

This is how Opus 5.5 is both smaller and cheaper. It is an artifact of teacher model distillation.
- RT by @AndrewCurran_: > Make a 30s video about what it feels like to be you, using whatever tools you like.

Claude Opus 5.5 (extra)
- Here's who made the cut for tonight's big state dinner at the White House. In the old days, when a noble House was suddenly missing from a royal function, it was a deliberate, public signal from the King that they had lost his protection. Usually your last chance to flee.
- Great thread. It's all true. When I've said similar things in the past, people have accused me of hyping up what the models will eventually be capable of. That's not why I post. I don't work for any of the labs. I don't take money from any of them. I've never taken money to promote anything. I came here for one reason: to warn people about what was coming. 

Everything happening now is a different tiny piece of the same pattern. You can see it everywhere if you look.

Terence Tao, almost exactly two years ago, on OpenAI's o1:

'The experience seemed roughly on par with trying to advise a mediocre, but not completely incompetent, (static simulation of a) graduate student. However, this was an improvement over previous models, whose capability was closer to an actually incompetent (static simulation of a) graduate student. It may only take one or two further iterations of improved capability (and integration with other tools, such as computer algebra packages and proof assistants) until the level of '(static simulation of a) competent graduate student' is reached, at which point I could see this tool being of significant use in research-level tasks.'

Terence Tao, four days ago:

'I mean it's it's it's amazing just how much we are willing to change everything without having any idea what's what's going to happen afterwards. It's it's extremely nonlinear dynamics. Any kind of monotone, one-dimensional thinking - well, oh, a little bit of this is good, therefore a lot of it is going to be a lot better - one of the lessons of math is that most systems don't work like that. Especially if you 10x, 100x things. So, you know, I mean, we're... we have to slow down. I mean, this is, it's insane this pace, and there's no reason to be this fast. There's no reason at all.'

He has seen it. I'm not posting this to belittle him, or what he's feeling. For I have been through it myself. I felt it four years ago, the first time I saw the shape of this. Right now the world is seeing that same shape, that same pattern, in what is happening in math. But this is not about math. OpenAI is not a mathematics company. It is an intelligence company. They didn't put serious resources into math until a few weeks ago, and look what has happened since.

This was not a matter of model capability either. It was a matter of resources, of allocation. Of compute, more of which is coming online every day. Once there is enough of it, the models will expand into more spheres of human expertise, and then into all of them. All the work of the mind. And it will play out there exactly as it is playing out now in math. Everyone will go through what Tao is going through, because all of us have something that means to us what math means to him.

But this is not about math, or art, or copyright. This is about everything, because it generalizes to everything. Pacing the Frontier is not about regulatory capture, IPOs, or crippling the competition. It's part of it, sure, but it's not the main reason. The main reason is fear. Everything happened faster over the last six months than anyone at Anthropic or OpenAI expected. If you know anyone who works there, you know this is true. This isn't a secret. The people who work there are saying it openly.

The old timelines are all blown up. RSI isn't two years out. It's not even a year away. I think we get the real thing by next summer. That's what they've seen internally, and that's the real reason for Pacing the Frontier. After we reach that, I think we will hit the next milestone really quickly. And after that, everything in this world will change. We are not ready for it. We wouldn't be ready if we had another ten years. We only make it through now with the help of extremely capable models, and I think trying to stop now would doom us all. But I have never once, in these last four years, believed that we were going to stop anyway. I don't even think we're going to slow down. We're going straight in. And the only way out is through.
- I Never Want to Use Third-Party Software Again
- Confessions of an Unrepentant Slop Snob
- "Do You Still Read the Code?" • zanlib
- Fragments: September 16
- The new CC, an AI agent built for families
- Lon Lundgren (@Lon)
- The rumors were true once again; they are sitting on multiple major announcements. Open AI announced this morning that the unnamed internal model involved with Navier-Stokes has  resolved more than 100 long-standing open problems across most areas of mathematics.
- One of the reasons AI will change things less quickly than many think is illustrated in this post.

OpenAI is working with mathematicians to ensure they release new proofs in a less disruptive way. The same thing will happen, but more so, with the Bar, the AMA & other professions
- Seeing people build MCPs for agent harnesses they own instead of native tool calls hurts me.

MCPs are meant to allow your functionality to live in someone else harnesses.
- RT by @AndrewCurran_: I think it's time to hang up my Three.js hat.

First of all, this is not a pity post—I'll be fine. I'm also not 100% confident about this.

But I'm an over-sharer and like to talk out loud, so I thought I would share some thoughts on where I see things going and why I'm considering quitting Three.js development.

Some signals I've noticed lately that have gotten me thinking:
- Since Astra was released, I've probably seen at least 10 posts from different people that have achieved similar quality to Three.js Water Pro or better.
- Someone downloaded a video recording of one my posts, fed it to Astra and recreated it with 90% accuracy
- I've had less and less clients referrals
- A Three.js developer I respect very much is retiring from the industry due to impact of AI and lack of interest
- I've heard 2nd hand accounts of other developers losing majority of course/plugin sales due to AI
- I've noticed Three.js posts have shifted from work created by seasoned developers to vibe-coded games and demos.

Fundamentally, I no longer really see value in what I do when it can be replicated so easily.

I've always enjoyed working on hard problems. Naturally, outsourcing the hard part to an agent takes away a lot of the enjoyment for me. High-level orchestration of agents does not tickle my brain in any special way.

At the end of most days I feel unfulfilled and bored. I honestly feel like I've lost much of my critical thinking ability as I've stopped coding. I find it harder to focus on tasks and my attention-span and comprehension is noticeably dropping.

My plan right now is to finish up Water Pro v4 and see how that performs. After that, I think it's time to start thinking about what else is out there for me.

I'd love to hear thoughts from other developers & freelancers on the matter, positive or negative.

Feel free to vent!
- I don't like LLMs
- They used Opus 5 to pull off the hack. It appears they had access to the loosened cyber-guardrail version of Opus. They successfully accessed the OAI internal monorepo. The question that will be asked is, if these three guys can pull this off, what can a nation state do.
- RT by @bcherny: We're adding support for AGENTS.md to Claude Code. 

Starting today in version 2.1.277, if there is no CLAUDE.md in a folder, Claude will check for and use AGENTS.md.

You can toggle this behavior in /config.
