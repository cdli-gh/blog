---
layout: page
title: "Scalable Email Infrastructure: Week 7"
author: 'Sonika Chowdary Gutha'
tags: ['week', 'gsoc', 'gsoc2026', 'ScalableEmailInfrastructure', 'week#7']
---

## Summary

Week 7 focused on building the admin facing side of the email pipeline: a dashboard for monitoring and managing queued and failed emails, on the `gsoc/feature/email-admin-dashboard` branch, tracked in [MR !1246](https://gitlab.com/cdli/framework/-/merge_requests/1246).

Until now, the state of the email queue could only be inspected directly through the `email_jobs` table. This week, I added an admin dashboard that makes it easier to monitor the queue, identify failures, and retry failed emails.

## The dashboard and its widgets

I added a new admin only controller, `Admin/EmailJobsController`, gated behind the existing `GranularAccess` component, with a dashboard available at `/admin/email-jobs`.

The dashboard includes queue state widgets for Pending, Sent, Failed, and Retrying jobs, along with metrics such as daily sent and failed totals and backlog size. These are backed by a new `getSummaryStats()` method on `EmailJobsTable`.

Below the summary widgets is a jobs table showing the recipient, email type, status, creation date, retry count, and last error for each job.

## Filtering the queue

The jobs table can be filtered by status, email type, date range, and recipient search. These filters are handled through a custom `findFiltered()` finder on `EmailJobsTable`.

## Making failures actionable

The dashboard also provides actions for recovering failed jobs. A per job retry action resets a failed job to `pending` and redispatches it.

A bulk "retry all failed" action performs the same operation for all matching failed jobs, with a limit of 100 jobs per request to avoid overwhelming the worker.

Both retry paths use a new `retryFailedJob()` method in `EmailQueueService`, which reuses the job's original payload so the admin does not need to re-enter any information.

## Handling Redis dispatch failures

While implementing the retry flow, I also handled a case where the database update can succeed but the Redis dispatch can fail.

To make this failure explicit, I added a dedicated `QueueDispatchException`. The job remains in the database with a `pending` status, allowing the worker's periodic scan to pick it up on its next pass even if the Redis notification was unsuccessful.

## Routes and tests

I added routes for the dashboard and retry actions alongside the existing admin routes.

The week was completed with tests covering admin only access, filtering, per job retry, bulk retry behavior, and summary statistics.

## Daily Work Update

|#|Day|Date| A short description of the work done                                                                                                            |
|---|---|---|-------------------------------------------------------------------------------------------------------------------------------------------------|
|1|Monday|2026/07/06| Scoped the admin dashboard, including the `/admin/email-jobs` route and `EmailJobsController` with `GranularAccess`-gated admin-only access.    |
|2|Tuesday|2026/07/07| Built `EmailJobsController::index()` and `EmailJobsTable::getSummaryStats()` to power the Pending, Sent, Failed, and Retrying widgets.          |
|3|Wednesday|2026/07/08| Added the `findFiltered()` finder for status, email type, date range, and recipient search, and wired it into the dashboard view.               |
|4|Thursday|2026/07/09| Implemented per job `retryFailed()` and bulk `retryAllFailed()` actions with a 100 job limit, along with `EmailQueueService::retryFailedJob()`. |
|5|Friday|2026/07/10| Added `QueueDispatchException` to handle Redis dispatch failures during retry.                                                                  |
|6|Saturday|2026/07/11| Added controller, table, and service tests.                                                                                                     |
|7|Sunday|2026/07/12|                                                                                                                                                 |