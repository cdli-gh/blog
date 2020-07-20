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
| 1 |:white_check_mark:|  Manage publications and authors | Creating add, edit and delete functions for the publications and authors pages. | #122 |
| 2 |:heavy_check_mark: | Link publications | Feature for linking publications with artifacts, editors and authors.   |    #122, #274      |
| 3 |  | Bulk upload publications      | Feature for bulk uploading publications to the database using CSV files.            |   #122       |
| 4 | :heavy_check_mark: | Bulk link publications | Feature for bulk linking publications to artifacts, authors and editors using CSV files. | #122 |
| 5 |  | Export citations   | Feature for bulk exporting citations realted to artifacts from the search results.  |   #122       |
| 6 |  | Documentation           | User and technical documentation for all the features.             |          |


### Additional Objectives

| | Status  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1 |  | Merge publications | Admin feature for merging publications with search for publications. |         |
| 2 |  | Link entities | Linking entities with bibliographies.       |          |


### Dependent Tasks
List of tasks which need to be co-ordinated with other developers:

- Handling the bulk export citation interface using bibliography API.
- Changing the publication table view to list of bibliographies using bibliography API.

### Tentative timeline  

| Week  |Objectives | Deliverables |
|---|---|---|
|1| :heavy_check_mark: Implement linking of artifacts to the selected publication through the view page of the publication. <br> :heavy_check_mark: Implement linking of publications to the selected artifact through the view page of the artifact. <br> :heavy_check_mark: Implement linking of authors to the selected publication through the view page of the publication. <br> :heavy_check_mark: Implement linking of publications to the selected author through the view page of the author. |  :heavy_check_mark: Features for linking publications with artifacts and authors. |
|2| :heavy_check_mark: Implement linking publications to editors using the Author-Publication link pages. <br> :heavy_check_mark: Fixing bugs in the view pages and, creating add, edit and delete functions for authors data.  | :heavy_check_mark: Feature for linking editors and publications. <br> :heavy_check_mark: Features for managing authors data.  |
|3| :heavy_check_mark: Implement bulk linking of publications to artifacts using CSV file uploads. (making components for the task for easy reusability for similar tasks).  | :heavy_check_mark: Bulk upload for linking publications to artifacts.  |
|4| :heavy_check_mark: Implement bulk linking of publications to authors using CSV files. <br> :heavy_check_mark: Implement bulk linking of publications to editors using CSV files. <br> :heavy_check_mark: Creating add, edit and delete functions for publication data. <br>  :heavy_check_mark: Making some data input and display improvements to the link artifacts-publications features.  | :heavy_check_mark: Bulk upload for linking publications to authors and editors. <br> :heavy_check_mark: Feature for managing publications data. |
|5| :white_check_mark: Implement bulk upload of publications using CSV files. (While most of the work is done, a bug fix is remaining which has not been figured out yet). | :white_check_mark: Feature for bulk upload of publications. <br>  |
|6| :heavy_check_mark: Bug fixes for the previous features.  | -  |
|7| :heavy_check_mark: Design and implement merge publication feature.   | :heavy_check_mark: Entire structure for merge publications feature.  |
|8|   |   |
|9|   |   | 
|10|  |   |
|11| Final thorough testing for all features and bug fixes. <br> Finalizing the user and developer documentations.   | Completed documentation and bug fixes.  |
|12| Buffer time for any remaining bug fixes and documentation. Final report for all the work done.  | -  |



