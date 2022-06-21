---
layout: page
title: Seals Portal
author: 'Aditi Singh'
tags: ['project', 'gsoc', 'gsoc2022', 'sealsPortal']
---


## Seals Portal

The seals portal aims at displaying all of the resources in the CDLI concerning a seal, aggregated in one place, with important features like viewing image annotations and graphical representation of seals chemistry. The objectives of the project are: Creating the seals portal which lists different CDLI seals as groups i.e. physical, composite, sealings, and all cdli seals for a better user experience. It shows a list of best-attested composite seals along with an image and description. It presents a table containing seals and impressed tablets by period, here the users can view seals grouped by period (name and duration). The seals' single view will display the seal image, a graphical way to present seals' chemical information; this graph can be viewed in a bar chart, pie chart, line chart and can be converted to tabular format. The seals’ single view includes accordions to display physical information, inscription, identifiers, provenience, Composites, Inscriptions, and Chemical information. It also displays Image annotations. This project will also have a standalone converter tool for converting annotations from COCO format to w3c.json format. There will be a bulk update interface to upload annotations to the database the user can upload the annotations in w3c.json or COCO format. 

### Objectives and Deliverables

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks

| \# | Status  | Objectives                    | Associated Deliverables         | issue(s) |
| --- | --- | ----------------------------- | ---------------------------------------------- | -------- |
| 1 |:white_check_mark:|  Implement required changes to the database and edit the model files accordingly | - | [#1136](https://gitlab.com/cdli/framework/-/issues/1136) |
| 2 |:white_check_mark:|  The seals portal | - | [#700](https://gitlab.com/cdli/framework/-/issues/700) |
| 3 |:white_check_mark:|  Implementing seals single view | - | [#1132](https://gitlab.com/cdli/framework/-/issues/1132) |
| 4 |:white_check_mark:|  Adding image annotation viewer and integrating it with annotorious -open seadragon | Integrating GD extension | [#736](https://gitlab.com/cdli/framework/-/issues/736) |
| 5 |:white_check_mark:|  Implement a convertor from coco format to w3c.json format | - | [#318]() |




### Tentative timeline

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks  :raised_hands: --> Work Demonstration

| Week  |Objectives | Deliverables |
|---|---|---|
|1| Implement required changes to the database and edit the model files accordingly | - Setting up the image_annotations table <br> - Creating respective model files<br> - Bulk update of image_annotations table<br> - Adding chemical composition of seals|
|2| Testing the image_annotations table with SQL commands  |  |
|3|  The seals portal | - Displaying Best Attested Composite seals with image  sand description.<br> - Displaying and grouping seals categories: Physical Seals, Composite Seals, Sealings, All CDLI seals |
|4|  The seals portal |  - Create a table and respective model files for best_attested_seals <br> - Tabular representation of seals, categorized by period.|
|5|  Testing the seals portal | Implementing changes suggested by mentors |
|6| Implementing seals single view | - Making basic layout of seal single view page (Images, summary, accordions)  |
|7| Implementing seals single view | -Implementation of a PHP library for graphical representation of chemical information of seals. <br> A feature to view only top n elements(based on weight)<br> A switch to convert the graph into a table view.|
|8| Implementing seals single view | Graphical visualisation of element weight in that seal in the form of pie chart, line chart, and bar graph |
|9| Testing seals single view| Implementing changes suggested by mentors |
|10| Adding image annotation viewer and integrating it with annotorious -open seadragon | - Create the viewer page <br> - Generate tiles for deepzoom |
|11| Adding image annotation viewer and integrating it with annotorious -open seadragon| - Integrate with annotorious-openseadragon |
|12| Testing annotation viewer | Implementing changes suggested by mentors |
|13| Implement a convertor from coco format to w3c.json format | - To Study more about w3c.json and COCO image annotations format<br> - Comparing both coco and w3c.json annotation formats to create SVG points layout<br> - Writing a python script that takes in coco_format and gives w3c.json format<br> - Add the convertor to the docker container.|
|14| Testing COCO convertor| Implementing changes suggested by mentors |
