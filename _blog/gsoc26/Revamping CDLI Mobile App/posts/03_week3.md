---
layout: page
title: "Mobile App: Week 3"
author: 'Shiva Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'mobile', 'react-native', 'week#3', 'Phase-1']
---

## Week Summary

Week 3 built on the Browse experience from Week 2 by adding the **tablet detail screen** (the page you land on when you tap a tablet) and a **custom HTML renderer** for the rich descriptions the CDLI API returns.

**The detail screen:** Tapping a tablet opens a full detail view: a large hero image, an author badge, the date, a short blurb, and the long description. The tablet is looked up straight from the cached list via a shared `useTablet` hook, so no extra network request is needed. Because the feed doesn't expose an `id` or `author` field yet, the screen currently uses the tablet's `url` as a temporary key and a placeholder author name. To fix this at the source, I opened a backend MR on the CDLI framework [!1223](https://gitlab.com/cdli/framework/-/merge_requests/1223) that adds `id` and `author` to the feed -> once it merges, the app switches to a real unique `id` and proper author names, each a one-line change. The **Share, Bookmark, and View-on-CDLI** actions are in place as UI for now, to be wired up in a later week.

**Why a custom HTML renderer:** The description field (`full-info`) comes back as **HTML** - italics, bold, paragraphs, and links. The obvious choice was `react-native-render-html`, but I decided against it: it's effectively unmaintained and predates React 19, and it leans on patterns React has deprecated - a real risk of breaking on a future upgrade, which is a poor bet for a project meant to be maintained long-term.

Instead I inspected the actual descriptions across the whole catalogue and found the HTML uses a small, fixed set of tags (`<i> <b> <a> <sub> <sup> <p> <br> <font>`) - nothing exotic like tables or images. That made a dependency-free renderer both tractable and future-proof, so I built my own:

- **`parseHTML.ts`** -> a small parser that turns an HTML string into a node tree, using a tokenizer plus a stack to handle nesting (e.g. a link inside italics) correctly, and decoding HTML entities.
- **`HtmlContent.tsx`** -> walks that tree and renders it into nested React Native `<Text>` elements, mapping each tag to a style (italic, bold, sub/sup, paragraph breaks). Links are tappable and open via `Linking`, with relative CDLI links resolved to full URLs.

The result renders the descriptions natively (so they flow inside the scroll view and feel native), with zero external dependency and no compatibility risk.

> **Milestone 1 achieved: Data visible.** Users can now browse the CDLI catalogue, open any tablet, and read its full formatted description - the app is showing real data end to end.

## Work Breakdown

| Area | What I did | MR |
|------|-----------|-----|
| Detail screen | Hero image, author badge, date, blurb, description, action buttons (UI) | [!3](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/3) |
| Navigation | Tap -> detail via `url` key + cached `useTablet` lookup (no `id` yet) | [!3](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/3) |
| HTML rendering | Custom `parseHTML` (tokenizer + stack) + `HtmlContent` (tree -> native `<Text>`) | [!3](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/3) |

## What's next

- Sorting and a list/grid view toggle for the Browse screen and also caching.
