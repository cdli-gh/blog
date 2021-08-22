---
layout: page
title: Second Evaluation
author: "Apoorva Agarwal"
tags: ["eval","gsoc","gsoc2021","journalsOpenReviewWorkflowAndIntegration","eval#2"]
---

## Summary

I've successfully finished my milestones and all its deliverables . The following tasks were accomplished by me : 
- Developed single article web view with review page to display reviewers endorsements
- Created ojs database connection in cdli framework and created relations between ojs models to extract submissions from ojs.
- Created hourly command script to move submissions from ojs to cdli once they are reviewed and populates cdli database.
Now, an article can be submitted for open review and be managed by editors in ojs dashboard and once they are reviewed, admins can publish them on cdli journals dashboard and 

## Objectives and Deliverables

| \# | Objectives                    | Associated Deliverables         | Status |
| --- | ----------------------------- | ---------------------------------------------- | --- |
| 1 | Ojs Database Connection | Setup Ojs Database Connection and create relations between ojs models | :heavy_check_mark: |
| 2 | Write command script to move ojs submissions to cdli | Command script that will run hourly and move reviewed ojs submissions to cdli database | :heavy_check_mark: |
| 3 | Designing single article view | Remove header from latex convertor and design single article web view page |  :heavy_check_mark: |
| 4 | Displaying reviewers endorsements | Develop review page to display reviewers endorsements on article web page | :heavy_check_mark |

## Learning and Success

Working on the project has been a great learning experience. My mentor has been very supportive and his inputs have been helpful in improving my work. The team meetings give a good overview of the overall progress of the projects. I like that there is always something new to learn. Few things which I learnt in phase 2 of GSoC are:

- Learnt many new scss techniques
- Leant some advanced functions of cakephp while creating command script and creating relations between ojs models
- Learnt time management
- Learnt how to access files from container and create function to download it

I successfully finished my GSoC and looking forward to contribute more to CDLI.


## Difficulties

Setting up ojs database connection and creating relations between models was most important part of this phase and while working on it I got stuck at various points. My mentor helped alot in this. 
Solving those problems was a good learning experience that helped me gain better understanding of relations between tables .

## Plan update

I will be working on creating documentation for the complete ojs workflow and publishing the submissions. Apart from this I will be working on my additional objectives like citations for articles, oAuth integration , ORCID integration and CI/CD pipelines. 
