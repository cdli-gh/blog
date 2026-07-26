---
layout: page
title: "Week 7: Streaming the Chat Turn"
author: 'Armaan Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'McpServerAndAgent', 'week#7', 'Phase-2']
---

Week 6 ended with the chat backend able to call CDLI tools, but it couldn't stream anything and there was still no browser to talk to it from. This week I fixed the first of those two problems: I made the backend actually stream.

## Streaming the chat turn [#21](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/21)

Up to now the backend would wait for the whole answer before sending anything back, which isn't really how a chat should feel. I added a small SSE helper and changed the agent loop so it sends a token event as each piece of text comes in, and a tool event whenever it starts or finishes calling a tool. I also wired up cancellation properly: closing the connection now actually stops the model and any tool call that's still running, instead of letting it carry on in the background. I tested this by hand with curl, closing the connection partway through a tool call, and it stopped cleanly instead of leaving anything running on the server. While I was in there I also fixed a small bug where a bad request body was returning an HTML error page instead of the same JSON error shape every other error uses.

Still no browser to actually use any of this from, that's next.
