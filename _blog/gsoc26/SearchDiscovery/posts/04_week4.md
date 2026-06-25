---
layout: page
title: "Search & Discovery: Week 4"
author: 'Harsh Chandwani'
tags: ['week', 'gsoc', 'gsoc2026', 'SearchDiscovery', 'week#4', 'Phase-1']
---

## Week Summary

Week 4 completed the document builder and tested it across the full index.

**The ATF block ([!1240](https://gitlab.com/cdli/framework/-/merge_requests/1240)).** The ATF block was the last field group left to build. A new `AtfParser` parses an inscription's ATF string into its seven fields, and the builder emits the raw `atf`/`jtf`/`annotation` scalars alongside it. With this, `assemble()` produces every field the existing Logstash pipeline does.

**Full-index comparison.** Every artifact was then built and compared against the live index, after rebuilding the index from the same database so the comparison would be fair. Of the 419,480 documents, none were produced incorrectly: the large majority are identical, and the rest differ only where the builder is more correct than the existing pipeline, with one case left for the maintainers to decide.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2026/06/15	| Planned the ATF parser against the existing pipeline and live inscription data |  
|2   	| Tuesday  	|   2026/06/16	| Implemented `AtfParser`, wired it into `assemble()`, and wrote the unit tests |  
|3   	| Wednesday |  2026/06/17 	| Reviewed the parser and added the ATF comparator rule with two new parity fixtures |  
|4   	| Thursday  |   2026/06/18	| Restored the database and rebuilt the search index from it for a valid comparison |  
|5   	| Friday  	|   2026/06/19	| Built the full-index comparison tool and ran it across all 419,480 documents |  
|6   	| Saturday  |  2026/06/20	| Reviewed and verified the full set of flagged differences against the database |  
|7   	| Sunday  	|   2026/06/21	| Classified the remaining divergences and prepared the ATF block for merge ([!1240](https://gitlab.com/cdli/framework/-/merge_requests/1240)) |  
