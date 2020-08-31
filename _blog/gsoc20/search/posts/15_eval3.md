---
layout: page
title: Eval - 3
author: "Vedant"
tags: ["draft","eval","gsoc","gsoc2020","search","eval#3"]
---

## Summary

Phase 3 started with implementation of the remaining search category for Simple Search. Before advancing to Advanced Search, Search Settings Page was a priority issue which affects the search results page. After completion of the Search Settings page, it was planned to test it along with Advanced Search results.
 
The initial implementation for Advanced Search was to refactor present code using normal SQL queries. After implementing Simple Search using ElasticSearch, I was quite confident that this implementation can be further expanded to support Advanced Search. In order to do that, Advanced Search was written from scratch by integrating form (with more than 20 fields) and identifying which fields search are requested by the user, this was the first step. The second step was to index all the data which will be queried for Advanced Search. So, after figuring out all the data fields which comprises more than 8 tables, some of them linked by one to many relations and for some the relationship as complex as grouping data for table_1 from table_3, where both tables are linked by table_2 with many to many relationships. Finally the 100 line SQL query was over and data was indexed in ElasticSearch. Next task was to convert the search query into ElasticSearch Query and fetch results. The results fetched were two large (in some of the scenarios).It was tackled by implementing caching of results so that next sets of results can be retrieved within seconds. Then it was time to populate filters according to search results and apply filters to search results. The filters part was completed and working as expected.

The remaining objective was testing RocketChat and integrating it with the framework.  

Note: The implementation for Simple Search and Advanced Search are different. Advanced Search is implemented with all required functionality while Simple Search will be upgraded in the upcoming days to accommodate functionality implemented in Advanced Search.


## Objectives and Deliverables

Objectives and deliverables were successfully accomplished.

| Sr. No. | Objectives | Deliverables  |
| --- | ---------- | ------------- |
| 1 | Extending search category for Simple search. | “Publication” search category added for Simple Search. |
| 2 | Search Settings Page. | Implemented Search Settings page and integrated with search results page. |
| 2 | Advanced Search. | - Rewriting Advanced Search from scratch. <br> - Caching results for faster access for next set of results. <br> - Regex support. |
| 4 | Filter support for Search. | Populating Filters. <br> - Applying Filters. <br> - Displaying Applied Filters. |
| 5 | Custom Pagination. | Developed pagination for results with custom data. |
| 6 | Expanded and Compact View. | Extended view support for Advanced Search results. |
| 7 | RocketChat | Tested Rocketchat to integrate with the framework. |

## Learning and Success

The major learning part of this phase was to handle a large set of results and integrate various functionality related to search like populating filters and applying them on search results.

## Difficulties

This phase went quite smooth as expected. Due to familiarity with ElasticSearch while working on Simple Search, Advanced Search was completed within a span of 2 weeks with all the required functionalities. The major difficulty was to retrieve results which were close to 0.3 millions (in some of the cases) and then how to store them was a major question. Since querying the backend comes at a cost and for large sets of results, it's computationally expensive. This problem was tackled by storing a set of results in session and fetching the results for the next page from session. In this way, rather than querying for each page it was performed after a few sets of pages.

## Plan update

Most of the deliverables are completed. In the upcoming day, upgrading Simple Search will be a priority task and fixing minor issues related to search.
