---
layout: page
title: numerals Eval#1 Week#3 
author: "Logan"
tags: ["week","gsoc","gsoc2020","numerals","eval#1","week#3"]
---

## Week Summary

Extended commodity ID module to cover the ~400 most common terms in the Girsu corpus. Sample outputs suggest we get ~85% accuracy for the commodity labeling task, but precision is closer to 95% because of focus on rules which are not overly general. Implemented labeling of modifiers and vessels, allowing distinction between different subtypes of items (male vs female animals, for example). 

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2020/06/01	| Finish checking wordnet performance: commodity code now covers 400 common terms (26454 total tokens). Testing suggests a need to refactor to jointly classify all words in an entry, rather than iteratively classifying one at a time.   	|  
|2   	| Tuesday  	|   2020/06/02	| Restructured classification code to allow considering all words in an entry. Helps with cases where e.g. mun "salt" can be counted on its own, or can occur as a modifier describing fish. It is only the counted object in the former case.  	|  
|3   	| Wednesday  	|  2020/06/03 	| Improved ability to distinguish adjectives/modifiers from commodities. Tests show need to consider full tablet to disambiguate some implied objects (eg ration texts). Fixed handling of some vessels and metals.  	|  
|4   	| Thursday  	|   2020/06/04	| Meeting. Implement handling of vessels in commodity ID module.	|  
|5   	| Friday  	|   2020/06/05	| Clean, document, and refactor dev branch of commodity ID module. Merge with master branch.  	|  
|6   	| Saturday  	|   2020/06/06	|   	|  
|7   	| Sunday  	|   2020/06/07	|   	|  
