---
layout: page
title: Search Enhancements
author: 'Ajinkya Morankar'
tags: ['project', 'gsoc', 'gsoc2022', 'searchEnhancements']
---


## Search Enhancements

This project mainly focuses on updating and improving
the current search features. The search setup has been
completed under past programs of GSOC and hence the
documentation of it is needed which would also be
covered under the scope of this project. I would be
adding features which would help the user to get a 
understanding of filtering system and also try to change
the way we write Elasticsearch queries in dev files so that it
is easier to understand and update them.This also includes solving 
some current search related issues present in the framework. As 
everyone is aware of the indexing issues with logstash I shall also 
devote some of my research time to find a better schedule or method 
to make indexing more developer friendly.     

### Objectives and Deliverables

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks

| \# | Status  | Objectives                    | Associated Deliverables         | issue(s) |
| --- | --- | ----------------------------- | ---------------------------------------------- | -------- |
| 1 |:white_check_mark:|  Optimize search filters |  Filtering would become faster | [!1128](https://gitlab.com/cdli/framework/-/issues/1128) |
| 2 |:white_check_mark:|  Show number of hits in the parenthesis | Users will be able see number of hits in the parenthesis before applying a filter | [!526](https://gitlab.com/cdli/framework/-/issues/526) |
| 3 |:white_check_mark:|  Search Filter Problem |  The filters would now return the intersection of all the applied filters | [!531](https://gitlab.com/cdli/framework/-/issues/531) |
| 4 |:white_check_mark:|  Search breaks when searching for a certain string | Search would be fixed for the strings whichwere breaking earlier | [!1067](https://gitlab.com/cdli/framework/-/issues/1067) |
| 5 |:white_check_mark:|   search children entities |  child, grandchild would be included in thesearch result for a parent | [!1035](https://gitlab.com/cdli/framework/-/issues/1035) |
| 6 |:white_check_mark:|  Show stats for search results | Static Data visualizations to represent an overview of the corpus | [!863](https://gitlab.com/cdli/framework/-/issues/863) |
| 7 |:white_check_mark:|  Encode Elasticsearch queries using JSON |  Developers will be able to write elasticsearch queries more systematically | [!1129](https://gitlab.com/cdli/framework/-/issues/1129) |
| 8 |:white_check_mark:|   Extend free search | Free search would now include Comments field | [!996](https://gitlab.com/cdli/framework/-/issues/996) |
| 9 |:white_check_mark:|   Complete Documentation | Two types of documents: User and Developer would be created with respect to search | [!675](https://gitlab.com/cdli/framework/-/issues/675) |

### Additional Objectives

| \# | Status  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1 | :white_check_mark: | Reviewd a PR  | updating logstash schedule |    [!645](https://gitlab.com/cdli/framework/-/merge_requests/645)     |


### Tentative timeline

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks  :raised_hands: --> Work Demonstration

| Week  |Objectives | Deliverables |
|---|---|---|
|1 and 2| :white_check_mark: Optimize search filters  |  :heavy_check_mark: Filtering would become faster <br/> :heavy_check_mark: Filtering would be done before applying filters|
|3 and 4| :white_check_mark: Show number of hits in the parenthesis <br/> :white_check_mark: Search Filter Problem  |  :heavy_check_mark: Users will be able see number of hits in the parenthesis before applying a filter <br/> :heavy_check_mark: The filters would now return the intersection of all the applied filters|
|5| :white_check_mark: Search breaks when searching for a certain string <br/> :white_check_mark: search children entities |  :heavy_check_mark: Search would be fixed for the strings which were breaking earlier <br/> :heavy_check_mark: child, grandchild would be included in the search result for a parent |
|6| :white_check_mark: Buffer week  |  :heavy_check_mark: Report for phase 1 <br/> :heavy_check_mark: code submission for phase 1|
|7 and 8| :white_check_mark: Show stats for search results  |  :heavy_check_mark: Static Data visualizations to represent an overview of the corpus <br/> :heavy_check_mark: Dynamic data visualizations after filters have been applied so that the user gets a better understanding of how many different results are present inside each filter|
|9 and 10| :white_check_mark: Encode Elasticsearch queries using JSON <br/> :white_check_mark: Extend free search |  :heavy_check_mark: Developers will be able to write elasticsearch queries more systematically <br/> :heavy_check_mark: Free search would now include Comments field|
|11| :white_check_mark: Complete Documentation  |  :heavy_check_mark: Two types of documents: User and Developer would be created with respect to search|
|12| :white_check_mark: Buffer week |  :heavy_check_mark: Submit the code <br/> :heavy_check_mark: Submit the final project report|
