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
| 1 |:heavy_check_mark:|  Manage publications and authors | Creating add, edit and delete functions for the publications and authors pages. | #122 |
| 2 |:heavy_check_mark: | Link publications | Feature for linking publications with artifacts, editors and authors.   |    #122, #274      |
| 3 | :heavy_check_mark: | Bulk upload publications      | Feature for bulk uploading publications to the database using CSV files.            |   #122       |
| 4 | :heavy_check_mark: | Bulk link publications | Feature for bulk linking publications to artifacts, authors and editors using CSV files. | #122 |
| 5 | :white_check_mark: | Documentation      | User and technical documentation for all the features.             |          |


### Additional Objectives

| | Status  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1 | :heavy_check_mark: | Merge publications | Admin feature for merging publications with search for publications. |         |
| 2 |  | Link entities | Linking entities with bibliographies.       |          |


### Tentative timeline  

| Week  |Objectives | Deliverables |
|---|---|---|
|1| :heavy_check_mark: Implement linking of artifacts to the selected publication through the view page of the publication. <br> :heavy_check_mark: Implement linking of publications to the selected artifact through the view page of the artifact. <br> :heavy_check_mark: Implement linking of authors to the selected publication through the view page of the publication. <br> :heavy_check_mark: Implement linking of publications to the selected author through the view page of the author. |  :heavy_check_mark: Features for linking publications with artifacts and authors. |
|2| :heavy_check_mark: Implement linking publications to editors using the Author-Publication link pages. <br> :heavy_check_mark: Fixing bugs in the view pages and, creating add, edit and delete functions for authors data.  | :heavy_check_mark: Feature for linking editors and publications. <br> :heavy_check_mark: Features for managing authors data.  |
|3| :heavy_check_mark: Implement bulk linking of publications to artifacts using CSV file uploads. (making components for the task for easy reusability for similar tasks).  | :heavy_check_mark: Bulk upload for linking publications to artifacts.  |
|4| :heavy_check_mark: Implement bulk linking of publications to authors using CSV files. <br> :heavy_check_mark: Implement bulk linking of publications to editors using CSV files. <br> :heavy_check_mark: Creating add, edit and delete functions for publication data. <br>  :heavy_check_mark: Making some data input and display improvements to the link artifacts-publications features.  | :heavy_check_mark: Bulk upload for linking publications to authors and editors. <br> :heavy_check_mark: Feature for managing publications data. |
|5| :heavy_check_mark: Implement bulk upload of publications using CSV files. | :heavy_check_mark: Feature for bulk upload of publications. |
|6| :heavy_check_mark: Bug fixes for the previous features.  | -  |
|7| :heavy_check_mark: Design and implement merge publication feature.   | :heavy_check_mark: Entire structure for merge publications feature.  |
|8| :heavy_check_mark: Integrating add authors and editors for the publications data management pages. <br> :heavy_check_mark: Design changes for artifacts-publications pages. |:heavy_check_mark: Publications data management pages. |
|9| :heavy_check_mark: Implement publication index and view pages.  | :heavy_check_mark: Publication view and index.  | 
|10| :heavy_check_mark: Filters for index and merge publication pages and complete display for merge publications. | :heavy_check_mark: Completed merge publications feature.  |
|11| Buffer time for completing remaining work. <br> Final thorough testing for all features and bug fixes.    | -  |
|12| Buffer time for any remaining bug fixes and documentation. <br> Final report for all the work done.  | Completed documentation and bug fixes.  |



