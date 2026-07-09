---
layout: page
title: "Week 6: Rendered Views, Deployment, and the First Chat Backend Code"
author: 'Armaan Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'McpServerAndAgent', 'week#6', 'Phase-1', 'Phase-2']
---

Week 5 ended with the server hardened and the chat interface plan fully written out. This week I gave two tools their own rendered views using MCP Apps, got the server deployed, and opened the first branch of the actual chat backend.

## Rendered views for two tools

`get_inscription` and `advanced_search` were only returning plain text and JSON. Using MCP Apps (SEP 1865), I built a proper renderer for each: one that lays out ATF and CoNLL annotations nicely, and one that shows search results as a card grid instead of raw JSON. Both are registered as `ui://` resources, so any client that supports MCP Apps now shows a real view instead of text. I also generalised the build pipeline once there were two apps to bundle instead of one.

## Getting the server deployed

I added a `render.yaml` and a proper README, and got the server deployable on Render for testing purposes till I deploy it to the CDLI infra. It now has a real path to being reachable from outside my own machine.

## Starting the chat backend

With the server in a good place, I opened `chat/backend-skeleton`, the first branch of the actual Phase 2 build: a small Express backend with one route that takes a conversation and a BYOM key, connects to the MCP server, and lets the model call the CDLI tools itself using the Vercel AI SDK's tool calling loop, with a cap on tool calls per turn. Five providers are wired in already (openai, anthropic, google, mistral, groq) so BYOM users can bring whatever key they have.

No streaming and no browser yet, that's next. But this is the first time a model is calling CDLI tools through a real backend instead of Claude Desktop or the Inspector.
