---
layout: page
title: numerals Eval#1 Week#4
author: "Logan"
tags: ["week","gsoc","gsoc2020","numeralsl#1","week#4"]
---

## Week Summary

Finished initial implementation of commodity ID script; it may still change in the future if the visualization reveals errors or if a better output format becomes necessary.

Finished preparatory sketches for the visualization component and implemented a demo with placeholder data. Began adding features to the demo, including the main histogram display and summary statistics.

## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2020/06/01	| Compiled examples of inconsistent tokenization and opened github issue. Add test cases for dry capacity measures and update sign values. Updated format of output from commodify module. Started viz sketches. 	|  
|2   	| Tuesday  	|   2020/06/02	| Improve segmentation of lines with multiple numerals; fix minor bugs in commodity ID (ERIM substitution, weights in ki-la2-bi). Redeploy heroku app with new commodify module. Get sketch feedback from Max and post sketches to slack.  	|  
|3   	| Wednesday  	|  2020/06/03 	| Implement visualization UI using placeholder data. Add QoL features like table sorting, filtering, and toggling display formats. Implement basic search function. Update commodify output for ease of use in the visualization. 	|  
|4   	| Thursday  	|   2020/06/04	| Meeting. Reimplement existing functions as API endpoints instead of processing the data in javascript. Extend summary statistics to include more measures such as skewness, and different measures of central tendency which are not currently displayed.  	|  
|5   	| Friday  	|   2020/06/05	| Implement filtering by count type via radio buttons; add unit to the sum displayed below histogram. Add API endpoint to serve histogram data. Add tooltips to get exact values from the bars; convert y axis to a symlog scale to make the shorter bars more visible.   	|  
|6   	| Saturday  	|   2020/06/06	|   	|  
|7   	| Sunday  	|   2020/06/07	|   	|  
