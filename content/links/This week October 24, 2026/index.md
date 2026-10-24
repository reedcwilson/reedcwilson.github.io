---
title: "This week: October 24, 2026"
date: 2026-10-24T09:00:09-06:00
lastmod: 2026-10-24T09:00:09-06:00
draft: true
description: ""
tags: []
categories: []
source_url: 
source_type: digest
---

## Reading

- Recursive launches Flint, a laptop coding model it says was largely built by AI
- Thank you for this, @_NathanCalvin. I appreciate and am a fan of the investigative work you’ve done on behalf of AI safety and believe your comments are coming from a constructive, honest place, and that it benefits the public to have people whose job is to scrutinize the actions of frontier AI companies. I think something would be wrong if companies of the size of Anthropic didn’t get harshly criticized basically every day; strong antibodies against corporate power are a healthy feature of a free society, and especially so when issues of the gravity of the one we’re facing are at play. I also do agree that some of the examples you cite were mistakes by Anthropic.

That said, I disagree with the thrust of your post. At the core, a good fraction of the things you criticize are consequences of Anthropic’s basic theory of change that we have held for many years. Our strategy has always been what I’ve called the “race to the top” — by showing how it’s possible to build the technology responsibly, we can raise the bar for the entire industry. The forces that drive the race to the top are hugely more effective if the company practicing them is at the frontier; that’s one lesson I’ve learned repeatedly. And looking at that strategy as a whole, I’m proud of our track record and stand by it.

I believe that if we take a list of things that Anthropic did in the past year that were pro-safety and commercially costly to us, they far outweigh the list you’ve made, while at the same time I also disagree with some of the items on your list. Here are some things Anthropic has done, in the same period you’ve cited (the last year), which were very costly to us commercially while having strong safety benefits:

1. We played a key role in SB53 (and other state laws), at a time when doing so was politically perilous to the company and AI regulation was very unpopular. We in fact argued for a stronger version of SB53 than was ultimately passed; there were a lot of stakeholders and we were not the limiting factor in the strength of the bill that was passed.

2. We have very strong biological safeguards on our models, because we’ve seen concerning results in bio uplift trials and even seen and blocked potential attempts to misuse our models for bioweapons (as seen in our threat intelligence report from a few weeks ago). This is a very serious threat that we want to have zero tolerance for. But having very low false negatives means having significant false positives (despite months of effort on our part to improve the classifiers), enough so that biologists joke about how restrictive our classifiers are, and competitors sometimes sell against us by touting their more permissive bio capabilities. This has been very painful to us in an area where we care a lot about supporting an ecosystem of Claude users (biomedical science; and it is particularly frustrating to me as a biologist), but it’s the right thing to do and we intend to keep doing it.

3. Similarly, we first had Mythos-class models in February but didn’t make them generally available until June (when we had stronger cyber safeguards in place). We only offered them to a limited set of partners in order to focus on cyberdefense. It would have been much more economically rational to simply release the model to everyone. We likely sacrificed a significant chunk of a several-month model lead. But because of this, many companies secured their cyber infrastructure before the deluge of widely available cyber-capable models. Of course there are ways it could have gone better or been run better, but this was what we were aiming to do.

4. I advocated forcefully and publicly, in my essay Policy on the AI Exponential in June of this year, for the government to have the power to block model releases. Back then this was still outside or maybe on the edge of the Overton window, though I understand the window has moved since then. We were attacked intensely for this.

5. I don’t want to re-ignite conflict, but the events of February 2026 are a strong example. It is clear that our public stance could have seriously damaged the company’s future.

6. We’ve continued to advocate for export controls on chips and chipmaking equipment to China, because we think it allows democracies to negotiate from a position of strength on AI safety agreements. We’ve done this despite problems it’s created for us with industry partners who hold very different views and on whom we are very dependent.

7. As far as I’m aware we were the first, and still only, frontier company to restrict the sale of AI services to PRC-controlled companies, including those operating through third countries (otherwise a major loophole). We’ve therefore forfeited significant short-term business to prevent fueling AI platforms and applications that would help the CCP’s military and intelligence services. We are also cracking down on distillation; generally, distillation is not a major threat to us commercially, but like chip exports it has concerning national security and safety implications, so we expend significant energy and company resources to address it.

