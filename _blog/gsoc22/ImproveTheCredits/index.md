---
layout: page
title: "Improve the credits: ownership and licencing of digital assets"
author: 'Chidiebere'
tags: ['project', 'gsoc', 'gsoc2022', 'improveTheCredits']
---


## Improve the credits: ownership and licencing of digital assets

This project is targeted at updating how digital assets’ license, ownership
and credits are stored, while considering how they can be displayed in a
more detailed way. The system should be able to manage one or multiple owners, should they be individuals or institutions; manage credits, to one or more individual or institutions and the type of credit. 

### Objectives and Deliverables

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks

| \# | Status  | Objectives                    | Associated Deliverables         | issue(s) |
| --- | --- | ----------------------------- | ---------------------------------------------- | -------- |
| 1 |:white_check_mark:| Design tables with their relationships with schema to handle the new data using cakePHP table and migration conventions | Perfect database schema for credit system implementation | [!318]() |
| 2 |:white_check_mark:| Extending the API to accomodate new data for machines to access the data for the credit system| Write a rest API using cakephp for machines to access the additional information regarding digital assets for search results, and single artifacts | [!318]() |
| 3 |:white_check_mark:| Extend the interface to display the information regarding the credits system where appropriate ( all the places where a digital asset can be displayed) | --Work on the views/template for the places where a digital asset can be displayed <br/> -- Make adjustments so that the credit information displayed will align properly with the figma design and adjustments will not distort the interface aesthetics.<br/> | [!318]() |
| 4 |:white_check_mark:| Collaborate with design challenge I person to feed the cite button for digital assets| --Accurate Citation button etc as well as other provision of good user experience for the credit system. | [!318]() |
| 5 |:white_check_mark:| Create appropriate edition forms and bulk upload functionality for the addition/edition of credit data for digital assets | --Edit form and bulk upload functionality Implemented | [!318]() |



### Additional Objectives

| \# | Status  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1 | :heavy_check_mark: |  Address a related issue alreading existing which involves assigning proper roles (Author, Reviewer, Creator)for the authors contribution table.  | List the respective roles (Reviewer, Author, Creator ) for event updates for artifacts while removing non essential columns | [!630](https://gitlab.com/cdli/framework/-/merge_requests/630)   |
| 2 | :white_check_mark: | images management | The objectives of this issue are to put in place the infrastructure so displaying the web images and checking access will be done through the images table. This will also require minimal add / edit / delete functionality. A bonus objective is preparing a page that will harvest information about orphan web images so the admin can add them to the images table. |    [#885](https://gitlab.com/cdli/framework/-/issues/885)     |


### Tentative timeline

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks  :raised_hands: --> Work Demonstration

| Week  |Objectives | Deliverables |
|---|---|---|
|1| :white_check_mark: --Reevaluate the table schema to fully represent the targeted objectives. <br/> Reevaluate the other necessary table relationships that we should have between the credit tables and other tables. <br/> Implement the migration schema following cakephp conventions. | Perfect database schema for credit system implementation |
|2| :white_check_mark: --Preparing models and start off writing basic controller logic for my project idea |--Preparing the models and other business logic for my project idea.  <br> -- Start writing the logic in the controller for passing the right data to the views/template/in terface for displaying 
|3| :white_check_mark: --UI interface for the storing credits as well as other meta data needed|--Rough UI Mockup for the interface. <br> -- Updating exisitng stated model to reflect the feedback from mentor
|4| :white_check_mark: --Work on seeing to it that the images are uploaded, in the right folder...ALso setting up multiple images upload<br> -- Iterating and getting feedback from mentor 
