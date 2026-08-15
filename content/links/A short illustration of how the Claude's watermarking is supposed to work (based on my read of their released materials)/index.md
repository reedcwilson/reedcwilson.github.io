---
title: "A short illustration of how the Claude's watermarking is supposed to work (based on my read of their released materials).

In general, when we are generating tokens, there can be multiple high-scoring tokens at certain next-word positions. Usually, we sample with top-k or top-p sampling so the highest-scoring token is most often selected (if we repeat the sampling many times), but other tokens may be selected as well.

With watermarking, there is a key that says which of the (ideally equally) highest-scoring tokens to select. Or, more concretely, the secret key and previous token influence the randomness here.

Now, if we repeat this at many token positions, this creates the watermark as it will be a pattern that is statistically unlikely to get otherwise (due to combinatorics).

One thing I am confused about: They basically say that they HAVE to do this for everyone due to EU regulation. Why?

Sure, but this is an inference-time technique that doesn't require retraining or training a separate model, so, if they wanted, they could only do that for EU users? 🤔"
date: 2026-08-15T09:33:00-06:00
lastmod: 2026-08-15T09:33:00-06:00
draft: true
description: "A short illustration of how the Claude's watermarking is supposed to work (based on my read of their released materials).

In general, when we are generating tokens, there can be multiple high-scoring tokens at certain next-word positions. Usually, we sample with top-k or top-p sampling so the highest-scoring token is most often selected (if we repeat the sampling many times), but other tokens may be selected as well.

With watermarking, there is a key that says which of the (ideally equally) highest-scoring tokens to select. Or, more concretely, the secret key and previous token influence the randomness here.

Now, if we repeat this at many token positions, this creates the watermark as it will be a pattern that is statistically unlikely to get otherwise (due to combinatorics).

One thing I am confused about: They basically say that they HAVE to do this for everyone due to EU regulation. Why?

Sure, but this is an inference-time technique that doesn't require retraining or training a"
tags: []
categories: []
source_url: https://nitter.reedcwilson.com/rasbt/status/2088631263737364818#m
source_type: article
---

[A short illustration of how the Claude's watermarking is supposed to work (based on my read of their released materials).

In general, when we are generating tokens, there can be multiple high-scoring tokens at certain next-word positions. Usually, we sample with top-k or top-p sampling so the highest-scoring token is most often selected (if we repeat the sampling many times), but other tokens may be selected as well.

With watermarking, there is a key that says which of the (ideally equally) highest-scoring tokens to select. Or, more concretely, the secret key and previous token influence the randomness here.

Now, if we repeat this at many token positions, this creates the watermark as it will be a pattern that is statistically unlikely to get otherwise (due to combinatorics).

One thing I am confused about: They basically say that they HAVE to do this for everyone due to EU regulation. Why?

Sure, but this is an inference-time technique that doesn't require retraining or training a separate model, so, if they wanted, they could only do that for EU users? 🤔](https://nitter.reedcwilson.com/rasbt/status/2088631263737364818#m)

## 

> 
