---
layout: page
title: First Evaluation
author: "Yashraj Desai"
tags: ["eval","gsoc","gsoc2021","discoverySearchAndAdvancedSearchFeatures","eval#1"]
---

## Summary

The first phase of my GSoC journey was overall a great learning experience for me. In the initial part of first phase, I added and enabled the Id's and Keywords search fields in both simple as well as advanced search. These fields were also made fuzzy so that users who are not familiar with the proper search query format can also yield search results! In the later phase, I implemented objectives which included implementing CakePhp HTTP client, integrating search settings page and implementing inscriptions search in both simple and advanced search along with highlighting matching search inscriptions in full and compact search results page.

## Objectives and Deliverables
| \# | Objectives                    | Associated Deliverables         |
| --- | ----------------------------- | ---------------------------------------------- |
| 1 | Ids and Keywords search fields | Users will be able to search for specific keywords,Id/Numbers artifacts both in simple and advanced search. |
| 2 | Fuzzy queries | Fuzzy queries would yield search results in all id's fields.	|
| 3 | CakePhp HTTP Client | Ported request to Elasticsearch replacing cURL to HttpClient.|
| 4 | Search settings page | Integrated search setting page functionalities with front-end. |
| 5 | Implement inscriptions search | Users can search inscriptions in both simple and advanced search and get the pretiffied and processed inscriptions in search results. |
| 6 | Highlight matching inscriptions | On searching inscriptions, users get the matching inscriptions highlighted in search results |

## Learning and Success
* Learned and implemented Elastic stack for adding new search fields and optimising search.
* Learned and implemented PHP and CakePHP for framework development.
* Implemented Regex for special processing of text. 

## Difficulties
I faced difficulty while implementing "search inscriptions with sign value permutation" objective as it can be done with several approaches all of which are a bit complex. After a lot of discussions, we have finalized the approach using jtf-lib which I will implement in the second phase.

## Plan update
As I had dependency on Ilya for implementing "search inscriptions with sign value permutation" objective I have shifted it to next phase and swapped some objectives of second phase with it.
