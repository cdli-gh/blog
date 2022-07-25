---
layout: page
title: Towards a General-Purpose Entity-Bibliography Linking System
author: 'Circle Chen'
tags: ['project', 'gsoc', 'gsoc2022', 'towardsAGeneralPurposeEntityBibliographyLinkingSystem']
---


## Towards a General-Purpose Entity-Bibliography Linking System

Project Description 

### Objectives and Deliverables

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks

| \# | Status  | Objectives                    | Associated Deliverables         | issue(s) |
| --- | --- | ----------------------------- | ---------------------------------------------- | -------- |
| 1 |:heavy_check_mark:|  Adapt the old reference database system to the new one. | - Publication View Page should work <br/> - Elastic Search should work | [!1154](https://gitlab.com/cdli/framework/-/issues/1154) |
| 2 |:heavy_check_mark:| Clean the current bibliography data. | - Merge existing publication entries. | [!318]() |
| 3 |:white_check_mark:| Identify the reference relationships between our publications and our entities, and populate the database with new data | hello world | [!318]() |
| 4 |:white_check_mark:| Enable single publication file submission and suggestion for connecting new entities | hello world |[!318]() |


### Additional Objectives

| \# | Status  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1 | :white_check_mark: | Enable bulk-uploading submission.  | hello world |    [!318]()     |


### Tentative timeline

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks  :raised_hands: --> Work Demonstration

| Week  |Objectives | Deliverables |
|---|---|---|
|1| :heavy_check_mark: Adapt the old reference database system to the new one.  | :heavy_check_mark: Publication View Page should work <br/> :heavy_check_mark: Elastic Search should work|
|2| :heavy_check_mark: Adapt the old reference database system to the new one.  | |
|3| :heavy_check_mark: Testing whether refactoring is broken <br> :heavy_check_mark: Initial exploration of publications dataset to see hwo to clean  |  :heavy_check_mark: Test PR <br> :heavy_check_mark: Write existing ipynb notebooks on the data <br>  |
|4| :heavy_check_mark: Sent initial round of data cleaning to Adam for proofreading, refining script  | |
|5| :heavy_check_mark: Explore ML-based methods for reference parsing (it worked poorly). Wrote ``regex`` methods to match and sent to Emilie to proofread exact_reference  | |
|6| :heavy_check_mark: Modified script to account for Bibtex Key updates. :heavy_check_mark: Prefill merge exact_ref in merge page. [!997](https://gitlab.com/cdli/framework/-/issues/997) | |
