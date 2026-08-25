---
layout: page
title: "Scalable Email Infrastructure: Week 8"
author: 'Sonika Chowdary Gutha'
tags: ['week', 'gsoc', 'gsoc2026', 'ScalableEmailInfrastructure', 'week#8']
---

## Summary

Week 8 added rate limiting to the forgot-password flow, on the `gsoc/feature/email-rate-limiting` branch, tracked in [MR !1257](https://gitlab.com/cdli/framework/-/merge_requests/1257). The existing protection was a single 5-minute per-user cooldown — it only kicked in after a user was already found in the database, so it did nothing against probing unknown email addresses or one IP cycling through many accounts.

### What was built

`RateLimiterService` checks the request *before* any database lookup, closing that gap. It's built on the Redis instance the project already runs (DB 9, same as `TaskComponent`), using fixed window counters, and enforces two independent limits as the first thing `ForgotController` does:

- **Per-email** : default 5 attempts/hour, keyed on the submitted address.
- **Per-IP** : default 20 attempts/hour, keyed on the requester's IP.

The old 5 minute per user cooldown is untouched. Both it and the new limiter now return the same message "Too many requests. Please try again later." so an attacker can't tell which one they tripped. Unknown-email, banned, and suspended messages stay exactly as they were.

If Redis is down, the limiter fails **open** by default: password resets stay available rather than everyone being blocked during a Redis outage. Both limits (max attempts, window, fail-open behavior) are configurable via `config/app.php` and `config/.env.example`.

I closed the week with unit tests for `RateLimiterService` and `ForgotController` against Redis fakes, and manual verification of every case: over the limit, within cooldown, unknown email, banned/suspended, and the normal success path.

|#|Day|Date| A short description of the work done                                                                                                      |
|---|---|---|-------------------------------------------------------------------------------------------------------------------------------------------|
|1|Monday|2026/07/13| Reviewed the existing per-user cooldown in `ForgotController` and scoped `RateLimiterService` around Redis DB 9 fixed-window counters.    |
|2|Tuesday|2026/07/14| Implemented `RateLimiterService` with independent per-email and per-IP fixed window limits.                                               |
|3|Wednesday|2026/07/15| Wired the rate limiter into `ForgotController` ahead of user lookup and added the uniform "Too many requests" denial message.             |
|4|Thursday|2026/07/16| Added configurable limit/window/fail-open defaults to `config/app.php` and `config/.env.example`.                                         |
|5|Friday|2026/07/17| Wrote `RateLimiterServiceTest` and `ForgotControllerTest` and verified the rate-limiting behaviour with Redis fakes.                      |
|6|Saturday|2026/07/18| Ran manual verification across rate-limit, cooldown, fail-open, and fail-closed scenarios and reviewed the implementation for edge cases. |
|7|Sunday|2026/07/19|                                                                                                                                           |