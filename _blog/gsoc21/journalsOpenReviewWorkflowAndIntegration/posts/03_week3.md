---
layout: page
title: Week 3
author: "Apoorva Agarwal"
tags: ["week","gsoc","gsoc2021","journalsOpenReviewWorkflowAndIntegration","week#3","eval#1"]
---

## Week Summary

 
Hola, by the end of week 2 the ojs container was up and running fine, but found an error while submitting an article in ojs("driver not found"), thus worked on debugging that error by adding various php extensions. 
I created two different columns in cdli articles table for year and article number and modified journals add template accordingly.
In the last two days of the week, I worked on creating database volume in cdli framework using init, so that database can be migrated and updated in different systems automatically, ie. without importing manually.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2021/06/21 | <a href="https://gitlab.com/cdli/framework/-/issues/575">#575</a> |  
|2   	| Tuesday  	|   2021/06/22 | Worked on error about " SQL driver cannot be found" |  
|3   	| Wednesday |   2021/06/23 | error in <a href="https://gitlab.com/cdli/framework/-/issues/575">#575</a>  |  
|4   	| Thursday  |   2021/06/24 | Research about migration of database through volumes |  
|5   	| Friday  	|   2021/06/25 | Modified journal index to link to ojs |  
|6   	| Saturday  |   2021/06/26 | Added database volume to ojs container |  
|7   	| Sunday  	|   2021/06/27 | Debug the database init script  |  
