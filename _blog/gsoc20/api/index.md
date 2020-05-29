---
layout: page
title: api
author: "Lars Willighagen"
tags: ["project","gsoc","gsoc2020","api"]
---

## Metadata and data API
In this project, data is made usable outside of the visual interface. This process
is guided by FAIR principles:

  1. Data is findable:
    - As linked data is used, unique IDs are necessary (A4)
    - Metadata is complete and well-described (A3, B3)
    - The API takes search queries just as the regular interface (A5)
  2. Data is accessible:
    - An API is setup for individual records, both metadata (A1, A2, B4) and when available data (A1)
  3. Data is interoperable:
    - Various formats will be supported (A1, A2, A6, B2), including forms of linked data
  4. Data is reusable:
    - License and data usage information is clearly documented (B3)

### Objectives and Deliverables
Objectives are separated in two categories: essential and additional, listed in order of priority.

#### Essential Objectives

| \# | Objectives | Associated Deliverables | Issue(s) |
|----|------------|-------------------------|----------|
| A1 | Make CDLI framework API | An API for artifact data and inscriptions | #126 |
| A2 | Make publication metadata API | An API for bibliographical data |  |
| A3 | Convert database to new schema | Richer data to be used for the APIs | #202 |
| A4 | Define and document URIs for linked data | i. URI schema for database fields ii. Documentation at those URIs |  |
| A5 | Make CDLI framework search API | An API for search results |  |
| A6 | Use publication metadata API in journal system | Journal system were references can be linked to the general database for display | #229 |

#### Additional Objectives

| \# | Objectives | Associated Deliverables | Issue(s) |
|----|------------|-------------------------|----------|
| B1 | Make API for conversion services | An API for conversion services related to inscription and/or metadata formats |  |
| B2 | Add (linked) data to (artifact) pages | Pages with Schema.org/Dublin Core annotations |  |
| B3 | Document progress | Technical documentation for API use, use of data, etc. |  |
| B4 | Extend publication metadata API to journal system | Journal system where citations of articles can be exported |  |
| B5 | Make a SDK for the API | An SDK to consume the new API (in R?) |  |

### Tentative timeline

| Week | Objectives | Deliverables |  
|-----:|------------|--------------|  
|  1\* | Prepare non-PHP scripts | Documentation on how to call external scripts from CakePHP |  
|  2\* | Setup Bibliography API | Functional internal Bibliography API |  
|  3\* | Finish Bibliography API | Functional Component and REST API |  
|  4\* | Prepare data for catalogue API | Prepared ATF and CONLL files |  
|  5   | Finish CDLI inscription API | Functional API for inscriptions and annotations |  
|  6   | Document LD schema | Documentation and URIs for the schema of RDF, XML and JSON-LD files |  
|  7   | Finish CDLI LD API | Functional API for linked data (RDF and JSON-LD) |  
|  8   | Finish links to journal system | Two-way link between Bibliography API and journal system |  
|  9   | Setup search API | Functional search API for the catalogue |  
| 10   | Annotate HTML pages | HTML pages with microdata and metadata |  
| 11   | Document APIs | API documentation |  
| 12   | Quality assurance and/or SDK | Integration tests, simple SDK |  
> \* Mostly on weekends
