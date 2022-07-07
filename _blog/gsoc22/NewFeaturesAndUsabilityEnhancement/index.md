---
layout: page
title: New Features and Usability Enhancement
author: 'Shivoham Angal'
tags: ['project', 'gsoc', 'gsoc2022', 'newFeaturesAndUsabilityEnhancement']
---

## New Features and Usability Enhancement

This project aims at adding new features to the CDLI framework and enhancing the usability of some of the pre-existing features. The objectives of this project are : Presenting retired artifacts in a tabular format and redirecting users to the new entry when they link to a retired artifact. A new feature like the download button for the publications page will help users download it with all bib type options like bib, ris, formatted etcetera. Adding a feature to bulk update artifacts (multiple edit form) based on any of the properties of artifacts will be a huge time saver. Lastly, displaying a dropdown to export entity indexes in various formats like csv, ttf, json, json-rdf on all entity pages.

### Objectives and Deliverables

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks

| \# | Status  | Objectives                    | Associated Deliverables         | issue(s) |
| --- | --- | ----------------------------- | ---------------------------------------------- | -------- |
| 1 |:white_check_mark:|  Implementing Features for Retired Artifacts | Modifying tables in the database, making index page, adding retired artifact section | [#747](https://gitlab.com/cdli/framework/-/issues/747) |
| 2 |:white_check_mark:|  Export Data on Entities Indexes | Create export button, implement Utility class for entity exports | [#786](https://gitlab.com/cdli/framework/-/issues/786) |
| 3 |:white_check_mark:|  Bulk Update on interface | Create bulk update button and modal to choose fields, create controller, create bulk edit page | [#280](https://gitlab.com/cdli/framework/-/issues/280) |
| 4 |:white_check_mark:|  Export Bibliography from Publications Pages | Create export button for single and indexviews | [#521](https://gitlab.com/cdli/framework/-/issues/521) |

### Additional Objectives

| \# | Status  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | --- | ------------------ | ------------------------------------------------------------------- | -------- |
| |  |    |   |    |


### Tentative timeline

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks  :raised_hands: --> Work Demonstration

| Week  |Objectives | Deliverables |
|---|---|---|
|1| :heavy_check_mark: Retired Artifacts Backend  |  :heavy_check_mark: Fix artifact_id & new_artifact_id fields. <br/> :heavy_check_mark: Move artifact_id and retired_for to artifacts table and delete retired_artifacts table. <br> :heavy_check_mark: Modify Artifact Update & Artifact Entities. <br> :raised_hands: Tables should be prepared.|
|2| :heavy_check_mark: Retired Artifacts Functionality  |  :heavy_check_mark: Create index page. <br/> :heavy_check_mark: Redirect users to new entry. <br> :raised_hands: Index page for retired artifacts and redirecting should work properly.|
|3| :heavy_check_mark: Retired Artifacts Functionality  |  :heavy_check_mark: Not searching among/displaying retired artifacts. <br/> :heavy_check_mark: Adding retired artifacts section to edit artifact form. <br> :raised_hands: Section for retired artifacts in edit form and not earching among them.|
|4| :heavy_check_mark: Testing Retired Artifacts Implementation and writing Documentation  |  :heavy_check_mark: Checking if the added functionality is working as expected and if a bug is found, debug it.
|5| :heavy_check_mark: Export data on Entities Index  |  :heavy_check_mark: Create export button element and display it on entity indexes. <br/> :raised_hands: The added button element should not distort the entity pages.|
|6| :heavy_check_mark: Export data on Entities Index |  :heavy_check_mark: Implement the Utility class for exporting entity data. <br> :raised_hands: The export functionality should work properly and export all the required data.|
|7| :heavy_check_mark: Testing Entity Export Functionality and Writing Documentation |  :heavy_check_mark: Checking if the added functionality is working as expected and if a bug is found, debug it.
|8| :heavy_check_mark: Bulk Update on Interface|  :heavy_check_mark: Create Bulk Update button on the search results page. <br> :heavy_check_mark: Create modal for choosing fields to be bulk updated. <br> :raised_hands: The button should make the modal to be displayed and fields chosen here should be detected properly.
|9| :heavy_check_mark: Bulk Update on Interface |  :heavy_check_mark: Create buld edit controller. <br> :heavy_check_mark: Create bulk edit page. <br>
|10| :heavy_check_mark: Testing Bulk Update Functionality and Writing Documentation |  :heavy_check_mark: Checking if the added functionality is working as expected and if a bug is found, debug it.
|11| :heavy_check_mark: Export Bibliography from Publication Pages |  :heavy_check_mark: Create button to export bibliography in BibTex format on single and index views. <br> :raised_hands: The export button should work properly.
|12| :heavy_check_mark: Testing Export Bibliography Functionality and Writing Documentation |  :heavy_check_mark: Checking if the added functionality is working as expected and if a bug is found, debug it.
