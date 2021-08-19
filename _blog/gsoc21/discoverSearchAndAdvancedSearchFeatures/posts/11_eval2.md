---
layout: page
title: Second Evaluation
author: "Yashraj Desai"
tags: ["eval","gsoc","gsoc2021","discoverySearchAndAdvancedSearchFeatures","eval#2"]
---

## Summary
The second phase of my GSoC journey was challenging and a great learning curve for me. \
It consisted following two major objectives : 
#### 1. Images and Transliteration Filter
  This objective was accomplished by creating a new index of images table and adding Elasticsearch queries which would filter images according to different image types. This also includes managing access according to individual images for different users and displaying the results accordingly.
#### 2. Search inscriptions with sign value permutation
  This objective was accomplished by initially populating the sign_names field of latest inscriptions in the inscriptions table of the database using jtf-lib. When user performs a search in Transliteration Permutation field of Advanced Search, the sign values are converted to sign-names using jtf-lib container and search is performed using these sign names and sign values. I also made the input flexible which enables users to search with both utf8 and ascii characters. 

## Objectives and Deliverables
| \# | Objectives                    | Associated Deliverables         |
| --- | ----------------------------- | ---------------------------------------------- |
| 1 | Images and Transliteration Filter | Users can apply filters such as RTI Image, Transliterations, 3D Data, etc. and get search results according to the access granted to them. |
| 2 | Search inscriptions with sign value permutation | When a user will search for sign values in Transliteration Permutation field of Advanced search, all possible sign values with matching sign names of the query will be returned as search result. |
| 3 | Input flexibility enhancements | Users will have the flexibility to search with both UTF-8 and ASCII characters in inscription search. |
| 4 | Enable search for list of Id's | Users can search for list of id's seperated by commas in Identification Numbers fields of both simple and advanced search.|
| 5 | Format transliteration on single artifact page | Formatted transliteration will be displayed on single artifact page under the Inscriptions tab. |


## Learning and Success
* Explored and implemented complex Elasticsearch queries for various search and filter operations.
* Learned and implemented python scripting to perform request to jtf-lib container and store the response in the database.
* Learned and practised good coding principles throughout my GSoC project. 

## Difficulties
Populating the sign_names field of entire inscriptions table containing more than 0.4 million records using the response form jtf-lib container was quite a challenging task. With the guidance of my amazing mentors and fellow mentees we were able to accomplish this objective. 

## Future Plan 
* Robust testing and documentation of all the newly added features.
* Once Lars and Vishv are done with API integration, sanitised version of sign values and sign names can be stored in the database when user adds/edits inscriptions.	
