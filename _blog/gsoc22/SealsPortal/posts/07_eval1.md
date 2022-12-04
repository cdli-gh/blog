---
layout: page
title: Eval 1
author: "Aditi Singh"
tags: ["eval","gsoc","gsoc2022","sealsPortal","eval#1"]
---

## Summary
The first evaluation was triumphant, and I have implemented all associated deliverables successfully.

### Objectives and Deliverables
Completed tasks -> :heavy_check_mark: <br> Ongoing task -> :white_check_mark:

| \# | Objectives                    | Associated Deliverables         | issue(s) | Pull Requests |    Status | 
| --- | ----------------------------- | -------------------------------------------- | -------| -------- | ---- |
| 1 |  Implement required changes to the database and edit the model files accordingly| Setting up the image_annotations table <br>- Creating respective model files <br>- Bulk update of image_annotations table | [#1336](https://gitlab.com/cdli/framework/-/issues/1136) | [!649](https://gitlab.com/cdli/framework/-/merge_requests/649) |:heavy_check_mark:|
| 2 | The seals portal | - Displaying Best Attested Composite seals with image and description.<br>- Create a table and respective model files for best_attested_seals <br>- Tabular representation of seals, categorized by period.<br>- Displaying and grouping seals categories: Physical Seals, Composite Seals, Sealings, All CDLI seals|[#700](https://gitlab.com/cdli/framework/-/issues/700)<br> [#1227](https://gitlab.com/cdli/framework/-/issues/1227)<br>[#1241](https://gitlab.com/cdli/framework/-/issues/1241)|[!661](https://gitlab.com/cdli/framework/-/merge_requests/661)<br>[!700](https://gitlab.com/cdli/framework/-/merge_requests/700)<br>[!737](https://gitlab.com/cdli/framework/-/merge_requests/737)|:heavy_check_mark: |
| 3 | Implementing seals single view | Implementation of a PHP library for graphical representation of chemical information of seals.<br>- A feature to view only top n elements (based on weight)<br>A switch to convert the graph into a table view. <br> - Graphical visualisation of element weight in that seal in the form of line chart and bar graph | [#1332](https://gitlab.com/cdli/framework/-/issues/1132)<br>| [!687](https://gitlab.com/cdli/framework/-/merge_requests/687)<br>[!707](https://gitlab.com/cdli/framework/-/merge_requests/707) | :heavy_check_mark: |

## Learning and Success
I learned to create complex sql queries in CakePHP, got even more familiar with CDLI search, and got used to code efficiently and produce less redundant code.
I successfully completed the seal portal and the seal's single view.

## Difficulties
I was able to almost complete all the deliverables smoothly, except I got stuck with the graphical representation for seal chemistry, but with some research I was able to tackle that issue!.

## Plan update
I will be planning to implement the following tasks ahead - 
1. Creating Well Attested seals add and edit forms 
2. Creating add edit forms for seal chemistry.
3. Creating add edit forms for seal chemistry standards.
4. Export of chemical data as CSV

