---
layout: page
title: "MCP Server: Week 1"
author: 'Armaan Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'McpServerAndAgent', 'week#1', 'Phase-1']
---

## Week Summary

This week marked the official start of the GSoC coding period. The focus was on setting up the project infrastructure and delivering the first working CDLI MCP tools. The week began with scaffolding the server, CDLI HTTP client, and error utilities, then progressed to building `get_metadata` and `search_entity`. The second half of the week was spent on API exploration, planning the inscription and bibliography tools, and implementing `get_inscription`.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2026/05/25	| Merged `infra/setup` [#1](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/1) MR: scaffolding, CDLI client, error utils, and ping tool; smoke tested via MCP Inspector |  
|2   	| Tuesday  	|   2026/05/26	| Implemented get_metadata and search_entity; added timing utility; fixed stdout→stderr bug in STDIO transport [#2](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/2)	|  
|3   	| Wednesday |  2026/05/27 	| Reviewed merged MRs; tested entity tools against live CDLI API; documented observed API quirks |  
|4   	| Thursday  |   2026/05/28	| Explored CDLI API surface for inscription and bibliography endpoints; noted broken filter routes  |  
|5   	| Friday  	|   2026/05/29	| Discussed inscription tool design with mentors on Slack; agreed on adding multiple format support (ATF, CDLI-CoNLL) |  
|6   	| Saturday  |  2026/05/30	| Finalized get_inscription design and implemented it [#3](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/3)  |  
|7   	| Sunday  	|   2026/05/31	| Implemented get_bibliography with flexible output formats [#4](https://gitlab.com/cdli/cdli-mcp/-/merge_requests/4)  |  
