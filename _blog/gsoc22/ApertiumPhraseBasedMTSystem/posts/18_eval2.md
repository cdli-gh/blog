---
layout: page
title: Eval 2
author: "Himanshu Choudhary"
tags: ["eval","gsoc","gsoc2022","apertiumPhraseBasedMTSystem","eval#2"]
---

## Summary

The final integrated rule based pipeline is set up to translate from sumerian to english. The Phrase Based Machine Translation for Sumerian-English can be found here - 
* [apertium-sux-eng](https://github.com/cdli-gh/apertium-sux-eng)

The Rule based engine is comprised of data from -
- [mtaac_gold_corpus](https://github.com/cdli-gh/mtaac_gold_corpus)
- [mtaac_syntax_corpus](https://github.com/cdli-gh/mtaac_syntax_corpus/tree/master/parallel/consolidated)

Further details regarding the project, setup, preprocessing and details regarding NMT vs Rule Based engine can be found in **apertium-sux-eng** repo as mentioned above.

<br/>

The evaluation is done using the BLEU metric on the dev set as mentioned above - 


| Machine Translation System  | Mean  | Median |
|---|---|---|
| **rule based**     | 19.156  |  20.4517 |
|  **neural network** |  18.868 | 6.881  |

*The **mean** and **median** scores for both Rule Based and NMT Engine* \
*with weightage of (0.75,0.25,0,0) over n-grams*



## Objectives and Deliverables
| \# | Objectives                    | Associated Deliverables         |
| --- | ----------------------------- | ------- |
| 1 | updateding transfer rules and SVO reordering, sumerian to english | the final compact updated Transfer rules with and post processing if required |
| 2 |Integrated pipeline and NMT Comparision | Developing a notebook interface to try out both Neural network and Rule based engine for (sentence or file), with comparison |  |



## Learning and Success
- Developed sumerian machine translation rules
- built end to end integrated pipeline for rule based engine 
- interpretable and extandable machine translation system

## Difficulties
- understadning sumerian
- understadning apertium working

## Plan update
- A numeral translation pipeline can be integrated with the current rule based engine for better results

