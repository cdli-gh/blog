---
layout: page
title: "Search & Discovery: Week 9"
author: 'Harsh Chandwani'
tags: ['week', 'gsoc', 'gsoc2026', 'SearchDiscovery', 'week#9', 'Phase-2']
---

## Week Summary

One entity this week, but the hardest one. Publications is twenty times the size of
proveniences, searched through ten filters instead of two, and it is where the template
from last week had to prove it survives contact with a bigger entity.

**Publications ([!1277](https://gitlab.com/cdli/framework/-/merge_requests/1277)).**
The shape is the proveniences template: a document builder and PHP mapping, capture at
the approval path with fan-out (an author rename rebuilds publication documents and
artifact documents from one approval, and the three-way merge flow is captured too), an
engine-backed page with facets and a database fallback, and a parity harness run at the
end. Two things had to change at this scale, and both were settled by measurement rather
than taste. First, ordering: proveniences let MySQL sort because the whole match set fit
in one request, but 16,686 rows do not, so the page is now sorted by the engine, using
sort keys derived from the database's own collation weights, and the result was checked
the hard way: zero differing positions across all 16,686 rows on every offered ordering.
Second, accent folding: publications has 341 titles storing combining marks, so the
proveniences approach of pinning each case one by one would have drowned the harness.
Instead the fold was rebuilt to mirror exactly what the database collation does, which
collapsed the divergences from hundreds down to a pinned, explained few dozen. The
harness ran 904 parameter sets against the live data and every remaining divergence is
pinned with the condition under which its pin gets deleted.

The harness also turned up the same data quirk the proveniences run found, just at a
larger scale: many of those combining-mark titles cannot be found by typing on the live
site today. That is written up for the mentors next to the proveniences case, since the
same eventual fix covers both.

With publications open, four of the five entity types are searchable through the engine
or on their way there. Collections and periods are next, and both are smaller than
anything the template has already survived.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---    |---    |---    |---    |  
|1       | Monday     |   2026/07/20    | Measured the two open questions on real data: the accent-folding approach and the sort-key design for engine-side ordering |  
|2       | Tuesday      |   2026/07/21    | Built the publication document builder and mapping, sort keys included |  
|3       | Wednesday |  2026/07/22     | Built capture: approval-path rows, author fan-out, and the merge flow with its proof test |  
|4       | Thursday  |   2026/07/23    | Built the search query and the controller refactor with engine-sorted paging |  
|5       | Friday      |   2026/07/24    | Built the facets and the fallback path; walked deep paging and every filter against SQL |  
|6       | Saturday  |  2026/07/25    | Ran the parity harness's 904 parameter sets; pinned and explained the remaining divergences |  
|7       | Sunday      |   2026/07/26    | Walked the whole entity end to end, wrote the MR story, and opened the publications MR ([!1277](https://gitlab.com/cdli/framework/-/merge_requests/1277)) |  
