---
layout: page
title: "Mobile App: Week 5"
author: 'Shiva Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'mobile', 'react-native', 'week#5', 'Phase-1']
---

## Week Summary

As I'd flagged to my mentor last week, most of this stretch went to college, end-semester exams and mock interviews - so it was a lighter coding week by design. Even so, I worked on the **in-app search** for the catalogue.

**Search:** Search runs entirely **client-side over the cached catalogue**, so it's instant and works offline (no extra network calls). Typing filters tablets by title, theme, and blurb, with a live result count and clear empty / no-results states. The input is **debounced** (a short pause after you stop typing) - it barely matters at the current data size, but it's the right seam for when search grows later.

**Recently Viewed:** When the search box is empty, the screen shows a **Recently Viewed** list instead of a blank state. Opening any tablet records it (stored in MMKV, most-recent-first), so the screen always has a useful starting point.

**Entry points:** The search bar on the home screen now routes into the Search tab with the input **auto-focused**, so you can start typing straight away. The query also clears when you leave the screen, so you always come back to a clean slate.

## Work Breakdown

| Area | What I did | MR |
|------|-----------|-----|
| Search | Debounced client-side search over title / theme / blurb, with count + empty states | [!6](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/6) |
| Recently Viewed | MMKV-backed recent list shown when the query is empty | [!6](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/6) |
| Entry points | Home search bar -> Search tab with auto-focus; clear-on-leave | [!6](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/6) |

## What's next

- A full-screen image viewer with zoom and pan.
- Wiring the Share / Bookmark / View-on-CDLI actions.
