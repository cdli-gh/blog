---
layout: page
title: Week 1
author: 'Circle Chen'
tags: ["week","gsoc","gsoc2022","towardsAGeneralPurposeEntityBibliographyLinkingSystem","week#1","eval#1"]
---

## Week Summary

The focus of this week will be to adapt the old referencing system to the new one. Currently, we have the ``artifacts`` table in the database and the ``publications`` table, as well as an ``artifacts_publications`` join table that describes associations between the artifacts and publications.

However, a publication may refer to more entities than just ``artifacts``. Therefore, it is necessary to replace ``artifacts_publications`` with a new join table called ``generic_entities_publications``, which represents the relationship between ``publications`` and all other types of entities.

The first step is to populate ``generic_entities_publications`` with the entries of ``artifacts_publications``, and then ensure nothing is wrong here.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2022/06/13	|  |  
|2   	| Tuesday  	|   2022/06/14	| 	|  
|3   	| Wednesday |  2022/06/15 	|  |  
|4   	| Thursday  |   2022/06/16	|  |  
|5   	| Friday  	|   2022/06/17	|  |  
|6   	| Saturday  |  2022/06/18	|  |  
|7   	| Sunday  	|   2022/06/19	|  |  
