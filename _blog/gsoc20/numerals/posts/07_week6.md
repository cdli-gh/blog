---
layout: page
title: numerals Eval#2 Week#6
author: "Logan"
tags: ["week","gsoc","gsoc2020","numerals","eval#2","week#6"]
---

## Week Summary

Finished the first demo of all visualizations, and made a first round of simple performance improvements. Began learning to use docker and gaining familiarity with the CDLI framework in order to start moving the project over.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2020/06/01	| Implement first attempt at similarity measurement and associated bar charts.   	|  
|2   	| Tuesday  	|   2020/06/02	| Complete implementation of similarity charts: add axis labels, tooltips, and fix crashes when words contain a curly-brace character. Redeploy on Heroku and merge changes from dev branch to master branch: demo is now live, but Heroku endpoint is unstable due to wordnet tmp files being deleted by the server.  	|  
|3   	| Wednesday  	|  2020/06/03 	| Debug slow responsiveness in visualizations. Limit size of force-directed graphs to increase speed. Look for ways to lazy load this content to reduce performance impact.  	|  
|4   	| Thursday  	|   2020/06/04	| Setup CDLI framework dev environment. Learn how to use docker and docker-compose; setup simple container for this project and get a simple HTML interface working on the framework.  	|  
|5   	| Friday  	|   2020/06/05	| Separate api and interface components into different services.  	|  
|6   	| Saturday  	|   2020/06/06	|   	|  
|7   	| Sunday  	|   2020/06/07	|   	|  
