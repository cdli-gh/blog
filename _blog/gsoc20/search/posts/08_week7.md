---
layout: page
title: search Eval#2 Week#7
author: "Vedant"
tags: ["week","gsoc","gsoc2020","search","eval#2","week#7"]
---

## Week Summary

Namaste 🙏 ,    
Welcome to the seventh weekly blog of GSoC'20 for CDLI.  

### What did you do this week?

From the previous week’s ElasticSearch + Logstash setup, I tried querying data and found out a major issue of data duplication in indices generated. On further research related to this issue, I made required changes to the Logstash configuration so that there won’t be duplication of data during indexing. 

The simple search supports multiple search categories, the approach undertaken was to implement a single search category till the final output we desired and then expand it to other search categories. At the end of the week, the simple search for “Collection” category was working as expected along with displaying data on the search result page.

### What is coming up next?

Now after working with ElasticSearch for a week and more, I have a somewhat idea about how it works and how we should query data. So next week, the main aim will be to implement remaining search categories.

### Did you get stuck anywhere?

For other search categories, I have the database fields which need to be searched but do not have a clear idea about database structure, so will need a discussion with my mentor regarding it.

### Branch (worked on): 
1. [phoenix/feature/authorization](https://gitlab.com/cdli/framework/-/tree/phoenix/feature/authorization)
2. [phoenix/feature/search](https://gitlab.com/cdli/framework/-/tree/phoenix/feature/search)

### Issues : 
1. **Closed or worked related to:**
  - [#285](https://gitlab.com/cdli/framework/-/issues/285)
  - [#298](https://gitlab.com/cdli/framework/-/issues/298)
2. **Opened:** No new issue created during this week

### Pull Request : 
1. **Merged (or under review):**
  - [!137](https://gitlab.com/cdli/framework/-/merge_requests/137)
2. **Reviewed:** No PR reviewed during this week.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2020/07/13	| a. WIP : Indexing from MariaDB to ElasticSearch using Logstash. |  
|2   	| Tuesday  	|   2020/07/14	|  a. Completed setup for Logstash + ElasticSearch + Kibana. <br> b. Currently, indexing is supported for single table will be expanded to multiple table. 	|  
|3   	| Wednesday  	|  2020/07/15 	| a. WIP: Simple Search using ElasticSearch.  	|  
|4   	| Thursday  	|   2020/07/16	| a. WIP: Simple Search using ElasticSearch (Query Formation).  	|  
|5   	| Friday  	|   2020/07/17	|  a. WIP: Simple Search using ElasticSearch (Query Formation).	|  
|6   	| Saturday  	|   2020/07/18	| a. WIP: Simple Search using ElasticSearch (Sample search result display). 	|  
|7   	| Sunday  	|   2020/07/19	|  a. WIP: Simple Search using ElasticSearch (According to modified requirements). 	|  
