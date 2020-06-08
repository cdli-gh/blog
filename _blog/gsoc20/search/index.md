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
|5   	| Search Result display | a. Expanded & Compact result.<br>b. Stats for Search Result.<br>c. Search Filters.<br>d. Search Setting Page. | [#238](https://gitlab.com/cdli/framework/-/issues/238) |    

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
    <td align="center"> :man_technologist: </td>
    <td></td>
    <td align="center"> Completed </td>
    <td align="center"> :heavy_check_mark: </td>
  </tr>
</table>

<table>
    <thead>
        <tr>
            <th> Week </th>
            <th> Objectives </th>
            <th> Status </th>
            <th> Deliverables </th>
        </tr>
    </thead>
    <tbody>
        <!-- Week-1 -->
        <tr>
            <td rowspan=6 align="center"> 1 </td>
            <td rowspan=2> A. Authentication (2FA) </td>
            <td rowspan=2 align="center"> :heavy_check_mark: </td>
            <td> a. Merged and restructured, 2FA-login and 2FA-Register Controller into single 2FA Controller. </td>
        </tr>
        <tr>
            <td> b. Testing 2FA Controller. </td>
        </tr>
        <tr>
            <td rowspan=2> B. Password Strength Checker </td>
            <td rowspan=2 align="center"> :heavy_check_mark: </td>
            <td> a. Implemented Bad Password Checker. </td>
        </tr>
        <tr>
            <td> b. Testing on the Register Page. </td>
        </tr>
        <tr>
            <td rowspan=2> C. Implement Password Retrieval </td>
            <td rowspan=2 align="center"> :man_technologist: </td>
            <td> a. Implemented Password Retrieval Module. </td>
        </tr>
        <tr>
            <td> b. Testing on the Login Page.</td>
        </tr>
        <!-- Week-2 - 3 -->
        <tr>
            <td rowspan=6 align="center"> 2-3 </td>
            <td rowspan=1>A. Access control page.</td>
            <td rowspan=1 align="center"></td>
            <td>a. To view, add or remove the roles of users of the system.</td>
        </tr>
        <tr>
            <td rowspan=2>B. System setup for roles viz. Users, Editors and Granular Access.</td>
            <td rowspan=2 align="center"></td>
            <td>a. System should display contents based on roles as described in objectives.</td>
        </tr>
        <tr>
            <td>b. Testing web pages in the system.</td>
        </tr>
        <tr>
            <td rowspan=2>C. System setup for the Admin role.</td>
            <td rowspan=2 align="center"></td>
            <td>a. Admin should be able to access all pages.</td>
        </tr>
        <tr>
            <td>b. Re-testing of web pages according to admin role.</td>
        </tr>
        <tr>
            <td rowspan=1>D. Documenting Role based Access.</td>
            <td rowspan=1 align="center"></td>
            <td>a. Documentation which developers should follow to add functionality to the framework based on roles.</td>
        </tr>
        <!-- Week-4 -->
        <tr>
            <td rowspan=5 align="center"> 4 </td>
            <td rowspan=1>A. Triggers for inactive users.</td>
            <td rowspan=1 align="center"></td>
            <td>a. For login activity older than 6 months, make account status inactive. </td>
        </tr>
        <tr>
            <td rowspan=1>B. Create 2FA Google Authenticator Guide.</td>
            <td rowspan=1 align="center"></td>
            <td>a. Documented 2FA Google Authenticator. </td>
        </tr>
        <tr>
            <td rowspan=1>C. Fix ‘/logout’ functionality.</td>
            <td rowspan=1 align="center"></td>
            <td>a. Restricting logout using GET request and accepting only POST request. </td>
        </tr>
        <tr>
            <td rowspan=2>D. Documentation & Report for Phase-1.</td>
            <td rowspan=2 align="center"></td>
            <td>a. Phase-1: all implementation should be documented. </td>
        </tr>
        <tr>
            <td>b. Report For Phase-1 evaluation.</td>
        </tr>
        <!-- Week-5 -->
        <tr>
            <td rowspan=1 align="center"> 5 </td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
        <!-- Week-6 -->
        <tr>
            <td rowspan=1 align="center"> 6 </td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
        <!-- Week-7 -->
        <tr>
            <td rowspan=1 align="center"> 7 </td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
        <!-- Week-8 -->
        <tr>
            <td rowspan=1 align="center"> 8 </td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
        <!-- Week-9 -->
        <tr>
            <td rowspan=1 align="center"> 9 </td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
        <!-- Week-10 -->
        <tr>
            <td rowspan=1 align="center"> 10 </td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
        <!-- Week-11 -->
        <tr>
            <td rowspan=1 align="center"> 11 </td>
            <td rowspan=1></td>
            <td rowspan=1 align="center"></td>
            <td></td>
        </tr>
        <!-- Week-12 -->
        <tr>
            <td rowspan=1 align="center"> 12 </td>
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

