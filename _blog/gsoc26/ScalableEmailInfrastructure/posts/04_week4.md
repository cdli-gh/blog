---
layout: page
title: "Scalable Email Infrastructure Week: 4"
author: 'Sonika Chowdary Gutha'
tags: ['week', 'gsoc', 'gsoc2026', 'ScalableEmailInfrastructure', 'week#4']
---

## Summary

Week 4 is where queued jobs stopped being a dead end. This is the same branch and MR as last week — `email-background-worker`, [MR !1241](https://gitlab.com/cdli/framework/-/merge_requests/1241) — continuing from Week 3's refactor.

Everything up to this point wrote `pending` rows to `email_jobs` and signaled Redis. Nothing was reading them back out. `EmailWorkerCommand` (`bin/cake email_worker`) is the piece that closes that loop.

## The main loop

The worker is a long-running CakePHP console command built around one core idea: prefer Redis for speed, fall back to the database for correctness.

### Claiming via Redis

Its primary path is a `BRPOP` on `cdli:queue:email` — a blocking pop that waits up to 5 seconds for a job ID rather than busy-looping.

When it gets one, it claims that row with `SELECT ... FOR UPDATE`, checking the row is still actually `pending` (and, if it's a scheduled retry, that it's actually due) before flipping it to `processing` and incrementing the attempt count.

### Falling back to the database

If Redis has nothing to offer for 5 seconds, the worker doesn't just idle. It runs a database scan (`findAndClaimDueJob()`) that looks for any pending, due job directly — ordered by priority first, then by how long it's been waiting.

This uses `FOR UPDATE SKIP LOCKED`, so multiple potential workers would never fight over the same row.

That fallback matters for a very specific failure mode: if the `LPUSH` to Redis ever fails at enqueue time (which Week 2's `EmailQueueService` deliberately doesn't treat as fatal), the job would otherwise sit in the database forever with nothing to wake a worker up to claim it.

## Sending, and not silently losing track of failure

Once a job is claimed, `processJob()` hands it to `sendViaMailer()`, which resolves the job's `mailer` and `action` fields and calls the matching `UserMailer` method for whichever of the four flows it is:

- `welcome`
- `adminNewUser`
- `adminCrowdsourcingPrivilege`
- `resetPassword`, with its URL payload reconstructed from what `ForgotController` enqueued back in Week 3

Success marks the row `sent`. Anything the mailer throws marks it `failed`, and the loop keeps going regardless.

One bad job was never allowed to take the whole worker down — that's the entire point of having a background worker instead of hoping every send succeeds inline.

## Recovering from a worker that dies mid-job

Claiming a job means locking it. But a worker can crash between claiming a row and finishing it, and that row would otherwise sit `processing` forever, invisible to any of the normal claim paths.

`releaseStuckJobs()` runs about once a minute and resets any job that's been `processing` for more than 10 minutes back to `pending`, so another pass of the worker can pick it up — without needing anyone to notice and intervene manually.

## Testing it properly

I added a `--once` flag so the worker can process a single job (or one idle cycle) and exit, instead of running forever. That made it actually testable and debuggable, rather than something you have to `docker attach` to and watch.

`TestableEmailWorkerCommand` and the accompanying PHPUnit suite cover claiming, sending, failure, the watchdog, priority ordering, and — importantly — that a job never gets sent twice even under contention.

## Wiring it into the stack

On the infrastructure side, `app_email_worker` was registered in `docker-compose.dev.yml` and `config.dev.json`. The worker now runs as its own container alongside Cake, Redis, MariaDB, and Postfix, rather than needing to be started by hand.

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
