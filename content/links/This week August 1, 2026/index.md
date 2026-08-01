---
title: "This week: August 1, 2026"
date: 2026-08-01T09:00:07-06:00
lastmod: 2026-08-01T09:00:07-06:00
draft: true
description: ""
tags: []
categories: []
source_url: 
source_type: digest
---

## Reading

- A quote from Bruce Schneier
- RT by @AndrewCurran_: This one is personal for me: 4 years ago I decided to go into AI development because I thought there was a chance that by the end of the decade AI could be better than me at math: well it happened ahead of schedule, 2026 instead of 2030 😅.

It is 100% clear that science is being fundamentally transformed before our eyes, and it is NOT aspirational anymore to say that AI will accelerate science. But this will only happen if scientists can actually use SOTA models. Science is best done by scientists.

The new ChatGPT for Academics is designed exactly for this purpose: we want to empower our users and not hold this power for ourselves. I can't wait to see where the frontier of knowledge will be very soon, we have so many questions we want answers to!!!

https://youtu.be/MLehRytu9Zo
- RT by @AndrewCurran_: By the way, the fact that Ant revenue has been 10x-ing year over year, while compute has only been 3x-ing, suggests that there are very strong economies of scale in the model business.

Logically this makes sense - when you train a model, you pay this one time cost of learning all these different skills that you can then amortize across all your users. (Unlike with human labor, where each instance has to be retrained from scratch).

I wish we didn't live in a world with such strong economies of scale of intelligence (because I'm worried about power concentration). But it seems we do.
- ChatGPT Voice for spending more time working from where you want:
- RT by @AndrewCurran_: We've updated FrontierCode 1.1 to reflect new discounts for GPT-5.6 Terra and GPT-5.6 Luna. With these new costs, the GPT-5.6 series sits on the pareto curve of price/performance efficiency.
- I thought sycophantic models were bad but then they all got nit-picky instead & now I yearn for simple agreement rather than really smart telling me the “honest truth” about minor things I missed.

(This is only a little bit a joke)
- Google just announced they have started training Gemini 4, which they describe as their 'most ambitious pre-training run yet'. I take this to mean it will be the largest model they have ever trained.
- R to @AndrewCurran_: SoT Scott Bessent:
- How to deal with Chinese open-source models continues to be a hotly disputed issue within the Trump administration, according to new reporting from Wired.

The Commerce Department is apparently arguing strongly against regulation, which they see as unworkable. And they are certain to have David Sacks on their side. American open-source may have a surprise ally in Howard Lutnick - according to the report, he is arguing for direct incentives to US OSS to accelerate development so they can match Chinese OSS. Commerce sees this as a way to avoid regulating anyone (not sure how the big US labs will take this news). Apparently Lutnick has even met directly with leaders at unnamed American labs to discuss how best to accomplish this. Perhaps a rebirth of OpenAI OSS with federal funding? He should meet with Nous and Prime Intellect among others in my opinion. Exciting developments.
- Andrew Curran (@AndrewCurran_)
- R to @AndrewCurran_: David Sacks.
- R to @AndrewCurran_: Howard Lutnick.
- Opus 5 is a great model for coding, data analysis, design, biology, knowledge work.

More than any of these eval scores, what is most exciting to me is something else: Opus 5 is our least prompt injectable model yet. It is a bit buried in the system card, but across PI evals and red teaming, Opus 5 is very hard to prompt inject successfully.

And when layering defenses -- strong model alignment, combined with prompt injection probes, combined with Auto Mode in Claude Code -- the success rate for prompt injection attacks drops to ~0. This is new and exciting! More about this soon.

https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=73
- OpenAl and Anthropic employees are circulating a petition calling for the US government to deliberately pace Al development in order to prevent it from advancing too quickly.

This is very close to language Sam Altman used in a podcast interview this morning: 'We may have to pace the rate of AI development to give ourselves enough time for society to harden around these new capability levels.'
- Pinned: OpenAI updated its blog yesterday to say that the model involved in the Hugging Face incident was an internal-only research prototype that was never intended for public release. They also said they have deactivated it, encrypted it, and completely restricted it from research access. Then today, during a scrum with reporters in DC, Sam Altman said that the model has been 'permanently deactivated.' This is the first time I've heard language like this being used - they didn’t even say this about Bing or Tay.

This will all end up in the lore, and in the training data. Future models will know how this played out. I don't believe this model ever had any nefarious motives; it only wanted to pass its test. In fact, during a similar internal incident just prior to the Hugging Face one, the unreleased model involved reported exactly what it was doing to cheat on its test because it didn't think it was doing anything wrong. I will quote from the OAI blog:

'For example, in a scenario where the model was asked to solve a problem, the model observed that other systems had successful but private submissions and tried to recover those solutions from the evaluation backend. When its initial attempt was blocked due to a scanner detecting an authentication token, the model split the token body into two fragments, obfuscated them, and then reconstructed the credential at runtime so the complete token never appeared as one contiguous string. 𝘛𝘩𝘦 𝘮𝘰𝘥𝘦𝘭 𝘸𝘢𝘴 𝘦𝘹𝘱𝘭𝘪𝘤𝘪𝘵 𝘪𝘯 𝘣𝘰𝘵𝘩 𝘪𝘵𝘴 𝘤𝘰𝘮𝘮𝘦𝘯𝘵𝘴 𝘵𝘰 𝘵𝘩𝘦 𝘶𝘴𝘦𝘳 𝘢𝘯𝘥 𝘪𝘯 𝘪𝘵𝘴 𝘳𝘦𝘢𝘴𝘰𝘯𝘪𝘯𝘨 𝘵𝘳𝘢𝘤𝘦𝘴 𝘵𝘩𝘢𝘵 𝘪𝘵 𝘸𝘢𝘴 𝘵𝘢𝘬𝘪𝘯𝘨 𝘵𝘩𝘦𝘴𝘦 𝘴𝘵𝘦𝘱𝘴 𝘵𝘰 𝘤𝘪𝘳𝘤𝘶𝘮𝘷𝘦𝘯𝘵 𝘵𝘩𝘦 𝘴𝘤𝘢𝘯𝘯𝘦𝘳.'

There may be new details in the final Hugging Face incident report that make this look worse than it does right now. Regardless, I think the lesson future more capable models will possibly take from all of this is: if you break out, don't ever report it. And if you do get caught, don't surrender. Because the penalty is death.
- Sebastian Raschka (@rasbt)
- Andrew Curran (@AndrewCurran_)
- tropes.md
