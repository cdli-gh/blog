---
layout: page
title: Week 7
author: "Apoorva Agarwal"
tags: ["week","gsoc","gsoc2021","journalsOpenReviewWorkflowAndIntegration","week#7","eval#2"]
---

## Week Summary

Hola, in the first half of the week I completed implementing single article web view and created a view template to display it with default cdli header and footer. I removed the heder from ckeditor and corrected it to store only main content of an article. In the second half of this week, I created connection for ojs database in cdli framework and went through the complete ojs database to collect the tables required to display submission and reviewers endorsement. Once I collected all the tables, I created their models inside cdli framework and tested if its linked propoerly by creating a controller and template for submissions table.  

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2021/07/26	| Designed the single article view template in ckeditor | 
|2   	| Tuesday  	|   2021/07/27	| Added the single article web view in our default layout |  
|3   	| Wednesday |   2021/07/28	| Designed and seperated header part from main content in web view | 
|4   	| Thursday  |   2021/07/29	| Configured ojs_db in framewok and setup the connection |  
|5   	| Friday  	|   2021/07/30	| Created models for the required table from ojs_db |  
|6   	| Saturday  |   2021/07/31	| debug error while creating models and collected the database information for all the tables needed |  
|7   	| Sunday  	|   2021/08/01	| created and tested model, controller and template for a ojs table |  
