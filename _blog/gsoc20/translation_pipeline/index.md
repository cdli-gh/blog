---
layout: page
title: translation_pipeline
author: "Himanshu"
tags: ["project","gsoc","gsoc2020","translation_pipeline","eval#1","week#2"]
---

## Translation Pipeline for whole Ur III corpus
The primary objective for this project is to build the End to End translation pipeline which takes a raw sumerian text as input and gives the detailed structure of the sentence along with its English translation. The POS Tagging and NER models are used to give valuable information about the sentences. In Linguistics, part-of-speech tagging (POS) and Named-Entity-Recognition(NER) are the fundamental tasks which are very useful for Information retrieval, information extraction, text categorisation and linguistic research for corpora. POS is the process of marking up a word in a text (corpus) as corresponding to a particular part of speech, such as nouns, verbs, adjectives, adverbs, etc. whereas Named-entity recognition (NER) is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into predefined categories such as person names, organizations, locations etc.

Presently we have two datasets to build our models.
1. [MTACC_GOLD_CORPUS](https://github.com/cdli-gh/Sumerian-NER/tree/master/Raw/CDIL_morph_raw)
2. Dictionary of words tagged with Named Entities  (Ex. Word - '{d}li9-si4',Tag - DN) 

There are different POS tags in sumerian as described here [ORACC](https://cdli-gh.github.io/guides/guide_tagsets.html) but out of these we will work on Noun(N), Verb(V), Numbers(NU), Conjunction(CNJ) and all other named entities which will be tagged as NE. These four are majorly used POS tags in Sumerian, other POS tags are rarely used and there is no dataset available to understand those. For the Named-Entity-Recognition also we will majorly rely on the first datasets as well. As in the second dataset we only have words without any left or right context which may not be helpful in training. For NER we have almost all the tags in the dataset (DN,EN,FN,GN,RN,MN,ON,PN etc.) (Though some are very limited) which are available here [ORACC](https://cdli-gh.github.io/guides/guide_tagsets.html). Out of these some are majorly used such as (PN - Personal name) and some are very rare such as (AN - Agricultural Name).

Since Dataset is very limited (Most of the sentences are one word as well) we will try to combine different approaches as described below. We will use a rule based methods (rules such as words ending with -ta most likely to be verbs, word followed by dumu(son of) most likely to be Personal name(Noun)) along with probabilistic approaches such as CRF(Conditional Random Fields) and HMM(Hidden Markov Models). We will also use Deep learning architectures used for Sequence modeling Using LSTMs and will try to combine it with previously used model features to make the best out of the limited dataset. 

My primary work is to build a Translation pipeline for which we will integrate the following models in a pipeline.
Best performing POS model.
Best Performing NER model.
Numeral model implemented by Logan
Improvised Machine translation model by Rachit Bansal

The final model will provide the detailed information about any input Sumerian text in human readable form using the above models.

**GitHub Repository: [cdli-gh/Sumerian-NER](https://github.com/cdli-gh/Sumerian-NER)**

### Objectives and Deliverables
Objectives are separated in two categories: essential and additional, they are also listed in pririty order. 
#### Essential Objectives

|\#|Objectives|Associated Deliverables|issue(s)|  
|---	|---	|---	|---	|  
|1   	|  Building Part of speech model using Rule based Probabilistic methods (CRF, HMM), and Deep learning approach 	|  POS tagging model for sumerian language 	|   	|  
|2   	|   Building Named-Entity-Recognition  model using POS tagger, Rule based Probabilistic methods(CRF), Spacy  and Deep learning approaches 	|   Sumerian Named-Entity-Recognition model 	|   	|  
|3   	|  Combining features of probabilistic approach along with Neural networks for both POS and NER models 	|   Improved performance of POS and NER models |     |  
|4   	|   Integrating POS, NER, Numeral and Machine translation model	|  Final translation pipeline, will be used to provide the detailed information about input sumerian text |    |
|5   	|   Deploying Command line interface on Github for the complete integrated pipeline	|  A command line interface for user  	|   	|  

#### Additional Objectives

|\#|Objectives|Associated Deliverables|issue(s)|  
|---	|---	|---	|---	|  
|1   	|  Coordinating with Rachit Bansal (Working on Machine Translation) to make rules based on POS and Named Entity tags for experimenting with MT models. such as Sumerian words tagged with any Named Entity or NU (Number for which we have seperate Numeral model) need not to be translated]  	|  Improved Translation accuracy of Sumerian language. 	|   	|  
|2   	|   Implementing other models for POS tagging and NER by introducing different features or changing in deep learning architectures(such as different word embeddings, BERT models etc.)	|   Part of research, may improve accuracy	|   	|  

### Tentative timeline  

| Week  |Objectives |Deliverables |  
|---|---|---|  
|1|  Preparing data for training POS model by extracting from the above dataset using conll-U parser and creating rules with the help of previous research papers and discussing with the language experts to take inputs as features | Prepared sumerian data and rules to be worked with.  |  
|2|  Implementing Conditional Random Field(CRF) and Hidden Markov Models (HMMs) to train POS tagging model on the prepared dataset | First POS tagging Model for sumerina language  |  
|3| Preparing data to be used for NER, Creating rules with the help of previous research papers and language experts. Creating a Classification model as an experiment using RNNs for the second dataset [ Word, Tag ] to integrate that as input in our Probabilistic Model.  | Prepared features and dataset to be worked with. Classification Model using second Dataset   |  
|4|  Implementing model using Conditional Random Field(CRF), Spacy and other statistical machine translation techniques |  First Named Entity recognition model.  |  
|5|  Extracting monolingual sumerian data using regex according to our input and training Fast-text and Word2vec word embeddings for sumerian language. Preparing data to be used for Neural Network model | Extracted monolingual sumerian data with word vectors to be used for training   |  
|6|  Training Deep Neural Network Models for POS tagging with the variations in the model ( such as changing optimisers, word embeddings etc.) |  Second POS tagging model based on Seq2seq modeling(Neural Network architecture) |  
|7|  Training Deep Neural Network model for Named entity recognition with the variations in the model ( such as changing optimisers, word embeddings etc.) |  Second NER model based on Seq2seq modeling(Neural Network architecture) |  
|8|  Combining features of probabilistic approach with the Deep neural networks  for both POS and NER model |  Improved Results for both NER and POS tagging |  
|9 - 10|  Discussion with other student developers Rachit Bansal(Machine translation) and Logan (Numeral Models)  to understand their Models, combining and connecting different models (POS, Numeral, MT systems) based on rules to improve translation. | Understanding the whole pipeline processing and preparing basic connected pipeline architecture   |   
|11 - 12|  Integrating all the models and deploying command line interface for the final pipeline to be used by the user | Translation Pipeline for sumerian language  |  

