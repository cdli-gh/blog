---
layout: page
title: search
author: "Vedant"
tags: ["project","gsoc","gsoc2020","search"]
---

## CDLI Search and other improvements
CDLI Framework integrates features of the project in a logical infrastructure, prepares new data displays, including machine-readable outputs, to enhance knowledge diffusion. It includes a unified interface for the project website, more powerful search capabilities, more internal links to navigate the catalogue, and intuitive displays for calendars, glossaries, bibliographies, etc.

The Project focuses on :  
1. Building an authentication and authorization system for the framework. 
2. Integrating Elastic Search for Simple Search.
3. Optimizing queries for Advance Search.
4. Preparing search results (Expanded and Compact format) with data preprocessing.

Proposal Link : [Improving_CDLI_Framework.pdf](https://github.com/cdli-gh/Framework/blob/master/Proposal/2020/Improving_CDLI_Framework.pdf)

Community Bonding Document : [Community_Bonding.doc](https://docs.google.com/document/d/10jLp2_WdBhSancW3kfLFrthvOO7PO-UgB5nqGVjsDMk/edit?usp=sharing)

### Objectives and Deliverables
Objectives are separated in two categories: essential and additional, they are also listed in priority order. 

#### Essential Objectives

|\#|Objectives|Associated Deliverables|issue(s)|  
|---	|---	|---	|---	|  
|1   	| Authentication (2FA)|Established more secure login by enforcing 2FA. | [#4](https://gitlab.com/cdli/framework/-/issues/4) |  
|2   	| Authorization Setup (Role Based) | Successfully setup role based access. | [#84](https://gitlab.com/cdli/framework/-/issues/84) |    
|3   	| Simple Search | Integrating Elastic Search for fast and accurate search results. | [#50](https://gitlab.com/cdli/framework/-/issues/50) |  
|4   	| Advance Search Optimization | Optimized advanced search queries. | [#48](https://gitlab.com/cdli/framework/-/issues/48) |   
|5   	| Search Result display | a. Expanded & Compact result.<br>b. Highlighted search results.<br>c. Search Filters. | []() |    

##### Notes
* Data download (backend) - Lars
* Frontend - Samarth

#### Additional Objectives

|\#|Objectives|Associated Deliverables|issue(s)|  
|---	|---	|---	|---	|  
|1   	| Search Settings | A separate setting page for displaying search page and search result according to configuration. |  [#37](https://gitlab.com/cdli/framework/-/issues/37) |  
|2   	| Rocket.Chat Setup | Setting up and deploying Rocket.Chat for CDLI Developers. |[#95](https://gitlab.com/cdli/framework/-/issues/95)|  

### Tentative timeline  

| Week  |Objectives |Deliverables |  
|---|---|---|  
|1| Creating a middleware to redirect users not having 2FA enabled <br>Testing Login and Registers with 2FA middleware<br>Setup Password Strength Checker<br>Develop Password Retrieval Module<br>Documentation of Implementation|Full functionality of login with password strength checker and password retrieval developed<br>2FA middleware force enabling 2FA <br>Documentation of 2FA middleware|
|2|   |   |  
|3|   |   |  
|4|   |   |  
|5|   |   |  
|6|   |   |  
|7|   |   |  
|8|   |   |  
|9|   |   |  
|10|   |   |  
|11|   |   |  
|12|   |   |  




