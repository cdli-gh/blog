---
layout: page
title: "Search & Discovery: Week 3"
author: 'Harsh Chandwani'
tags: ['week', 'gsoc', 'gsoc2026', 'SearchDiscovery', 'week#3', 'Phase-1']
---

## Week Summary

Week 3 was about turning `assemble()` into the real thing. The data layer from Week 2 pulls the rows, this week is the transform that turns them into the actual search document, in two halves, with a parity test checking the output against the live index the whole way. Two MRs.

**Flat half and the parity test ([!1236](https://gitlab.com/cdli/framework/-/merge_requests/1236)).** `assemble()` now builds the flat fields: the scalars and single joins, the ascii-folded fields, the Arabic `provenience_ar` graft, the multi-value arrays (collections, materials, genres, languages), and the id consolidation. The parity test is the piece everything else leans on. It runs `assemble()` over captured rows and compares the result to the live ES document, and since the transform never touches a database it runs off JSON fixtures with no database or search engine. The builder isn't an exact copy of Logstash, it quietly fixes a few of its quirks, so the comparator knows about each one: an intended difference passes, a real regression still fails. The review caught a good one, a composite-number split the comparator was missing that would have failed a correct builder on ~560 artifacts.

**Nested objects ([!1237](https://gitlab.com/cdli/framework/-/merge_requests/1237)).** The other half: the four record arrays (`external_resource`, `asset`, `update`, and `publication`), again as pure transforms over the same rows. Each array is compared as an unordered multiset, and the orderings a multiset can't catch (author/editor order, the creator-first update combine) are pinned by unit tests instead. Two of the differences here are actually places the builder is more correct than the current index: it de-duplicates an update event Logstash counts twice, and it indexes publications Logstash drops entirely when their type is empty (574 documents). Those will change `_source` for those documents at cutover, so they're flagged to check before the switch. After this, the only thing left to build is the ATF block.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2026/06/08	| Planned the transform and checked every output rule against the live index and database |  
|2   	| Tuesday  	|   2026/06/09	| Built the flat `assemble()` fields: scalars, diacritics, the multi-value arrays, the id consolidation |  
|3   	| Wednesday |  2026/06/10 	| Built the parity test and its fixtures, and the per-stage unit tests |  
|4   	| Thursday  |   2026/06/11	| Reviewed the flat half, opened the first MR ([!1236](https://gitlab.com/cdli/framework/-/merge_requests/1236)) |  
|5   	| Friday  	|   2026/06/12	| Built the nested arrays (external_resource, asset, update, publication) |  
|6   	| Saturday  |  2026/06/13	| Added the multiset comparator rule and the unit tests for the nested arrays, cross-checked against live ES |  
|7   	| Sunday  	|   2026/06/14	| Reviewed the nested half, found two Logstash bugs the builder corrects, opened the second MR ([!1237](https://gitlab.com/cdli/framework/-/merge_requests/1237)) |  
