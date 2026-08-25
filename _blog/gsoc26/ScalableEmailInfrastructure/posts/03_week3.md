---
layout: page
title: "Scalable Email Infrastructure: Week 3"
author: 'Sonika Chowdary Gutha  '
tags: ['week', 'gsoc', 'gsoc2026', 'ScalableEmailInfrastructure', 'week#03']
---

## Summary

Week 3 was about pulling the trigger — literally, the `->send()` trigger — out of the request handlers and pointing it at the queue instead. This is tracked in [MR !1241](https://gitlab.com/cdli/framework/-/merge_requests/1241). The first two weeks built a queue nobody was using yet; this week made it the only path four of the app's transactional emails actually take.

### Rewiring the four flows

`UsersTable.php`'s `afterSaveCommit` callback used to call `$this->getMailer('User')->send()` directly for two different situations: a brand-new user getting both a `welcome` email and triggering an `adminNewUser` notification, and an existing user requesting crowdsourcing privileges, triggering `adminCrowdsourcingPrivilege`. 

All three calls became `EmailQueueService::enqueueMailerAction()` calls instead, wrapped in their own try/catch so that a queuing failure gets logged rather than breaking the save that triggered it — a user's account still gets created even if, for whatever reason, the email can't be queued. `ForgotController.php` got the same treatment for `resetPassword`, with one difference: it's enqueued at `EmailQueueService::HIGH_PRIORITY` rather than the default, since a password-reset link sitting behind a pile of lower-priority welcome emails defeats the point of it being time-sensitive in the first place.

### Why the priority constant and the cleanup

Adding `HIGH_PRIORITY` as an actual named constant rather than a magic number was a small thing, but it's the kind of small thing that matters once more mailer actions get added later and someone has to guess what priority value means "this one's urgent." Once both controllers were enqueuing through the service instead of calling the mailer directly, `MailerAwareTrait` wasn't doing anything for them anymore — so it came out of both files. Leaving unused trait usage in place is exactly the kind of thing that looks harmless right up until someone reads it as a hint that direct sending is still an option somewhere.

### What this week doesn't do yet

Emails triggered by these four flows are now landing in `email_jobs` as `pending` rows and getting signaled to Redis correctly — I confirmed that much by checking the table directly after triggering each flow locally. What doesn't happen yet is anything picking those jobs up and actually sending them. That's deliberate: this week's scope was the enqueue side only, and the consumer — the background worker that claims a job, calls the mailer, and marks it `sent` or `failed` — is next week's work. Right now, a `pending` row is as far as the story goes.

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
