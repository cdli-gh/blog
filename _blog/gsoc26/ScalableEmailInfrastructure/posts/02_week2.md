---
layout: page
title: "Scalable Email Infrastructure: Week 2"
author: 'Sonika Chowdary Gutha  '
tags: ['week', 'gsoc', 'gsoc2026', 'ScalableEmailInfrastructure', 'week#02']
---

## Summary

Week 2 built the queueing layer on top of the Week 1 `email_jobs` foundation, on the `email-queue-service` branch, tracked in [MR !1238](https://gitlab.com/cdli/framework/-/merge_requests/1238). No existing email flow was changed yet — this was still infrastructure work, one layer closer to something a controller could actually call.

The centerpiece is `EmailQueueService`, with a single entry point: `enqueueMailerAction()`. Controllers will eventually call this instead of sending mail directly. It does two things: first, it creates and persists an `email_jobs` row with the given mailer, action, and payload. Then it hands the job off to Redis through a separate `dispatchToRedis()` step, which registers the queue name and pushes the job ID onto it.

For the Redis side, I reused the queue-key formatting already established in `TaskComponent` — its constants and `queueKey()` helper — rather than inventing a new convention. That way the existing task queue and the new email queue stay consistent about how a Redis key gets built. The Redis connection itself is lazy-loaded on first use rather than opened eagerly. And if the Redis push fails, that failure is caught and logged without rolling back the database write — the job stays safely `pending` in `email_jobs` either way, since the database write is the source of truth here and Redis is just a dispatch signal on top of it. I closed the week out with tests covering the three paths that actually matter: the job getting written to the database correctly, the Redis push happening with the right queue name and job ID, and the failure path where Redis is unavailable but the database write still succeeds.

## Daily Work Update

|#|Day|Date|A short description of the work done|
|---|---|---|---|
|1|Monday|2026/06/01|Reviewed Week 2 scope and studied existing `TaskComponent` Redis queue conventions.|
|2|Tuesday|2026/06/02|Designed the `EmailQueueService` interface and `enqueueMailerAction()` method.|
|3|Wednesday|2026/06/03|Implemented `EmailQueueService` to save pending jobs in `email_jobs`.|
|4|Thursday|2026/06/04|Added Redis dispatch to `cdli:queue:email` and shared queue key constants in `TaskComponent`.|
|5|Friday|2026/06/05|Added service tests for DB write, Redis push, and Redis failure handling.|
|6|Saturday|2026/06/06|Verified queue service behavior and checked syntax/lint on Week 2 files.|
|7|Sunday|2026/06/07||