8. As you mentioned, we’ve put out a lot of reports, announcements, long model cards, public advocacy, etc, all trying to inform the public about the risks of AI. These involve a level of detail and effort that would be implausible for a purely profit-maximizing company.

9. Just this week, we announced we were putting 5% (and possibly more over time) of the company into a public benefit fund.

All of these decisions came with very substantial costs to us. To be fair, those that involved holding back or restricting access to frontier capabilities also had a broader cost — for example, the public might otherwise have benefitted from faster progress in biology, so I am not saying that our decisions were without tradeoffs — but they were not driven by profit-seeking.

For each decision, you can come up with ulterior motives that could have driven us — I think it is a general truth that any decision, on any topic, can always be portrayed as a nefarious scheme. But most of those end up being pretty farfetched or don’t fully make sense if you actually examine them closely. For example, it is deeply implausible that it would be a shrewd business move to block a large swath of research biology in order to do the work ourselves and compete with our customers; we expect the benefit to the ecosystem to greatly exceed the work Anthropic does itself, and for the two to complement each other. It is not in Anthropic’s interest to be perceived as unfriendly to biologists. Our Life Sciences Verification Program, which gives vetted biology professionals access to our models, also refutes this idea. 

Of course, a different set of people will see this and make a different criticism: that Anthropic shouldn't be making decisions about who gets access to what in the first place. I agree, in the sense that ideally the government would be making these decisions, and that’s why we advocate for regulation. But for now we are forced to make them, and enabling bioterrorism isn’t a better option.

I think that even if I conceded every item in your list, I would happily hold up mine next to it; I don’t think it’s a close call. That is of course partly subjective and different things are important to different people. Maybe one way you could object is that several of the items above relate to AI misuse and not loss-of-control; if you think the latter is much more important than the former, that might change your calculus. But this is not Anthropic’s view — we view both as serious issues. You can also disagree with our decisions, as many have, but they are consistent.

But I also disagree with at least some of your list. Several items don’t represent a deviation from Anthropic’s strategy or values at all, once we postulate the “race to the top” strategy that requires being a frontier AI company. Your items 1-4 are all simply examples of what it means to compete at the frontier, and we stand by them, both in the sense that they are transparently ordinary things to do as part of that strategy, and that we stand by the strategy as a whole. 

To be fair, there are important questions worth confronting (and that we are confronting) about what to do when the AI-driven acceleration gets fast enough that it is hard for safety to keep up. We are nearing that point and that’s what’s driving some of our thinking about “pacing.” But 1-4 are actions taken before that point and should be perfectly expected based on Anthropic’s strategy as a company. Of course it is possible to disagree with that strategy, but that’s a more fundamental disagreement that you could have had any time over the last few years.

I agree we could have handled your items 7, 8, and 9 better. All fall into the category of “rhetoric or policy communication that wasn’t carefully written or resulting from fast-changing circumstances not propagating from one team to another fast enough.” This kind of thing happens a lot in large organizations (Anthropic is over 5,000 people), and doesn’t even necessarily represent a failure or mistake of any single person. I am of course the CEO, and I take responsibility. The volume of communication from Anthropic is enormous and if these are the worst examples, I think we’re frankly doing pretty well, though I will continue to work hard to make sure we do even better.

Your 5th item (the change to our RSP) is the most substantive item, and people can debate this, but I think that the old, more rigid RSP created a lot of situations where we were technically required to do something that required a lot of effort but in retrospect wasn’t very important for safety, as well as not covering some of the most important things. Our current RSP’s focus on transparency brought things like risk reports and roadmaps, and its emphasis on independent external review laid the groundwork for even more intensive embedded evaluation, all of which I think have been valuable in driving a race to the top. In the original announcement in September 2023, we described the RSP as an “early iteration that we [would] build on” and said that “rapid iteration…will almost certainly be necessary.” I understand that changing plans is always a move that creates justifiable scrutiny — I just don’t think we ever represented that we wouldn’t do so.

Relating to your 6th item (having an FCF in addition to our RSP), I know our intent is to meet the letter and spirit of our regulatory obligations (via our FCF) while also remaining able to experiment with more novel approaches to risk management that go beyond what the law currently requires (via our RSP). I promise to look into it further, as it’s a complex issue and it is possible we are not weighing the considerations in the right way.

