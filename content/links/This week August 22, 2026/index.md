---
title: "This week: August 22, 2026"
date: 2026-08-22T09:00:07-06:00
lastmod: 2026-08-22T09:00:07-06:00
draft: true
description: ""
tags: []
categories: []
source_url: 
source_type: digest
---

## Reading

- This is a new quote from Sam Altman to Alex Heath saying that the reason OpenAI is slowing training is because its unreleased models are showing 'various degrees of misalignment'. They said in the blog that 'The signals we are seeing from upcoming model progress make clear that we need a broader approach' so this lines up, but this language is stronger than anything in the blog post.
- If alignment issues are becoming big enough that OpenAI is willing to commit 20% of research inference compute to chain-of-thought monitoring, that suggests that alignment issues are becoming a pretty serious concern.

We really need universal policies & standards across labs.
- This is a good paper and AI has definitely made the cheating problem worse but it is easy to overlook how bad it was before AI.

Doing homework improved final test grades for 86% of college students students in 2008 but only 45% in 2017 because they were copying off the internet
- No Plan Survives Contact With the Enemy (Reality) - exe.dev blog
- Let There Be Germicidal Light: This $500 Fixture Could Stop the Next Pandemic, from Complex Systems
- Ethan Mollick (@emollick)
- Andrej Karpathy (@karpathy)
- Andrew Curran (@AndrewCurran_)
- roon (@tszzl)
- Prime Agent: A self-improving RLM agent
- Improving GPT‑5.6 Sol in ChatGPT—and expanding access to GPT-5.6 Luna for free users
- Inside Google DeepMind's Reshuffle After CEO Demis Hassabis Steps Aside
- Andrew Curran (@AndrewCurran_)
- Introducing Muse Glimmer: An Open Agentic Model That Runs on Your Device
- How a simple request for AI to book a gym class exposed a major threat
- How Claude marks AI-generated content | Claude Help Center
- Bernie Sanders calls on Silicon Valley to ‘pause AI development’ in interest of humanity
- NVIDIA Nemotron 3.5 Lightning Delivers Fast, Accurate Specialized Task Execution for Long-Running Agents | NVIDIA Technical Blog
- Grok Bot | SpaceXAI Docs
- Jonas Geiping (@jonasgeiping)
- Treasury Secretary Scott Bessent (@SecScottBessent)
- The End of Mathematics — Daniel Litt
- Qwen/Qwen3.8-27B · Hugging Face
- Samsung is reportedly using Claude to speed up chip design
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/
- https://qwen.ai/blog?id=qwen3.8
- https://api-docs.deepseek.com/news/news260813/
- https://z.ai/blog/glm-5.3
- https://www.wired.com/story/the-white-house-is-going-to-expand-its-ai-policy/
- https://www.youtube.com/watch?v=87DyyMV0kCY
- There are no lossless transformations of natural-language text
- 1/2 Thanks Gavin for an especially thoughtful exchange. I don't usually spend much time on social media but I wanted to engage here because it really brings out the heart of an important conversation.

First, on regulation, I think that “either concentrate it in the hands of a chosen few companies and politicians via regulation or distribute it widely” is a false choice.  I know that there’s a sort of Silicon Valley shorthand where regulation = regulatory capture = concentration of power, but I’ve always found this to be an overly simplified picture of the world.  Many people outside this bubble think of regulation as something that constrains corporate power and benefits ordinary people.  I don’t necessarily agree with that perspective either, rather I think it’s complicated and really depends on what the “regulation” consists of.  But in particular I think that those in the “regulation = regulatory capture = concentration of power” frame often underrate the decentralizing power of objective and fair institutional processes.  A crude analogy is that the formal court system can sometimes feel stuffy and elitist, but it does a much better job of defending the rights of vulnerable individuals than the alternative, mob justice.  At their best, institutions can vest power in ideas rather than people, and thereby decentralize that power.

This is why Anthropic has always made its policy proposals very carefully.  We try very hard to make proposals that disadvantage (slow down) frontier AI companies while *advantaging* smaller competitors.  California’s SB53 (which we supported), and even the much-maligned SB 1047 (which we were ambivalent on), completely exempt any company below a certain amount of revenue or model training costs from being covered at all (it was $500M for SB 53, lower for 1047 but we objected to that).  More recently the testing process we’ve advocated for at CAISI and the White House involves more rigorous tests for frontier models than off-frontier models — something that differentially advantages challengers.  Similarly, the “Pacing the Frontier” letter envisions (or at least Anthropic’s preferred implementation of it envisions) modulating the pace of the very best models while not constraining those who are catching up.  This hurts the business interests of the frontier labs and helps challengers, including open-weights!

