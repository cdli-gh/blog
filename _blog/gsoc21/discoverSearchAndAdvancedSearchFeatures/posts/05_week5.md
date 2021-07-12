---
layout: page
title: Week 5
author: "Yashraj Desai"
tags: ["week","gsoc","gsoc2021","discoverySearchAndAdvancedSearchFeatures","week#5","eval#1"]
---

## Week Summary

Namaste 🙏 ,    
Welcome to my fifth week blog of GSoC'21 !

### What did you do this week?

This week I implemented inscriptions search in both simple and advanced search and highlighted matching search inscriptions in full and compact search results page. For implementing this, I had to first index data as latest version of database had new entries in inscriptions table. For processing and highlighting matching search inscriptions, I added functions in search view file to render the inscriptions data accordingly.

### Did you get stuck anywhere?

I had doubts related to rendering processed version of atf data, which I cleared with the help of mentors and taking reference from old working version of CDLI codebase.

### Issues : 
* **Closed or worked related to:**
    - [#347](https://gitlab.com/cdli/framework/-/issues/347)
    - [#635](https://gitlab.com/cdli/framework/-/issues/635)

### Pull Request : 
* **Merged/Under review:**
    - [!354](https://gitlab.com/cdli/framework/-/merge_requests/354)

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2021/07/05	| Updated local database with updated Inscriptions table. |  
|2   	| Tuesday  	|   2021/07/06	| Added logstash queries to index the updated Inscriptions table.|  
|3   	| Wednesday  	|  2021/07/07 	| Researched on how atf should be processed and displayed. |  
|4   	| Thursday  	|   2021/07/08	| Highlighted matching inscriptions in search results.|  
|5   	| Friday  	|   2021/07/09	| Displayed prettified version of inscriptions on full search results page. |  
|6   	| Saturday  	|   2021/07/10	| |  
|7   	| Sunday  	|   2021/07/11	| Displayed prettified version of inscriptions on compact search results page. |  
