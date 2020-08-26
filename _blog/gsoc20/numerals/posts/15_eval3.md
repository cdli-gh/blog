---
layout: page
title: numerals Eval#3
author: "Logan"
tags: ["eval","gsoc","gsoc2020","numerals","eval#3"]
---

## Summary
The data format has changed significantly since the previous evaluation. Data has been sharded into one file per text, and the APIs and data module have been updated to use the new format. This allows us to recover which text a given piece of information comes from. The visualization has been updated to incorporate this information by linking back to CDLI search results where the user can see the texts which contributed to a given result.

This has also allowed for the use of custom corpora. By specifying the `corpus` URL parameter the user can visualize results from an arbitrary collection of (Sumerian) texts. Linking to the visualization from the CDLI search page will allow for easier access without the need to manually specify all of the texts in the desired corpus. 

The URL may become long when the corpus argument is very large. To reduce the URL size and prevent issues with browsers truncating links, we have added support for encoded URL parameters. These are not human readable, but permit more compact links. The page stores all figure settings as URL parameters to enable easy sharing of figures: we store these in human-readable format whenever possible, and revert to the encoded format when the URL grows too long (>2048 characters).

Since the last evaluation, we have fixed minor errors in the data generation (e.g. fixing some terms which should be counted as commodities, but which were not recognized based on their definitions). We have improved the UI by fixing overlapping DOM elements and improving visual consistency across figures.

We have made UX improvements in the form of a Cite button, which generates citations in common formats and provides easy access to a URL which will reproduce the figures. We have proofread and clarified all user-facing text and adjusted when the loading indicator appears to prevent frustration with unresponsive figures.

## Objectives and Deliverables
Explain what were your objectives and the deliverables associated for this period.

The first main deliverable for this period was to finish the search and filtering tools, which were not fully functional at the last evaluation. This has been completed, and all modules now respect the user's choice of number system, search term, and corpus. 

During the last evaluation, support for a custom corpus was emphasized as a useful feature for prospective users. The ability to quickly see which texts a given piece of data came from was also requested. These features have been successfully completed.

At the last meeting, tools for data generation were requested which could be used to regenerate the data when a text is updated. The script which generates the data in the new format is designed to work on a single text, satisfying this requirement. There is currently no hook to run this script when a text updates, as to my knowledge the forms which would be used to update texts are not functional. 

Speed improvements were suggested at the last evaluation. By sharding the data and removing redundant information from some API calls, we have managed to reduce load times to less than one second on small and moderately sized corpora. Large corpora (e.g. all Ur IIIb texts from Girsu) have seen improvemens of several seconds but are still slow to load.


## Learning and Success
Briefly outline what you have learned and the sucesses you have achieved.

Making my code into a proper submodule broke the pipeline on gitlab. In fixing it, I learned how exactly continuous integration works in gitlab, and what is involved in the CDLI's CI pipeline in particular. Fixing this also helped me figure out how to remove manual interventions from my docker builds, and how to upload docker images to a registry to save users from having to build them on their own time.

Making my code into a submodule forced me to try to merge two unrelated git histories, which revealed a variety of features which I had never encountered. Despite the lost time, I feel the experience was worthwhile as an opportunity to learn about `git cherry pick`, `git rebase`, and grafts.

## Difficulties
Briefly outline roadblocks and difficulties you have enountered.

The scarcity of good linguistic resources for Sumerian continues to be an issue, and during this evaluation period I had to manually specify additional rules to fix inadequacies in the ePSD.

The other main difficulty this evaluation period was time. There are always new ideas to add, and too little time for them all. I am aware of issues in the data processing which are minor enough to ignore, but it is challenging to end the project without resolving them. Likewise, during cross-browser testing I have identified issues in how some browsers (mainly Chromium) display the figures. The issues are purely cosmetic and do not impact the accuracy of the figures, but I would have liked to resolve them. Thank goodness for git issues...