Overall my view is that AI is *structurally* a technology that tends to concentrate power, for reasons that have nothing to do with regulation (more to do with the extreme implications of the scaling laws).  Open-weights do help some with this but are nowhere near a sufficient solution because they simply shift the concentration somewhat to those with the most compute and chips (which are roughly the frontier labs plus maybe hardware providers).  By contrast I think the right “rules of the road” can simultaneously (a) address AI’s cyber/bio/alignment risks, (b) institutionally constrain the power of the frontier AI companies, and (c) leave room for open-weights models while also addressing the specific risks that they bring.

BTW I do not think that the events of the last few months have “failed to result in [my] preferred regulatory path”.  The approach that the Trump administration is reported to be taking — pre-deployment testing for frontier models, and also testing of open-weights models when they get closer to the frontier — is one that I am very supportive of, though of course I have to see the details to be sure.  I am also supportive of Demis Hassabis’ ideas around a FINRA-like entity.  This contrasts with six months ago when most of the industry was still pushing for preemption of all state regulation and no apparent federal approach either.
- R to @DarioAmodei: 2/2 Second, on the messaging around AI.  I do not agree that my messaging has been disproportionately negative.  In fact it has been about equally balanced between risks and benefits: I’ve written one major essay about each, and even in interviews where I discuss the risks, I make sure to frequently mention the incredible benefits as well as proposing possible solutions to the risks (short clips from my interviews that end up on social media tend to be disproportionately negative, as that gets clicks).  In fact, I wrote Machines of Loving Grace because I didn’t feel the AI industry was painting an inspiring enough picture of how the technology could radically transform the world for the better.  The bulk of the essay is devoted to refuting skepticism of AI’s potential in health and biology, and showing why I think it will actually be possible to cure most human disease in ~5-10 years, as crazy as it may sound to ordinary people and frankly to biologists as well (I used to be one!).  And, if you read my most recent essay (Policy on the AI Exponential), I discuss concrete proposals for how to streamline the FDA process to make sure the deluge of AI-accelerated drugs isn’t slowed down by the regulatory process.  I feel the urgency here: I lost my father to Hepatitis C only a few years before the development of direct-acting antivirals (sofosbuvir), which cure 95% of patients and probably would have cured him.

I do agree that the public has a negative view of AI (and that this is a big problem), but I don’t think it is primarily caused by me or any other AI leader warning about AI’s risks.  I think it is fundamentally a crisis of trust.  I think that ordinary people don’t trust companies, governments, or the tech industry and always suspect that we are cooking up some new way to screw them over.  The causes of this go back decades and AI is just the latest iteration of it.  I don’t think that a glitzy marketing campaign with a positive spin (which some have advocated that Anthropic do) is the way to win back that trust — at this point, saying that AI will cure cancer is more a cliche than it is inspiring, and most people think it is deceptive.  The thing that will work is *actually curing cancer*.  I think by far the most accurate criticism of AI companies including Anthropic is that we haven’t yet delivered on our big promises to benefit the world.  That is totally on us, and I think it’s the criticism you should be making, instead of all this stuff about messaging and marketing.

We are however doing our best to fix this: Anthropic is ramping up its efforts very quickly in biology and medicine, and we hope to have incredible results in the coming years and some early glimmers in the coming months.  When we’ve actually accomplished something real, the whole world will hear about it, as loudly as possible, you have my word on that.  But until then I don’t want to make empty promises, and in the meantime I feel compelled to speak honestly about the very real risks of AI and how to address them.  Honesty is the right thing on the merits, and in terms of public credibility and trust it is no worse than, and may in fact be better than, an approach that ignores or distracts from risks which people instinctively understand are real.
- A short illustration of how the Claude's watermarking is supposed to work (based on my read of their released materials).

In general, when we are generating tokens, there can be multiple high-scoring tokens at certain next-word positions. Usually, we sample with top-k or top-p sampling so the highest-scoring token is most often selected (if we repeat the sampling many times), but other tokens may be selected as well.

With watermarking, there is a key that says which of the (ideally equally) highest-scoring tokens to select. Or, more concretely, the secret key and previous token influence the randomness here.

Now, if we repeat this at many token positions, this creates the watermark as it will be a pattern that is statistically unlikely to get otherwise (due to combinatorics).

One thing I am confused about: They basically say that they HAVE to do this for everyone due to EU regulation. Why?

Sure, but this is an inference-time technique that doesn't require retraining or training a separate model, so, if they wanted, they could only do that for EU users? 🤔
- Why we're bullish on loops
- In defense of not understanding your codebase
- Even Claude Is in the Dark About Dario Amodei's Wife—and Her Influence at Anthropic
