---
layout: page
title: 3D Viewer Integration
author: 'Mustafa Dhar'
tags: ['project', 'gsoc', 'gsoc2021', '3dViewerIntegration']
---

## 3D Viewer Integration

This project is to load 3D Models in PLY format from the CDLI database into the existing 3D Model Web Viewer using the Three.js library and to integrate it into the CDLI framework. 

To Enhance the 3D Viewer user experience by adding responsiveness, physical torque and friction, and other effects while interacting with the 3D Model in the 3D Viewer.

Implementing an RTI Viewer so that any CDLI tablet for which the PLY model is available has an easy-to-navigate option for the 3D viewer for that model in 3D viewer.  

Work Status: [Link](https://drive.google.com/drive/folders/1zx4uBOB8_9TkFnr3Hd5K0ckeTNb0gwj8)

### Objectives and Deliverables

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks

| \# | Status  | Objectives                    | Associated Deliverables         | issue(s) |
| --- | --- | ----------------------------- | ---------------------------------------------- | -------- |
| 1 |:heavy_check_mark:|  3D Viewer in cake-php | Convert 3D Viewer to cake-php. | [!318](https://gitlab.com/cdli/framework/-/merge_requests/318) |
| 2 |:heavy_check_mark:|  Load 3D Model(.PLY) | Loading 3D Model in .PLY format from CDLI database. | [!318](https://gitlab.com/cdli/framework/-/merge_requests/318) |
| 3 |:heavy_check_mark:|  Responsiveness | 3D Viewer should be responsive to all devices with their associated 3D Models. | [!318](https://gitlab.com/cdli/framework/-/merge_requests/318) |
| 4 |:white_check_mark:|  User Experience(UX) | Suggesting and implementing user experience(UX) of 3D Viewer. | - |


### Additional Objectives

| \# | Status  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1 | :heavy_check_mark: | Easy Navigation  | User should easily navigate to 3D Viewer for the particular model. |    [!318](https://gitlab.com/cdli/framework/-/merge_requests/318)     |
| 2 | :heavy_check_mark: | Documentaion for 3Dviewer development | It should be easy for getting started with the development of 3DViewer by going through its documentation. |    [!350](https://gitlab.com/cdli/framework/-/merge_requests/350)     |


### Tentative timeline

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks  :raised_hands: --> Work Demonstration

| Week  |Objectives | Deliverables |
|---|---|---|
|1| :heavy_check_mark: Make basic 3D Viewer  |  :heavy_check_mark: Convert 3D Viewer files to CakePHP. <br> :heavy_check_mark: Make URL controller for 3D Viewer in the framework. <br> :raised_hands: 3D Viewer should be up on framework with error in loading 3D models.|
|2| :heavy_check_mark: Basic 3D Viewer up  |  :heavy_check_mark: Setting up the routes for the 3D Viewer page in the framework. <br> :heavy_check_mark: Setting up parameterized routes to take ObjectID from URL and render model accordingly. <br> :raised_hands: 3D Viewer should be able to load 3D models from assets in the webroot. |
|3| :heavy_check_mark: Responsiveness   |  :heavy_check_mark: Make 3D viewer responsive to all devices. <br> :raised_hands: 3D viewer should be able to change its size according to viewport.  |
|4| :heavy_check_mark: Render 3D Model from database.  | :heavy_check_mark: Set up routes to get 3D Model (.PLY) from data from the CDLI database. <br> :heavy_check_mark: Load 3D Model(.PLY) in the 3D viewer and render it from the database. <br> :raised_hands: 3D Viewer should be able to load 3D models from cdli database. |
|5| :heavy_check_mark: Testing and Debugging   |  :heavy_check_mark: Check all the functionality added is working good and if any bug is present debug it. |
|6| :heavy_check_mark: UX Optimisation  |  :heavy_check_mark: Suggest and implement different features for 3D Viewer to enhance User Experience(UX) while interacting with 3D Model(CDLI tablet). |
|7| :heavy_check_mark: UX Optimisation  |  :heavy_check_mark: Suggest and implement different features for 3D Viewer to enhance User Experience(UX) while interacting with 3D Model(CDLI tablet). |
|8| :heavy_check_mark: UX Optimisation  |  :heavy_check_mark: Suggest and implement different features for 3D Viewer to enhance User Experience(UX) while interacting with 3D Model(CDLI tablet). |
|9| :heavy_check_mark: Usability enhancing   |  :heavy_check_mark: Search different usability aspects and implemnt it. |
|10| :white_check_mark: Test and Debug   |  :white_check_mark: Check all the functionality added is working good and if any bug is present debug it and complete documentation and launch. |




