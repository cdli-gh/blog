---
layout: page
title: MCP Server And Agent for CDLI
author: 'Armaan Gupta'
tags: ['project', 'gsoc', 'gsoc2026', 'McpServerAndAgent']
---

## Project Overview

I'm <a href="https://in.linkedin.com/in/armaanngupta">Armaan Gupta</a>, participating in Google Summer of Code 2026 with CDLI.
I've been accepted for the project MCP Server and Agent for CDLI. This project improves access to the CDLI database by enabling natural language queries instead of complex search forms and syntax. It allows researchers and students to explore the database more easily without needing detailed knowledge of its structure. The system consists of an MCP server that translates plain English queries into structured CDLI API calls, along with an AI-powered research workspace embedded on the CDLI website. Users can search, retrieve, and explore data through a simple chat interface, and generate structured research outputs. Key deliverables include a production-ready MCP server, an interactive research interface, a guided research paper generation workflow, and comprehensive documentation with testing support.

<b>Mentors: </b>
<a target="_blank" href="https://in.linkedin.com/in/nishealjohn">Nisheal John</a>,
<a target="_blank" href="https://jaykmr.com/">Jayanth Kumar</a>,
<a target="_blank" href="https://epageperron.info/">Émilie Pagé-Perron</a>

### Links

| | |
| --- | --- |
| **GSoC project** | [GSoC'26](https://summerofcode.withgoogle.com/programs/2026/projects/mlVyalno) |
| **Proposal** | [CDLI_MCP_GSOC26.pdf](https://github.com/cdli-gh/Framework/blob/master/Proposal/2026/CDLI_MCP_GSOC26.pdf) |
| **Repository** | [gitlab.com/cdli/cdli-mcp](https://gitlab.com/cdli/cdli-mcp) — branch `develop` |
| **Merge requests** | [cdli-mcp](https://gitlab.com/cdli/cdli-mcp/-/merge_requests?scope=all&state=all) |
| **Hosted MCP endpoint (demo)** | `https://cdli-demo.duckdns.org/mcp` — development instance, public and unauthenticated by design |
| **Weekly journals** | indexed at the end of this report, and linked at the foot of this page |

---

# Final Report

CDLI's catalogue holds over 400,000 artifacts, and all of it is already reachable over a public API — if you know the field names, the canonical vocabulary, and which of several search surfaces answers your question. This project puts a language model in that gap. It exposes the CDLI REST APIs and the CQP4RDF corpus service as [Model Context Protocol](https://modelcontextprotocol.io) tools, so a researcher can ask "find Ur III tablets from Nippur written in Sumerian" and get back real catalogue records, each traceable to a P-number, rather than a plausible-sounding paragraph. There are two ways in: connect the server to a desktop MCP client such as Claude Desktop or Cursor, or use the hosted chat interface built on top of it, which adds a `/paper` command that drafts a cited research note.

## Problem and approach

The obvious build here is a chatbot with CDLI search wired into it. I did not do that, because a bespoke chatbot serves exactly one interface. MCP is a protocol, so the same tool server answers Claude Desktop, Cursor, the CDLI web client, and the Python paper agent without any of them knowing about each other — the chat backend and the paper agent are separate codebases in different languages, and both are just MCP clients against the same public `/mcp` endpoint.

Two constraints shaped the rest. The tool surface is kept small — nine tools, each doing one thing — because a model choosing between forty near-identical tools chooses badly, and every tool costs context on every turn. And CDLI wants to offer funded LLM access to logged-in users; a funded key shipped to a browser would be extracted within hours. That ruled out the pure-browser widget in the original proposal and made the chat a React SPA on a Node backend CDLI controls, rather than a drawer of JavaScript on every page.

## Architecture

![CDLI MCP architecture]({{ site.baseurl }}/gsoc26/McpServerAndAgent/assets/architecture.png)

| Component | What it is |
|---|---|
| `packages/server` | The MCP server. Tools, term grounding, response compression, the shared CDLI HTTP client, and both transports — STDIO and Streamable HTTP on `/mcp`. |
| `packages/chat-backend` | Express agent host: MCP client, agentic tool loop, one SSE endpoint, plus identity, credentials, rate limits and context trimming. |
| `packages/chat-web` | Vite/React SPA served at `cdli.earth/chat`: streaming thread, slash commands, in-browser key encryption, artifact cards. |
| `agent-paper` | Standalone Python service — a seven-node LangGraph pipeline behind FastAPI, with its own MCP client and PDF export. Not an npm workspace; it shares no tooling. |

One correction to the proposal: it describes the paper agent as client-side middleware. A browser cannot run LangGraph, so it became its own HTTP service early in Phase 3.

## Deliverables

### 1. The MCP server

| Tool | What it does |
|---|---|
| `advanced_search` | Metadata search over `/search.json` across 32 verified filter fields, with fuzzy grounding, match totals and deep paging |
| `get_metadata` | List or by-ID fetch for 17 curated entity types |
| `search_entity` | Filter-query for the 14 entities that actually support filtering |
| `get_inscription` | Transliteration as C-ATF, CDLI-CoNLL or CoNLL-U |
| `get_bibliography` | Compressed citations for an artifact or publication |
| `cqp_query` | CQP corpus queries via CQP4RDF/Fuseki, returning KWIC lines |
| `ping` | Health check |
| `show_artifact_cards` | Display-only: renders a card grid through MCP Apps |
| `show_inscription` | Display-only: renders a formatted transliteration view |

`advanced_search` is the centre of gravity, and its design comes from one API behaviour: `/search.json` silently drops any parameter it does not recognise, so a misspelt field name returns the *unfiltered* corpus instead of an error. The tool therefore exposes only fields I confirmed actually filter against the live API. Matching is phrase and keyword-wildcard, so the index operators (quoted exact, `/regex/`, `*` and `?`, `%AND%` / `%OR%`) pass straight through and are documented for the model. The response is a bare JSON array with no total in it, so match counts come from the RFC-5988 `Link` header, and `search_after` cursors page past CDLI's ~10k result window.

Because matching is phrase-literal, `provenience=Ur 3` returns one record while `Ur III` returns over 4,400 — a precision cliff hiding behind a formatting choice. `ground_term` closes it: every groundable value is matched by Levenshtein distance against a committed snapshot of 252 canonical terms across six fields, and any correction is reported back to the model rather than applied silently. It is deliberately never registered as a tool, only called from inside `advanced_search`.

Around that: a compression layer that flattens heavy artifact records into summary cards, keeping `has_inscription` and `publication_count` as signals for whether a follow-up call is worth making; an LRU cache (500 entries, 30-second TTL) with a singleflight guard, which took a repeat artifact fetch from ~960ms to instant; a uniform response envelope; and a timing wrapper on every handler. 91 tests across 10 files, all passing.

The two display tools were the last addition, and they encode a finding about MCP Apps: a UI binds to a *tool*, not to a call, so a widget on `advanced_search` renders on every intermediate search the model makes while it is still working. Splitting display from retrieval lets one widget appear once, in the final answer.

### 2. The chat interface

A React SPA at `cdli.earth/chat` on a stateless Node backend that hosts the MCP server on the user's behalf.

- **Streaming with visible tool calls.** Answers stream over SSE, with each tool call surfaced as it runs. Stopping a turn genuinely halts backend spend — the abort propagates from the closed response all the way down to the in-flight MCP call.
- **Bring your own key.** Six providers (OpenAI, Anthropic, Google, Mistral, Groq, OpenRouter). A key is encrypted in the browser with AES-256-GCM under a PIN and sent per request; nothing is stored server-side.
- **CDLI-funded access.** Logged-in users without a key fall through to a CDLI key, via a short-lived token minted by CakePHP and verified by the backend. One chokepoint decides BYOM, funded, or refuse.
- **Limits and scope.** Tiered per-minute rate limits and a daily funded-call budget, both placeholders until real traffic exists. Off-topic questions are declined by the system prompt — a code-level keyword gate was built first and removed, because it wrongly refused genuine questions like "Who was Gudea?".
- **Session context.** History is trimmed to a ~10k-token budget before each turn. Nothing persists past a reload, by design.
- **Slash commands.** `/search`, `/artifact` and `/cqp` bias the model toward a tool rather than routing around it, so it still chooses; `/paper` hands off to the agent below.
- **Domain rendering.** Transliteration is rendered properly (determinatives raised, indices subscripted), and results appear as artifact citation cards.

One rule matters more than the rest: **artifact cards are built only from tool results, never from model prose.** Anything without both a P-number and a URL from a real tool response is skipped. Parsed out of the answer text instead, a hallucinated P-number would render as a working CDLI link — the failure most likely to actually mislead a researcher.

### 3. The `/paper` agent

`/paper <topic>` runs a seven-node LangGraph pipeline: discovery → scoping → ingestion → clustering → evaluation → synthesis → citations. Evaluation loops back to scoping while the evidence is weak, capped at two retries. Evaluation and citation checking are plain code, not model calls — verifying a citation is a set difference against what was actually ingested, so there is nothing for a model to decide.

The pipeline's worst failure was a fabricating introduction: the intro and conclusion were written blind to the evidence and invented convincing artifacts and P-numbers. Both now receive the ingested summaries as an explicit valid-id whitelist, and the reference list is built only from ids that were actually read, so it cannot launder a hallucination into a real-looking link.

It runs as its own FastAPI service streaming node-by-node progress, which the chat backend proxies, and exports the finished draft as a PDF. `/paper` is BYOM-only: a run is roughly 15–30 LLM calls against 1–2 for a chat turn, and would exhaust the funded tier's daily cap in two runs. The same method is available to any MCP client without this service, as a `research_paper` prompt and a skill file.

### 4. Deployment and infrastructure

An npm-workspaces monorepo with the Python agent alongside it. All four services are containerized, with a compose file, an nginx config, and a script for a no-Docker hot-reload run — verified across all four containers on one network with a real streaming chat turn and a full `/paper` run producing a seven-page PDF in 56 seconds. `deploy/framework.md` specifies the framework-side merge request that puts this on CDLI infrastructure: the submodule entry, four compose services, three nginx locations, and the config entries. That merge request has not been raised yet.

## Proposal versus delivered

| Weeks | Proposal deliverable | Status | Note |
|---|---|---|---|
| 1–2 | Study CDLI APIs; finalize server design; basic server; standard response format | Delivered | With `get_metadata` / `search_entity` and `get_inscription` pulled forward |
| 3–4 | `advanced_search` with `ground_term`; `search_entity` and `get_metadata`; Inspector testing | Delivered with changes | Landed in weeks 1–2, freeing weeks 3–5 for `cqp_query`, the HTTP transport and the chat plan |
| 5 | Response compression; normalize output; reduce token usage | Delivered | Shipped in week 2 |
| 6 | STDIO and Streamable HTTP transports; Inspector and Claude Desktop; Dockerize | Delivered | HTTP transport in week 3; Docker and the Claude Desktop test in week 6 |
| 7–8 | React/Vite chat widget; AES-256-GCM keys; FIFO context window | Delivered with changes | A full SPA rather than a per-page widget, since funded keys cannot live in a browser; it talks to a Node backend that hosts MCP, not to `/mcp` directly; context trimming is a token budget, not a fixed message count |
| 9–10 | `/paper` LangGraph workflow | Delivered with changes | All seven nodes built. Runs as its own service, not client-side middleware. `get_metadata` is not called at ingestion — the search cards already carry that metadata |
| 11 | Local site integration; E2E tests; edge cases; performance | Delivered with changes | Local integration is real (compose plus nginx). Tests cover the server only — 91 passing; nothing automated covers the chat workspaces or `agent-paper` |
| 12 | Soft-deploy on CDLI-like cloud infra; documentation; feedback; finalize | Partially delivered | Fully documented and containerized, but the framework merge request is not raised, so nothing runs on CDLI infrastructure yet. A development instance is public on GCP |
| — | Tool-loop guard: 5 consecutive calls | Delivered with changes | Documentation-only in the MCP server, by design; the chat backend enforces a real cap of 25 |
| — | Beyond the proposal | Delivered | MCP Apps renderers, the `research_paper` prompt and skill, `search_after` deep paging, PDF export, a sixth provider, and the identity / rate-limit / budget layer |

## Weekly index

Week 1 begins Monday 2026-05-25, the first day of the coding period; the community-bonding post covers the period before it.

| Week | Dates | Headline |
|---|---|---|
| 0 | to 05-24 | [Community bonding]({{ site.baseurl }}/gsoc26/McpServerAndAgent/posts/00_week0) — architecture agreed with mentors, and the decision to build `cdli.earth/chat` as a page rather than a widget |
| 1 | 05-25 – 05-31 | [Scaffolding the server and the first CDLI tools]({{ site.baseurl }}/gsoc26/McpServerAndAgent/posts/01_week1) |
| 2 | 06-01 – 06-07 | [Search, fuzzy grounding, and leaner payloads]({{ site.baseurl }}/gsoc26/McpServerAndAgent/posts/02_week2) |
| 3 | 06-08 – 06-14 | [The CQP query tool and HTTP transport]({{ site.baseurl }}/gsoc26/McpServerAndAgent/posts/03_week3) — the seventh tool completes the Phase 1 surface |
| 4 | 06-15 – 06-21 | [Drafting and finalizing the chat interface plan]({{ site.baseurl }}/gsoc26/McpServerAndAgent/posts/04_week4) |
| 5 | 06-22 – 06-28 | [Hardening the server, and finishing the chat plan]({{ site.baseurl }}/gsoc26/McpServerAndAgent/posts/05_week5) |
| 6 | 06-29 – 07-05 | Monorepo restructure, the first test suite, MCP Apps renderers, Docker, and the first chat-backend branch |
| 7 | 07-06 – 07-12 | The chat backend skeleton — Express route, MCP client, agentic tool loop |
| 8 | 07-13 – 07-19 | SSE streaming with tool-progress events, and an abort chain that halts backend spend mid-stream |
| 9 | 07-20 – 07-26 | The React SPA shell, verified end to end against the full local stack |
| 10 | 07-27 – 08-02 | BYOM key encryption, the identity and rate-limit layer, and the domain gate reduced to a prompt |
| 11 | 08-03 – 08-09 | Context trimming, the IPv6 rate-limit fix, and the first full cut of the `/paper` agent |
| 12 | 08-10 – 08-16 | [Boxing it up, and the last of the interface]({{ site.baseurl }}/gsoc26/McpServerAndAgent/posts/12_week12) — containerization, the deployment spec, the funded tier made reachable, and the final UX work |
