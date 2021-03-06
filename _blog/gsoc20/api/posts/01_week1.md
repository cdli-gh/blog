---
layout: page
title: "API Week 1: Preparing non-PHP scripts"
author: "Lars Willighagen"
tags: ["week","gsoc","gsoc2020","api","eval#1","week#1"]
---

Deliverable: Documentation on how to call external scripts from CakePHP.

## Week Summary

I started out this week by figuring out how to call external scripts. To this end,
I made an issue in the repository to get some technical information, since I was
not the first person planning on using external scripts.

While I waited for an update about that I started working ahead, to next weeks
deliverable: a "Functional internal Bibliography API". This went well, and the
result already includes most of the intended features. Next week, I will continue
working on the internal server, mainly improving BibTeX support, and link it up
to the CakePHP container when possible.

## Daily Work Update

| \# | Day | Date       | A short description of the work done |
|----|-----|------------|--------------------------------------|
| 1  | Mon | 2020/06/01 | Finished PR about simple API ([!113](https://gitlab.com/cdli/framework/-/merge_requests/113)); started exploring how to call external scripts. |
| 2  | Tue | 2020/06/02 |  |
| 3  | Wed | 2020/06/03 | Some additional work on !113, opened issue for tool communication ([#242](https://gitlab.com/cdli/framework/-/issues/242)) |
| 4  | Thu | 2020/06/04 | Weekly meeting |
| 5  | Fri | 2020/06/05 | Set up a NodeJS docker container for testing |
| 6  | Sat | 2020/06/06 | Created Citation.js server with artifact support ([branch](https://gitlab.com/cdli/framework/commits/phoenix/feature/nodejs-container)) |
| 7  | Sun | 2020/06/07 | Got !113 merged |
