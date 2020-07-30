---
layout: page
title: img_pipeline Eval#2
author: "Aman"
tags: ["eval","gsoc","gsoc2020","img_pipeline","eval#2"]
---
 
## Summary
This month was spend to make integrations of python from the framework leveraging the task queue, in addition to that we created an algorithm to process lossy jpeg images of tablets these were again the composition of flatbed scans and HDR images. Unlike last time the algorithm performed and resolved the flatbed scans too with decent side edges. There are some misses with the algorithm due to shadow interferes and there is a fallback simpler algorithm which when in place would automatically boost the accuracy and create outputs that are valid
 
## Objectives and Deliverables
- Algorithm: This months algorithm is based on processing and it can be found up [here](https://digcuneiform.slack.com/archives/CV0HQJ1GQ/p1596082165000400)
- Framework: A basic task queue with conjunction to file service is set up, when passed correct parameters it automatically retrieve files and executes python functions from another container.
 
 
## Learning and Success
- Image Processing
- Computational Photography
- OpenCV
- OOPS
- Message Queue
- Redis
 
## Difficulties
- Unavailability of packages for both PHP and python for task queue forces us to implement everything manually which takes a toll on the robustness of the system.
- The jpeg images thus used loose quality when being converted in the format this usually makes the whole process harder but we somehow managed to even process them the accuracy does take a hit with this.
 
## Plan update
- With a good enough algorithm on our side, we seem to be confident enough to be doing good work in that department but on the other side the framework development is stalled and should be started as soon as possible.

