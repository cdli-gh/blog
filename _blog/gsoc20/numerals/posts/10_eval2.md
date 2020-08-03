---
layout: page
title: numerals Eval#2
author: "Logan"
tags: ["eval","gsoc","gsoc2020","numerals","eval#2"]
---

## Summary
Implemented visualization interface with all components finished or nearly so. Planned features which are not complete include (i) option to search for adjectives or more complicated queries than just a single sign; and (ii) ability to filter the concordance component by number system. 

## Objectives and Deliverables
The main deliverable for this period was the visualization interface, which comprises five main components:
- histogram view, with summary statistics and overall item distribution
- similar items view, showing summary histograms of items with similar distributions to the search term
- concordance view, showing instances of the item in context
- nearby items view, showing items which occur in tablets along with the chosen item. Also includes a graph view where strongly connected components and cliques correspond to administrative subgenres.
- descriptors view, showing adjectives and other modifiers which occur with the chosen term. Also includes a graph view where cliques and strongly connected components represent common use cases for the chosen item. 

These components are all complete to the extent described in the initial proposal. There remain improvements which I would like to implement, such as more expressive search queries and extension of the filtering tools to cover the concordance view in the same way they affect the other modules. 

I have begun to add improvements which were not in the original proposal, such as the option to explore a custom corpus by providing a list of P-numbers. This work is still in progress, and is currently only accessible by querying the API directly (it is not yet part of the HTML interface).

## Learning and Success
The project continues to proceed ahead of schedule. This evaluation period, I was able to learn how to use docker and docker-compose to containerize my project as part of the CDLI framework. Otherwise, this evaluation period has been an opportunity to exercise my existing skills with d3 and web design.

## Difficulties
User feedback suggests that a major limitation of this work is the quality of the linguistic resources used to extract the data. Unusual spellings and definitions in the ePSD cause words to be included which should be ignored, and vice versa. The lack of quality word-sense disambiguation for Sumerian also limits our ability to accurately distinguish between homonyms. This suggests that the implementation of the commodity detection tools should be made as modular as possible to allow easy addition of new linguistic resources.

The need for python modules such as numpy and scipy cause the docker containers for this project to be large. It may be useful to reimplement the needed parts of these libraries and remove them from the dependency list to save space.

## Plan update
The work of integrating this project with the CDLI framework was moved forward into this evaluation period. This delayed work on the search and filtering tools, which will be moved to the next evaluation period. The priority of the improved search tools has also shifted towards options which support exploration of custom corpora, for example by specifying individual texts by P-number.

Much of the inline documentation and user guidance (e.g. help tooltips) is complete. Testing reveals that data processing is quite slow, so it is likely that the week scheduled for documentation will instead be used to speed up the project.

Other planned features which will be added to the next evaluation period include adding hooks to run every time the corpus is updated, and refactoring the data output to store a summary for each text separately. This is required so that these summaries can be combined to produce an overview of a custom corpus.
