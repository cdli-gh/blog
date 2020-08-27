---
layout: page
title: img_pipeline Eval#3
author: "Aman"
tags: ["eval","gsoc","gsoc2020","img_pipeline","eval#3"]
---
 
## Summary
This week went by making an archival algorithm, this algorithm stitches all the six sides of the artifacts. This is achieved by three main steps :
 
* Cropping
* Padding
* Stiching
 
#### Cropping :
This part includes using the image which was processed by our earlier algorithm, a box is created around the artifact with min area.
- Challenge:
 - The challenge of cropping the rectangular box was extremely tough and mathematical. There were some references on opencv but they were quite complex and required deep knowledge of trigonometry.
 - With the help of internet and reading some articles the algorithm is able to capture the artifact but it cannot keep the orientation intact and snaps to the lowermost angle possible
 - This unnecessary snapping is the reason that we need to provide rotation inputs from the user as the algorithm failed to do so.
 #### Padding :
This part includes adding some black color space around the crop so that there is some separation between the images.
- Challenge:
 - Dynamic Padding : It's quite easy to make a padding of a set parameter lets say every image have a padding of 1 inch but becomes inefficient when images changes shape lets say the image was of 1/2 inch adding 1 inch in padding makes it useless.
 - Automatic Padding based on Percentage : This absolute nature of padding can be ruled if we start using the parameters of the image. So if the image is 1/2 inch, we can ask for a 10 percent padding which would make sure the extra space added be small all the time
 
#### Stiching :
This part was probably the most challenging and analytical apart from the other two steps. This step makes sure that all the images we process get converted into a single image.
- Challenge:
 - Maths : The problem while appending all the images is most of the api from opencv gives quite in-detail mathematical outputs which are harder to interpret and work on.
 - Resizing images : This corresponds to resizing of the images, which is not properly supported by OpenCV
 
 
 
## Objectives and Deliverables
The archival algorithm would let the users to generate archival from a single object instance in python, on the algorithm layer it's divided into two parts. First, the image is processed and then the archival algorithm deals with cutting the image and tiling them in place.
 
 Not just that this also allows user to overwrite a single image directly which would let it easier
for the editors to work on.
 
 
 
## Learning and Success
This algorithm made me understand the complex mathematics behind images, interpreting them with opencv and even designing a solution which uses these api's and get desirable results
 
## Difficulties
Maths really became intense with this project, there was a lot of trigonometry and graph methods involved which had strange effects that were only visible through analysis.
 
 
One such thing was rotation, so when the image is rotated via openCV it uses three types of interpolation which decides the quality of the image. Each of these interpolation would produce same result but with less quality hence was a tricky thing to observe
 
## Plan update
Even this month the algorithm had positive results, some initial work was implemented on the framework but it doesn't even come close to the power and accessibility the algorithm possess. So on the code layer the project have gained significant weight and agility but the work is lacking on the framework which would cap the real algorithm. I would continue to adding these updates to the framework, and for me the project is halfway complete.
 
 
### Some Screenshots Depicting Difficult Segments of Algorithm :
 
![Rotation Image Loss]({{ site.baseurl }}/gsoc20/img_pipeline/assets/icrrect2.png "Incorrect Crop")
![Rotation Image Loss]({{ site.baseurl }}/gsoc20/img_pipeline/assets/wrong_crop.png "Incorrect Crop")
 
## Final Images for Archival from Algorithm :
![Final Arhival]({{ site.baseurl }}/gsoc20/img_pipeline/assets/archival_trial.jpg "Incorrect Crop")
![Final Arhival]({{ site.baseurl }}/gsoc20/img_pipeline/assets/alpha.png "Incorrect Crop")
 
 

