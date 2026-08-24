---
layout: page
title: "Mobile App: Week 9"
author: 'Shiva Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'mobile', 'react-native', 'week#9', 'Phase-2']
---

## Week Summary

Week 9 was **Highlights** - CDLI's curated artifacts (The Flood Tablet, The Cyrus Cylinder, Codex Hammurapi, and others), which come from the `postings` system rather than the daily tablet feed. I built the data layer, a list screen, a detail screen, and a strip on Home.

**It is not the tablet feed with different words.** I expected to reuse most of the Tablets code and found the two endpoints differ in ways that all needed handling:

- **Images are relative and nested.** The tablet feed hands you a finished URL. A highlight gives you `artifact.artifact_assets[0].path` as a fragment like `dl/photo/P273210.jpg`, three levels deep, so the client has to build the URL itself.
- **Fields can be genuinely absent.** Two of the six highlights have no `publish_start` at all - the key is missing, not null. So the published date is optional by design, and the detail screen and list row render it conditionally rather than printing "Invalid Date".
- **Assets can be empty.** Public-access filtering happens server-side, so a highlight whose artifact has only non-public images comes back with an empty asset list. `artifact`, `artifact_assets` and `path` are each optional, and the whole chain collapses into a single `imageUrl: undefined` that the components handle with a placeholder icon.
- **There is no author.** The postings JSON exposes `created_by` as a numeric user id, not a name, so there's no author badge on a highlight the way there is on a tablet for now.
- **The ids overlap.** Highlight ids run 185 to 214, which sits **inside** the tablet id range of 29 to 782. So highlight 187 and tablet 187 are different things, and anything that stores an id has to know which kind it is. That shaped next week's work.

**The screens:** A Home strip with View All, a full list with the same sort menu and list/grid toggle as Browse, and a detail screen with the image, date, HTML body, zoom viewer, and a "View on CDLI" button. Since highlights have a real public page of their own at `/postings/{id}`, that button opens the article the user is actually reading rather than the underlying artifact record.

**One bug I did not expect:** sorting the list made rows visibly appear and disappear. The sort logic was provably fine - all four options return six items with six unique ids. The cause was **FlashList recycling**. Highlight rows vary in height (titles wrap to one or two lines, and two entries have no date line), and when only the *order* changes, FlashList sees the same ids and reuses cells without re-measuring them. Including the sort in the list's `key` forces a remount so every row is measured again. Tablets never showed this because every tablet row is exactly the same height.

**Current status:** the client is done and verified against the endpoint locally - six entries, all with images - but `GET /highlights.json` still returns a 500 on production, so these screens show the offline state until [!1288](https://gitlab.com/cdli/framework/-/merge_requests/1288) is merged and deployed. The mobile MR notes the dependency.

## Work Breakdown

| Area | What I did | MR |
|------|-----------|-----|
| Backend | JSON output added to the `/highlights` endpoint so the app can consume it | [!1288](https://gitlab.com/cdli/framework/-/merge_requests/1288) |
| Data layer | `fetchHighlights` + `useHighlights` / `useHighlight`, relative image paths resolved against the CDLI base | [!9](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/9) |
| Optionality | `publishedAt` and `imageUrl` optional by design; conditional date, placeholder image | [!9](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/9) |
| Screens | Home strip, list with sort + list/grid, detail with zoom and "View on CDLI" -> `/postings/{id}` | [!9](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/9) |
| Fix | Sort included in the FlashList `key` so variable-height rows re-measure on reorder | [!9](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/9) |

## What's next

- Wire the **Share** and **Bookmark** actions that have been sitting as UI since Week 3.
- The **Saved** screen.
