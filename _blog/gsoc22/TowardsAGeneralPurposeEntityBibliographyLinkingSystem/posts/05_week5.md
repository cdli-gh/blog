---
layout: page
title: Week 5
author: 'Circle Chen'
tags: ["week","gsoc","gsoc2022","towardsAGeneralPurposeEntityBibliographyLinkingSystem","week#5","eval#1"]
---

## Week Summary

## Part 1: Still working on the data cleaning part

This week I decided to ditch the ``sciwing`` method because it is not 100% accurate at this point, and it is very slow to parse the different entries.

I feel like ``regex`` might be more useful here. So I used different regex to match the authors and filter out irrelevant data to ``exact_reference`` like year, etc.

Regex turns out to be good at this job, however Emilie pointed out that Bibtex keys may also be updated this way.

## Part 2: About managing the cakePHP code before (generic_entities branch)

Lars pointed out some issues which may lead to merge conflicts in the future, so I just decided to revert these changes here.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2022/07/11	| Created scripts that uses regex to match the contents |  
|2   	| Tuesday  	|   2022/07/12	| Fixed bugs regards to the problem of misidentifying parts of the "pl." and "p." as author name	|  
|3   	| Wednesday |  2022/07/13 	| CDLI meeting  |  
|4   	| Thursday  |   2022/07/14	| Fixed the issue of extraneous fields by only picking publications with an author attached.  |  
|5   	| Friday  	|   2022/07/15	| Sent Emilie the data about the fully processed data for checking  |  
|6   	| Saturday  |  2022/07/16	| Started working on fixing the bibtex keys.  |  
|7   	| Sunday  	|   2022/07/17	|   |  
