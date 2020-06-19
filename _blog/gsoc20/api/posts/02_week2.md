---
layout: page
title: "API Week 2: Setting up the Bibliography API"
author: "Lars Willighagen"
tags: ["week","gsoc","gsoc2020","api","eval#1","week#2"]
---

Deliverable: Functional internal Bibliography API

## Week Summary

This week I had more discussions on how to call external scripts. Work is being
done on a Redis system which may apply. However, for now I went with a temporary
but functional solution. Additionally, I made routes to resolve P-, Q- and
S-numbers, corresponding to CDLI artifacts, composites and seal numbers respectively.

Regarding this weeks deliverable, the internal Bibliography API is functional now,
for both artifacts and publications.

Next week, I will be working on making a public version of the API, write documentation
on how to use the `ScriptsHelper` for APIs, and update BibTeX support.

The deliverable of the week after (W4) is actually already finished in the new
database schema. This is good news because I have exams that week.

## Daily Work Update

| # | Day | Date       | A short description of the work done |
|---|-----|------------|--------------------------------------|
| 1 | Mon | 2020/06/08 |  |
| 2 | Tue | 2020/06/09 |  |
| 3 | Wed | 2020/06/10 | Mentor meeting: planning this and next week |
| 4 | Thu | 2020/06/11 | Demonstrate link between CakePHP and Citation.js |
| 5 | Fri | 2020/06/12 |  |
| 6 | Sat | 2020/06/13 | Reviewing merge requests |
| 7 | Sun | 2020/06/14 | Make routes for resolving IDs; add reference formatting for publications |
