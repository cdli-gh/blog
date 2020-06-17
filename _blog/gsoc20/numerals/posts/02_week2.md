---
layout: page
title: numerals Eval#1 Week#2
author: "Logan"
tags: ["week","gsoc","gsoc2020","numerals","eval#1","week#2"]
---

## Week Summary

**Numerals**
- Hosted API at https://cdli-numerals.herokuapp.com/{convert,canparse}
- API documentation
- Add new test cases based on parallel data 
- Handle subtraction notation
- Discovered issues in Dry Capacity conversion [#11](https://github.com/MrLogarithm/cdli-accounting-viz/issues/11)

**Commodity ID**
- hosted API at https://cdli-numerals.herokuapp.com/commodify
- API documentation
- Wordnet rules for commodity ID: 
  - alongside determinative rules, we cover about 95% of the words that can follow a numeral

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2020/06/01	| Setup APIs online for access by other groups. Endpoint at `https://cdli-numerals.herokuapp.com/`. Added API documentation.   	|  
|2   	| Tuesday  	|   2020/06/02	| Wordnet: better filtering of word senses; start to filter by broad hypernym categories.  	|  
|3   	| Wednesday  	|  2020/06/03 	| Restructured API responses. Ported API documentation to swagger. Evaluated wordnet performance on the most frequent words in the corpus.  	|  
|4   	| Thursday  	|   2020/06/04	| Check coverage of wordnet rules. Meeting. Share API instructions and questions with Jacob. Add negative rules to exclude persons from commodity counts.  	|  
|5   	| Friday  	|   2020/06/05	| Extract test cases from parallel data (for both numerals and commodities). Fix segmentation of area measures around the token GAN2. Fix segmentation of all values around la2. Implement and test conversion for subtraction written using la2. Extra tests revealed issues in Dry Capacity conversion, on schedule to be fixed next week. 	|  
|6   	| Saturday  	|   2020/06/06	|   	|  
|7   	| Sunday  	|   2020/06/07	|   	|  
