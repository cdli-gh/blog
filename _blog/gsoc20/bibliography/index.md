---
layout: page
title: Bibliography management and display
author: 'Ajit Jadhav'
tags: ['project', 'gsoc', 'gsoc2020', 'bibliography', 'eval#1', 'week#2']
---

## Bibliography Management and Display

This project concerns in the first place,
the conception of the management pages for this data, and in second, the display of
bibliographic data. In order to make CDLI’s bibliographic data more useful, it should be
easily manageable by the admin, and also have a nice linked display.

### Objectives and Deliverables

:heavy_check_mark: --> Completed Tasks
:white_check_mark: --> Ongoing Tasks

| | Status  | Objectives                    | Associated Deliverables         | issue(s) |
| --- | --- | ----------------------------- | ---------------------------------------------- | -------- |
| 1 | :white_check_mark:  | Link publications | Feature for linking publications with artifacts and authors.   |          |
| 2 |  | Bulk linking for publications | Feature for bulk linking of publications to artifacts and authors using CSV files.  |          |
| 3 |  | Bulk upload publications      | Feature for bulk uploading publications to the database using CSV files.            |          |
| 4 |  | Documentation           | User and technical documentation for all the features.                                      |          |
| 5 |  | Export citations              | Feature for bulk exporting citations realted to artifacts from the search results.  |          |

#### Additional Objectives

| | Status  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1 |  | Merge publications | Admin feature for merging publications with search for publications. |          |
| 2 |  | Link entities | Linking entities with bibliographies.       |          |


### Tentative timeline  

| Week  |Objectives | Work completed |  
|---|---|---|  
|1|  Implement linking of artifacts to the selected publication through the view page of the publication. <br> Implement linking of publications to the selected artifact through the view page of the artifact. <br> Implement linking of authors to the selected publication through the view page of the publication. <br> Implement linking of publications to the selected author through the view page of the artifact. <br> Modifying the existing add and edit functions for publication, author and artifact pages. <br> Document the completed features.    | Feature for linking publications with artifacts and authors. |  
|2| Implement bulk linking of publications to artifacts using CSV file uploads. <br> Adding appropriate file format checking and error handling.  Implement bulk linking of publications to authors using CSV files.  | Feature for bulk linking of publications and artifacts using CSV files. <br> Feature for bulk upload of publications. |  
|3| Implement bulk upload of publications using CSV files. <br> Document the completed features. <br> Implement merge publication feature.   |   |  
|4| Add search integration for the merge publication feature. Document the completed features <br> (tentative) Finalize details for linking entities with bibliographies and start working on it.   | - Feature for merging publications.  |  
|5|   |   |  
|6|   |   |
|7|   |   |  
|8|   |   |  
|9|   |   |  
|10|  |   |
|11| Final thorough testing for all features and bug fixes. <br> Finalizing the user and developer documentations.   | Completed documentation and bug fixes.  |  
|12| Buffer time for any remaining bug fixes and documentation. Final report for all the work done.  | -  |  

### Dependent Tasks
List of tasks which need to be co-ordinated with other developers.

Handling the bulk export citation interface using API developed by Lars.


<table>
<colgroup>
<col width="30%" />
<col width="70%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span"> <ul><li> - [x] item1</li><li> - [ ] item2</li></ul> First column **fields**</td>
<td markdown="span">Some descriptive text. This is a markdown link to [Google](http://google.com). Or see [some link][mydoc_tags].</td>
</tr>
<tr>
<td markdown="span">Second column **fields**</td>
<td markdown="span">Some more descriptive text.
</td>
</tr>
</tbody>
</table>
