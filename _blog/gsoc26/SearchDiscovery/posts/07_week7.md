---
layout: page
title: "Search & Discovery: Week 7"
author: 'Harsh Chandwani'
tags: ['week', 'gsoc', 'gsoc2026', 'SearchDiscovery', 'week#7', 'Phase-2']
---

## Week Summary

Phase 1 wired the pipeline for exactly one entity type: artifacts. Phase 2 brings
publications, collections, proveniences and periods into search, and none of that can
start while the pipeline assumes artifacts everywhere. This week removed that
assumption, then gave PHP ownership of the one thing Logstash still did: creating the
index itself.

**Pipeline generalization ([!1266](https://gitlab.com/cdli/framework/-/merge_requests/1266)).**
The outbox table always had an `entity_type` column, but nothing read it: every enqueue
hardcoded artifact, the poller only knew how to build artifact documents, and the search
controller queried the `artifacts` index by a literal string. This MR turns each of
those into a real seam. Enqueue calls take an entity type now, defaulting to artifact so
the existing call sites don't change. The poller groups claimed rows by type and picks
each group's document builder from a factory. The read side asks a small registry for
the index name instead of spelling it out. Groups fail independently, which matters more
than it sounds: if a future entity type ships a broken builder, its rows park for the
watchdog and artifact indexing keeps flowing. The whole MR is behavior-preserving, and
the gate proves it: every indexed document byte-identical, the full suite green.

**Index lifecycle in PHP ([!1270](https://gitlab.com/cdli/framework/-/merge_requests/1270)).**
Until now, no PHP code could create a search index: the mapping lived in a Logstash
template that gets deleted at cutover. This MR adds a lifecycle service and two
commands: one creates a versioned index (`artifacts_v1`) with its mapping and settings
and verifies what the engine actually stored by reading the mapping back, the other
moves aliases atomically. Reads and writes get separate aliases, so a future rebuild can
fill a new index version while readers stay on the old one, then switch with no
downtime. The artifacts mapping is now authored in PHP as the first user, with one
deliberate change from the legacy template: the wildcard-typed fields become keyword,
because measuring both on real data showed keyword matches Elasticsearch behavior on
OpenSearch where wildcard diverges, and runs about twice as fast doing it. The read-back
check earned its keep immediately: pointed at Elasticsearch, the command catches the
cluster's catch-all legacy template silently merging old fields into new indexes, and
refuses.

Between the two MRs, the pipeline stopped caring which entity it moves and the index
stopped being something only Logstash could make. That is the foundation the new
entities build on.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---    |---    |---    |---    |  
|1       | Monday     |   2026/07/06    | Audited how artifact-specific the pipeline really is: which parts already generalize and which hardcode artifacts |  
|2       | Tuesday      |   2026/07/07    | Planned the generalization: entity-type dispatch in the poller, a builder factory, a registry for read-side index names |  
|3       | Wednesday |  2026/07/08     | Built the factory and threaded entity type through enqueue, claim, and the poller's dispatch; moved the read side onto the registry |  
|4       | Thursday  |   2026/07/09    | Verified documents unchanged byte for byte, ran the poller end to end, and opened the generalization MR ([!1266](https://gitlab.com/cdli/framework/-/merge_requests/1266)) |  
|5       | Friday      |   2026/07/10    | Probed OpenSearch query compatibility on real data; measured keyword against wildcard fields and settled the mapping conventions |  
|6       | Saturday  |  2026/07/11    | Built the index lifecycle service and the create/swap commands with read-back verification; authored the artifacts mapping in PHP |  
|7       | Sunday      |   2026/07/12    | Walked the lifecycle end to end on a live engine, including the rebuild window, and opened the lifecycle MR ([!1270](https://gitlab.com/cdli/framework/-/merge_requests/1270)) |  
