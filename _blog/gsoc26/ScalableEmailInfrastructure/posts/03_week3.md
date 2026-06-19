---
layout: page
title: "Scalable Email Infrastructure: Week 3"
author: 'Sonika Chowdary Gutha  '
tags: ['week', 'gsoc', 'gsoc2026', 'ScalableEmailInfrastructure', 'week#03']
---

## Summary

This week refactored the current transactional email flows to use the queue instead of sending directly. I replaced `UserMailer->send()` calls in `UsersTable.php` and `ForgotController.php` with `EmailQueueService->enqueueMailerAction()` for `welcome`, `adminNewUser`, `adminCrowdsourcingPrivilege`, and `resetPassword`. Emails are now queued in `email_jobs` and signaled to Redis, but actual sending will start in Week 4 with the background worker.

## Daily Work Update

|#|Day|Date| A short description of the work done                                                              |
|---|---|---|---------------------------------------------------------------------------------------------------|
|1|Monday|2026/06/08| Reviewed current email send call sites and finalized Week 3 refactor scope.                       |
|2|Tuesday|2026/06/09| Planned payload structure for the four transactional email flows.                                 |
|3|Wednesday|2026/06/10| Refactored `UsersTable` to enqueue `welcome`, `adminNewUser`, and `adminCrowdsourcingPrivilege`.  |
|4|Thursday|2026/06/11| Refactored `ForgotController` to enqueue `resetPassword` with high priority.                      |
|5|Friday|2026/06/12| Added `HIGH_PRIORITY` constant and removed direct `MailerAwareTrait` usage from refactored files. |
|6|Saturday|2026/06/13| Verified Weeks 1–3 alignment with syntax, lint, and flow checks and started raising PR.           |
|7|Sunday|2026/06/14|                                                                                                   |