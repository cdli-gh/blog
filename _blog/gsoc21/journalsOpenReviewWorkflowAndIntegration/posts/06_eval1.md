---
layout: page
title: First Evaluation
author: "Apoorva Agarwal"
tags: ["eval","gsoc","gsoc2021","journalsOpenReviewWorkflowAndIntegration","eval#1"]
---

## Summary

I've successfully finished my milestone-1 . I've created docker container for ojs submodule and have changed ojs configuration file and created volume for ojs database to keep the changes persistent in different systems. 
Now, an article can be submitted for open review and be managed by editors in ojs dashboard.
I've successfully modified journals index to integrate direct links to ojs dashboard and created the ui for filter button.
I did work on some of the additional issues as well like <a href="https://gitlab.com/cdli/framework/-/issues/481">#650</a>, <a href="https://gitlab.com/cdli/framework/-/issues/291">#291</a>, <a href="https://gitlab.com/cdli/framework/-/issues/481">#623</a>, <a href="https://gitlab.com/cdli/framework/-/issues/481">#415</a>


## Objectives and Deliverables

| \# | Objectives                    | Associated Deliverables         | Status |
| --- | ----------------------------- | ---------------------------------------------- | --- |
| 1 | Integrating ojs Docker Container in the framework | Creating a docker container for ojs submodule | :heavy_check_mark: |
| 2 | Ojs workflow for submission and review of articles |  Creating a workflow for open submission and open review of articles| :man_technologist: |
| 3 | Develop the journals index for integrating ojs | Updating CDLI journals index to create a link between CDLI journals dashboard and ojs dashboard | :heavy_check_mark: |
| 4| Documentation | Wrote Readme file for deploying ojs and running ojs container | :heavy_check_mark: |

## Learning and Success

Working on the project has been a great learning experience. My mentor has been very supportive and his inputs have been helpful in improving my work. The team meetings give a good overview of the overall progress of the projects. I like that there is always something new to learn. Few things which I learnt in phase 1 are:

- Learnt many new docker commands
- Learnt to debug docker related errors
- Learnt to work with scss 
- Got more confident with cakephp and mySQL
- Got more confident with git and pipeline

I successfully finished my phase 1 and looking forward to work on further tasks.

## Difficulties

Creating docker container is the most important part of the project, and while working on it I got stuck at various points dealing with some errors. Since I was not experienced with docker, it becomes quite tricky to debug all those errors. My mentor helped alot in this.
Solving those problems was a good learning experience that helped me gain better understanding of the docker.

## Plan update

There were few changes made in the milestone. Thus, I will start working on 
- API integration for details of a reviewed article
- Design single article web view and display reviewers endorsements 
I will even work on additional objectives like oAuth integration , ORCID integration and CI/CD pipelines. 
