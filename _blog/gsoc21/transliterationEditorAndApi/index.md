---
layout: page
title: Transliterations editor and API
author: 'Vishv Kakadiya'
tags: ['project', 'gsoc', 'gsoc2021', 'transliterationsEditorAndAPI']
---

## Transliterations editor and API

JTF is a new JSON-based format for transliterations that aims to make cuneiform textual data easily accessible for processing and modifications. It comes with a NodeJS API, jtf-lib,to provide an ATF format parser and converter, a CRUD interface and a module for sign list operations, jtf-signlist. A React web application, uqnu, is being developed to import transliterations from files, validate, edit, export etc.

The task is to integrate this infrastructure into CDLI's framework and allow crowdsourcing and individual work on texts.
 
### Objectives and Deliverables

:heavy_check_mark: --> Completed Tasks
:white_check_mark: --> Ongoing Tasks

| \# | Status  | Objectives                    | Associated Deliverables         | issue(s) |
| --- | --- | ----------------------------- | ---------------------------------------------- | -------- |
| 1 |:heavy_check_mark:|  Framework integration | Integrate JTF API and web application run in a framework docker container. | [#604](https://gitlab.com/cdli/framework/-/issues/604) [#605](https://gitlab.com/cdli/framework/-/issues/605) |
| 2 |:heavy_check_mark:|  Accessibility  | Make web application accessible via a framework URL. | [#629](https://gitlab.com/cdli/framework/-/issues/629) |
| 3 |:white_check_mark: |  Database Operations  | Storing JTF data into CDLI Database. | - |
| 4 ||  Version Control  | Implement version control system that efficiently stores changes to transliterations. | - |
| 5 |:heavy_check_mark:|  JTF-LIB Integration  | JTF API integration with the framework's public API & JTF output function in the API. | [!357](https://gitlab.com/cdli/framework/-/merge_requests/357) |


### Additional Objectives

| \# | Status  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1 |  | CDLI Crowdsourcing functions  | Users should add / modify transliterations data and send them for approval directly from the application. |  -  |

### Tentative timeline  

| Week  |Objectives | Deliverables |
|---|---|---|
|1| Implement Docker Conatiner for uqnu |  Makes the web app up and running inside a container. |
|2| Integrate web app in framework | Enable service that communicates between newly added and already existed containers.  |
|3| Database operations for JTF-data  | Make routes(Endpoint)  and controllers in CDLI backend to communicate with the service and Store JTF data in the Database along with the author and timestamp|
|4| Version Control  | Integrating the git actions which can eventually enable version control. |
|5| Storing and Retriving JTF-data  | Implementing the mechanism for the system that stores the data when changes occur to transliterations.  |
|6| Tests and Fallback Plan  | Manually test the work has been done so far and write a few unit tests for this and tests for services which have been made so far and Trying a different approach if the git server won’t work as I have planned. |
|7| Integrate version control in framework  | Integrating Version control  System with the CDLI interface.|
|8| Communication between web app and API    | Implement a Service which can communicate to both the docker container. |
|9| Data Accessibility  | Working on a Controller to store JTF data and make it accessible. |
|10| Document, test add further features addons | Prepare the whole Documentation of the work I have done so far.Start working on bonus tasks, if time permits. and Create a service layer in the framework that can get requests and enable admins to approve the request. So modification of transliterations data can be done.  |


