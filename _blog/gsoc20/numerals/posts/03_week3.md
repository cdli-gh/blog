---
layout: page
title: numerals Eval#1 Week#3 
author: "Logan"
tags: ["week","gsoc","gsoc2020","numerals","eval#1","week#3"]
---

## Week Summary


## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2020/06/01	| Finish checking wordnet performance: commodity code now covers 400 common terms (26454 total tokens). Testing suggests a need to refactor to jointly classify all words in an entry, rather than iteratively classifying one at a time.   	|  
|2   	| Tuesday  	|   2020/06/02	| Restructured classification code to allow considering all words in an entry. Helps with cases where e.g. mun "salt" can be counted on its own, or can occur as a modifier describing fish. It is only the counted object in the former case.  	|  
|3   	| Wednesday  	|  2020/06/03 	| Improved ability to distinguish adjectives/modifiers from commodities. Tests show need to consider full tablet to disambiguate some implied objects (eg ration texts). Fixed handling of some vessels and metals.  	|  
|4   	| Thursday  	|   2020/06/04	|   	|  
|5   	| Friday  	|   2020/06/05	|   	|  
|6   	| Saturday  	|   2020/06/06	|   	|  
|7   	| Sunday  	|   2020/06/07	|   	|  
