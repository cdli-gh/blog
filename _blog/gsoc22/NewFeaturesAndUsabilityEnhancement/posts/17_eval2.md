---
layout: page
title: Eval 2
author: "Shivoham Angal"
tags: ["eval","gsoc","gsoc2022","newFeaturesAndUsabilityEnhancement","eval#2"]
---

## Summary
The second phase of my GSoc journey was a very great learning experience and of course it had its own challenges. I had never thought I would create such code which will be used by people in their daily lives. The last week was the most stressful as I was constantly worried about the bulk update not working.

## Objectives and Deliverables
| \# | Objectives                    | Associated Deliverables         |
| --- | ----------------------------- | ---------------------------------------------- |
| 1 | Implementing Features for Retired Artifacts | Modifed tables in the database, created index page and added a retired artifact section to artifact edit form |
| 2 | Export Data on Entities Indexes  | Created a drop-down element for export, modified model files of entities to include the `getTableRow()` and `getCidocCrm()` functions, implemented a view for txt files |
| 3 | Bulk Update on interface  | Created bulk update button and modal to choose fields, created controller and index page for the bulk update with a master form in the index page. Also modified the ArtifactUpdates controller to check if data is coming from BulkUpdate form and process it.|
| 4 | Export Bibliography from Publications Pages  | Modified and reused the entity export drop-down element and added constraints on the export based on number of results |

## Learning and Success
- Learned how exports for different categories of formats work and implemented them.
- Learned to change an element dynamically according to conditions while modifying the export drop-down for publications export.
- Learned to manipulate data from one form to another while implementing the modal and forms for the BulkUpdate functionality.

## Difficulties
- It was a bit challenging to change the publications drop-down according to the number of search results.
- I had some difficulties when working on the bulk update master form because it had data of different types and I had to modify this data to suit the input for the existing artifact update functionality.

## Plan update
- Brush up any problems the bulk update functionality may have.

