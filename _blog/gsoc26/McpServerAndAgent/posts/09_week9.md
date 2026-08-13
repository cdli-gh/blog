---
layout: page
title: "Week 9: Funded keys and the domain gate"
author: 'Armaan Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'McpServerAndAgent', 'week#9', 'Phase-2']
---

Week 8 ended with a chat interface that works if you bring your own key. This week was the other half: letting logged-in CDLI users chat without one, on keys CDLI pays for.

## Identity, funded keys, and limits [#24](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/24)

The reason the chat backend exists at all is that a CDLI-funded key can't be shipped to a browser, so the backend has to know who's asking. CakePHP mints a short-lived signed token and the backend verifies it locally, no round trip, no shared session store. The verification fails closed on everything I could think of: no secret, no header, bad signature, expired, or garbage all end up as an anonymous user rather than an error. A broken token should cost you your funded access, not the page.

From there, one function decides which key a request runs on, and I kept it as the only place that decision happens. Your own key if you sent one, CDLI's funded key if you're logged in and didn't, a 401 if neither. The funded path ignores whatever provider the request asked for and pins it to one model, which I checked by asking for OpenAI with no key while logged in and watching it go through on Mistral. On top of that sit per-minute limits (different for anonymous, logged-in, and funded) and a daily cap on funded calls. Every one of those numbers is a guess. There's no real usage to tune against yet, so I'd rather have the seam in place with an honest guess in it than pretend at precision. The funded tier tripped exactly on the sixth call in a minute when I tested it.

One catch: the CakePHP route that hands out the token doesn't exist yet. The funded path is built and tested, but no real user can reach it until that lands.

## The domain gate, and deleting my first version [#25](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/25)

This is a cuneiform research assistant, not a general chatbot, and on the funded tier that difference costs money. So I built a gate to refuse off-topic questions.

My first version was a keyword check running before the model: about thirty domain terms plus a pattern for artifact IDs, applied to the first message only. It worked, off-topic questions got refused instantly with nothing spent. Then I asked myself what happens to an on-topic question containing none of my thirty words. "Who was Gudea?" is a perfectly good question here, and my gate would have refused it. A keyword list is really just a guess about how people phrase things, and it was wrong in the direction that hurts most.

So I deleted it and moved the whole thing into the system prompt. The model is told what it's for and declines anything outside that without calling any tools. The trade-off is real and I'd rather say it than hide it: the refusal now happens inside the paid call, so an off-topic question on the funded tier still costs one, which the keyword version prevented. I took that deal because wrongly refusing a real question is the worse failure. I checked three cases by hand: clearly off topic gets a polite decline with no tool calls, "Who was Gudea?" now gets answered, and a normal search question behaves as before.

## What's next

- In-session context management, so a long conversation doesn't blow past the model's window.
- Starting Phase 3, the `/paper` agent.

## Daily Work Update

|\#|Day|Date|A short description of the work done|
|---	|---	|---	|---	|
|1   	| Monday 	|   2026/07/20	| Re-verified the CakePHP identity assumptions against the framework's HEAD, then built token verification that fails closed to anonymous [#24](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/24) |
|2   	| Tuesday  	|   2026/07/21	| Built the credentials chokepoint: your own key, else CDLI's funded key when logged in, else a 401 before anything is spent [#24](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/24) |
|3   	| Wednesday |  2026/07/22 	| Added per-minute rate limits per tier and a daily funded-call cap, thresholds left as placeholders until there's real usage [#24](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/24) |
|4   	| Thursday  |   2026/07/23	| Tested every identity path with a self-minted token, including the funded key overriding a requested provider, then merged [#24](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/24) |
|5   	| Friday  	|   2026/07/24	| Built the domain gate as a keyword check running before the model [#25](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/25) |
|6   	| Saturday  |  2026/07/25	| Realised it would refuse on-topic questions with no matching keyword, so I deleted it and moved the gate into the system prompt [#25](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/25) |
|7   	| Sunday  	|   2026/07/26	| Verified the prompt-only gate on three cases, off topic, previously-failing on topic, and tool-using, then merged [#25](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/25) |
