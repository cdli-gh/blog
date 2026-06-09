---
layout: page
title: "Search & Discovery: Week 2"
author: 'Harsh Chandwani'
tags: ['week', 'gsoc', 'gsoc2026', 'SearchDiscovery', 'week#2', 'Phase-1']
---

## Week Summary

Week 2 was all about starting the **ArtifactDocumentBuilder**, the PHP replacement for the Logstash Ruby filter that builds artifact search documents. Moving this into PHP lets us assemble documents one artifact at a time, which is what makes incremental indexing possible instead of a nightly full reindex. The work went out as two MRs.

**Foundation ([!1230](https://gitlab.com/cdli/framework/-/merge_requests/1230)).** The `DocumentBuilderInterface` contract, the builder skeleton with an `assemble()` seam for the later parity tests, and the diacritics and exact-reference helpers ported from `artifacts.rb`, backed by 22 pure unit tests (no database or search engine). Review caught a real bug: the `provenience_ar` graft used `preg_replace`, which would misread a `$` or `\` in an Arabic name as a backreference, so I switched it to `preg_replace_callback`.

**Data layer ([!1231](https://gitlab.com/cdli/framework/-/merge_requests/1231)).** The trickier half. Four recursive CTEs build the hierarchy paths (artifact_types, materials, genres, languages), loaded once and cached, and twelve fetchers reproduce the Logstash SQL pipeline per artifact in batched `WHERE id IN (...)` queries with every pipeline filter re-applied and no `GROUP_CONCAT`. `build()` returns delete signals for retired or missing artifacts, and a documented row-shape contract gives the next MR a fixed shape to build on. A database-backed test cross-checks each relation against the real `cdli_db` and against the live ES document, including an `EXISTS` guard around a `chemical_data` LEFT JOIN that would otherwise multiply rows.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2026/06/01	| Finalized the ArtifactDocumentBuilder plan and locked the data-fetch and parity decisions |  
|2   	| Tuesday  	|   2026/06/02	| Built the foundation: interface, builder skeleton with the `assemble()` seam, the diacritics and reference helpers, unit tests |  
|3   	| Wednesday |  2026/06/03 	| Tested and reviewed the foundation; hardened the Arabic-name graft against a `preg_replace` backreference edge case |  
|4   	| Thursday  |   2026/06/04	| Wrapped up the first MR ([!1230](https://gitlab.com/cdli/framework/-/merge_requests/1230)); started the data layer, checking each query against the live database |  
|5   	| Friday  	|   2026/06/05	| Built the hierarchy CTEs and the core and multi-value relation fetchers |  
|6   	| Saturday  |  2026/06/06	| Finished the nested fetchers (assets, publications, update events) and wired `build()` and the row-shape contract |  
|7   	| Sunday  	|   2026/06/07	| Tested and reviewed the data layer, cross-checked against the live ES document, opened the second MR ([!1231](https://gitlab.com/cdli/framework/-/merge_requests/1231)) |  
