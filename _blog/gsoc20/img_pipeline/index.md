---
layout: page
title: img_pipeline
author: 'Aman'
tags: ['project', 'gsoc', 'gsoc2020', 'img_pipeline', 'eval#1', 'week#2']
---

## Image Processing Pipeline

CDLI Framework helps the author's to write and process tablet's from a simple web interface, in the current situation the user's have to manually process image's and convert into fatcrosses this leads to inconsistency and requires human effort's. To simplify this situation this summer under the guidance of Mr. Jacob Dahl, we would work on moving this manual task to process automatically with the image pipeline.

### Objectives and Deliverables

The goals of this project are as follows :
1. Image Processing Library: A custom made library using OpenCV and other image processing libraries that pipelines the whole task with simple function call's and can be customized with configs.
2. Image Processing Pipeline: Leveraging the library an scalable pipeline which processes all the image's. This pipeline would be easily integrated with the framework.
3. Frontend Implementation: After the pipeline in place we have to make it accessible via the framework itself, this would finally complete the implementation of the system.
4. Local Standalone Image Processing Tool | EXTENDED | : This would further add capability to process images based on the library offline on user's local machine. 


#### Essential Objectives

| \#  | Objectives | Associated Deliverables | issue(s) |
| --- | ---------- | ----------------------- | -------- |
| 1   | Basic Async Setup for processing | Boilerplate task processing from the framework. | Creating Architecture for the processing. |
| 2   | Perfecting Methods and Algorithm's for favorable results. | Set of images before and after processing. | Finding and manipulating variables for the best images. |
| 3   | Integrating library with Async Setup | Basic image processing from PHP to images. | Implementing async tasks with PHP. |
| 4   | Frontend Development | A UI for user to interact and processing files. | Following the consistent design theme and a good UI. |
| 5   | Documentation | Writeup about the pipeline, instructions to add more steps with ease. | Create a user-friendly documentation. |


#### Additional Objectives

| \#  | Objectives | Associated Deliverables | issue(s) |
| --- | ---------- | ----------------------- | -------- |
| 1   | Offline Image Processing Tool | An platform agnostic tool that allows user to process images from their machines. | Writing a standalone tool in a different stack. |
| 2   | Moving storage and processing of images from a storage interface rather than directly from mount's. | Deploying the file storage system's in the framework. | Flexible storage services. |

### Tentative timeline

| Week | Objectives | Deliverables |
| ---- | ---------- | ------------ |
| 1 -2   | Completing algorithm's and finalizing image output's | A set of algorithm's that processes the image in a desired manner. |
| 3    | Implementing Programs with image processing library. | Final Library for processing image. |
| 4    | Managing storage of images. | API's to upload images. |
| 5    | Loggging and manipulating tags of image. | A proper image upload setup with persistence. |
| 6    | Implementing Async Setup from PHP. | A sample task processing system with PHP. |
| 7-8    | Integration of the Libraries as Tasks. | A basic image processing system. |
| 9-10    | Implementing Frontend | UI for processing these tasks. |
| 11    | Adding batch processing utilities to framework. | Capability to edit and process set of images from framework. |
| 12    | Documentation and kick off of stretch goals | Documentation of the system, guide on how to extend processing capabilities. |
