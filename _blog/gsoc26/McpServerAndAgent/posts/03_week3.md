---
layout: page
title: "Week 3: The CQP query tool & HTTP transport"
author: 'Armaan Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'McpServerAndAgent', 'week#3', 'Phase-1']
---

Week 2 left the server able to search and ground fuzzy terms, but it could still only be reached from a local stdio client. Week 3 was about reach and completeness. I put the server on the web, shipped the seventh and final tool, and went back to sharpen `advanced_search`. With that, all of Phase 1's tools are in place.

## HTTP transport: a Streamable HTTP `/mcp` endpoint [#11](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/11)

Until now the server only spoke over stdio, which is fine locally but useless for anything hosted. I added a Streamable HTTP transport and a separate entrypoint, so the stdio build stays untouched. Each POST to `/mcp` gets its own transport instance, and the endpoint is fully public with open CORS.

The work was mostly in the hardening around that openness. An `ALLOWED_HOSTS` env var locks down the `Host` header for DNS-rebinding protection. I also handled EADDRINUSE and SIGTERM/SIGINT shutdown so a hosted process exits cleanly. I tested the whole thing across MCP Inspector (local and through a Cloudflare tunnel), Claude Desktop Client, and the online MCP Playground.

## The corpus query tool: `cqp_query` [#12](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/12)

This is the seventh and final tool, and it talks to a different backend: CDLI's CQP4RDF service, which compiles CQP corpus queries down to SPARQL over a Fuseki triplestore. Where `advanced_search` filters metadata, `cqp_query` searches inside the annotated corpus, single tokens or joined sequences over the currently annotated Ur III material, and returns KWIC lines. 

The endpoint's behaviour shaped the design. A multi-token query without an explicit `::` join is a Cartesian product that always times Fuseki out, so the tool rejects that shape instantly with `INVALID_INPUT` instead of letting the model wait for a guaranteed timeout, which will be modified, once the CQP4RDF backend is optimized to run multi-worded queries. I also made the three outcomes unambiguous, because an LLM needs to tell them apart: an empty result means "ran fine, nothing matched, don't retry", a `TIMEOUT` means "too expensive, matches may exist, narrow and retry"; a 5xx syntax error stays a distinct third signal. And each KWIC line leads with the source tablet's P-number, pulled from the annotation URI, so the model can hand it straight to `get_metadata` or `get_inscription`.

One honest limitation, documented in the tool: against the deployed backend, multi-word joins still 504 at the nginx gateway even when properly joined, because an upstream push-down fix isn't live yet. Single-token queries work cleanly. Our own 15s timeout fires before nginx's 60s one, so the model always gets a clean `TIMEOUT` rather than a hung request. With this merged, all 7 tools are done.

## Sharper search: refinements to `advanced_search`

With the toolset complete, I came back to close gaps in the search fields. I added three more ATF text fields, `atf_transcription`, `atf_structure` (structural tags like `@obverse`), and `atf_comments`, plus `update_external_resource`.

The two more interesting additions were `has` and `order`, and the point with both was restraint. `has` keeps only artifacts that actually carry a named kind of data (translation, transliteration, annotations, and so on); `order` exposes the framework's sort keys. Both are easy to over-apply, so their descriptions tell the model not to reach for them by default. `has` should be used only when missing that data would make a result useless, and `order` only when a specific sort is genuinely needed, since the default order is already stable. Finally a small but useful doc fix: translations in CDLI live inline within the ATF, on `#tr.` lines, not as a separate export, so `get_inscription` now says so, and the model knows to look inside the default output for one.

## What's next

- `util/cache.ts`: a small LRU plus singleflight layer to collapse duplicate CDLI calls.
- A project-wide test suite and CI, now that all the tools are in place.
- Exploring MCP Prompts and Resources.

## Daily Work Update

|\#|Day|Date|A short description of the work done|
|---	|---	|---	|---	|
|1   	| Monday 	|   2026/06/08	| Implemented the Streamable HTTP `/mcp` transport and a separate entrypoint: open CORS, `ALLOWED_HOSTS` DNS-rebinding protection, and graceful shutdown [#11](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/11) |
|2   	| Tuesday  	|   2026/06/09	| Code-reviewed and hardened the transport, tested it across MCP Inspector, Antigravity, and MCP Playground, then merged [#11](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/11) |
|3   	| Wednesday |  2026/06/10 	| Built `cqp_query`, the 7th and final tool, over CDLI's CQP4RDF endpoint: KWIC output, `.env` config, and a server-side join guard [#12](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/12) |
|4   	| Thursday  |   2026/06/11	| Made the three CQP outcomes unambiguous and prefixed each KWIC line with the source tablet's P-number, then merged [#12](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/12) |
|5   	| Friday  	|   2026/06/12	| Probed the deployed CQP backend: single-token queries return cleanly, multi-word joins still 504 at the nginx gateway, documented as a known upstream limitation |
|6   	| Saturday  |  2026/06/13	| Extended `advanced_search` with the `has`/`order` refinements and the `atf_transcription`/`atf_structure`/`atf_comments` fields |
|7   	| Sunday  	|   2026/06/14	| Directed the model that translations live inline in the ATF, then live-tested the full 7-tool surface and reviewed the week |
