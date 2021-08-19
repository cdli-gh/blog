---
layout: page
title: Discovery Search and Advanced Search features
author: 'Yashraj Desai'
tags: ['project', 'gsoc', 'gsoc2021', 'discoverySearchAndAdvancedSearchFeatures']
---

## Discovery Search and Advanced Search Features

Hi 👋, I am [Yashraj Desai](https://www.linkedin.com/in/yashraj-desai-55a78a1a5/) ! I worked on "Discovery Search and Advanced Search Features" project under CDLI organisation for GSoC '21. 
The project mainly focuses on enhancing the Search and Advanced search features in the CDLI framework and adding new features to it using [Elasticsearch](https://www.elastic.co/elasticsearch/) and [CakePHP](https://cakephp.org/).

<i>Proposal Link</i> : [Discovery search and advanced search features](https://docs.google.com/document/d/1WEeNnALSUN4yecCbYxuDyMNUMOzkGcev6Dss4XuNydc/edit#)\
<i>Contributions to CDLI</i> : [Link](https://gitlab.com/cdli/framework/-/merge_requests?scope=all&state=all&author_username=yashrajdesai30)


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
| 6 | On add or edit save a sanitized version of inscription as a list of sign names |When an artifact is added/edited the sign values and sign-names will be stored in the database|[#120](https://gitlab.com/cdli/framework/-/issues/120#note_550066667)
| 7 | Input flexibility enhancements |Users will have the flexibility to search with both UTF-8 and ASCII characters |[#597](https://gitlab.com/cdli/framework/-/issues/597)|[!375](https://gitlab.com/cdli/framework/-/merge_requests/375) |:heavy_check_mark: |
| 8 | Filter search results by RTI Image, Transliterations , 3D Data | Users can apply filters such as RTI Image, Transliterations, 3D Data and get search results | [#136](https://gitlab.com/cdli/framework/-/issues/136) | [!369](https://gitlab.com/cdli/framework/-/merge_requests/369) |:heavy_check_mark: |



### Additional Objectives

| \#  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1 | Implementation of CakePHP elasticsearch plugin  | Cakephp Elasticsearch plugin implemented along with documentation | [#460](https://gitlab.com/cdli/framework/-/issues/460) |

### Dependencies
* JTF Data (Vishv)
* Images Table (Daksh)

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
|4|Highlight transliteration sign values in ATF display|The sign values will be highlighted in the compact search results page|:heavy_check_mark:|
|5|Testing and Documentation |Testing and documentation of all the objectives in coding phase 1|:heavy_check_mark:|
|6|Search Inscription with sign value permutaion|When a user will enable this search feature and search for sign values, all possible sign values with matching sign names of the query will be returned| :heavy_check_mark: |
|7| Store sign data in database on add/edit inscriptions|When an artifact is added/edited the sanitised jtf data along with sign values and sign-names will be stored in the database||
|8|Input flexibility enhancements|Users will have the flexibility to search with both UTF-8 and ASCII characters| :heavy_check_mark: |
|9|Filter search results by RTI Image, Transliterations, 3D Data|Users can apply filters such as RTI Image, Transliterations, 3D Data and get search results.|:heavy_check_mark: |
|10|Testing and Documentation|Testing and documentation of all the objectives in coding phase 2| :man_technologist: |


