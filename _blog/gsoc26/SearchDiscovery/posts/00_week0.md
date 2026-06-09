---
layout: page
title: 'Search & Discovery: Community Bonding'
author: 'Harsh Chandwani'
tags: ['week', 'gsoc', 'gsoc2026', 'SearchDiscovery', 'week#0', 'Community Bonding']
---

## Summary

Community bonding ran from **May 1 to May 24**, and for me it was almost entirely about planning and aligning with my mentors before writing a single line of code. It kicked off with the joint onboarding session where all four GSoC 2026 contributors and the CDLI mentors got together, introduced ourselves, and talked through our projects.

Most of the real work this period happened in mentor meetings. I had **two meetings with Vedant** where we walked through the full scope of the project and split the coding period into two phases, each tracked as an epic on GitLab:

- [**Phase 1: Search & Discovery Improvements**](https://gitlab.com/cdli/framework/-/work_items/2609) (before midterm): OpenSearch setup, the PHP document builder that replaces the Logstash Ruby filter, the ATF parser, incremental indexing via the Transactional Outbox, and fixing existing search bugs.
- [**Phase 2: Search & Discovery Improvements**](https://gitlab.com/cdli/framework/-/work_items/2619) (after midterm): making publications, collections, proveniences, and periods searchable through OpenSearch, building fallback reindex utilities with an admin UI, and adding performance logging for the Elasticsearch-to-OpenSearch comparison.

I linked every sub-issue under its phase epic, and each sub-issue carries its own design document covering the approach, edge cases, acceptance criteria, and a rough estimate, so once coding starts there's no ambiguity about what each piece needs to do.

### Phase 1 sub-issues

| Task | Issue |
| --- | --- |
| OpenSearch Setup | [#2614](https://gitlab.com/cdli/framework/-/work_items/2614) |
| ArtifactDocumentBuilder (PHP replacement for the Logstash Ruby filter) | [#2616](https://gitlab.com/cdli/framework/-/work_items/2616) |
| Incremental Indexing (Approach & Design) | [#2610](https://gitlab.com/cdli/framework/-/work_items/2610) |

### Phase 2 sub-issues

| Task | Issue |
| --- | --- |
| Search Inconsistency Across Entity Types (Approach & Design) | [#2611](https://gitlab.com/cdli/framework/-/work_items/2611) |
| Fallback Reindex Utilities | [#2615](https://gitlab.com/cdli/framework/-/work_items/2615) |
| Elasticsearch Performance Timing & Logging | [#2613](https://gitlab.com/cdli/framework/-/work_items/2613) |
| Existing Search Issues (Triage & Grouping) | [#2622](https://gitlab.com/cdli/framework/-/work_items/2622) |

I also had a meeting with **Émilie and Lars** to lock down the trickier technical calls, mainly the Transactional Outbox pattern for incremental indexing, and the decision to run **OpenSearch alongside Elasticsearch** for a while so we can compare the two side by side rather than doing a hard cutover.

By the end of community bonding the full roadmap was agreed on and ready to execute, so I could jump straight into building once the coding period began.
