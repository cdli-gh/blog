---
layout: page
title: Digital Library Management
author: 'Daksh Paleria'
tags: ['project', 'gsoc', 'gsoc2021', 'digitalLibraryManagement']
---

## Digital Library Management

Hey, I'm [Daksh Paleria](https://www.linkedin.com/in/daksh-paleria-606211190/) participating in Google Summer of Code 2021 with CDLI.
I've been accepted for the project Digital Library Management, the project is about preparing a dashboard that can show an admin the visual assets of the digital library for each artifact but also add, edit, delete, images using our archival images serve as a source of better quality images to prepare their web counterpart. Access to images should also be managed there (some images are not public).

Project: [GSoC'21](https://summerofcode.withgoogle.com/projects/#6327175881424896)

Work Status, Proposal: [Link](https://drive.google.com/drive/folders/17zfao7u9gfowSWieSYWuw8JJVlluXdE0?usp=sharing)

### Objectives and Deliverables

:heavy_check_mark: --> Completed Tasks
:man_technologist: --> Ongoing Tasks

| \# | Status  | Objectives                    | Associated Deliverables         | issue(s) |
| --- | --- | ----------------------------- | ---------------------------------------------- | -------- |
| 1 | :man_technologist: | Design Pages | Design the pages for viewing archival images, selecting multiple artficats at a time, upload archival images | - |
| 2 | :man_technologist: | Prepare Image Table | Storing information regarding images in our table | - |
| 3 | :man_technologist: | Converting archive images to their web counterpart | Adding the functionality to convert archival images to web counterpart | - |
| 4 | :man_technologist: | Dealing with Multiple Entries | Allowing the admins to select multiple entries and converting the images for them in one go | - | 
| 5 | :man_technologist: | Dealing with Non Associated Images | Working around the images which are not associated with any of the artifacts | - |   


### Additional Objectives

| \# | Status  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1 | :man_technologist: | CMD Script  | CMD Script to upload archival images from web server to wasabi server. Script should handle adding, remaining files on wasabi and deleting. | - |


### Tentative timeline  

| Week  |Objectives | Deliverables |
|---|---|---|
|1| Designing the Pages | Get reviews from mentors regrding the design of pages and formalize the workflow | 
|2| Installation of Conversion Algorithm  | Installing the library and try to add them in nginx or cake container |
|3| Preparing Image Table  | Raise an issue to get review regarding theimage table, prepare a script to populate the tables intially |
|4| Generating Standard Templates  | Preparing standard templates, controllers for providing intial functionalities. Documetation of the work done till now |
|5| Preparing Custom Controllers  | Preparing custom controllers for conversion, viewing of archival images |
|6| Editing Current Templates | Editing current Artifact templates for adding a new tab to view Archival Image |
|7| Working for Non Associated Images  | Developing controllers, templates for accessing Non Associated Images. |
|8|  View Templates for Non Associated Images | Creating view templates for viewing non associated archival images, documenting the work done till now. |
|9| Allowing Admins to Change type of Image | Developing the functionality to allow admins change the type of image. |
|10| Document, test and further feature addons | Documenting the work, working around the additionl Objectives. |