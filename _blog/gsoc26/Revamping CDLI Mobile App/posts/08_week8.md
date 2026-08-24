---
layout: page
title: "Mobile App: Week 8"
author: 'Shiva Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'mobile', 'react-native', 'week#8', 'Phase-2']
---

## Week Summary

Week 8 added the two informational screens - **About CDLI** and **Help & FAQ** - and the **side drawer** that gets you to them. Up to this point the drawer existed but held a single item, so this was as much about navigation as content.

**Why the drawer needed custom content:** Expo Router's drawer generates its item list automatically from the registered screens, and you can style the rows with plain options - active background, active tint, inactive tint. That covers the rows, but it renders **only** the rows. There's no slot above or below them, and the design needs both: a CDLI header with the app version at the top, and a "Visit cdli.earth" button plus an "Open Source • GSoC 2026" line pinned to the bottom.

So I passed custom `drawerContent`, but deliberately **kept the framework's item list** rather than hand-rolling the rows. Wrapping `DrawerItemList` between my own header and footer means labels, icons, the active pill and accessibility all still come from each screen's own options, and I only own the parts the framework doesn't provide. That's about 40 fewer lines than looping over my own `Pressable`s, and the row behaviour isn't mine to get wrong.

**About CDLI:** The app logo (the same asset as the app icon and splash, so there's one source of truth), the CDLI wordmark, the mission statement, the team, and buttons through to cdli.earth and the CDLI GitLab. The app version renders from `expo-constants`, reading `app.json` at runtime - bump the version in one place and both the drawer badge and this screen follow. I render it **conditionally** rather than falling back to a hardcoded `"1.0.0"`, because a hardcoded fallback duplicates the version number and would confidently display the wrong one if the config were ever unavailable. A missing badge is better than a lying badge.

**Help & FAQ:** A FAQ / Send Feedback segmented control. The FAQ is a single-open accordion of five entries covering the Tablet of the Day, contributing, searching, image use and citation. All the content is bundled in the app, so it needs no network. Both the "Contact Support" and "Send Feedback" actions open the device mail client via `mailto:` - consistent with how CDLI already handles user communication on the website - going to the same support address with **different subject lines**, so the team can still tell feedback from a bug report.

All the shared copy - URLs, the support address, the mission text, the team, the FAQ entries - lives in one `lib/constants.ts` rather than being scattered across the two screens.

## Work Breakdown

| Area | What I did | MR |
|------|-----------|-----|
| Drawer | Custom `drawerContent`: header + version badge, framework `DrawerItemList`, Visit cdli.earth, GSoC footer | [!8](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/8) |
| About CDLI | App-icon logo, mission, team, links to cdli.earth + GitLab, runtime app version | [!8](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/8) |
| Help & FAQ | FAQ / Feedback tabs, single-open accordion, `mailto:` support actions | [!8](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/8) |
| Content | `lib/constants.ts` as the single source for URLs, email, mission, team, FAQ | [!8](https://gitlab.com/cdli/cdli-mobile/-/merge_requests/8) |

## What's next

- The **Highlights** feature: CDLI's curated artifacts, from the postings endpoint.
