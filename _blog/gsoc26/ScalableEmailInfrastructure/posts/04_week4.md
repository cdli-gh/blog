---
layout: page
title: Scalable Email Infrastructure Week 4
author: 'Sonika Chowdary Gutha'
tags: ['week', 'gsoc', 'gsoc2026', 'ScalableEmailInfrastructure', 'week#4']
---

## Summary

This week implemented the email background worker that processes jobs queued. I added `EmailWorkerCommand` (`bin/cake email_worker`), a long-running CakePHP console worker that listens on Redis (`BRPOP` on `cdli:queue:email`), claims jobs transactionally in `email_jobs`, and sends them through `UserMailer` for `welcome`, `adminNewUser`, `adminCrowdsourcingPrivilege`, and `resetPassword`. The worker includes a DB fallback scan when Redis is idle or dispatch failed at enqueue time, priority-based claiming, a stuck-job watchdog that resets jobs locked for more than 10 minutes, and safe failure handling that marks jobs `sent` or `failed` without crashing the loop. I also wired the worker into dev Docker (`app_email_worker` in `docker-compose.dev.yml`) and added PHPUnit coverage for claiming, sending, watchdog behavior, duplicate prevention, and Redis-failure recovery.

## Daily Work Update

| # | Day       | Date       | A short description of the work done                                                                                                                           |
|---|-----------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | Monday    | 2026/06/15 | Designed the worker architecture: Redis-first job pickup, transactional DB claiming, and status transitions (`pending` → `processing` → `sent`/`failed`).      |
| 2 | Tuesday   | 2026/06/16 | Implemented `EmailWorkerCommand` core loop with Redis connection, `fetchNextJob()`, and `claimJob()` using `FOR UPDATE` row locking.                           |
| 3 | Wednesday | 2026/06/17 | Added `processJob()`, `sendViaMailer()`, and mailer dispatch for the four transactional flows, including `resetPassword` URL payload handling.                 |
| 4 | Thursday  | 2026/06/18 | Implemented DB fallback claiming (`findAndClaimDueJob()` with `FOR UPDATE SKIP LOCKED`), priority ordering, and the stuck-job watchdog (`releaseStuckJobs()`). |
| 5 | Friday    | 2026/06/19 | Added `--once` for test runs, mailer-action allowlist validation, and registered `app_email_worker` in `docker-compose.dev.yml` and `config.dev.json`.         |
| 6 | Saturday  | 2026/06/20 | Built `TestableEmailWorkerCommand` and PHPUnit coverage for claim, send, fail, watchdog, priority, and duplicate-send prevention paths.                        |
| 7 | Sunday    | 2026/06/21 |                                                                                                                                                                |