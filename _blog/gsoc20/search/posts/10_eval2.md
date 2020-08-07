---
layout: page
title: search Eval#2
author: "Vedant"
tags: ["eval","gsoc","gsoc2020","search","eval#2"]
---

## Summary

After a successful first phase, the second phase was quite hard as expected but manageable. So hard in sense as integrating ElasticSearch took more than allocated time which delayed Simple and Advanced Search. And manageable because at the end of the 2nd phase, I was able to achieve the Simple Search but have to push Advanced Search in the next phase.

Although it took time, after seeing search results loading within a few seconds was quite satisfactory, which was the main objective of integrating ElasticSearch.


## Objectives and Deliverables

Most of the objectives and deliverables were successfully accomplished.

| Sr. No. | Objectives | Deliverables  |
| --- | ---------- | ------------- |
| 1       | Access Setup for Public, Granular and Admin roles. | Public pages along with Admin and Editor roles in Framework are set up. As functionality for Granular roles is currently in development, it will be addressed in the last phase. | 
| 2       | Setting up ElasticSearch. | ElasticSearch is configured along with Logstash and ElasticSearch API’s queries works as expected. | 
| 3       | Creating ElasticSearch indices using Logstash. | ElasticSearch indices created from data in MySQL Database. | 
| 4       | Simple Search with ElasticSearch. | Simple search works as expected using ElasticSearch. (4 out of 6 Search Categories) | 
| 5       | Testing Simple Search. | Compared to previous simple search implementation, the results are retrieved within a span seconds. | 
| 6       | Expanded and Compact View. | Users can view the search results in expanded and compact view format. | 
| 7       | Backup indexes and Advance Search. | Shifted to the next phase. | 

## Learning and Success

It was quite a learning phase, starting with totally new ElasticSearch and writing efficient SQL queries.

One thing to note, if there are technologies available to improve the efficiency of your project then totally go for it as it will provide a great boost altogether to the project.     

This was realized when Simple Search was implemented using the ElasticSearch queries compared to normal CakePHP queries.  The query time was almost down by 90%. The results, which used to take more than a minute using CakePHP queries, now takes only 10 sec.


## Difficulties

Learning something new requires time. So setting up ElaticSearch took an extra week, which led to a change in plan as scheduled previously. But the main point is to take time to learn new things during the initial period as this basic learning will be helpful in future.

## Plan update

The overall completion rate for this phase is around 70% (excluding Advanced Search).
The Advance search is shifted to the next phase due to time constraints. The next phase will also aim at implementing filters for search and web chat server: RocketChat.
