---
layout: page
title: Morphological Parser for Sumerian
author: 'Mohammad Sameer'
tags: ['project', 'gsoc', 'gsoc2022', 'morphologicalParserForSumerian']
---

## Morphological Parser for Sumerian

As for now, all the translation that can be done of Sumerian is that by Assyriologists, which are not that many, or by non-rule-based parsers who don’t do a good job at translating the sentences. This project aims to do the first step in the right direction to develop a rule-based morphological parser to ease the growth of further development in the study of the language of Sumer and Akkadian civilizations.

SFST is a finite-state transducer that will be used to write the morphologies for Sumerian. The analysis would be on three-level: 

i. Morphological, turning the grammatical features into morphemes with morpheme boundaries and zero morphemes. 

ii. Morphophonological, transcribing the morphemes to the conventional transcription (by removing morpheme boundaries).

iii. Transliteration, changing to make it orthographically accurate by the conventions of CDLI orthography.

## Objectives and Deliverables
----------

:heavy_check_mark: --> Completed Tasks  :white_check_mark: --> Ongoing Tasks

| \# | Status  | Objectives                    | Associated Deliverables         | issue(s) |
| --- | --- | ----------------------------- | ---------------------------------------------- | -------- |
| 1 |:heavy_check_mark:| Create a script extracting the lexicon | Script analyses CDLI corpus and outputs in SuMor compatible format|  |
| 2 |:heavy_check_mark:|  Build a valid Sumerian lexicon | A tsv file with words, tags and meaning |  |
| 3 |:heavy_check_mark:|  Have a working parser | Changes to flexion.fst so that it can generate new morphologies in CDLI format| |
| 4 |:white_check_mark:| Write a whitepaper| Submit a paper to Christian Chiarcos, with stats|  |
| 5 |:white_check_mark:| Polish the edges of SuMor| Change it to be seemless with one command and the magic happens, Add the leftout endings to the flexion file |  |
