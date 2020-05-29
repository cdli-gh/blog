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
|:---:|---	|---	|:---:|  
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
|---	|---	|---	| :---:	|  
|1   	| Search Settings | A separate setting page for displaying search page and search result according to configuration. |  [#37](https://gitlab.com/cdli/framework/-/issues/37) |  
|2   	| Rocket.Chat Setup | Setting up and deploying Rocket.Chat for CDLI Developers. |[#95](https://gitlab.com/cdli/framework/-/issues/95)|  

### Tentative timeline  

<!---
| Week  |Objectives |Deliverables |  
|:---:|---|---|  
|1| a. Authentication (2FA) <br><br> b. Password Strength Checker <br><br> c. Implement Password Retrieval | a. Successful implementation of 2FA middleware. <br> b. Testing 2FA Middleware. <br> a. Implemented Password Checker. <br> b. Testing on the Register Page. <br> a. Implemented Password Retrieval Module. <br> b. Testing on the Login Page. |
|2|  |   |
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
-->
<!---
<table>
  <tr>
    <td rowspan=2> Status </td> 
    <td align="center"> Working </td>
    <td align="center"> :technologist: </td>
  </tr>
  <tr>
    <td align="center"> Completed </td>
    <td align="center"> :heavy_check_mark: </td>
  </tr>
</table>
-->

<table>
  <tr>
    <td> <strong>Status</strong> </td> 
    <td></td>
    <td align="center"> Working </td>
    <td align="center"> :technologist: </td>
    <td></td>
    <td align="center"> Completed </td>
    <td align="center"> :heavy_check_mark: </td>
  </tr>
</table>

<table>
    <thead>
        <tr>
            <th>Week</th>
            <th>Objectives</th>
            <th>Status</th>
            <th>Deliverables</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=6 align="center">1</td>
            <td rowspan=2>a. Authentication (2FA) </td>
            <td rowspan=2 align="center"></td>
            <td>a. Successful implementation of 2FA middleware. </td>
        </tr>
        <tr>
            <td>b. Testing 2FA Middleware. </td>
        </tr>
        <tr>
            <td rowspan=2> b. Password Strength Checker </td>
            <td rowspan=2 align="center"></td>
            <td>a. Implemented Password Checker.</td>
        </tr>
        <tr>
            <td>b. Testing on the Register Page. </td>
        </tr>
        <tr>
            <td rowspan=2>c. Implement Password Retrieval</td>
            <td rowspan=2 align="center"></td>
            <td> a. Implemented Password Retrieval Module. </td>
        </tr>
        <tr>
            <td> b. Testing on the Login Page.</td>
        </tr>
        <tr>
            <td rowspan=1 align="center">2</td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=1 align="center">3</td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=1 align="center">4</td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=1 align="center">5</td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=1 align="center">6</td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=1 align="center">7</td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=1 align="center">8</td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=1 align="center">9</td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=1 align="center">10</td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=1 align="center">11</td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
        <tr>
            <td rowspan=1 align="center">12</td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
<!--         <tr>
            <td rowspan=4>L1 Name</td>
            <td rowspan=2>L2 Name A</td>
            <td>L3 Name A</td>
        </tr>
        <tr>
            <td>L3 Name B</td>
        </tr>
        <tr>
            <td rowspan=2>L2 Name B</td>
            <td>L3 Name C</td>
        </tr>
        <tr>
            <td>L3 Name D</td>
        </tr> -->
    </tbody>
</table>



