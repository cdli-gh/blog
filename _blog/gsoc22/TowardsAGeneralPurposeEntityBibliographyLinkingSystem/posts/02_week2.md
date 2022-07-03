---
layout: page
title: Week 2
author: 'Circle Chen'
tags: ["week","gsoc","gsoc2022","towardsAGeneralPurposeEntityBibliographyLinkingSystem","week#2","eval#1"]
---

## Week Summary

The focus of this week will be to continue adapting the old referencing system to the new one, as well as starting running the publication entry merging script.

Update: Now there is currently a list of files that should be completed in order for the script to be adapted. -> means the old file should be removed and changed to the new one:

- Controllers
    - Controller\Admin\ArtifactsPublicationsController.php -> EntitiesPublicationsController.php 
    - Controller\Admin\PublicationsController.php 
    - Controller\Component\BulkUploadComponent.php
- Model
    - Model\Table\ArtifactsPublicationsTable.php -> EntitiesPublicationsTable.php
- View
    - templates\Admin\ArtifactsPublications\add.php 
    - templates\Admin\ArtifactsPublications\index.php 
    - templates\Admin\Home\dashboard.php 
    - templates\Pages\api.php 
    - templates\Publications\view.php 
- Test (framework\app\cake\tests) 
    - Fixture\ArtifactsPublicationsFixture.php
    - TestCase\Controller\ArtifactsPublicationsControllerTest.php
    - TestCase\Controller\PublicationsControllerTest.php
    - TestCase\Model\Table\ArtifactsPublicationsTableTest.php

All of these files now have been modified. We'll now move on to testing.


The new ``entities_publications`` table is created by copying the content + structure from the ``artifacts_publications``, adding a field called ``table_name``, and setting it to "artifacts" for all rows.


TODO 2: Run the python script on the actual data to see what can be done.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2022/06/20	| Successfully adapted the entities_publications code to the logstash JDBC statements, and indexing for entities_publications worked.  |  
|2   	| Tuesday  	|   2022/06/21	| Identified admin files to be modified	|  
|3   	| Wednesday |  2022/06/22 	| Updated controller files and model files, view files in progress |  
|4   	| Thursday  |   2022/06/23	| Finished modifying PHP files, starting to test the website|  
|5   	| Friday  	|   2022/06/24	| Tested most of the code files for the admin dashboard |  
|6   	| Saturday  |  2022/06/25	| Took a break for weekend |  
|7   	| Sunday  	|   2022/06/26	| Took a break for weekend |  
