---
layout: page
title: Eval 1
author: "Himanshu Choudhary"
tags: ["eval","gsoc","gsoc2022","apertiumPhraseBasedMTSystem","eval#1"]
---

## Summary
The basic rule based pipeline is set up to translate from sumerian to english.The Phrase Based Machine Translation for Sumerian-English can be found here - 
* [apertium-sux-eng](https://github.com/cdli-gh/apertium-sux-eng)

The current pipeline has a limitied vocabulary(from mtaac_gold_corpus) and the rules are without much ordering(SVO). The next phase is to make more concerete rules. The test is done on dev data from mtaac_syntax_corpus. The test pipeline contains both rule based and nn based (will be integrated) machine translation  systems for the comparisions.

The evaluation is done using the BLEU metric and the current rule based model score - \

**RBMT BLEU SCORE -** 9.0025  

\* with weightage (0.75,0.25,0,0) over n-grames

<br>


## Objectives and Deliverables
| \# | Objectives                    | Associated Deliverables         |
| --- | ----------------------------- | ---------------------------------------------- |
| 1 | createing sux(sumerian) morphological analyser | morphological dict with default tags for sumerian morph representation, basic morph analyzer |
| 2 | Updating previous eng morph dict with sumeiran words  | morphological english dict for sumerian words translation and/or handling bi-dictioanry results |
| 3 |The Bi-lingual dictionary and rules for the sumerian to english translation | The sux-eng.dix file and .rtx file containing the trasnfer rules (basic) | 
| 4 |Integrated apertium sux pipeline and testing | the integrated machine translation pipeline and testing comparision between nn based and rule based model |

## Learning and Success
* learning of Sumerian language
* learning of apertium (open source MT software)
* The integrated rule based sumerian-english machine translation pipeline


## Difficulties
* The morphology of sumerian language
* The apertium documentation
* less interactions with the language experts

## Plan update
The next milestone is to update the rules and to make the correct ordering(SVO) using NP(noun phrase) and VP(verb phrase) to make the exact translation. Also adding morphological disambiguator to select the correct analysis of the word.
