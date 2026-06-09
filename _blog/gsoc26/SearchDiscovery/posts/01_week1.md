---
layout: page
title: "Search & Discovery: Week 1"
author: 'Harsh Chandwani'
tags: ['week', 'gsoc', 'gsoc2026', 'SearchDiscovery', 'week#1', 'Phase-1']
---

## Week Summary

Week 1 kicked off the coding period, and the focus was standing up OpenSearch alongside the existing Elasticsearch in the CDLI dev environment. I added OpenSearch 2.19.5 as a second search engine next to Elasticsearch 7.17.28 in `docker-compose.dev.yml`, giving it its own ports (9202/9302), a bind-mounted data directory, and basic auth with SSL disabled for local development. The service URL is registered in `app.php` and `config.dev.json`, disabled by default so developers opt in. To confirm both engines behave identically, I ran a 7-test API compatibility check (match_all, match, term, bool, aggregation, and count): all returned identical results, including bit-identical BM25 scores. Mentor review led to enabling authentication on OpenSearch, which had initially gone up with security disabled, and the password was chosen without an `@` character to avoid URL-parsing issues in PHP. The MR ([!1226](https://gitlab.com/cdli/framework/-/merge_requests/1226)) is up against the search-discovery branch with all 9 acceptance criteria met.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2026/05/25	| Confirmed the branching strategy with mentors: a dedicated `phoenix/gsoc/search-discovery` branch that every MR targets throughout the project |  
|2   	| Tuesday  	|   2026/05/26	| Researched and triaged the existing search issues to tackle during the coding period |  
|3   	| Wednesday |  2026/05/27 	| Created issue [#2622](https://gitlab.com/cdli/framework/-/work_items/2622), grouping and categorizing all existing search issues by priority and phase |  
|4   	| Thursday  |   2026/05/28	| Started implementing the OpenSearch service alongside Elasticsearch |  
|5   	| Friday  	|   2026/05/29	| Raised the OpenSearch implementation MR ([!1226](https://gitlab.com/cdli/framework/-/merge_requests/1226)) |  
|6   	| Saturday  |  2026/05/30	| Addressed Vedant's review feedback on MR [!1226](https://gitlab.com/cdli/framework/-/merge_requests/1226) (enabled basic auth, added reference links) |  
|7   	| Sunday  	|   2026/05/31	| Started planning the ArtifactDocumentBuilder approach for Week 2 |  
