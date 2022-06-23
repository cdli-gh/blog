---
layout: page
title: "Improve the credits: ownership and licencing of digital assets"
author: 'Chidiebere'
tags: ['project', 'gsoc', 'gsoc2022', 'improveTheCredits']
---


## Improve the credits: ownership and licencing of digital assets

This project is targeted at updating how digital assets’ license, ownership
and credits are stored, while considering how they can be displayed in a
more detailed way. The system should be able to manage one or multiple owners, should they be individuals or institutions; manage credits, to one or more individual or institutions and the type of credit 

### Objectives and Deliverables

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks

| \# | Status  | Objectives                    | Associated Deliverables         | issue(s) |
| --- | --- | ----------------------------- | ---------------------------------------------- | -------- |
| 1 |:white_check_mark:| Improve the credits: ownership and licencing of digital assets and how digital assets’ (artifacts) license, ownership and credits are stored. | --The Aim is to make the credits for authors more granular | [!630](https://gitlab.com/cdli/framework/-/merge_requests/630) |



### Additional Objectives

| \# | Status  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1 | :heavy_check_mark: |  Address a related issue alreading existing which involves assigning proper roles (Author, Reviewer, Creator)for the authors contribution table.  | List the respective roles (Reviewer, Author, Creator ) for event updates for artifacts while removing non essential columns | [!630](https://gitlab.com/cdli/framework/-/merge_requests/630)   |
| 2 | :white_check_mark: | images management | The objectives of this issue are to put in place the infrastructure so displaying the web images and checking access will be done through the images table. This will also require minimal add / edit / delete functionality. A bonus objective is preparing a page that will harvest information about orphan web images so the admin can add them to the images table. |    [#885](https://gitlab.com/cdli/framework/-/issues/885)     |


### Tentative timeline

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks  :raised_hands: --> Work Demonstration

| Week  |Objectives | Deliverables |
|---|---|---|
|1| :white_check_mark: <br/> Reevaluate the table schema to fully represent the targeted objectives. <br/> Reevaluate the other necessary table relationships that we should have between the credit tables and other tables. <br/> Implement the migration schema following cakephp conventions. | Perfect database schema for credit system implementation |
|2| :heavy_check_mark: Preparing models and start off writing basic controller logic for my project idea |--Preparing the models and other business logic for my project idea.  <br> -- Start writing the logic in the controller for passing the right data to the views/template/in terface for displaying credits. <br/> --Write the logic for saving the necessary credit information into the database |
|3| :heavy_check_mark: hello world  |  :heavy_check_mark: hello world <br/> :heavy_check_mark: hello world <br> :raised_hands: hello world|
