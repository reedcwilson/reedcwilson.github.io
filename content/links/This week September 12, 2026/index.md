---
title: "This week: September 12, 2026"
date: 2026-09-12T09:00:07-06:00
lastmod: 2026-09-12T09:00:07-06:00
draft: true
description: ""
tags: []
categories: []
source_url: 
source_type: digest
---

## Reading

- Comment: Feeling sad about AI
- R to @AndrewCurran_: Sebastien Bubeck:
- RT by @sama: This model represents a step-function improvement on many benchmarks, and its training is ongoing.

Our internal model group arrived at the Navier–Stokes solution in 88 hours, using around 10,000 coordinating AI agents. 

Throughout the effort, we maintained the strict safeguards—including monitoring and isolation—that we apply to all our frontier evaluations.
- I spent much of the weekend talking with the team who did this work. Seb--and everyone else--acted with integrity and generosity throughout.

Initially we believed the other team had also solved the problem. We wanted to collaborate and do a joint release. 

When we learned that they had Euler but not Navier-Stokes, we offered to let them go first, to suggest that they should be the ones to get the prize, and optionally for Tristan to be the lead author on a rewrite of the OpenAI proof. We felt it was challenging to offer the same to Levent (an Anthropic employee), who was not willing to talk or coordinate with us anyway. We were open to other solutions.

We would have greatly preferred coordination. We did not rush to publish even though the other team wasn't communicating with us. The team threatened us with unfounded accusations of plagarism.

Now that we can see their work, the approaches appear to be different. It is also worth noting that our latest model can solve many, many other math problems.

It is true that we tried this because there were rumors on the internet last week that Anthropic's models had solved a millennium problem and we were curious if ours could do it too.
- Quick, spread some rumors about other really hard problems that Anthropic is on the verge of solving.
- Increasingly clear over the past two weeks that however much your company is worried about the cybersecurity environment, it is not worried enough.

The WeWorm demonstration shows how effective bad actors can be. The Hugging Face Incident shows you don’t even need bad actors.
- Ethan Mollick (@emollick)
- I am deskilling myself with AI so quickly on so many annoying tasks I don't want or need to be skilled at. Cannot deskill on these fast enough.
- A critical factor in using agents successfully in Codex and Code is deciding when & how to use these options.

If you are not steering long-running agentic work, then you probably aren't managing agents enough (or building interim reporting to give you visibility along the way)
- OpenAI confirmed to the New York Times that they have made "substantial progress" on another Millennium Prize problem in the last five days, and are preparing to announce.

The rumors for the last 48 hours have been OpenAI solved the Hodge Conjecture, and that Anthropic has solved the Birch and Swinnerton-Dyer Conjecture. Since Navier-Stokes rumors abound, so I was reluctant to post about either. However, OpenAI's statement to the NYT now gives the Hodge rumors some very serious support.

In general people have not updated yet that the new unnamed OpenAI model, the one that finished training about two weeks ago, which I believe will be named Aeon, is massively better at math than Astra, which two weeks ago was the best in the world. Aeon solved Navier-Stokes in 88 hours, start to finish. Follow the trend line. That means everything is on the table. Literally everything. And this does not end with math. Please update. We are taking off.
- What you are seeing in math right now is a consequence of the jagged frontier, and a precursor of what is to come in other professions. Yes, mathematicians do math, but they also have other tasks they view as important (mentor students, maintain a scientific community, safeguard the future of a field, foster a love of math) that AI can't do.

At least one worry that mathematicians seem to have is that by focusing on the flashiest, most obvious element of what mathematicians do (make proofs), the AI companies are damaging the other tasks that AI can't do. AI can discover superhuman proofs, but that is not all that the math profession is about, and actually can undermine and reduce the attention to the other aspects of the job that are important to mathematicians. It becomes harder to defend the value of the many other tasks mathematicians do to the outside world if the most visible part is taken away.

I suspect we will see more of this across fields and professions that will increasingly be forced to help people understand that their jobs consist not only the most visible tasks that AI can do, but also tasks that the AI cannot do or does badly.
- On the Navier–Stokes Millennium Prize Problem
- The loop closes
- Introducing Claude Fable 5.1 and Claude Mythos 5.1
- Claude Fable 5.1 tops the Artificial Analysis Intelligence Index
- RT by @AndrewCurran_: 'At a minimum, the creative possibilities and public benefits that LLM training advances far outweigh any competitive harm (even assuming such harm is cognizable). The entire reason that Al models are rapidly reshaping the economy and national security is that they help people, including those working in creative fields, make things and get things done. LLMs can inspire or help someone to write a story, compose a song, write a movie script, or produce any other kind of art.'

'Given all these considerations, the fourth factor heavily favors fair use. At a minimum, any effect on the market for the copyrighted works cannot overcome the significant, world-changing value of the training use's transformative purpose.'
- R to @AndrewCurran_: 'With Astra, we’re introducing a new way for Codex to preserve and retrieve context when the context window fills. Historically, models have used compaction to summarize work during long sessions, such as when debugging complex issues or tackling large refactors. Each compaction can leave out details about why a fix failed or how a component behaves. In Codex, Astra can keep notes across context windows, preserving accumulated details without repeatedly compressing them into a single summary. Earlier context windows remain searchable, so Astra can find requirements or test results from previous messages and tool outputs—even if that information wasn’t captured in its notes.'
- R to @AndrewCurran_: Tibo clearing up some confusion:
'It was very important to us that we bring it to all Plus users and not only Pro, Business and Enterprise.

It will take a few days for the rollout to complete and behind the scenes many novel systems will operate at scale for the first time and we are bringing a lot of compute up.'
- Cursor was one of OpenAI's top five customers by revenue when OpenAI ended the deal last week, and had been projected to bring in more than $1 billion in annualized revenue. But OpenAI still chose to walk away rather than do business with Elon. The vendetta continues.
- An example of useful knowledge work: I assigned GPT-6 to read through tens of thousands of my emails, my writings, my calendar appointments and more to assemble a personal knowledge base of research, contacts, ideas, relationships, and tasks over my recent career. GPT-6 downloaded the appropriate software, figured out a strategy, and built a multi-gigabyte personal wiki without any further intervention from me over the course of five days of uninterrupted work.

Twice a day, the AI now goes through my emails, cross-references them with this extensive knowledge base, and sends me a summary of things I should be paying attention to, things I might be interested in, etc. 

(Two questions you may have: Yes, I gave the AI access to my computer and this involves risks, and you should be careful before you do the same. And I do not take money from any AI lab and pay for my own usage, but during the trial period, I was not charged for tokens, so I cannot tell you how much this process would have cost, but it likely would have been very substantial. The ongoing briefings do not use substantial amounts of token)
- One thing that makes Astra (and Fable) so interesting and, in some ways, so hard to grapple with is that they just take action.

I asked for an ill-defined deliverable in Blender and Astra spins up a historical research agent and a visual critic etc. & just starts doing stuff.
- TIL: Using Blender with coding agents on macOS
- President Trump declared on Truth Social this morning that 'The Moon is ours.' The implication is that the Moon is a sovereign territory of the United States of America, which is great news for Elon's lunar data center.
- If you are competing against OpenAI or Anthropic, you are going up against people using models two generations ahead of the best public models in the world, burning through $7k–$10k worth of tokens per day on an infinite token budget, running at 8x normal speed.
- I would buy that we are in an AGI era for "jagged AGI" (better than human in many areas, worse in others) but is that AGI? If you mean better than a human expert at most human tasks, we aren't there (yet?).

But it is still astonishing that AI is where it is & got there so fast.
- There's No Limit to How Bad Code Can Get
