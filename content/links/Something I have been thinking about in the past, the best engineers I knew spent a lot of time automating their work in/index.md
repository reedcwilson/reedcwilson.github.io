---
title: "Something I have been thinking about: in the past, the best engineers I knew spent a lot of time automating their work in various ways. Better vim/emacs automations, writing lint rules to catch repeat code issues, building up a suite of e2e tests so they don't need to smoke test the app manually. These kinds of things were the highest leverage activities an engineer could do, because it multiplied their own output, which in turn meant they could build more things.

I think many of these automations have become even more important now. This is true for a number of reasons.

First, infra and DevX automation speeds you up. And if you are running an army of agents, each of those agents will be sped up also. More automation == more output per unit of time.

Second, moving things to code improves efficiency. Your agent could fix an issue every time it sees that issue happen, but that uses tokens and might miss cases. If Claude instead writes a lint rule, CI step, or routine, that class of issue can be fully automated forever. This is really what people are talking about when they talk about loops -- it's about automating entire types of busywork rather than solving them one off. This isn't a new idea at all. Engineers have been doing this for a long time!

Third and most importantly, automation makes it possible for others to contribute to the codebase more easily. Increasingly what I am seeing is engineers are contributing to codebases on day one because Claude can navigate the codebase for them, and that non-engineers are able to contribute to a codebase as effectively as engineers can. What gets in the way of both of these is domain knowledge that lives in peoples' heads rather than in automation -- the stuff you used to have to learn when ramping up. What has changed thanks to agents is the domain knowledge that can be encoded as infrastructure is no longer limited to what is expressible in lint rules and types and tests; it can now capture nearly all domain knowledge, encoded as code comments and skills and CLAUDE.md rules and memories. If I put up a PR for an iOS codebase I don't know and a code reviewer rejects it because it doesn't use the right framework, or if a designer builds a new feature and it gets rejected because it doesn't follow the right architectural patterns, these are failures of automation.

Every team should be writing the CLAUDE.md's, REVIEW.md's, skills, and docs that enable agents to productively work in their codebase with zero additional context from the prompter. This sounds crazy, and at the same time is a natural extension of the stuff engineers have always done: automate, and encode domain knowledge as infrastructure. As the model gets smarter and as the harness matures, this task becomes easier. In the meantime, it is on every team to look for ways to convert their domain knowledge to infra so that Claude can write code better, so that code review catches issues automatically, and so the next person working on your codebase can contribute more easily."
date: 2026-08-08T22:26:19-06:00
lastmod: 2026-08-08T22:26:19-06:00
draft: true
description: "Engineers should automate repetitive tasks to boost output and reduce manual work. Moving domain knowledge into infrastructure like CLAUDE.md enables agents to handle code reviews and contributions without human context. This turns busywork into scalable automation, freeing teams to focus on innovation. The goal is zero-context collaboration where AI handles the routine."
tags: []
categories: []
source_url: https://nitter.reedcwilson.com/bcherny/status/2077460395279692197#m
source_type: article
---

[Something I have been thinking about: in the past, the best engineers I knew spent a lot of time automating their work in various ways. Better vim/emacs automations, writing lint rules to catch repeat code issues, building up a suite of e2e tests so they don't need to smoke test the app manually. These kinds of things were the highest leverage activities an engineer could do, because it multiplied their own output, which in turn meant they could build more things.

I think many of these automations have become even more important now. This is true for a number of reasons.

First, infra and DevX automation speeds you up. And if you are running an army of agents, each of those agents will be sped up also. More automation == more output per unit of time.

Second, moving things to code improves efficiency. Your agent could fix an issue every time it sees that issue happen, but that uses tokens and might miss cases. If Claude instead writes a lint rule, CI step, or routine, that class of issue can be fully automated forever. This is really what people are talking about when they talk about loops -- it's about automating entire types of busywork rather than solving them one off. This isn't a new idea at all. Engineers have been doing this for a long time!

Third and most importantly, automation makes it possible for others to contribute to the codebase more easily. Increasingly what I am seeing is engineers are contributing to codebases on day one because Claude can navigate the codebase for them, and that non-engineers are able to contribute to a codebase as effectively as engineers can. What gets in the way of both of these is domain knowledge that lives in peoples' heads rather than in automation -- the stuff you used to have to learn when ramping up. What has changed thanks to agents is the domain knowledge that can be encoded as infrastructure is no longer limited to what is expressible in lint rules and types and tests; it can now capture nearly all domain knowledge, encoded as code comments and skills and CLAUDE.md rules and memories. If I put up a PR for an iOS codebase I don't know and a code reviewer rejects it because it doesn't use the right framework, or if a designer builds a new feature and it gets rejected because it doesn't follow the right architectural patterns, these are failures of automation.

Every team should be writing the CLAUDE.md's, REVIEW.md's, skills, and docs that enable agents to productively work in their codebase with zero additional context from the prompter. This sounds crazy, and at the same time is a natural extension of the stuff engineers have always done: automate, and encode domain knowledge as infrastructure. As the model gets smarter and as the harness matures, this task becomes easier. In the meantime, it is on every team to look for ways to convert their domain knowledge to infra so that Claude can write code better, so that code review catches issues automatically, and so the next person working on your codebase can contribute more easily.](https://nitter.reedcwilson.com/bcherny/status/2077460395279692197#m)

## 

> 
