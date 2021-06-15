---
layout: page
title: Week 1
author: "Yashraj Desai"
tags: ["week","gsoc","gsoc2021","discoverySearchAndAdvancedSearchFeatures","week#1","eval#1"]
---

## Week Summary

Namaste 🙏 ,    
Welcome to my first weekly blog of GSoC'21 ! 

### What did you do this week?

After a great community bonding period, I officially started working on my project. This week, I addded the Id's and keywords search fields in simple search and implemented fuzzy queries for both simple and advanced search. I thoroughly tested both these fields with various fuzzy queries configurations and updated the regex according to the requirements.

In this week, I completed 1st and 2nd objectives of my project. 

I also completed my earlier PR [!307](https://gitlab.com/cdli/framework/-/merge_requests/307).

### What is coming up next?

Next week, I will be working on "Enabling search inscription with sign value permutation" objective and also update and improve PR [!317](https://gitlab.com/cdli/framework/-/merge_requests/317) according to feedback from mentors.

### Did you get stuck anywhere?

Yes, I had doubts regarding generating indices using logstash and the current logstash queries in framework. But a short meeting with my amazing mentor cleared all my doubts and got me working again! ✌

### Issues : 
1. **Closed or worked related to:**
    - [#314](https://gitlab.com/cdli/framework/-/issues/314)
    - [#593](https://gitlab.com/cdli/framework/-/issues/593)     
2. **Opened:** No new issue opened during this week.

### Pull Request : 
1. **Merged/Under review:**
    - [!307 (Merged)](https://gitlab.com/cdli/framework/-/merge_requests/307)
    - [!317 (Under review)](https://gitlab.com/cdli/framework/-/merge_requests/317)
2. **Reviewed:** No PR reviewed during this week.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2021/06/07	| Added ES queries for ID's and keywords fields. |  
|2   	| Tuesday  	|   2021/06/08	| Added front-end for ID's and keywords fields and tested simple queries.	|  
|3   	| Wednesday  	|  2021/06/09 	| Prepared and tested Regex on input query. |  
|4   	| Thursday  	|   2021/06/10	| Researched about logstatsh jdbc queries in current framework. |  
|5   	| Friday  	|   2021/06/11	| Implemented processing of input using regex for simple search.  |  
|6   	| Saturday  	|   2021/06/12	| Implemented and tested processing of input using regex for advanced search.	|  
|7   	| Sunday  	|   2021/06/13	| Generated indices for seals and inscriptions table and tested fuzzy queries. |  
