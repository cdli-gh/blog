---
layout: page
title: bibliography
author: 'Ajit'
tags: ['project', 'gsoc', 'gsoc2020', 'bibliography', 'eval#1', 'week#2']
---

## Bibliography Management and Display

This project concerns in the first place,
the conception of the management pages for this data, and in second, the display of
bibliographic data. In order to make CDLI’s bibliographic data more useful, it should be
easily manageable by the admin, and also have a nice linked display.

### Objectives and Deliverables

| \#  | Objectives                    | Associated Deliverables                                                            | issue(s) |
| --- | ----------------------------- | ---------------------------------------------------------------------------------- | -------- |
| 1   | Link publications             | Feature for linking publications with artifacts and authors.                        |          |
| 2   | Export citations              | Feature for bulk exporting citations realted to artifacts from the search results.  |          |
| 3   | Bulk linking for publications | Feature for bulk linking of publications to artifacts and authors using CSV files.  |          |
| 4   | Bulk upload publications      | Feature for bulk uploading publications to the database using CSV files.            |          |
| 5   | User documentation            | User documentation for using all the features.                                      |          |
| 6   | Technical documentation       | Documentation of all the feature architectures and details for future development. |          |

#### Additional Objectives

| \#  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1   | Merge publications | Admin feature for merging publications with search for publications. |          |
| 2   |                    |                                                                     |          |
| 3   |                    |                                                                     |          |
| 4   |                    |                                                                     |          |
| 5   |                    |                                                                     |          |
| 6   |                    |                                                                     |          |


### Tentative timeline  

| Week  |Objectives |Deliverables |  
|---|---|---|  
|1| Implement linking of artifacts to the selected publication through the view page of
the publication.  |   |  
|2| Implement linking of publications to the selected artifact through the view page of
the artifact.
<br> Implement linking of authors to the selected publication through the view page of
the publication.
<br> Add auto complete feature for the author name.  |   |  
|3| Implement linking of publications to the selected author through the view page of
the artifact.
<br> Modifying the existing add and edit functions for publication, author and artifact
pages.  |   |  
|4| Creating the backend parser for the CSV files used for bulk linking of publications to artifacts.  |   |  
|5| Creating the feature for bulk linking of publications to artifacts by using the file parser and adding the interface and appropriate error handling.   |   |  
|6| Similarly, implement bulk linking of publications to authors using CSV files.  |   |  
|7| Implement bulk upload of publications using CSV files.  |   |  
|8| Implement merge publication feature.  |   |  
|9| Add search integration for the merge publication feature.  |   |  
|10| Buffer time for handling the bulk export citation interface using API developed by Lars.   |   |  
|11| Final thorough testing for all features and bug fixes. 
<br> Finalizing the user and developer documentations.   |   |  
|12| Buffer time for any remaining bug fixes and documentation.  |   |  

