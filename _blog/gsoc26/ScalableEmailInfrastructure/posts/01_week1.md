---
layout: page
title: "Scalable Email Infrastructure: Week 1"
author: 'Sonika Chowdary Gutha  '
tags: ['week', 'gsoc', 'gsoc2026', 'ScalableEmailInfrastructure', 'week#1']
---

## Summary

Week 1 laid the foundation for the email queue system: the `email_jobs` table, the CakePHP model layer around it, and the validation that keeps the queue consistent before any worker exists to consume it. This work is tracked in [MR !1235](https://gitlab.com/cdli/framework/-/merge_requests/1235).

I started with a CakePHP migration to create the `email_jobs` table, defining columns for job identity (`mailer`, `action`, `payload`), lifecycle status, scheduling data (priority, attempt count, retry timing), and outcome tracking (`sent_at`, `failed_at`, `last_error`). On top of that I added an `EmailJob` entity that keeps worker-managed fields like `status` and `attempt_count` out of mass assignment, so only the background worker (once it exists) will ever be able to move a job through its lifecycle — not a controller by accident. The `EmailJobsTable` class defines which mailer/action combinations are actually allowed to be queued, along with the payload keys each one requires, and validates mailer names, action names, JSON payload structure, user IDs, and URLs. I closed the week out with fixtures and a first pass of unit tests covering valid saves, invalid statuses, malformed JSON, and unsupported mailer/action combinations.

## Daily Work Update

|#|Day|Date|A short description of the work done|
|---|---|---|---|
|1|Monday|2026/05/25|Reviewed current email flow and finalized Week 1 scope.|
|2|Tuesday|2026/05/26|Created the `email_jobs` migration with status, retry, and timestamp fields.|
|3|Wednesday|2026/05/27|Added `EmailJob` entity and `EmailJobsTable` validation.|
|4|Thursday|2026/05/28|Added model tests for email jobs.|
|5|Friday|2026/05/29|Checked file structure |
|6|Saturday|2026/05/30||
|7|Sunday|2026/05/31||
