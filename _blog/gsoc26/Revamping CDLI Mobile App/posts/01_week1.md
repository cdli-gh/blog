---
layout: page
title: "Mobile App: Week 1"
author: 'Shiva Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'mobile', 'react-native', 'week#1', 'Phase-1']
---

## Week Summary

Week 1 marked the official start of the coding period, and the focus was on laying the **foundation** the rest of the app will stand on. Since the previous CDLI mobile apps are no longer maintained, this is a from-scratch build, so getting the groundwork right mattered more than shipping features.

The app is built on **Expo (SDK 56) with Expo Router's file-based routing** and **TypeScript**. I set up the **navigation architecture** first: a layered **root Stack -> Drawer -> Tabs** structure (Home, Search, Saved, Settings), so detail and modal screens can push *over* the tabs without the routing turning into a tangle later. I also wired up a `@/*` **path alias** so imports stay clean as the tree grows.

Alongside that I configured **NativeWind v4 (with Tailwind v3)** for utility-first styling, and defined a set of **semantic design tokens** - `background`, `brand`, `ink`, `surface`, `muted` - in the Tailwind config, so colors stay consistent app-wide instead of scattered hex values I'd have to retrofit later.

With the skeleton in place I built the first pass of the **onboarding flow**: a three-slide, full-screen intro with pagination indicators and skip/continue actions. It only shows **once** - completion is persisted with **MMKV** and gated via **`Stack.Protected` route guards**, so returning users skip straight into the app. I also added the **app icon** and **splash screen**.

The second half of the week was design iteration driven by mentor feedback. After review, I **redesigned the app logo** and reworked several **onboarding screens** to match the direction the mentors wanted. I recorded a short walkthrough video of the updated flow and shared it, and the new designs were **approved**.

All of this landed in [**!1**](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/1) (`feat/app-scaffold-and-styling`).

## Work Breakdown

| Area | What I did | MR |
|------|-----------|-----|
| Navigation | Layered root Stack -> Drawer -> Tabs (Expo Router), `@/*` alias | [!1](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/1) |
| Styling | NativeWind v4 + Tailwind v3, semantic design tokens | [!1](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/1) |
| Onboarding | 3-slide flow, MMKV-persisted, `Stack.Protected` (shows once) | [!1](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/1) |
| Branding | Logo redesign, app icon, splash screen | [!1](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/1) |

> **Walkthrough video:** [Link](https://drive.google.com/file/d/19uRtaUuE8Y17dzDsDfuJYIA6HeExAdpg/view?usp=sharing)

Walking out of Week 1, the app has a navigation backbone, a styling system, branding assets, and an approved onboarding flow - exactly the base I wanted before moving into real features.

## What's next

- Begin the **Browse** experience: listing CDLI tablets in the app.
- Wire up data fetching against the CDLI API.
