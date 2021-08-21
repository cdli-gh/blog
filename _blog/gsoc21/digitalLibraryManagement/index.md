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

**Mentor**: [Jacob L. Dahl](mailto:jacob.dahl@orinst.ox.ac.uk)

### GSoC Final Report & Summary.
Getting selected as a student developer at CDLI under Google Summer Of Code has been an absolute pleasure. These three months have been exciting, challeging and have been a great journey of learning new things that came through.

## What Was Done
During these three months I have completed all the essential objectives which includes

| \# | Objectives | PR/Commit/Link | Associated Deliverables | Status |
|----|-------------|----------------|---------|--------|
| 1 | Design Pages   | [Link](https://www.figma.com/file/jOKep53xdWK6YS6Xqtqoef/CDLI-GSoC-Design?node-id=0%3A1) | Design the pages for viewing archival images, selecting multiple artifacts at a time, upload archival images [#609](https://gitlab.com/cdli/framework/-/issues/609) | Completed  |
| 2 | Prepare Images Table  |  [Link](https://gitlab.com/cdli/framework/-/issues/87#note_602032029)  | Storing information regarding images in our table  [#87](https://gitlab.com/cdli/framework/-/issues/87) |Completed |
| 3  |  Work Around Web Images   |  [!355](https://gitlab.com/cdli/framework/-/merge_requests/355), [!377](https://gitlab.com/cdli/framework/-/merge_requests/377/)  | Allowing the admins to work around the web images by giving them the option to add, edit, delete  [#87](https://gitlab.com/cdli/framework/-/issues/87) |Completed   |
| 4  |  Python Script | --  |  A python script to extarct information and dump them in CSV. [#87](https://gitlab.com/cdli/framework/-/issues/87) | Completed |
| 5  | Testing Functionalities | -- | Testing fucntionalities of the web images. | Completed |

## What Is Left
Dealing with arcival images is the task which is now on my to-do list. We have to work around the conversion algorithm which can help us in displaying the images to admin on the framework and then allow them to make changes on it. 

### Objectives and Deliverables

:heavy_check_mark: --> Completed Tasks
:white_check_mark: --> Ongoing Tasks

| \# | Status  | Objectives                    | Associated Deliverables         | issue(s) |
| --- | --- | ----------------------------- | ---------------------------------------------- | -------- |
| 1 | :heavy_check_mark: | Design Pages | Design the pages for viewing archival images, selecting multiple artifacts at a time, upload archival images | [#609](https://gitlab.com/cdli/framework/-/issues/609) |
| 2 | :heavy_check_mark: | Prepare Image Table | Storing information regarding images in our table | [#87](https://gitlab.com/cdli/framework/-/issues/87) |
| 3 | :heavy_check_mark: | Work Around Web Images | Allowing the admins to work around the web images by giving them the option to add, edit, delete | [#87](https://gitlab.com/cdli/framework/-/issues/87) |
| 4 | :heavy_check_mark: | Python Script to store details | A python script to extarct information and dump them in CSV. | [#87](https://gitlab.com/cdli/framework/-/issues/87) |
| 5 | :white_check_mark: | Dealing with Archival Images | Adding the functionality to convert, view and peform operations on  archival images. | [#87](https://gitlab.com/cdli/framework/-/issues/87) |  


### Additional Objectives

| \# | Objectives         | Associated Deliverables                                             | issue(s) |
| --- |------------------ | ------------------------------------------------------------------- | -------- |
| 1 | CMD Script  | CMD Script to upload archival images from web server to wasabi server. Script should handle adding, renaming files on wasabi and deleting. | - |


### Timeline  

| Week  | Status |Objectives | Deliverables | issue(s)
|---|---|---|---| --- |
|1| :heavy_check_mark: | Designing the Pages | Get reviews from mentors regarding the design of pages and formalize the workflow | [#609](https://gitlab.com/cdli/framework/-/issues/609) |
|2| :heavy_check_mark: | Preparing Image Table   | Raise an issue to get review regarding the image table, prepare a script to populate the tables intially | [#87](https://gitlab.com/cdli/framework/-/issues/87)  |
|3| :white_check_mark: | Installation of Conversion Algorithm | Installing the library and try to add them in nginx or cake container | [#87](https://gitlab.com/cdli/framework/-/issues/87)  |
|4| :heavy_check_mark: | Generating Standard Templates  | Preparing standard templates, controllers for providing intial functionalities. Documetation of the work done till now | [#87](https://gitlab.com/cdli/framework/-/issues/87)  |
|5| :heavy_check_mark: | Preparing Custom Controllers  | Preparing custom controllers for conversion, viewing of archival images |[#87](https://gitlab.com/cdli/framework/-/issues/87)   |
|6| :heavy_check_mark:| Editing Current Templates | Editing current Artifact templates for adding a new tab to view Archival Image | [#87](https://gitlab.com/cdli/framework/-/issues/87)  |
|7| :white_check_mark: | Using Archival Images  | Testing conversion algorithm on archival iamges to check whether the thumbnails are of required specifiction | [#586](https://gitlab.com/cdli/framework/-/issues/586) |
|8| :white_check_mark: | Working for Non Associated Images & View Templates for Non Associated Images | Developing controllers, templates for accessing Non Associated Images. Creating view templates for viewing non associated archival images, documenting the work done till now. | [#608](https://gitlab.com/cdli/framework/-/issues/608) |
|9| :heavy_check_mark: | Allowing Admins to Change type of Image | Developing the functionality to allow admins change the type of image. | [#87](https://gitlab.com/cdli/framework/-/issues/87) |
|10| :heavy_check_mark: | Document, test and further feature addons | Documenting the work, working around the additionl Objectives. | - |