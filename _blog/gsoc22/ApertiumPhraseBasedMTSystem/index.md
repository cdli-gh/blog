---
layout: page
title: Apertium - Phrase-based MT system
author: 'Himanshu Choudhary'
tags: ['project', 'gsoc', 'gsoc2022', 'apertiumPhraseBasedMTSystem']
---

## Apertium - Phrase-based MT system
The previously developed Machine Translation systems for Sumerian face sparsity issues because of their low-resource. The advanced translation techniques work better with the higher availability of data, whereas for low-resource languages, Rule Based/Symbolic Machine translation is a good alternative which can be used to improvise the accuracy. The objective is to build a sumerian-english machine translation system using one of the widely used machine translation platforms Apertium. This project also intended to compare the translation accuracy of both Neural Netowrk based and Rule Based machine translation System. 

The Phrase Based Machine Translation for Sumerian-English can be found here - 
* [apertium-sux-eng](https://github.com/cdli-gh/apertium-sux-eng)

The Sumerian and English and morph dictionaries can be found here -
* [apertium-sux](https://github.com/cdli-gh/apertium-sux)
* [apertium-eng](https://github.com/apertium/apertium-eng)


## Previous Work
-------------------
The SOTA neural netwrok based translation can be found here - 
* [Semi-Supervised-NMT-for-Sumerian-English](https://github.com/cdli-gh/Semi-Supervised-NMT-for-Sumerian-English) 

The whole integrated translation pipeline with pos and ner tagger can be found here -
* [Sumerian-Translation-Pipeline](https://github.com/cdli-gh/Sumerian-Translation-Pipeline)




## Objectives and Deliverables
----------

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks

| \# | Status  | Objectives                    | Associated Deliverables         | issue(s) |
| --- | --- | ----------------------------- | ---------------------------------------------- | -------- |
| 1 |:heavy_check_mark:|  createing sux(sumerian) morphological analyser | morphological dict with default tags for sumerian morph representation, basic morph analyzer |  |
| 2 |:heavy_check_mark:|  Updating previous eng morph dict with sumeiran words  | morphological english dict for sumerian words translation and/or handling bi-dictioanry results |  |
| 3 |:heavy_check_mark:| The Bi-lingual dictionary and rules for the sumerian to english translation | The sux-eng.dix file and .rtx file containing the trasnfer rules (basic) | |
| 4 |:heavy_check_mark:| Integrated apertium sux pipeline and testing | the integrated machine translation pipeline and testing comparision between nn based (will be added later) and rule based model | |
| 5 |:white_check_mark:| updateding transfer rules and SVO reordering, sumerian to english | the final compact updated Transfer rules with and post processing if required |  |
| 6 |:white_check_mark:| morphological disambiguator for sumerina | morph disambiguator to select correct lemma for processing |  |




## The related files 
----------

* english morph dict (https://github.com/apertium/apertium-eng/blob/main/apertium-eng.eng.dix)
* sumerian morph dict (https://github.com/himanshudce/apertium-sux)

* sumerian-englush bi-dict (https://github.com/cdli-gh/apertium-sux-eng/blob/main/apertium-sux-eng.sux-eng.dix)
* sumerian-english rule transfer (https://github.com/cdli-gh/apertium-sux-eng/blob/main/apertium-sux-eng.sux-eng.rtx)






<!-- ### Additional Objectives
| \# | Status  | Objectives         | Associated Deliverables                                             | issue(s) |
| --- | --- | ------------------ | ------------------------------------------------------------------- | -------- |
| 1 | :heavy_check_mark: | hello world  | hello world |    [!318]()     |
| 1 | :white_check_mark: | hello world  | hello world |    [!318]()     | -->


## Tentative timeline

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks  :raised_hands: --> Work Demonstration

| Week  |Objectives | Deliverables |
|---|---|---|
|1 - 2| :heavy_check_mark: learning apertium (The RBMT toolkit) |  :heavy_check_mark: the basic functanality to use apertium |
|3 - 4| :heavy_check_mark: learning sumerian morphology  |  :heavy_check_mark: Basic grammer of Sumerian and translations  |
|5 - 8| :heavy_check_mark: creating basic sumerian analyzer , bi-lingual dict, rule trasnfer and testing  |  :heavy_check_mark: The integrated translation pipeline sux-eng |
|9 - 11| :white_check_mark: updating trasnfer rule (verbal and noun phrase) and re-ordering SVO |  :white_check_mark: the improved machine translation results |
|11 - 15| :white_check_mark: Working on morphological disambiguator and Number pipleine integration and Rule based bs NN based comparision |  :white_check_mark: Final robust pipeline and model comparisions |



<!-- |2| :heavy_check_mark: hello world  |  :heavy_check_mark: hello world <br/> :heavy_check_mark: hello world <br> :raised_hands: hello world|
|3| :heavy_check_mark: hello world  |  :heavy_check_mark: hello world <br/> :heavy_check_mark: hello world <br> :raised_hands: hello world| -->

