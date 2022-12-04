---
layout: page
title: Week 1
author: 'Circle Chen'
tags: ["week","gsoc","gsoc2022","towardsAGeneralPurposeEntityBibliographyLinkingSystem","week#1","eval#1"]
---

## Week Summary

The focus of this week will be to adapt the old referencing system to the new one. Currently, we have the ``artifacts`` table in the database and the ``publications`` table, as well as an ``artifacts_publications`` join table that describes associations between the artifacts and publications.

However, a publication may refer to more entities than just ``artifacts``. Therefore, it is necessary to replace ``artifacts_publications`` with a new join table called ``entities_publications``, which represents the relationship between ``publications`` and all other types of entities.

The first step is to populate ``entities_publications`` with the entries of ``artifacts_publications``, and then modify the cakePHP application to ensure everything is holding up alright.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2022/06/13	| - Contacted Rune about getting provenience-publication data <br/> - Inclusion of ``exact_referece``,``publication_type``, as well as ``publication_comments`` in ``entities_publications`` |  
|2   	| Tuesday  	|   2022/06/14	| - Exploratory data analysis on ``publications`` table to see most effective ways to merge the publication entries together	|  
|3   	| Wednesday |  2022/06/15 	| - Discussion of recent work and project. <br/> - Attempt to setup ElasticSearch but found that database was quite old |  
|4   	| Thursday  |   2022/06/16	| - Refinement of the code that merges different publication entries. <br/> - Continue to setup the elastic search indexing |  
|5   	| Friday  	|   2022/06/17	| - Fixed Elastic Search JDBC queries error <br/> |  
|6   	| Saturday  |  2022/06/18	| - Fixed Heatmap Code <br/> |  
|7   	| Sunday  	|   2022/06/19	| - Documentation writing <br/> |  
