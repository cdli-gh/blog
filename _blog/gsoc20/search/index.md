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

### Objectives and Deliverables
Objectives are separated in two categories: essential and additional, they are also listed in priority order. 

#### Essential Objectives

|\#|Objectives|Associated Deliverables|issue(s)|  
|---	|---	|---	|---	|  
|1   	|Prepare the main search|A fast and accessible main search function|   	|  
|2   	|Prepare the advanced search|A fast and accurate advanced search function|[#48](https://gitlab.com/cdli/framework/-/issues/48)|    
|3   	|Prepare the expanded search result display|   	|   	|  
|4   	|Prepare the compact search result display|Highlighted search in ATF<br>Sort columns asc/desc according to 3 columns|   
|5   	|Set up the search filters|   	|   	|  
|6   	|Extend the Role based access system|   	|[#84](https://gitlab.com/cdli/framework/-/issues/84)|  

##### Notes
* Data download backend will be handled by Lars and frontend by Samarth


#### Additional Objectives

|\#|Objectives|Associated Deliverables|issue(s)|  
|---	|---	|---	|---	|  
|1   	|Implement the search options|   	|   	|  
|2   	|Implement Rocket Chat|A rocket chat docker container which can be deployed without fuss|[#95](https://gitlab.com/cdli/framework/-/issues/95)|  

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




