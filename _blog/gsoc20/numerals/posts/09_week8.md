---
layout: page
title: numerals Eval#2 Week#8
author: "Logan"
tags: ["week","gsoc","gsoc2020","numerals","eval#2","week#8"]
---

## Week Summary

(Apparently my schedule got mixed up at some point so there are two weeks of progress here... not sure where I gained the extra time.)

Removed hundreds of files from git repository to save space. Large updates to swagger documentation to include all new endpoints, and refactoring to standardize API parameter names and output format. Commenting and cleaning javascript which runs the visualizations.

Met to discuss viz demo; began implementing ideas from user feedback including ability to view a custom corpus; saving state to URL parameters for sharing/reproducibility; and QoL features such as autocomplete in the search bar.


## Daily Work Update

Week 7 I think:
|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2020/06/01	| Remove node\_modules and other unnecessary items from git repo. Restructure docker images to make node\_modules at build time. |  
|2   	| Tuesday  	|   2020/06/02	| Update swagger documentation to include new API endpoints. Refactor API endpoints to have consistent input and output  formats.	|  
|3   	| Wednesday  	|  2020/06/03 	| Comment and clean flask code and half of javascript code.  	|  
|4   	| Thursday  	|   2020/06/04	| Finish commenting and cleaning code: should now be fully documented with inline comments. Weekly meeting.  	|  
|5   	| Friday  	|   2020/06/05	| Meet to discuss visualization demo. Begin implementing suggested changes: reposition radio buttons; hide previous defintion if word is not in dictionary. Make loading div stay visible until loading finishes.   	|  
|6   	| Saturday  	|   2020/06/06	| 	|  
|7   	| Sunday  	|   2020/06/07	|   	|  

Week 8:
|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2020/06/01	| Extend number system filtering to modifier list and graphs. Refactor commodify endpoints to accept a custom list of texts. Save figure state in URL parameters when user interacts with figures. |  
|2   	| Tuesday  	|   2020/06/02	| Set figure state from URL parameters on page load. |  
|3   	| Wednesday  	|  2020/06/03 	| Make similar item histograms use log scale, for easier comparison to the main histogram. Update sign mapping with new values incl. urud-da = uruda. Add autocomplete to search bar, to help find unexpected spellings. |  
|4   	| Thursday  	|   2020/06/04	| Weekly meeting. |  
|5   	| Friday  	|   2020/06/05	| |  
|6   	| Saturday  	|   2020/06/06	| 	|  
|7   	| Sunday  	|   2020/06/07	|   	|  
