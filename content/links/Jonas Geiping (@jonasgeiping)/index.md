---
title: "Jonas Geiping (@jonasgeiping)"
date: 2026-08-17T11:23:38-06:00
lastmod: 2026-08-17T11:23:38-06:00
draft: true
description: "Why am I being baited by watermark misinformation on this app, is it 2023 again? A small FAQ: 1. 𝗪𝗵𝗮𝘁'𝘀 𝗮 𝘁𝗲𝘅𝘁 𝘄𝗮𝘁𝗲𝗿𝗺𝗮𝗿𝗸? -- A modification of the LLM sampling algorithm that, if there are multiple ways to write something, will pick one that agrees with a pseudorandom key. This is a local, invisible signature hidden in the way phrases are used in any LLM text that persists when text is copied. 2. 𝗗𝗼𝗲𝘀 𝘁𝗵𝗶𝘀 𝗺𝗮𝗸𝗲 𝘁𝗵𝗲 𝘁𝗲𝘅𝘁 𝘄𝗼𝗿𝘀𝗲? -- A good implementation is 'undetectable' (in polynomial time), meaning: If you do not have the private key, then neither you, the model itself, or pangram could detect that this is happening. 3. 𝗪𝗶𝗹𝗹 𝘁𝗵𝗶𝘀 𝗯𝗿𝗲𝗮𝗸 𝘁𝗵𝗲 𝗺𝗼𝗱𝗲𝗹'𝘀 𝗿𝗲𝗮𝘀𝗼𝗻𝗶𝗻𝗴? -- Because Ant already encrypts the model's reasoning, they can just not watermark the model's internal reasoning, leaving the thinking unaffected. 4. 𝗪𝗶𝗹𝗹 𝘁𝗵𝗶𝘀 𝗺𝗮𝗸𝗲 𝘁𝗵𝗲 𝗺𝗼𝗱𝗲𝗹 𝗹𝗲𝘀𝘀 𝗰𝗿𝗲𝗮𝘁𝗶𝘃𝗲/ 𝗺𝗼𝗿𝗲 𝘀𝗮𝗺𝗲-𝘆? -- If anything this (marginally) increases entropy across different generations, so it will make model outputs slightly more varied. 5. 𝗕𝘂𝘁 𝗜 𝗰𝗮𝗻 𝗷𝘂𝘀𝘁 𝗿𝗲𝗺𝗼𝘃𝗲 𝗶𝘁 𝗽𝗮𝗿𝗮𝗽𝗵𝗿𝗮𝘀𝗶𝗻𝗴? -- Absolutely! But, judging from the amount of writing on the web that already unmistakably sounds like Claude, most people likely will not bother. 5b: Also, not any paraphrase will work. To remove (for example) a k=5-minhash watermark completely from a long document, you need to make sure none of the original 2-grams, 3-grams, 4-grams, 5-grams and 6-grams of the text remain. 6. 𝗪𝗶𝗹𝗹 𝘆𝗼𝘂 𝗶𝗻𝗮𝗱𝘃𝗲𝗿𝘁𝗲𝗻𝘁𝗹𝘆 𝗰𝗼𝗽𝘆 𝘁𝗵𝗲 𝘄𝗮𝘁𝗲𝗿𝗺𝗮𝗿𝗸? -- No, with a good implementation the space of possible realizations of the key is too large to memorize. 7. 𝗪𝗶𝗹𝗹 𝘁𝗵𝗶𝘀 𝗮𝗹𝗹𝗼𝘄 𝗖𝗹𝗮𝘂𝗱𝗲𝘀 𝘁𝗼 𝗶𝗱𝗲𝗻𝘁𝗶𝗳𝘆 𝗼𝘁𝗵𝗲𝗿 𝗶𝗻𝘀𝘁𝗮𝗻𝗰𝗲𝘀 𝗶𝗻 𝗮 𝘀𝘄𝗮𝗿𝗺? -- The watermark will 'appear' like random sampler fluctuation to the model and would not be detectable. But, if an agent gets hold of a detector endpoint, it can absolutely use the watermark to ID other Claude agents (not that it would have trouble noticing them based on their writing as of today). 8. 𝗪𝗶𝗹𝗹 𝘁𝗵𝗶𝘀 𝗱𝗲𝘁𝗲𝗰𝘁 𝗱𝗶𝘀𝘁𝗶𝗹𝗹𝗮𝘁𝗶𝗼𝗻? -- By default, no. If the watermark is set up to be 'undetectable' (as assumed above), it will not be picked up in training by other models. For that to happen, the watermark needs to be detectable by ML algorithms. 9. 𝗪𝗶𝗹𝗹 𝘁𝗵𝗶𝘀 𝗺𝗮𝗸𝗲 𝗣𝗮𝗻𝗴𝗿𝗮𝗺'𝘀 𝗷𝗼𝗯 𝗲𝗮𝘀𝗶𝗲𝗿? -- By default no, this is a separate avenue to detection. But, they might collaborate with Anthropic which would allow them to detect the watermark as well and show a watermark score next to their text detection score. 10. Bonus: All aside, is this a good idea? I don't know. The companies are doing it to follow the writing of the EU AI act, which was written based on 2024 information and when the field looked very different, and threat models were focused much more on slop/propaganda (like the Kokotajlo 2026 prediction). The actual 2026 looks quite a bit different."
tags: []
categories: []
source_url: https://x.com/jonasgeiping/status/2087094822146290170
source_type: article
---

[Jonas Geiping (@jonasgeiping)](https://x.com/jonasgeiping/status/2087094822146290170)

## 

> 
