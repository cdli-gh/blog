---
layout: page
title: Bibliography management and display.
author: 'Ajit Jadhav'
tags: ['project', 'gsoc', 'gsoc2020', 'bibliography', 'eval#1', 'week#2']
---

## Bibliography Management and Display

This project concerns in the first place,
the conception of the management pages for this data, and in second, the display of
bibliographic data. In order to make CDLI’s bibliographic data more useful, it should be
easily manageable by the admin, and also have a nice linked display.

### Objectives and Deliverables

| | Status  | Objectives                    | Associated Deliverables         | issue(s) |
| --- | --- | ----------------------------- | ---------------------------------------------- | -------- |
| 1 | - [x] Current - [ ] Completed | Link publications             | Feature for linking publications with artifacts and authors.                        |          |
| 2 | - [ ] Current - [ ] Completed | Bulk linking for publications | Feature for bulk linking of publications to artifacts and authors using CSV files.  |          |
| 3 | - [ ] Current - [ ] Completed | Bulk upload publications      | Feature for bulk uploading publications to the database using CSV files.            |          |
| 4 | - [ ] Current - [ ] Completed | Documentation           | User and technical documentation for all the features.                                      |          |
| 5 | - [ ] Current - [ ] Completed | Export citations              | Feature for bulk exporting citations realted to artifacts from the search results.  |          |

#### Additional Objectives

| | Status  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1 | - [ ] Current - [ ] Completed | Merge publications | Admin feature for merging publications with search for publications. |          |
| 2 | - [ ] Current - [ ] Completed | Link entities      | Linking entities with bibliographies.       |          |


### Tentative timeline  

| Week  |Objectives | Work completed |  
|---|---|---|  
|1| <div class="tip" markdown="1"> - [ ] Implement linking of artifacts to the selected publication through the view page of the publication. - [ ] Implement linking of publications to the selected artifact through the view page of the artifact. - [ ] Implement linking of authors to the selected publication through the view page of the publication. - [ ] Implement linking of publications to the selected author through the view page of the artifact. - [ ] Modifying the existing add and edit functions for publication, author and artifact pages. - [ ] Document the completed features.  </div>   | <div class="tip" markdown="1"> - Feature for linking publications with artifacts and authors.  </div> |  
|2| - [ ] Implement bulk linking of publications to artifacts using CSV file uploads. - [ ] Adding appropriate file format checking and error handling. - [ ] Implement bulk linking of publications to authors using CSV files.  | - Feature for bulk linking of publications and artifacts using CSV files. - Feature for bulk upload of publications. |  
|3| - [ ] Implement bulk upload of publications using CSV files. - [ ] Document the completed features. - [ ] Implement merge publication feature.   |   |  
|4| - [ ] Add search integration for the merge publication feature. - [ ] Document the completed features - [ ] (tentative) Finalize details for linking entities with bibliographies and start working on it.   | - Feature for merging publications.  |  
|5|   |   |  
|6|   |   |
|7|   |   |  
|8|   |   |  
|9|   |   |  
|10|  |   |
|11| - [ ] Final thorough testing for all features and bug fixes. - [ ] Finalizing the user and developer documentations.   | Completed documentation and bug fixes.  |  
|12| - [ ] Buffer time for any remaining bug fixes and documentation. - [ ] Final report for all the work done.  | -  |  

### Dependent Tasks
List of tasks which need to be co-ordinated with other developers.

- [ ] Handling the bulk export citation interface using API developed by Lars.
