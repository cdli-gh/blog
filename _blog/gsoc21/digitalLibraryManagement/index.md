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

Proposal: [Link](https://docs.google.com/document/d/1_B54MqUZHQOMm2iRRvYYVMqDiDcIz5tq9iY6Qm7fvnw/edit?usp=sharing)

Contributions: [Link](https://gitlab.com/cdli/framework/-/merge_requests?scope=all&utf8=%E2%9C%93&state=all&author_username=dakshp07)

Work Status: [Link](https://drive.google.com/drive/folders/17zfao7u9gfowSWieSYWuw8JJVlluXdE0?usp=sharing)

### Objectives and Deliverables

:heavy_check_mark: --> Completed Tasks
:man_technologist: --> Ongoing Tasks

| \# | Status  | Objectives                    | Associated Deliverables         | issue(s) |
| --- | --- | ----------------------------- | ---------------------------------------------- | -------- |
| 1 | :heavy_check_mark: | Design Pages | Design the pages for viewing archival images, selecting multiple artifacts at a time, upload archival images | [#609](https://gitlab.com/cdli/framework/-/issues/609) |
| 2 | :man_technologist: | Prepare Image Table | Storing information regarding images in our table | [#87](https://gitlab.com/cdli/framework/-/issues/87) |
| 3 |  | Converting archive images to their web counterpart | Adding the functionality to convert archival images to web counterpart | [#87](https://gitlab.com/cdli/framework/-/issues/87) |
| 4 |  | Dealing with Multiple Entries | Allowing the admins to select multiple entries and converting the images for them in one go | [#607](https://gitlab.com/cdli/framework/-/issues/607) | 
| 5 |  | Uploading Archival Folder | Upload archival folder and use those images to create a thumbnail | [#586](https://gitlab.com/cdli/framework/-/issues/586) | 
| 6 |  | Dealing with Non Associated Images | Working around the images which are not associated with any of the artifacts | [#608](https://gitlab.com/cdli/framework/-/issues/608) |   


### Additional Objectives

| \# | Status  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1 |  | CMD Script  | CMD Script to upload archival images from web server to wasabi server. Script should handle adding, renaming files on wasabi and deleting. | - |


### Tentative timeline  

| Week  | Status |Objectives | Deliverables | issue(s)
|---|---|---|---| --- |
|1| :heavy_check_mark: | Designing the Pages | Get reviews from mentors regarding the design of pages and formalize the workflow | [#609](https://gitlab.com/cdli/framework/-/issues/609) |
|2| :man_technologist: | Preparing Image Table   | Raise an issue to get review regarding theimage table, prepare a script to populate the tables intially | [#87](https://gitlab.com/cdli/framework/-/issues/87)  |
|3|  | Installation of Conversion Algorithm | Installing the library and try to add them in nginx or cake container | [#87](https://gitlab.com/cdli/framework/-/issues/87)  |
|4|  | Generating Standard Templates  | Preparing standard templates, controllers for providing intial functionalities. Documetation of the work done till now | [#87](https://gitlab.com/cdli/framework/-/issues/87)  |
|5|  | Preparing Custom Controllers  | Preparing custom controllers for conversion, viewing of archival images |[#87](https://gitlab.com/cdli/framework/-/issues/87)   |
|6|  | Editing Current Templates | Editing current Artifact templates for adding a new tab to view Archival Image | [#87](https://gitlab.com/cdli/framework/-/issues/87)  |
|7|  | Using Archival Images  | Testing conversion algorithm on archival iamges to check whether the thumbnails are of required specifiction | [#586](https://gitlab.com/cdli/framework/-/issues/586) |
|8|  | Working for Non Associated Images & View Templates for Non Associated Images | Developing controllers, templates for accessing Non Associated Images. Creating view templates for viewing non associated archival images, documenting the work done till now. | [#608](https://gitlab.com/cdli/framework/-/issues/608) |
|9|  | Allowing Admins to Change type of Image | Developing the functionality to allow admins change the type of image. | [#87](https://gitlab.com/cdli/framework/-/issues/87) |
|10|  | Document, test and further feature addons | Documenting the work, working around the additionl Objectives. | - |