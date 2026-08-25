---
layout: page
title: "Scalable Email Infrastructure: Week 9"
author: 'Sonika Chowdary Gutha'
tags: ['week', 'gsoc', 'gsoc2026', 'ScalableEmailInfrastructure', 'week#9']
---

## Summary

Weeks 1 through 8 built five separate pieces of this system — the job model, the queue service, the background worker, the branded templates, and the admin dashboard — largely one at a time. Week 9 was the week those pieces had to hold together: going back through mentor review comments on all five open MRs (!1235, !1238, !1241, !1242, !1246) and testing the flows end-to-end rather than in isolation.

### Email Job Model (!1235)

Dropped CakePHP's migration system for `email_jobs` and replaced it with a plain SQL schema file. The `cakephp/migrations` and `robmorgan/phinx` packages came out of `composer.json`, and Migrations plugin loading was removed from `Application.php`. `status` and `attempt_count` on the `EmailJob` entity were locked down from mass assignable to fully protected. URL validation was tightened to `FILTER_VALIDATE_URL`, and `contributionDeclined` finally got the same payload validation as the other four mailer actions.

### Email Queue System (!1238)

Review flagged a duplication risk: Redis queue key logic lived separately in `TaskComponent` and `EmailQueueService`, which could drift out of sync. That got pulled into a single `QueueKeys` service both now depend on. `EmailQueueService` also picked up a `$queueRegistered` flag so the queue registers once per instance instead of on every call. Added test coverage for custom priority/retry persistence, once only registration, and a new `LpushFailingRedisClient` double for the case where Redis accepts the connection but fails partway through the push.

### Email Worker Command (!1241)

The heaviest round of changes. Dispatch logic — validating a job's payload and resolving the target user  moved out of the worker loop into its own `EmailJobDispatcher` service. A new `UndeliverableEmailException` lets the worker cancel a permanently bad job outright instead of retrying it uselessly until attempts run out.

`EmailQueueService` gained an enable/disable toggle with a synchronous fallback so mail still sends if the queue is deliberately turned off. The worker now checks the `email_jobs` schema exists before starting and retries with exponential backoff. `ForgotController` rolls back the reset token if queuing fails, so a failed enqueue doesn't leave a dangling token. `email_worker` was added to the Docker configs across every dev environment, with Redis switched to enabled by default.

### Email Template (!1242)

`UpdateEventsController`'s contribution declined notification was still calling the mailer directly instead of going through the queue switched to `EmailQueueService`, with error handling so a queuing failure doesn't block the decline action. `BrandedEmailTrait`'s logo-CID handling was cleaned into a dedicated `cdliLogoCid()` method, and both layouts now fall back to text branding cleanly instead of risking a broken image. All five templates were standardized to route user facing strings through `__()` so they're actually translatable.

### Admin Dashboard (!1246)

Added the retry routes and the display layer helpers the dashboard view needed — `getDisplayStatus()`, `getEmailTypeLabel()`, `getEmailTypeOptions()`, and recipient resolution on `EmailJobsTable`. Built out the dashboard view with stats widgets, a filterable job list, a recent errors panel, and auto submitting filters. It's now linked from the main admin dashboard as "Email Monitoring," visible to super admins only, with a first controller test confirming it's actually gated behind admin auth.

### Testing across the whole pipeline

With fixes landed on all five MRs, I spent the back half of the week running the flows together rather than per feature — a password reset moving through validation, the queue, the worker's dispatcher, the translated templates, and showing up correctly on the dashboard. That combined pass caught mismatches at the seams between components, the kind unit tests on individual pieces wouldn't.

