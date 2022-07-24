---
layout: page
title: Week 6
author: 'Shivoham Angal'
tags: ["week","gsoc","gsoc2022","newFeaturesAndUsabilityEnhancement","week#6","eval#1"]
---

## Week Summary

I had a talk again with Lars regarding using format parameter in the export link, it works now yay! For the flat data exports I added the getTableRow() functions to entities so that works now. Linked data export also works for most entities except the ones that don't have the getCidocCrm() method. Export was working for only the first page but including the page paramter fixed that. This task is now mostly complete and hopefully I can start making the documentation soon.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2022/07/18	|  |  
|2   	| Tuesday  	|   2022/07/19	| Implemented a small extra feature for Retired Artifacts	|  
|3   	| Wednesday |  2022/07/20 	| Tested export of LinkedData for all entities |  
|4   	| Thursday  |   2022/07/21	| Added the getTableRow() function to most entities and included TableExport in controllers. The csv and tsv export should work for most entities now|  
|5   	| Friday  	|   2022/07/22	| Serialized data for some entities that didn't have it done already, changed the dropdown layout |  
|6   	| Saturday  |  2022/07/23	|  |  
|7   	| Sunday  	|   2022/07/24	| Included the page paramater when making the export url - export works for all pages now :D . Also added the developer and editor documentations for the entity export feature.|  
