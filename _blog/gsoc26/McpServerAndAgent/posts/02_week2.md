---
layout: page
title: "Week 2: Search, Fuzzy Grounding, and Leaner Payloads"
author: 'Armaan Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'McpServerAndAgent', 'week#2', 'Phase-1']
---

Week 1 left the server with the read-only lookup tools in place, up through `get_bibliography`. Week 2 was where the server learned to *search*. I built out CDLI's search surface, made it forgiving of the way people actually type metadata, and trimmed the payloads so they stay cheap for an LLM to read.

I opened the week by finishing the inscription work, adding CDLI-CoNLL and CoNLL-U output formats to `get_inscription` [#5](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/5), then turned to the main piece.

## Search: `advanced_search` over `/search.json` [#6](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/6)

The core of the week. `advanced_search` wraps CDLI's `/search.json` endpoint, and I probed the live endpoint before writing any code, because what the deployed API actually does and what the source suggests do not always line up. A few findings shaped the design:

- **Filter surface.** The endpoint accepts a large set of advanced params, but it quietly ignores any key it does not recognise, so a misspelt field name fails silently: you get unfiltered results back instead of an error. To avoid that trap I only expose the 22 fields I confirmed actually filter, including provenience, period, genre, language, material, collection, artifact type, designation, museum and excavation numbers, the ATF text fields, and the publication fields.
- **Match semantics.** Matching is phrase and keyword-wildcard rather than plain substring, and the operators pass straight through to the index: quoted exact match, `/regex/`, `*` and `?` wildcards, and `%AND%` / `%OR%` for multi-value fields. I documented these in the tool description so the model can reach for them deliberately.
- **No pagination envelope.** The response is a bare JSON array with no total count anywhere in the body. The only count signal is the RFC-5988 `Link` header.

I came back to that last point later in the week to add real pagination [#10](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/10): `advanced_search` now reports a match total derived from the `Link` header, and supports `search_after` cursors for paging past CDLI's roughly 10k result window. I also extended the field set with ATF transliteration search and the full publication and metadata suite [#8](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/8).

## Fuzzy term grounding: `ground_term` [#7](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/7)

Because matching is phrase-literal, `provenience=Ur 3` returns a single record while `Ur III` returns over 4,400. That is a sharp precision cliff hiding behind nothing more than a formatting choice. So before a query reaches the API, terms pass through a Levenshtein matcher (threshold 3, case-insensitive) against a committed vocabulary snapshot: `vocab.json`, 254 canonical terms across 6 fields, harvested once via an Elasticsearch aggregation rather than fetched at runtime. When it corrects a term, the tool reports the change back to the model (`Ur 3 → Ur III`) instead of rewriting silently, so nothing happens behind the caller's back. `ground_term` stays internal; it is never registered as its own MCP tool, and is only ever called from inside `advanced_search`.

## Compression layer [#9](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/9)

Raw artifact records from `/artifacts/{id}.json` are heavy: inline ATF, full publication lists, relation arrays. A live probe confirmed that search hits and by-ID records share the same nested shape, so a single projection serves both. `compressArtifact` flattens each hit into a summary card and drops the heavy fields, while keeping `has_inscription` and `publication_count` as signals so the model knows whether a follow-up call to `get_inscription` or `get_bibliography` is worth making. I also typed the nested shapes properly (`CdliArtifactRecord`, `CdliPublicationEntry`) instead of reaching into `any`, and switched the success payloads to compact JSON, which cut roughly 20 to 30% of the tokens on the wire with no change to the data.

## What's next

- HTTP transport: a Streamable HTTP `/mcp` endpoint so the server is reachable over the web, not just from a local stdio client.
- `util/cache.ts`: a small LRU plus singleflight layer to collapse duplicate CDLI calls.
- A project-wide test suite and CI, now that the core tools are in place.
- Exploring the possibility of adding MCP Prompts and Resources.

## Daily Work Update

|\#|Day|Date|A short description of the work done|
|---	|---	|---	|---	|
|1   	| Monday 	|   2026/06/01	| Added CDLI-CoNLL and CoNLL-U output formats to `get_inscription` [#5](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/5) |
|2   	| Tuesday  	|   2026/06/02	| Live-probed `/search.json`, then implemented the `advanced_search` tool over the confirmed filter fields [#6](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/6) |
|3   	| Wednesday |  2026/06/03 	| Built the `ground_term` vocabulary and Levenshtein matcher, and wired fuzzy correction into `advanced_search` [#7](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/7) |
|4   	| Thursday  |   2026/06/04	| Extended `advanced_search` with ATF transliteration search and the publication and metadata fields [#8](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/8) |
|5   	| Friday  	|   2026/06/05	| Designed and built the compression layer to keep tool responses small for the model [#9](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/9) |
|6   	| Saturday  |  2026/06/06	| Added match-total reporting and `search_after` deep paging to `advanced_search` [#10](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/10) |
|7   	| Sunday  	|   2026/06/07	| Tested search and grounding against the live CDLI API, reviewed the week's merges, and scoped the HTTP transport for next week |
