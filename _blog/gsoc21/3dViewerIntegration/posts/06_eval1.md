---
layout: page
title: First Evaluation
author: "Mustafa Dhar"
tags: ["eval","gsoc","gsoc2021","3dViewerIntegration","eval#1"]
---

## Summary
The first phase of GSoC was quite a busy one. The main focus of this phase was to get 3D Viewer on CDLI framework as soon as possible for that :

:octocat: 3D Viewer code was first converted to Cakephp and framework friendly.

:octocat: To load 3D Model of `.ply` format and its texture in `.jpg` format all 3D Data was stored in assets of webroot.

:octocat: Now it was time to make 3D Viewer responsive to mobile devices and that was done with 3rd week of GSoC'21.

:octocat: After responsiveness it needs to render 3D Model from Database and the same was implemented by changing the 3D Data path to `vcmodels` of `dl`.

:octocat: Just one week before first evaluation 3D Viewer URL was formalised according to MVC conventions. 


## Objectives and Deliverables
| \# | Objectives                    | Associated Deliverables         |
| --- | ----------------------------- | ---------------------------------------------- |
| 1 | 3D Viewer in cake-php  | Convert 3D Viewer to cake-php. |
| 2 | Load 3D Model(.PLY) | Loading 3D Model in .PLY format from CDLI database. |
| 3 | Responsiveness | 3D Viewer should be responsive to all devices with their associated 3D Models. |
| 4 | Easy Navigation | User should easily navigate to 3D Viewer for the particular model. |


## Learning and Success
With me first time contributing to CDLI codebase, there is always a challenge with every step for me and each and every challenge has got me something new to learn, starting with git command itself to getting the first PR merged learned the following things in 1st evaluation:

>Git branching

>Cakephp

>SCSS

>threejs

This all learning, made me able to deliver my committed objectives on time.  


## Difficulties
As there was a challenge/issue on each step of integration, It was again a challenge to be with the timeline of the project here I face some difficulties but I overcame it with increasing time on coding.

The second challenge I faced was to make 3D Viewer responsive to all screen sizes as 3Dmodel needs to be rendered according to the viewport.

## Plan update
Considering Phase-1 objectives and deliverables, I was able to accomplish 60% of total deliverables and the remaining 40% will be completed before the 2nd evaluation period.

For the next phase schedule, I will discuss it with my mentor and then start to work from next week onwards.
