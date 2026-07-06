---
layout: page
title: "Mobile App: Week 2"
author: 'Shiva Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'mobile', 'react-native', 'week#2', 'Phase-1']
---

## Week Summary

With the navigation backbone and onboarding in place from Week 1, Week 2 was where the app started showing **real CDLI data**. The focus was the **Browse** experience: listing tablets from the CDLI catalogue.

For the data layer I integrated **TanStack Query** against the live `cdli-tablet/feed` endpoint. It gives the screens caching, background refetching, and clean loading/error states out of the box, so I'm not hand-rolling fetch-and-store logic per screen. The fetch also **normalizes the API's hyphenated keys** (`thumbnail-url`, `blurb-title`, …) into a clean camelCase `Tablet` type, and a shared `useTablets` hook means one query is reused across every screen - one fetch, many consumers.

On the rendering side I used **FlashList** rather than a plain `FlatList`. FlashList recycles its row views instead of mounting one per item, so scrolling stays smooth and memory stays low as the catalogue grows.

The Browse experience shows up in two places:
- A **horizontal preview strip** on the **home screen** (first 8 tablets) - a quick entry point from the landing page.
- A full **View All** screen: a **vertical list** of the entire catalogue, with loading and error states (including a reusable offline/retry screen).

I also set up shared **Prettier + ESLint** tooling and formatted the codebase, so styling and linting stay consistent as more contributors touch the project in future.

Alongside the code, I attended the **weekly sync meeting** and had a **call with my mentor** to walk through the progress so far and align on the next steps.

Together this is the pattern I'll reuse across the rest of the data-driven screens: **fetch through TanStack Query, render through FlashList.**

## Work Breakdown

| Area | What I did | MR |
|------|-----------|-----|
| Data layer | TanStack Query + `fetchTablets` (camelCase mapping), shared `useTablets` hook | [!3](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/3) |
| Home | Horizontal preview strip (first 8 tablets) | [!3](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/3) |
| View All | Vertical FlashList of the full catalogue + loading/error states | [!3](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/3) |
| Tooling | Shared Prettier + ESLint config, formatted codebase | [!2](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/2) |

## What's next

- The **artifact detail screen** for an individual tablet.