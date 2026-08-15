---
layout: page
title: "Search & Discovery: Week 8"
author: 'Harsh Chandwani'
tags: ['week', 'gsoc', 'gsoc2026', 'SearchDiscovery', 'week#8', 'Phase-2']
---

## Week Summary

Week 7 made the pipeline generic and gave PHP the ability to create indexes. This week
added the last missing piece of machinery, a full rebuild command, and then used all of
it to bring the first non-artifact entity into search.

**The backfill command ([!1272](https://gitlab.com/cdli/framework/-/merge_requests/1272)).**
`bin/cake search_backfill --entity artifact` rebuilds an entity's whole index: it scans
the source table in keyset order, runs each page through the entity's document builder,
and bulk-pushes through the write alias. The full artifact corpus, 419,480 documents,
rebuilds in about two minutes, and re-running it is safe: same counts, same documents.
The subtle part was the poller running at the same time. Both writers share the write
alias, and every ordering of the two is safe except one: an edit that lands between a
batch being built and being pushed gets overwritten by the older document, and its
outbox row is already done, so nothing would notice. The command closes that window by
re-enqueueing, after the scan, every id the poller had in flight during the run, so the
poller rebuilds those few ids fresh. During testing, an edit approved mid-run came out
correct on the first try.

**Proveniences ([!1274](https://gitlab.com/cdli/framework/-/merge_requests/1274)).**
The first entity to go through the whole pipeline end to end, chosen because it is the
smallest, and built deliberately as the template the remaining entities copy. A document
builder and a PHP-authored mapping; capture at the approval path, including fan-out, so
a region rename rebuilds both the provenience documents and the artifact documents it
touches; and a read side where OpenSearch answers the matching and the region facet in
one query while MySQL keeps doing what it already did well, hydration, ordering,
pagination. If the engine is down, the page falls back to the exact database query it
used before. Proving the new search equal to the old one took a parity harness: the same
parameters through the old LIKE query and the new engine query, 265 parameter sets
derived from live data, every divergence pinned and explained. The harness earned its
keep by finding a real data quirk: seven provenience names store their diacritics in a
form the database collation cannot fold, two of which cannot be found on the live site
today by typing their name at all. The engine finds all of them; the curatorial call on
fixing the rows is now with the mentors.

Incremental indexing, index creation, and full rebuilds now all work for any registered
entity, and one real entity runs on them in production shape.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---    |---    |---    |---    |  
|1       | Monday     |   2026/07/13    | Planned the backfill: keyset scan, batch shape, and the concurrent-writer window the tail re-enqueue closes |  
|2       | Tuesday      |   2026/07/14    | Built the backfill service and command with the memory preflight and progress output |  
|3       | Wednesday |  2026/07/15     | Ran the full 419k rebuild live with the poller up, verified the mid-run edit case, and opened the backfill MR ([!1272](https://gitlab.com/cdli/framework/-/merge_requests/1272)) |  
|4       | Thursday  |   2026/07/16    | Built the provenience document builder and mapping, and registered the entity across the pipeline |  
|5       | Friday      |   2026/07/17    | Built capture for proveniences: approval-path rows, region and location fan-out, delete handling |  
|6       | Saturday  |  2026/07/18    | Built the read side: engine matching with the region facet, database fallback, the page unchanged otherwise |  
|7       | Sunday      |   2026/07/19    | Built the parity harness, pinned and explained every divergence, and opened the proveniences MR ([!1274](https://gitlab.com/cdli/framework/-/merge_requests/1274)) |  
