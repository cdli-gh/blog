---
layout: page
title: "Mobile App: Week 4"
author: 'Shiva Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'mobile', 'react-native', 'week#4', 'Phase-1']
---

## Week Summary

Week 4 focused on making Browse more usable and the app faster and offline-friendly: **sorting and a list/grid view toggle**, plus **offline caching** of both data and images.

**Browse controls:** I added a sort menu and a view toggle to the Browse list. The sort menu offers A-Z, Z-A, Newest first, and Oldest first - it sorts a copied array (never mutating the cache) and is memoized so it only recomputes when needed. The view toggle switches between a vertical list and a card grid, and the grid is **responsive**: the number of columns is derived from the screen width (minimum 2), so it shows more columns on tablets and adapts automatically on rotation.

**Offline data caching:** I persisted the TanStack Query cache to **MMKV** using `PersistQueryClientProvider` with an MMKV-backed persister. The feed is saved to disk, so on the next launch the app opens **straight to data with no network call**, and the catalogue stays browsable offline. A `maxAge` keeps the cache fresh over time.

**Image caching:** I set `cachePolicy="memory-disk"` on the tablet images (cards, list rows, and the detail hero). Viewed images are held in memory for instant re-display and saved to disk so they survive restarts - which makes scrolling smoother and list -> detail -> back navigation instant. So data lives in MMKV and image files in expo-image's own disk cache, two layers working together.

I attended the **weekly standup** to share progress. I also gave my mentor a heads-up that the next ~1.5 weeks will be lighter on my side - I have college exams and mock interviews in that window - so the pace slows a little during that stretch, and picks back up right after. Noting it here for transparency.

## Work Breakdown

| Area | What I did | MR |
|------|-----------|-----|
| Browse controls | Sort menu (A-Z / Z-A / newest / oldest) + list/grid toggle with responsive columns | [!4](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/4) |
| Offline data | Persist TanStack Query cache to MMKV (offline + instant cold start) | [!5](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/5) |
| Image caching | `cachePolicy="memory-disk"` on tablet images (memory + disk) | [!5](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/5) |

## What's next

- In-app search over the catalogue.
- A full-screen image viewer with zoom and pan.
