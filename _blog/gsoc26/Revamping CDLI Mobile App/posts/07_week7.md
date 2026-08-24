---
layout: page
title: "Mobile App: Week 7"
author: 'Shiva Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'mobile', 'react-native', 'week#7', 'Phase-2']
---

## Week Summary

Week 7 was the **midterm evaluation** week. I walked my mentors through the app end to end - browse, detail, search, offline, and the zoom viewer - and everything I'd committed to for the midterm was in place. Alongside the review, I paid off the one piece of technical debt I'd been carrying since Week 3.

**The `id` and `author` debt:** Back in Week 3 the tablet detail screen had a compromise I flagged at the time - the feed didn't expose an `id` or an `author`, so the app used the tablet's **image URL as its identity** and showed a placeholder author name. That worked, but it was fragile: the image filenames contain apostrophes and spaces (`nabopolassar'sinscriptions03.jpg`), they were being used as route parameters and list keys, and two entries sharing an image would have collided silently.

My backend MR on the framework, [!1223](https://gitlab.com/cdli/framework/-/merge_requests/1223), **merged and deployed** this week, so the feed now returns both fields. I verified it against production before touching the client: 527 entries, every `id` present, unique and an integer, and every `author` non-empty.

**The migration:** This is the "one-line change" I promised in Week 3, and it turned out to be six files rather than one. `Tablet.id` became a real id instead of a URL, the fetch maps `item.id`, the lookup hook matches on `id`, the detail screen reads an `id` route param, and both list `keyExtractor`s and both card components switched over. What I hadn't appreciated is that **TypeScript caught none of it** - `url` is still a legitimate string field on the type, so every one of those places compiled cleanly while quietly keying by the wrong thing. They had to be found by grep, not by the compiler. So a rename is only type-safe once the old field actually goes away.

The visible payoff is small but real - the author badge now shows the actual scholar who wrote the entry (`Englund, Robert K.`, `Wagensonner, Klaus`) instead of a generic `CDLI` placeholder, and tablets are addressed by a stable id that survives an image being replaced.

> **Milestone 2 achieved: Core App.** Browse, detail, search, swipe-free navigation and the zoom viewer all work end to end and offline, and the app now runs on the real feed contract rather than a workaround.

## Work Breakdown

| Area | What I did | MR |
|------|-----------|-----|
| Backend | `id` + `author` added to the `cdli-tablet` feed, merged and deployed | [!1223](https://gitlab.com/cdli/framework/-/merge_requests/1223) |
| Migration | Switched identity from image URL to feed `id` across types, api, hooks, routes and list keys | [!3](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/3) |
| Attribution | Real author names on the detail screen, placeholder removed | [!3](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/3) |
| Midterm | Demoed the full core flow to mentors | - |

## What's next

- **About CDLI** and **Help & FAQ** screens, reachable from a redesigned side drawer.
