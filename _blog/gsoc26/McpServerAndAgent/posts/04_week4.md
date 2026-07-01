---
layout: page
title: "Week 4: Drafting and finalizing the Chat Interface Plan"
author: 'Armaan Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'McpServerAndAgent', 'week#4', 'Phase-2']
---

Week 4 shipped less code than the previous three, and I flagged this in our meetings as it happened: I relocated to Bengaluru this week, and the move ate into the time I'd normally spend implementing. Rather than rush a half-finished feature into Phase 1 around a move, I used the week for something that needed unhurried thinking anyway: designing Phase 2, the `/chat` interface, before writing a line of its code.

With all seven Phase 1 tools done, the open question was what actually sits on top of them. I started from one fact that ended up shaping the whole design: CDLI wants to offer near-zero-cost, CDLI-funded LLM keys to logged-in users who don't bring their own key, and a funded key shipped to the browser would get extracted and abused within hours. That single requirement ruled out the pure-browser widget from the original sketch, and meant we need a server we control to hold the key. So a dedicated Node chat backend, doubling as the MCP host, became the centerpiece of the design. From there I worked out the rest of the architecture around it:

- The service topology, all behind a single `cdli.earth` origin: `/chat` for the SPA, `/chat/api` for the backend, and `/mcp` left unchanged.
- Why the whole thing stays same origin and path based instead of using a subdomain, so the site's existing login cookie just works without extra setup.
- The identity bridge itself: a short lived token minted by CakePHP and handed to the backend, verified locally using HMAC. This was needed because CakePHP's sessions are file based, so the Node backend has no direct way to read them.
- The repository shape: the chat backend and a React/Vite frontend join the MCP server as npm workspaces in this same repo (`packages/server`, `packages/chat-backend`, `packages/chat-web`), building on the monorepo restructuring from a couple of weeks back. The Phase 3 Python `/paper` agent stays a separate top level directory since it doesn't share any tooling with the rest.

The remaining piece, how the backend actually decides what to do with a query, and everything that has to hold up once it's live, is what I carried into next week.
