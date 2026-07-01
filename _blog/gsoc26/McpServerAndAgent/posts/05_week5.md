---
layout: page
title: "Week 5: Hardening the Server, and Finishing the Chat Plan"
author: 'Armaan Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'McpServerAndAgent', 'week#5', 'Phase-1', 'Phase-2']
---

Week 4 was lighter because of the move to Bengaluru. This week I picked the pace back up: I closed three small pieces of housekeeping on the Phase 1 server that had been sitting in the tracker, then went back and finished the chat interface plan I'd started drafting the week before.

## Caching repeated CDLI reads [#13](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/13)

The server was calling out to the CDLI API fresh every time, even for the same artifact asked twice in a row. I added a small cache in `util/cache.ts`: an LRU with a 30 second TTL, plus a guard so two requests for the same URL landing at once share one call instead of firing twice. Only successful responses get cached, a failed fetch is never remembered as a success. A repeated artifact fetch went from about 960ms to instant on the second try.

## Migrating off the deprecated tool registration [#14](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/14)

The MCP SDK deprecated `server.tool()` a while back in favour of `server.registerTool()`, and all seven tools were still on the old call. This was a purely structural change, the descriptions and schemas moved under `registerTool()`, and none of the actual handler logic changed. Lint, build, and a smoke test confirmed all seven tools still work exactly as before.

## Cleaning up error mapping and the HTTP transport [#15](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/15)

A couple of rough edges had been left over from earlier weeks. A CDLI 404 was mapping to a generic upstream error, so by ID tools now get a clean, non retryable NOT_FOUND instead, checked against a few real nonexistent artifact IDs. I also typed the HTTP server variable properly instead of leaving it loose, and fixed two error responses that were missing their JSON content type.

## Finishing the chat interface plan

With those merged, I went back to the chat interface plan and closed out what I'd left open the week before: how the backend actually decides what to do with a query, and everything that has to hold up once real users are on it. I settled on a simple layered design, a cheap router sits in front, and for now its only job is to politely refuse clearly off topic questions before we spend anything on the model. Everything on topic still goes to the full tool using agent underneath, since turning a real question into a structured search is genuinely something only the model can do well.

A few smaller pieces fell into place around that. A user's own key stays encrypted in their browser and is only sent per request, never stored on our side. CDLI's own funded keys stay on the server, only for logged in users, with a rate limit and a budget counter, though I'm only building the counter for now and leaving real cost tracking for later. I also locked the feature list for the chat itself: stop, regenerate, edit and resend, copy, starter prompts, error states, proper ATF rendering, and citation cards for artifacts. A newer extension called MCP Apps, which lets a server render its own UI in any client, got parked for later rather than built into the first version.

With the design settled, I wrote up the actual build order as a companion doc, so implementation has a clear sequence to follow once I start writing chat backend code.
