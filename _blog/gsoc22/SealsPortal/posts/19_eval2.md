---
layout: page
title: Eval 2
author: "Aditi Singh"
tags: ["eval","gsoc","gsoc2022","sealsPortal","eval#2"]
---

## Summary
The GSoC 2022 was a success for me, I almost met all the goals. I got to learn various tech stacks and got an opportunity to create a utility and portal, which is useful to several students and professors.

## Objectives and Deliverables
| \# | Objectives                    | Associated Deliverables         | Issue | Pull Request |
| --- | ----------------------------- | ---------------------------------------------- | ----------------- | ---------- |
| 1 | Adding image annotation viewer and integrating it with annotorious-open seadragon |Create the viewer page<br>- Generate tiles for deepzoom<br>- Integrate with annotorious-openseadragon|[#736](https://gitlab.com/cdli/framework/-/issues/736)<br>[#1288](https://gitlab.com/cdli/framework/-/issues/1288)| [Viewer page branch](https://gitlab.com/cdli/framework/-/tree/phoenix/feature/viewerpage) | :heavy_check_mark: |
| 2 | Implement a convertor from coco format to w3c.json format |To Study more about w3c.json and COCO image annotations format<br>- Comparing both coco and w3c.json annotation formats to create SVG points layout<br>- Writing a python script that takes in coco_format and gives w3c.json format<br>- Add the convertor to the docker container.| [#1430](https://gitlab.com/cdli/framework/-/issues/1430) | [Standalone repository for conversion](https://github.com/cdli-gh/coco-convertor) |:heavy_check_mark: |

## Learning and Success
I have learned a lot of new tech stack, like working with docker containers, pipeline and web annotations. Also I got a chance to create a converter which can be used by any assyriology student or proffessor, or any user looking for converting from COCO to open annotations format. 

## Difficulties
The process of for integrating the pipeline into the docker container was a bit tricky, however Lars helped me with the process.

## Plan update
After GSoC, I plan to implement - 
1. Search in annotations
2. Create converter from [VGG](https://www.robots.ox.ac.uk/~vgg/software/via/) annotations to W3C.json annotations
3. Export of Calibration standards as a zip file
4. Adding a check for view annotations button

