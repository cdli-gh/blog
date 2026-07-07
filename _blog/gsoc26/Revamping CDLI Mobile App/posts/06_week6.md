---
layout: page
title: "Mobile App: Week 6"
author: 'Shiva Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'mobile', 'react-native', 'week#6', 'Phase-1']
---

## Week Summary

Week 6 added the **full-screen image viewer**, the last piece of my midterm commitment. so a user can now open any tablet image and inspect it up close.

**The viewer:** Tapping the hero image (or the "View Full Image" button) on the detail screen opens a full-screen viewer with **pinch-to-zoom, panning with momentum, and double-tap zoom**. I built it on `ResumableZoom` from `react-native-zoom-toolkit`, which rides on the reanimated + gesture-handler I already had - so no new native modules, just one JS dependency.

**Crisp on zoom:** The main challenge with a zoom viewer is that images blur when you zoom in. I handle that with three things together: loading the **full-resolution** image (not the thumbnail), `allowDownscaling={false}` on expo-image (so it decodes at full resolution instead of downscaling to the display size), and a `memory-disk` cache policy. The result stays sharp as you zoom.

**Fast + graceful:** While the full image loads, the viewer shows the **already-cached thumbnail** as an instant placeholder (so you never stare at a black screen), with a spinner over it. If the image fails to load (offline, a bad URL, a 404), it shows a clear "couldn't load image" state instead of spinning forever.

> **Midterm milestone reached.** The app now covers the full core experience end to end: browse the catalogue (list + grid), open a tablet, read its formatted description, search, and view images full-screen with zoom - all working offline via on-device caching.

Alongside the code, I attended the **weekly standup** and shared a checkpoint with my mentors, along with a few product and data-quality questions to line up the next phase of work.

## Work Breakdown

| Area | What I did | MR |
|------|-----------|-----|
| Image viewer | Full-screen `ResumableZoom` viewer (pinch / pan / momentum / double-tap) | [!7](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/7) |
| Crisp zoom | Full-res image + `allowDownscaling={false}` + `memory-disk` (no blur) | [!7](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/7) |
| UX states | Thumbnail placeholder, loading spinner, and load-error state | [!7](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/7) |

## What's next

- Wire the **Share / Bookmark / View-on-CDLI** actions.
- The **Saved** (bookmarks) screen.
- Begin the **Highlights** feature.
