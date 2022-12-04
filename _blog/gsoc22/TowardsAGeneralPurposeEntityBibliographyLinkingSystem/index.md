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
| 1 |:heavy_check_mark:|  Adapt the old reference database system to the new one. | - Publication View Page should work <br/> - Elastic Search should work | [#1154](https://gitlab.com/cdli/framework/-/issues/1154) and [!653](https://gitlab.com/cdli/framework/-/merge_requests/653); [#1244](https://gitlab.com/cdli/framework/-/issues/1244) and [!695](https://gitlab.com/cdli/framework/-/merge_requests/695)|
| 2 |:heavy_check_mark:| Clean the current bibliography data. | Data workflow as well as resulting data table. | [This repository](https://github.com/cdli-gh/publication-merging) |
| 3 |:heavy_check_mark:| Identify the reference relationships between our publications and our entities, and populate the database with new data | Data workflow as well as resulting data table. | 1. [.ipynb for finding provenience-pub relationships](https://github.com/cdli-gh/publication-merging/blob/main/pdf/read_pdf.ipynb) <br/> 2. [Resulting CSV](https://github.com/cdli-gh/publication-merging/blob/main/pdf/publication_proveniences.csv) |
| 4 |:heavy_check_mark:| Enable single publication file submission and suggestion for connecting new entities | hello world |[#1270](https://gitlab.com/cdli/framework/-/issues/1270) and [!710](https://gitlab.com/cdli/framework/-/merge_requests/710) |


### Additional Objectives

| \# | Status  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1 | :white_check_mark: | Enable bulk-uploading submission.  | New interface on websites |    Not yet done     |
| 2 | :heavy_check_mark: | Miscellaneous issue fixing.  | Numerous functional improvements and patching |    Issues: [#997](https://gitlab.com/cdli/framework/-/issues/997) [#1053](https://gitlab.com/cdli/framework/-/issues/1053) [#1127](https://gitlab.com/cdli/framework/-/issues/1127)     |


### Tentative timeline

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks  :raised_hands: --> Work Demonstration

| Week  |Objectives | Deliverables |
|---|---|---|
|1| :heavy_check_mark: Adapt the old reference database system to the new one.  | :heavy_check_mark: Publication View Page should work <br/> :heavy_check_mark: Elastic Search should work|
|2| :heavy_check_mark: Adapt the old reference database system to the new one.  | |
|3| :heavy_check_mark: Testing whether refactoring is broken <br> :heavy_check_mark: Initial exploration of publications dataset to see hwo to clean  |  :heavy_check_mark: Test PR <br> :heavy_check_mark: Write existing ipynb notebooks on the data <br>  |
|4| :heavy_check_mark: Sent initial round of data cleaning to Adam for proofreading, refining script  | |
|5| :heavy_check_mark: Explore ML-based methods for reference parsing (it worked poorly). Wrote ``regex`` methods to match and sent to Emilie to proofread exact_reference  | |
|6| :heavy_check_mark: Modified script to account for Bibtex Key updates. :heavy_check_mark: Prefill merge exact_ref in merge page.  | [!997](https://gitlab.com/cdli/framework/-/issues/997) |
|7| :heavy_check_mark: Attempt to use machine learning based methods to do pdf mining and find publication-provenience relationships. | |
|8| :heavy_check_mark: Switched to pattern-matching based to do pdf mining. | |
|9| :heavy_check_mark: Finished pdf mining with pattern-matching and generated preliminary publication-proveniences connection dataset on Github. | 1. [.ipynb for finding provenience-pub relationships](https://github.com/cdli-gh/publication-merging/blob/main/pdf/read_pdf.ipynb) <br/> 2. [Resulting CSV](https://github.com/cdli-gh/publication-merging/blob/main/pdf/publication_proveniences.csv) |
|10| :heavy_check_mark: Exploring how to incorporate node-js and python to run single publication file parsing script.  | |
|11| :heavy_check_mark: Finalization of node-js and python scripts to run the single pub file parsing. Trying to code cakePHP to read from resulting csv file. | |
|12| :heavy_check_mark: Buffer week, clean up new converted dataset and fix some issues that just popped up. | |
