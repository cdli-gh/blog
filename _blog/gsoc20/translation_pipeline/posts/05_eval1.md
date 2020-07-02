---
layout: page
title: translation_pipeline Eval#1
author: "Himanschu"
tags: ["eval","gsoc","gsoc2020","translation_pipelinel#1"]
---

## Summary
Prepared data for training POS model by extracting from the above dataset using conll-U parser and creating rules with the help of previous research papers and discussing with the language experts to take inputs as features	Prepared sumerian data and rules to be worked with \

Implemented Conditional Random Field(CRF) and Hidden Markov Models (HMMs) to train POS tagging model on the prepared dataset, created first POS tagging Model for sumerian language	\

Extracted monolingual sumerian data using regex according to our input and training Fast-text and Word2vec word embeddings for sumerian language. Prepared data to be used for Neural Network model	Extracted monolingual sumerian data with word vectors to be used for training\

Trained Deep Neural Network Models for POS tagging with the variations in the model ( such as changing optimisers, word embeddings, etc.) \

Integrated Basic Pipeline taking input as atf file and giving the associated outputs \


## Learning and Success
Successfully built the 4 POS tagging models to achive the state of art results. Built the basic Sumerian-Translation-Pipeline integrating POS, NER and Machine Translation model. Produced results are good as reviewed by Mentor(s).   

## Difficulties
Hard to get context of the sentence as the phrases are too small, although models are working pretty well with the limited datasets. 

## Plan update
Pretty much ahead of the schedule, so planning to work on producing POS and NER results in Conll-U format as well along with the pipeline.  
