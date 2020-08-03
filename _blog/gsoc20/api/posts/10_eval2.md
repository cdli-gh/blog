---
layout: page
title: "API: Second Evaluation"
author: "Lars Willighagen"
tags: ["eval","gsoc","gsoc2020","api","eval#2"]
---

## Summary
Mainly, a number of API routes were added:

  - `/artifacts/:id` with an inscription `Accept` redirects to the latest
    inscription
  - `/inscriptions/:id` with an inscription `Accept` (`text/x-c-atf`, `text/x-cdli-conll`)
     returns the inscription in that format, or HTTP 406 if none of the requested
     formats are available.
  - `/:controller/:id` (basically any URL) with an RDF or JSON `Accept` returns
     metadata in that format.
  - `/docs/schema/1.0` houses schema information

## Objectives and Deliverables
| Week | Objectives | Deliverables | Status |
|-----:|------------|--------------|--------|
|  5   | Finish CDLI inscription API | Functional API for inscriptions and annotations | started |
|  6   | Document LD schema | Documentation and URIs for the schema of RDF, XML and JSON-LD files | started |
|  7   | Finish CDLI LD API | Functional API for linked data (RDF and JSON-LD) | started |
|  8   | Finish links to journal system | Two-way link between Bibliography API and journal system | started |

## Learning and Success
The Inscription API is mostly a success, but needs some additional features. This
involves linking the CDLI-CoNNL-to-CoNNL-U to the framework, as well as using
updated authorization code to bar access to non-public inscriptions. A simple
Linked Data was made to export all required formats, but additional mappings
need to be made for the actual data to be meaningful.

## Difficulties
A lot of phase 2 was finishing phase 1, as well as waiting for phase-less merge
requests to be merged. On top of that, some of my merge requests require
external scripts, and the process to run those is not perfected yet.

## Plan update
I will likely have to drop at least some of the additional objectives, mainly
the API SDK. Furthermore, some objectives depend on the development of other
projects, and I have limited influence on their progress.
