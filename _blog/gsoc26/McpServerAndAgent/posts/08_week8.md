---
layout: page
title: "Week 8: The Chat Web Shell & BYOM"
author: 'Armaan Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'McpServerAndAgent', 'week#8', 'Phase-2']
---

Week 7 got the backend streaming, but there was still no browser to actually use it from. This week I built that: a real chat-web app, then went back and made sure the one thing it stores on your machine, your own API key, is actually safe to store.

## A chat interface people can use [#22](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/22)

New workspace called `chat-web`, built with Vite, React, and TypeScript. There's a sidebar where you pick a provider (openai, anthropic, google, mistral, or groq) and paste in a key, a message thread that renders the model's replies as markdown, and small icons that show when the model is calling a tool so the chat doesn't just go quiet while a search is running. The part that reads the stream is a plain fetch reader that listens for the token, tool, done, and error events the backend started sending last week. I tested the whole thing live with the server, the chat backend, and the frontend all running together: asked a search question, watched `advanced_search` fire, got back a markdown answer with real P-numbers, then asked a follow-up ("the first one you listed") and it correctly figured out what I meant from the earlier messages and called `get_inscription`.

## Encrypting the BYOM key at rest

Until now, a user's key just sat in the app's state, fine for testing, but not something I'd want to actually ship, since anything left in `localStorage` as plain text is one XSS bug away from being stolen. So I added a proper key flow: you set a PIN, and the key gets encrypted with AES-256-GCM before it's saved, using PBKDF2 (100,000 rounds) to turn the PIN into the actual encryption key, with a new random salt and IV every time you save. If you reload the page, it shows a locked screen that only opens with the right PIN, a wrong PIN gets rejected, and there's a "forget key" option that wipes it completely. I also added a small field to override the default model per provider, since the default one isn't always the one you want. I checked the browser's storage panel directly to make sure only the encrypted version ever shows up, then walked through the whole flow by hand: save, reload, unlock, try a wrong PIN, forget.

That's the first working version of the whole chat interface, start to finish, type in a key and get back a real, streamed, tool-using answer. Next up is the funded-key path for people who are logged in.
