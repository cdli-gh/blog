---
layout: page
title: Journals Open Review Workflow and Integration
author: 'Apoorva Agarwal'
tags: ['project', 'gsoc', 'gsoc2021', 'journalsOpenReviewWorkflowAndIntegration']
---

## Journal Open Review Workflow And Integration

Hola, I'm <a href="https://www.linkedin.com/in/apoorva-agarwal-8420ab1b3/">Apoorva Agarwal</a>, participating in Google Summer of Code 2021 with CDLI. I’ve been accepted for the project Journals Open Review Workflow and Integration. This project focuses on creating a functional pipeline which will consist of open submission and open review process before publishing articles in our CDLI journals dashboard. To implement  open journals in the system,  an appropriate workflow needs to be developed which is intended to be carried out using https://pkp.sfu.ca/ojs/ojs_download/ software. OJS(Open Journal System) is an open source solution to managing and publishing scholarly journals online. OJS is a highly flexible editor-operated journal management and publishing system. In addition to this, we intend to make further integration in the CDLI journals dashboard and display the endorsement of reviewers with published articles.

<i>Project:</i>
<a href="https://summerofcode.withgoogle.com/projects/#6225579101126656">GSoC'21</a>
<br>
<i>My GSoC'21 Proposal:</i>
<a href="https://docs.google.com/document/d/1Bq1Be4UYaF08vBwasERpx2kiWuiVPWdkSEHBM-owUx4/edit#heading=h.rti1bbjk8idf">Link</a>
<br>
<i>Contributions to CDLI:</i>
<a href="https://gitlab.com/cdli/framework/-/merge_requests?scope=all&utf8=%E2%9C%93&state=all&author_username=apoorva1509">Link<a>
<br>
<i>Work status:</i>
<a href="https://drive.google.com/drive/folders/15kmsiilnMfBEomd03VwUyAmDdcU-lmBV?usp=sharing">Link<a>
<br>

<b>Mentor: </b> <a href='mailto:nisheal.work@gmail.com'>Nisheal John</a>

### Objectives and Deliverables

:heavy_check_mark: --> Completed Tasks
:man_technologist: --> Ongoing Tasks

| \# | Status  | Objectives                    | Associated Deliverables         | issue(s) | PRs |
| --- | --- | ----------------------------- | ---------------------------------------------- | -------- | -------- | 
| 1 | :heavy_check_mark: | Integrating ojs Docker Container in the framework | Downloading ojs software and creating a docker container for it | <a href="https://gitlab.com/cdli/framework/-/issues/598">#598</a> | <a href="https://gitlab.com/cdli/framework/-/merge_requests/313">!313</a>, <a href="https://gitlab.com/cdli/framework/-/merge_requests/348">!348</a> |
| 2 | :heavy_check_mark:| Ojs workflow for submission and review of articles | Creating a workflow for open submission and open review of articles | <a href="https://gitlab.com/cdli/framework/-/issues/603">#603</a> | - |
| 3 | :heavy_check_mark:  |  Ojs Datbase Connection | Setting up OJS Database Connection and creating relations between models | <a href="https://gitlab.com/cdli/framework/-/issues/606">#606</a> | <a href="https://gitlab.com/cdli/framework/-/merge_requests/374">!374</a> |
| 4 |  :heavy_check_mark: | Connecting ojs module to the CDLI journals dashboard | Publishing the articles with the endorsement of the reviewers in CDLI journals dashboard | <a href="https://gitlab.com/cdli/framework/-/issues/599">#599</a>, <a href="https://gitlab.com/cdli/framework/-/issues/470">#470</a>, <a href="https://gitlab.com/cdli/framework/-/issues/606">#606</a>, <a href="https://gitlab.com/cdli/framework/-/issues/620">#620</a>, <a href="https://gitlab.com/cdli/framework/-/issues/659">#659</a> | <a href="https://gitlab.com/cdli/framework/-/merge_requests/374">!374</a>, <a href="https://gitlab.com/cdli/framework/-/merge_requests/368">!368</a>, <a href="https://gitlab.com/cdli/framework/-/merge_requests/326">!326</a> |

### Additional Objectives

| \# | Status  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1 | :man_technologist: | Citation Index and metrics | Citation index is to cite the articles. Display the statistics related to articles | <a href="https://gitlab.com/cdli/framework/-/issues/491">#491</a> |
| 2 | - | DOI, ORCHID, and PUBLONS integration | Integration of DOI, ORCHID and PUBLONS in our workflow | - |
| 3 | - | CI/CD pipeline | Setting up CI/CD with lint | - |

### Tentative timeline  

| Week  | Status | Objectives | Deliverables |
|---|---|---|---|
| 1 | :heavy_check_mark: | Integrating ojs Docker Container in the framework | Downloading ojs software and creating a docker container for it and integrating it in CDLI framework| 
| 2 | :heavy_check_mark: | Setting up Editorial Workflow( for cdlj and cdlb) | Creating a workflow for open submission and open review of articles |
| 3 | :heavy_check_mark: | Develop the journals index for integrating ojs | Updating CDLI journals index to create a link between CDLI journals dashboard and ojs dashboard | 
| 4 | :heavy_check_mark: | Final Testing of ojs container | Debug the errors in ojs container and final testing of ojs container and editorial workflow | 
| 5 | :heavy_check_mark: | Create document for ojs and solve additional issues | Create document for ojs and <a href="https://gitlab.com/cdli/framework/-/issues/575">#575</a>, <a href="https://gitlab.com/cdli/framework/-/issues/481">#481</a>, <a href="https://gitlab.com/cdli/framework/-/issues/291">#291</a> | 
| 6 | :heavy_check_mark: | OJS Database Connection | Sharing data between CDLI and ojs databases | 
| 7 | :heavy_check_mark: | Designing single article view | Remove header from latex convertor and design single article web view page |
| 8 | :heavy_check_mark: | Create ojs models connections for reviewers endorsements | Create relations between ojs models and displaying the endorsement of reviewers | 
| 9 | :heavy_check_mark: | Write command script to move ojs submissions to cdli | Command script that will run hourly and move reviewed ojs submissions to cdli database |
| 10 | :heavy_check_mark: | Complete leftover milestone and improvements | Completed the single article web view with reviewers endorsements, get it tested and finalized the PR. | 
| 11 | :heavy_check_mark: | Finishing the project | Testing the project and making release/production | 
  
