---
layout: page
title: Week 6
author: "Vedant"
tags: ["week","gsoc","gsoc2020","search","eval#2","week#6"]
---

## Week Summary

Namaste 🙏 , 
Welcome to the sixth weekly blog of GSoC'20 for CDLI.  

### What did you do this week?

This week was lighter on the coding part but mostly setting up ElasticSearch. The Access Setup for the framework for Admin, Editor and Public roles is set up as per requirement, still granular roles access is yet to be set up as functionality for such roles are not fully developed. The granular roles will be handled in the final phase.

Now, it was time to work on the Simple Search. For optimizing search, we are going to integrate ElasticSearch.

**What is ElasticSearch?**
Elasticsearch is a search engine based on the Lucene library. It provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents.

ElasticSearch was successfully set up and then we need to insert data into ElasticSearch Server. Since we are using MySQL DB and ElasticSearch supports the NoSQL format, we have to fetch data from DB and insert it into ElasticSearch. So there are many ways to do it but most commonly used was the Logstash.

**What is Logstash?**
Logstash is a light-weight, open-source, server-side data processing pipeline that allows you to collect data from a variety of sources, transform it on the fly, and send it to your desired destination.

At the end of the week, I was able to set up ElasticSearch along with Logstash and set up an initial configuration to see if indexing of required data was working as expected.


### What is coming up next?

Next week will be more focused on writing optimised SQL queries to fetch data in ElasticSearch using Logstash.

### Did you get stuck anywhere?

On initial setup of ElasticSearch using docker, it requires a lot of memory (of course the volatile one!!) and additionally I have 4 docker containers (necessary one) running for the project. So let’s see if my system can handle the required processing in the upcoming week.

### Branch (worked on): 
1. [phoenix/feature/authorization](https://gitlab.com/cdli/framework/-/tree/phoenix/feature/authorization)
2. [phoenix/feature/optimize-setup](https://gitlab.com/cdli/framework/-/tree/phoenix/feature/optimize-setup)
3. [phoenix/feature/search](https://gitlab.com/cdli/framework/-/tree/phoenix/feature/search)

### Issues : 
1. **Closed or worked related to:**
  - [#84](https://gitlab.com/cdli/framework/-/issues/84)
  - [#285](https://gitlab.com/cdli/framework/-/issues/285)
2. **Opened:** No new issue created during this week

### Pull Request : 
1. **Merged (or under review):**
  - [!137](https://gitlab.com/cdli/framework/-/merge_requests/137)
2. **Reviewed:** No PR reviewed during this week.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2020/07/06	| a. WIP : Access setup for Public, Editor and Admin access. 	|  
|2   	| Tuesday  	|   2020/07/07	|  a. Done with access setup for Public, Editor and Admin. [PR !137](https://gitlab.com/cdli/framework/-/merge_requests/137) <br> b. Access Setup for Granular Roles will be addressed in buffer week. 	|  
|3   	| Wednesday  	|  2020/07/08 	|  a. Exploring Elastic Search for Cakephp. <br> b. Setting up Elastic Search. |  
|4   	| Thursday  	|   2020/07/09	|  a. Done with setup of Elastic Search. <br> b. Exploring search query using Elastic Search.	|  
|5   	| Friday  	|   2020/07/10	|   a. Created GeneralFunctionsComponent for commonly used functions. <br> b. WIP : Simple Search. 	|  
|6   	| Saturday  	|   2020/07/11	|  a. Exploring ways to migrate MySQL Data to Elastic Search.  	|  
|7   	| Sunday  	|   2020/07/12	|  a. ElasicSearch + Logstash docker setup completed. <br> b. Testing indexing from MariaDB to ElasticSearch using Logstash.	|  
