---
layout: page
title: Week 5
author: 'Ajinkya'
tags: ["week","gsoc","gsoc2022","searchEnhancements","week#5","eval#1"]
---

## Week Summary

Search was breaking for certain strings such "HS 1475(+)" and "nam-sipa-zu". It was actually ES having some reserved characters while using the query
query_string. To use these reserved characters you need to add a "\\" before every reserved character that occurs in the string that is to be searched.
Hence, I had to implement a function which would do the same for all the keywords that are being searched. This PR has led to discussion of many other issues
and how they could be solved.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	  |   2022/07/11	| check why search is breaking for certain strings |  
|2   	| Tuesday  	|   2022/07/12	| Find the a way to make the search work for such strings	|  
|3   	| Wednesday |   2022/07/13 	| Discuss the solution with mentor and begin implementation |  
|4   	| Thursday  |   2022/07/14	| Finish implementation |  
|5   	| Friday  	|   2022/07/15	| Test out if all the functions of search are working correctly with the new feature added |  
|6   	| Saturday  |   2022/07/16	| Create a PR for the feature |  
|7   	| Sunday  	|   2022/07/17	| Implement the suggestions |  
