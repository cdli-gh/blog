---
layout: page
title: numerals Eval#3 Week#9
author: "Logan"
tags: ["week","gsoc","gsoc2020","numerals","eval#3","week#9"]
---

## Week Summary

Added URL parameters to allow user to specify a custom corpus, but most API endpoints do not yet support filtering by a custom corpus. Regenerating data in new formats was tedious, so some time was spent on speed improvements to make later updates easier to test and run. Additional (minor) speed improvements to the flask API: API calls are still slow, but there are no obvious places to optimize. Began tutoring Himanshu in using Docker.


## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2020/06/01	| Holiday (Alberta Heritage Day) 	|  
|2   	| Tuesday  	|   2020/06/02	| Setup elastic search PR and generate indices; profile flask code and begin optimizing load times.   	|  
|3   	| Wednesday  	|  2020/06/03 	| Make custom corpus API accessible from web interface via URL parameters; fix hang on missing vocabulary; minor formatting bugfixes. 	|  
|4   	| Thursday  	|   2020/06/04	| Meeting. Speed improvements in data generation and flask API.  	|  
|5   	| Friday  	|   2020/06/05	| Docker tutorial for Himanshu; make and share example files. More speed improvements in the data generation. Remove unused features in graph view which slowed down API calls.  	|  
|6   	| Saturday  	|   2020/06/06	|   	|  
|7   	| Sunday  	|   2020/06/07	|   	|  
