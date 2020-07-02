---
layout: page
title: numerals Eval#1
author: "Logan"
tags: ["eval","gsoc","gsoc2020","numeralsl#1"]
---

## Summary
I have implemented a conversion between Sumerian numerals and modern Arabic notation. The conversion can handle cardinal and ordinal numbers, lengths, surfaces, volumes, wet and dry capacities, weights, and the special notation used for counting bricks. I have also implmented conversions for early number systems from Susa, which can be used if this tool is ever extended to include proto-Elamite texts. All conversions are confirmed to work with test cases extracted from Sumerian grammars (principally Edzard (2003) and Jaegersma (2010)).

I have implemented a commodity ID script, which uses wordnet synsets to identify items which are likely to be counted objects. This is supplemented by a list of manually compiled rules to handle special cases and words with misleading synsets. This identifies on the order of 28k tokens in the Girsu corpus as counted objects, and manual evaluations suggest that upwards of 90% of these labels are assigned correctly. With some manual corrections and proofreading, this labeled data could be used to train a more general-purpose machine-learning model which would be better able to generalize. This model also has (the rudiments of) a system for identifying implicit objects, as it can infer the presence of food rations in texts where these are not explicitly written. The system jointly classifies all words in an entry, and can identify cases where a counted object has been modified by an adjective or other descriptor.

I have sketched a suite of tools which will allow exploration of many facets of the data. These include identifying the different uses of an item based on its context, identifying subtypes of a counted object (e.g. animals fed with different diets), and finding other items with similar distributions to some query term. Slightly more than half of these these tools have been implemented, and a demo of the entire suite should be available by the week's end.

## Objectives and Deliverables
All code and other deliverables are hosted on the project repo at https://github.com/MrLogarithm/cdli-accounting-viz. The main branch provides a stable and well-tested version of the project, and usually lags ~1 week behind the dev branch where new features are tested.

The main objectives were to complete a data processing pipeline which would accept a text or corpus of texts as input, and return a summary of the counted objects as output. This has been completed, but may be revised to improve accuracy or to extract new information. The deliverables associated with this pipeline include:
- convert\_sumerian.py, to convert Sumerian numerals into Arabic notation
- segment.py, to split a text into entries counting different objects
- semantic.py, to retrieve semantic information from wordnet and label potential commodities
- commodify.py, to produce the final labeling of commodities using information from the semantic module and other features such as position in the sentence

The final deliverable for this evaluation period is a flask API prividing access to these scripts (app.py in the repository). An old but stable version of this API is hosted at https://cdli-numerals.herokuapp.com/docs. The API is being heavily expanded in order to implement the visualizations, so the most recent version is not yet stable enough to host. It can be found in the dev branch if needed.

## Learning and Success
I have learned how to use flask to develop webservices in python, and have a much more robust understanding of webservices and APIs in general. I've also learned to use docker and related utilities, first for deploying applications on heroku, and later as preparation for adding this project to the CDLI framework.

I have also become much more comfortable with the data from Girsu, and feel better able to read these texts and understand how to extract information from them. The challenges of working with these texts are very different from those associated with a corpus such as proto-Elamite, where transcriptions are all very strictly standardised and alternate spellings are clearly labeled in the data itself. 

## Difficulties
The data from Girsu has many variant spellings and tokenizations which make it difficult to work with. I have had to extract a dictionary of word-level translations from the ePSD, since such a dictionary does not seem to exist anywhere else, and I have had to emend this dictionary with alternate sign names and variant spellings found in the Girsu data. Word-sense disambiguation is another tool I have become accustomed to while working with modern languages, and have missed while working with Sumerian. I see now that the toolset available for working with Sumerian could be greatly expanded.

The lack of training data for the tasks I seek to complete has meant that most of my work has to be rule-based; however, now that I am producing labeled data this may not be an issue moving forward.



## Plan update
I believe it is important to get an interactive demo online as soon as possible, in order to get feedback from users. To this end I have decided to postpone the search/filtering tools by a least a week. I also think it would be nice to move the project from heroku to the CDLI framework sooner rather than later. This move was scheduled for the last week of the project, but I am tempted to move it forward to the second evaluation period. Overall, I am ahead of schedule, and I expect to have an extra week to add extra functionality or improve the deliverables from this evaluation period.
