---
layout: page
title: Discovery Search and Advanced Search features
author: 'Yashraj Desai'
tags: ['project', 'gsoc', 'gsoc2021', 'discoverySearchAndAdvancedSearchFeatures']
---

## Discovery Search and Advanced Search Features

Hi 👋, I am [Yashraj Desai](https://www.linkedin.com/in/yashraj-desai-55a78a1a5/) ! I worked on "Discovery Search and Advanced Search Features" project under CDLI organisation for GSoC '21. 
The project mainly focuses on enhancing the Search and Advanced search features in the CDLI framework and adding new features to it using [Elasticsearch](https://www.elastic.co/elasticsearch/) and [CakePHP](https://cakephp.org/).

<i>Proposal</i> : [Discovery search and advanced search features](https://docs.google.com/document/d/1WEeNnALSUN4yecCbYxuDyMNUMOzkGcev6Dss4XuNydc/edit#)\
<i>Contributions to CDLI</i> : [Link](https://gitlab.com/cdli/framework/-/merge_requests?scope=all&state=all&author_username=yashrajdesai30)\
<i>Final Report</i> : [Report](https://github.com/yashrajdesai/GSoC-2021-Report/blob/main/README.md#-google-summer-of-code-2021-)

Mentor : [Vedant Wakalkar](https://www.linkedin.com/in/karna98/)

## GSoC Final Report and Summary.
Participating in GSoC was a great learning curve for me, I faced alot of challenges in this journey which helped me in learning new skills.
I shall always be indebted to such a welcoming organisation to help me enhance my coding skills.

### Objectives and Deliverables

| \# | Objectives                    | Associated Deliverables         | issue(s) | Pull Requests |    Status |
| --- | ----------------------------- | -------------------------------------------- | -------- | -------- | ---- |
| 1 |  Add “Ids” and “Keywords” search fields to both simple and advanced search | Users will be able to search for specific keywords, Id/Numbers artifacts | [#314](https://gitlab.com/cdli/framework/-/issues/314) | [!317](https://gitlab.com/cdli/framework/-/merge_requests/317), [!307](https://gitlab.com/cdli/framework/-/merge_requests/307) |:heavy_check_mark:|
| 2 | Implementation of fuzzy queries | Fuzzy queries would yield search results in all search fields|[#593](https://gitlab.com/cdli/framework/-/issues/593) | [!317](https://gitlab.com/cdli/framework/-/merge_requests/317) |:heavy_check_mark: |
| 3 | Port request to Elasticsearch from cURL to HttpClient | Replaced cURL implementation with HTTP Client|[#350](https://gitlab.com/cdli/framework/-/issues/350)| [!338](https://gitlab.com/cdli/framework/-/merge_requests/338) | :heavy_check_mark: |
| 4 | Highlight transliteration sign values in ATF display |The sign values will be highlighted in the full and compact search results page|[#347](https://gitlab.com/cdli/framework/-/issues/347)| [!354](https://gitlab.com/cdli/framework/-/merge_requests/354) | :heavy_check_mark: |
| 5 | Enable search inscription with sign value permutation |When a user will enable this search feature and search for sign values, all possible sign values with matching sign names of the query will be returned| [#596](https://gitlab.com/cdli/framework/-/issues/596) | [!375](https://gitlab.com/cdli/framework/-/merge_requests/375) |:heavy_check_mark: |
| 6 | Search settings integration | Users will be able to save specific configuration of search settings and search results will be displayed accordingly. |[#540](https://gitlab.com/cdli/framework/-/issues/540) | [!332](https://gitlab.com/cdli/framework/-/merge_requests/332) | :heavy_check_mark: |
| 7 | Input flexibility enhancements |Users will have the flexibility to search with both UTF-8 and ASCII characters |[#597](https://gitlab.com/cdli/framework/-/issues/597)|[!375](https://gitlab.com/cdli/framework/-/merge_requests/375) |:heavy_check_mark: |
| 8 | Filter search results by RTI Image, Transliterations , 3D Data | Users can apply filters such as RTI Image, Transliterations, 3D Data and get search results | [#136](https://gitlab.com/cdli/framework/-/issues/136) | [!369](https://gitlab.com/cdli/framework/-/merge_requests/369) |:heavy_check_mark: |

### Additional Objectives

| \#  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1 | Implementation of CakePHP elasticsearch plugin  | Cakephp Elasticsearch plugin implemented along with documentation | [#460](https://gitlab.com/cdli/framework/-/issues/460) |

### What Is Left
* Robust testing and documentation of all the newly added features.
* Once Lars and Vishv are done with API integration, sanitised version of sign values and sign names can be stored in the database when user adds/edits inscriptions.



### Tentative timeline  

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

| Week  |Objectives | Deliverables | Status |
|---|---|---|---|
|1|Ids and Keywords search fields|Users will be able to search for specific keywords,Id/Numbers artifacts both in simple and advanced search|:heavy_check_mark:|
|2|Fuzzy queries|Fuzzy queries would yield search results in all search fields|:heavy_check_mark:|
|3|Port request to Elasticsearch from cURL to HttpClient|Replaced cURL implementation with HTTP Client|:heavy_check_mark:|
|4| Search settings integration | Users will be able to save specific configuration of search settings and search results will be displayed accordingly.| :heavy_check_mark: |
|5|Highlight transliteration sign values in ATF display|The sign values will be highlighted in the compact search results page|:heavy_check_mark:|
|6|Search Inscription with sign value permutaion|When a user will enable this search feature and search for sign values, all possible sign values with matching sign names of the query will be returned| :heavy_check_mark: |
|7|Input flexibility enhancements|Users will have the flexibility to search with both UTF-8 and ASCII characters| :heavy_check_mark: |
|8|Filter search results by RTI Image, Transliterations, 3D Data|Users can apply filters such as RTI Image, Transliterations, 3D Data and get search results.|:heavy_check_mark: |
|9|Testing |Testing all the newly added features| :heavy_check_mark: |
