---
layout: page
title: search Eval#2 Week#8
author: "Vedant"
tags: ["week","gsoc","gsoc2020","search","eval#2","week#8"]
---

## Week Summary

Namaste 🙏 ,    
Welcome to the eight weekly blog of GSoC'20 for CDLI.  

### What did you do this week?

After discussion with my mentor about the Database structure and which tables to be included for other search categories, I was able to complete the queries for “Transliteration”, “Periods”, “Proveniences”. The search category “Publications” is quite a complex query one so will need more time for it and will be mostly completed during the 2nd evaluation period.

The backend functions have been optimized to send only required data for the search result view. Now the view works smoothly as expected.

### What is coming up next?

Next week will be focused on completing the “Publications” search category implementation along with pagination and setting up results per page. 

### Did you get stuck anywhere?

At the start, generating the index requires a high CPU. As indices for other search categories increase, generating all indices at some time would sometimes lead to unresponsiveness due to high CPU utilization and have to halt work until indices are completely generated. It might be an issue for developers with low system specs who are not aware of this issue, so documenting will be an important part.

### Branch (worked on): 
1. [phoenix/feature/search](https://gitlab.com/cdli/framework/-/tree/phoenix/feature/search)

### Issues : 
1. **Closed or worked related to:**
  - [#298](https://gitlab.com/cdli/framework/-/issues/298)
2. **Opened:** No new issue created during this week

### Pull Request : 
1. **Merged (or under review):**
  - [!137](https://gitlab.com/cdli/framework/-/merge_requests/137)
2. **Reviewed:**
  - [!134](https://gitlab.com/cdli/framework/-/merge_requests/134)


## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2020/07/20	|  a. WIP: Simple Search using ElasticSearch. 	|  
|2   	| Tuesday  	|   2020/07/21	|  a. WIP: Simple Search using ElasticSearch. 	|  
|3   	| Wednesday  	|  2020/07/22 	|  a. WIP: Simple Search using ElasticSearch. (Simple Search option - Collections indexed in ES) 	|  
|4   	| Thursday  	|   2020/07/23	|  a. WIP: Simple Search using ElasticSearch. (Formatting data for search result view) 	|  
|5   	| Friday  	|   2020/07/24	|  a. WIP: Simple Search using ElasticSearch. (Indexing remaining data for other Simple Search options in ES)	|  
|6   	| Saturday  	|   2020/07/25	|  a. WIP: Simple Search using ElasticSearch. (Search Query for remaining Search options) 	|  
|7   	| Sunday  	|   2020/07/26	| a. Completed Simple Search for 5 (out of 7) search options with search result display. <br> b. Created PR [!156](https://gitlab.com/cdli/framework/-/merge_requests/156) for Simple Search.	|  
