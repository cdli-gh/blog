---
layout: page
title: 'Mobile App: Community Bonding'
author: 'Shiva Gupta'
tags: ['week', 'gsoc', 'gsoc2026', 'mobile', 'react-native', 'week#0', 'Community Bonding']
---

## Summary

The community bonding period kicked off on **4th May** with a joint kickoff call where all four GSoC 2026 contributors and the CDLI mentors got together. We introduced ourselves, walked through our projects, and got a feel for how the community works. One line from that call stuck with me - **getting selected isn't the win; completing the project is the real win**. That framing has shaped how I've been approaching every standup and review since.

We agreed to run **weekly standups every Wednesday** with the whole GSoC cohort and mentors. We've had four so far, and they've been useful for pulse-checking the project - what each of us is doing, the approaches we're considering, and what blockers or resources we need. Hearing the other contributors talk through their problems has also been a good way to spot patterns I can apply to my own work.

On the project side, I had **two separate one-on-one meetings with my project mentor**. We went deep on the scope of the mobile app revamp. The previous CDLI mobile apps are no longer maintained and don't run on current devices, so this isn't a migration - we're starting fresh. That made a lot of the early conversation about foundational choices: the architecture, the libraries we want to commit to long-term, how the app will talk to the current CDLI API, and the platform differences we need to plan for between Android and iOS. We also covered the tooling and access I'll need to move quickly once coding officially begins.

I didn't wait for the official coding period to start writing code. I used the community bonding window to get a head start on the **backend pieces** that the mobile app will lean on, and opened three merge requests during this period:

- [!1223](https://gitlab.com/cdli/framework/-/merge_requests/1223) — add `id` and `author` to the `cdli-tablet` feed so the mobile app can navigate and attribute tablets correctly
- [!1183](https://gitlab.com/cdli/framework/-/merge_requests/1183) — fix the first-entry delete bug and add a confirmation dialog for bulk deletes in the cdli-tablet admin
- [!1224](https://gitlab.com/cdli/framework/-/merge_requests/1224) — enforce role 8 (cdli tablet manager) in the admin access gate so non-admins with that role can manage tablets

Alongside the backend work, I've been **finalizing the Figma designs** for the new app - settling the design system (colors, typography, spacing), the navigation flow, and the redesigned artifact detail screen. The goal is to walk into Week 1 with the designs locked so I can move straight to implementation rather than designing as I build.

Plenty more to go but community bonding has set a solid base. Next up: coding period officially begins, and I'll start cutting into the React Native upgrade and the new design system.
