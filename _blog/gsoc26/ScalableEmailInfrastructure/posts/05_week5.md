---
layout: page
title: Scalable Email Infrastructure Week 5
author: 'Sonika Chowdary Gutha'
tags: ['week', 'gsoc', 'gsoc2026', 'ScalableEmailInfrastructure', 'week#5']
---
## Summary

This week focused on validating the end-to-end email pipeline and starting branded template work. I manually tested the full flow — enqueue → Redis signal → `EmailWorkerCommand` → `UserMailer` send — for all four transactional emails (`welcome`, `resetPassword`, `adminNewUser`, `adminCrowdsourcingPrivilege`) in the dev Docker stack. I confirmed jobs move correctly through `email_jobs` statuses, the worker picks them up via Redis and DB fallback, and emails are delivered through Postfix. After testing, I began redesigning the HTML email templates and shared layout with consistent CDLI branding (logo header, CTA buttons, and structured admin notification tables).

## Daily Work Update

| # | Day       | Date       | A short description of the work done                                                                                                                                       |
|---|-----------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | Monday    | 2026/06/22 | Tested user registration flow end-to-end: verified `welcome` and `adminNewUser` jobs are enqueued and processed by the email worker.                                       |
| 2 | Tuesday   | 2026/06/23 | Tested password reset and crowdsourcing privilege flows; confirmed `resetPassword` and `adminCrowdsourcingPrivilege` emails send with correct payloads.                    |
| 3 | Wednesday | 2026/06/24 | Ran full pipeline checks in Docker — job status transitions, Redis dispatch, DB fallback recovery, and Postfix delivery for all four transactional emails.                 |
| 4 | Thursday  | 2026/06/25 | Started email template design: updated the shared HTML layout with CDLI logo header, branded footer, and consistent typography/spacing.                                    |
| 5 | Friday    | 2026/06/26 | Continued template designs for `welcome`, `resetpassword`, `admin_new_user`, and `admin_crowdsourcing_privilege` HTML templates with styled CTA buttons and detail tables. |
| 6 | Saturday  | 2026/06/27 |                                                                                                                                                                            |
| 7 | Sunday    | 2026/06/28 |                                                                                                                                                                            |