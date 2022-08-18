---
layout: page
title: Eval 1
author: "Mohammad Sameer"
tags: ["eval","gsoc","gsoc2022","morphologicalParserForSumerian","eval#1"]
---

## Summary

A script was written to extract the lexicon data and the rules required for
SuMor to generate correct analysis. The endings were integrated in the flexion
file and the words were added to the dict.tsv.

## Objectives and Deliverables
| \# | Objectives                    | Associated Deliverables         |
| --- | ----------------------------- | ---------------------------------------------- |
| 1 | Get all the CDLI data (rules and words)  | Write a script that scraps all the required information |
| 2 | Integrate the data to the generation files  | Add rules to the flexion file and words to the dictionary |
| 3 | Test if the given outputs are correct  | Write tests in Makefiles generating 22 correct analysis on 36 words |

## Learning and Success
Learnt about Sumerian grammar and SFST.

## Difficulties
The unusual difficulties in the scraping the files and trouble-shooting

## Plan update
In future, I plan to have a more polished design for SuMor
as the code right now is spaghetti.