Overall, although Anthropic has made plenty of mistakes as an organization — including some of the items on your list — I feel that we have repeatedly taken serious and substantive actions counter to our bottom line and that there is a significant negativity bias distorting assessments like the one you are making above. We’ll always try to do better but, again, I am extremely proud of our track record and stand by it. I will have more to say soon about how we are going to further live our values in this moment of rapid change.
- My obituary for programming
- What will we use our minds for?
- Own Every Word
- I hate this slide every time it comes up, and now from CSAIL

This has been false since before the slide was made. Automated systems make management decisions all the time (trading, logistics, customer service, insurance) & pretending they don't actually launders responsibility.
- Redesigning source control at Anthropic
- Significant update from Jack Clark this morning. His RSI timelines have moved up. He now says it is likely that full RSI will become possible in 2027, and that creativity was the last piece. I think we are less than six months away from closing the loop.
- OpenAI's offices were bugged by an employee. The employee has been terminated. The FBI has made an arrest. Detective Astra with the assist.
- The final frontier.
- Ethan Mollick (@emollick)
- Using Gemini 4 makes you realize how many other models must be distilling Claude/GPT (or using a similar training pipeline). It feels quite different than other models.
- Epic Games reportedly pivoting to "AI first" game development model
- Software engineers don't get to be Luddites about AI
- AI is mass decompiling games. That’s both awesome and scary.
- Anthropic tells investors quarterly revenue up nearly 50% to $16.8bn ahead of IPO
- We will soon see what will be, in effect, a perfectly legal distributed denial of service attack on customer service departments authorized by millions of consumers when it becomes widely known that Muse/Dot/etc can make unlimited requests for old refunds, negotiate deals, etc.
- If you don't use the models or watch the demos people post on social media, you may not realize there has been an astonishing jump in game development capability lately. We really are not that far away from a one-person game studio anymore.

You can mash up games now and the model will deliver a stable, playable fusion in one day. Some of them are so good that people don't post them openly online because they are afraid of getting sued. That's how quickly things have improved over the last few weeks with Astra and Opus 5.5.

Because of how virulently anti-AI the game industry has become, people are going to get completely blindsided by what's about to arrive. Not only are they unaware of how fast things are improving, they don't seem to understand the endgame. I see people taking about supply gluts, things like that.  This isn't about making games to sell on Steam and compete with the industry. If the player knows the type of game they want, and their model can code that game for them at the AAA level, in the genre they ask for, with the aesthetics and character design they prefer, then the question becomes: why buy a game from a studio at all?

I think Sir Demis sees this future with Genie. For the price of your subscription, you will get any style of game you want, tailored to you. Once that starts happening at scale, most game studios will very rapidly cease to exist. And that's the real endgame. Not competition; destruction. And it's closer than people think.
- This is a AAA game, a Marvel/Star Wars FPS, and Epic Games is vibe coding it. The directive went out to devs last week: 'No more hand-written code,' and all the art will be generated by AI as well. Claude is on the job. Things have changed dramatically over the last few weeks.
- R to @AndrewCurran_: Special guest star:
- Replit's CEO says the future of work is the 'self-driving company' | TechCrunch
- Dwarkesh told Tyler Cowen on the NYT podcast that Anthropic believes Claude will surpasses human researchers within nine months. I said it would be by the summer, so I'm feeling good about my prediction.
- R to @AndrewCurran_: Two days ago:
- R to @AndrewCurran_: roon again:
- Quoting from Anthropic's Michael Sellitto at the IMF Artificial Intelligence and Escalating Cyber Risks panel today. This is the first time Anthropic has given a projection for what percentage of frontier model training will be done by Claude in 2027. In March this number was 1%. By next year they are projecting 80-90%.

'Last year, about zero percent of our code was written by our model Claude. By August of that year, about 50% of the code inside the company was written by the model. That's because we released a new model in August of last year, and the engineers said, ‘Actually, this is the first time that Claude is writing code at my level.’ Anthropic only hires the best software engineers in the world, and it was at that point that Claude finally got to their level. In August we were at 50%. By the end of last year we were at 80–90% of the code in the company being written by the model.

What percentage of training the next-generation models is Claude leading today? This is following a similar step change. At the beginning of the year it was zero percent. In April it was 3%. In August, 26% of the process of building the next generation of models is being led by Claude. And we can project out - and we had a blog post about this not too long ago - that sometime next year it could be 80–90%.'
- Wow the new roadster looks quite amazing, good job @elonmusk
