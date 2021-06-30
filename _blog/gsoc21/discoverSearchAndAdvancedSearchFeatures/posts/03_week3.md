---
layout: page
title: Week 3
author: "Yashraj Desai"
tags: ["week","gsoc","gsoc2020","discoverySearchAndAdvancedSearchFeatures","week#3","eval#1"]
---

## Week Summary

Namaste 🙏 ,    
Welcome to my third week blog of GSoC'21 !

### What did you do this week?

This week was mostly researching and testing approaches. At the start of the week, we came up with a new approach for "Search Inscriptions with sign value permutation", which included direct indexing of jtf files. I tried and tested this approach but it turned out that the jtf files were not in 'nd-json' format which is accepted by elasticsearch for indexing and, converting it required special processing which was way to complex process of indexing than we had planned. So, finally we decided to go ahead with the original plan of extracting sign-values from jtf and storing it along with sign-names in our database.

I also researched and tested CakePHP HTTP client replacing the current curl based implementation in framework.

### What is coming up next?

Next week I will work on integrating the search-settings page and implementing the CakePHP HTTP client. There's a change in the tentative timeline as Ilya will be working on implementing the abstractization function in jtf-lib, after it's completion, I will use it to implement "Search Inscriptions with sign value permutation" objective. 

### Did you get stuck anywhere?

Yes, while implementing HTTP client I got erorrs which I will fix with the help of mentor in upcoming week.

### Issues : 
1. **Closed or worked related to:**
    - [#350](https://gitlab.com/cdli/framework/-/issues/350)
    - [#596](https://gitlab.com/cdli/framework/-/issues/596)
2. **Opened:** No new issue opened during this week.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2021/06/21	| Meeting with mentors to discuss implentation of "Search Inscriptions with sign value permutation". |  
|2   	| Tuesday  	|   2021/06/22	| Researched about indexing local jtf files using logstash. |  
|3   	| Wednesday  	|  2021/06/23 	| Researched about indexing local jtf files using curl. |  
|4   	| Thursday  	|   2021/06/24	| Tested indexing jtf files using logstash and curl.  |  
|5   	| Friday  	|   2021/06/25	|  |  
|6   	| Saturday  	|  2021/06/26	| Researched about implementation of CakePHP HTTP client. |  
|7   	| Sunday  	|   2021/06/27	| Tested HTTP client replacing the current curl based implementation in framework. |  
