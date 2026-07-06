---
layout: page
title: "Search & Discovery: Week 5"
author: 'Harsh Chandwani'
tags: ['week', 'gsoc', 'gsoc2026', 'SearchDiscovery', 'week#5', 'Phase-1']
---

## Week Summary

Week 5 designed incremental indexing and built its first merge request: the capture side, which records every change the search index needs to see.

**The approach.** Right now the index is rebuilt from scratch every night by a Logstash job, so an edit can take up to a day to show up. The plan is a transactional outbox: when a change is approved, the affected artifact ids get written to an outbox table in the same transaction as the change itself, so the change and its reindex signal can never disagree. A poller will later read the outbox, rebuild each artifact with the Week 4 document builder, and push it to the search engine within seconds. Most of the design work went into the ordering and failure behaviour: a single poller so updates apply in order, the Logstash job kept as a safety net during the switch, and the retry logic, all settled before any code got written.

**The write-path audit.** Incremental indexing only works if every change is caught. Most edits go through one approval step, which is where they get recorded, but some admin screens write index-relevant data directly, skipping that step, so those changes would be missed. This meant checking every write path to a table the document reads. There are thirteen of them across ten controllers, and some touch a lot of artifacts at once: renaming a single author or region can affect hundreds of thousands.

**The capture merge request ([!1243](https://gitlab.com/cdli/framework/-/merge_requests/1243)).** With the design settled and the write sites known, the first merge request builds the capture side: the outbox table, a small helper that records the affected artifacts, and a hook at every write path, both the approval flow and all thirteen direct-write sites. Each hook wraps its data change and its outbox write in one transaction, so the two commit or roll back together. There are tests for every site, and nothing reads the queue yet; the poller is the next merge request.

Two smaller things also went in this week: a change so the index only shows approved image annotations, the same way every other edit is handled, and a few open questions worked out with the mentors so the build could rest on settled decisions.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2026/06/22	| Studied the Logstash reindex and designed the transactional-outbox approach |  
|2   	| Tuesday  	|   2026/06/23	| Worked out the ordering, failure, and retry behaviour and the outbox table shape |  
|3   	| Wednesday |  2026/06/24 	| Audited every code path that writes data the search document depends on |  
|4   	| Thursday  |   2026/06/25	| Verified the audit, split the work into staged merge requests, and talked through the open questions with the mentors |  
|5   	| Friday  	|   2026/06/26	| Built the outbox table, the enqueue helper, and their tests |  
|6   	| Saturday  |  2026/06/27	| Added a capture hook at the approval flow and all thirteen direct-write sites, with per-site tests |  
|7   	| Sunday  	|   2026/06/28	| Reviewed and opened the capture merge request, and filtered the index to approved annotations |  
