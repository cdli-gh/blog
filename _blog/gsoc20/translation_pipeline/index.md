---
layout: page
title: translation_pipeline
author: 'Himanshu'
tags:
  ['project', 'gsoc', 'gsoc2020', 'translation_pipeline', 'eval#1', 'week#2']
---

## Translation Pipeline for whole Ur III corpus (GSCO-2020)

The primary objective for this project is to build the End to End translation pipeline which takes a raw sumerian text as input and gives the detailed structure of the sentence along with its English translation. The POS Tagging and NER models are used to give valuable information about the sentences. In Linguistics, part-of-speech tagging (POS) and Named-Entity-Recognition(NER) are the fundamental tasks which are very useful for Information retrieval, information extraction, text categorisation and linguistic research for corpora. POS is the process of marking up a word in a text (corpus) as corresponding to a particular part of speech, such as nouns, verbs, adjectives, adverbs, etc. whereas Named-entity recognition (NER) is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into predefined categories such as person names, organizations, locations etc. There are different POS and NER tags in sumerian which are described here [ORACC](https://cdli-gh.github.io/guides/guide_tagsets.html). We will work on two different tasks and build the models for NER and POS.  

Since Dataset is very limited (Most of the phrases are one word as well) we will try to combine different approaches as described below. We will use a rule based methods (for example word followed by dumu(son of) most likely to be Personal name(Noun)) along with probabilistic approaches such as CRF(Conditional Random Fields) and HMM(Hidden Markov Models). We will also use Deep learning architectures used for Sequence modeling Using LSTMs and will try to combine it with previously used model features to make the best out of the limited dataset. We will also apply text ausmentation to increase the number of phrases using the dictionary we have and try to apply current state of art techniques for the best results.

My primary work is to build an NLP-Pipeline for which I will integrate the following models in a pipeline and provide a command line interface for the user.
1. POS
2. NER
3. [Sumerian Machine translation](https://github.com/cdli-gh/Semi-Supervised-NMT-for-Sumerian-English) Model

The final model will provide the detailed information(POS tagging, Named Entity Recognation, English Translation) about any input Sumerian text (of UrIII period) in human readable form using the above models.

## GitHub Repository: [cdli-gh/Sumerian-Translation-Pipeline](https://github.com/cdli-gh/Sumerian-Translation-Pipeline)


### Objectives and Deliverables

Objectives are separated in two categories: essential and additional, they are also listed in priority order.

#### Essential Objectives

| \#  | Objectives                                                                                                                          | Associated Deliverables                                                                                | issue(s)                                                     |
| --- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| 1   | Building Part of speech model using Rule based Probabilistic methods (CRF, HMM), and Deep learning approach                         | POS tagging model for sumerian language                                                                | No Ending marked for the sentences, difficult to get context |
| 2   | Building Named-Entity-Recognition model using POS tagger, Rule based Probabilistic methods(CRF), Spacy and Deep learning approaches | Sumerian Named-Entity-Recognition model                                                                | No Ending marked for the sentences, difficult to get context |
| 3   | Using current state of art techniques for both POS and NER models                                 | Improved performance of POS and NER models                                                             |                                                              |
| 4   | Integrating POS, NER, Numeral and Machine translation model                                                                         | Final translation pipeline, will be used to provide the detailed information about input sumerian text |                                                              |
| 5   | Deploying Command line interface on Github for the complete integrated pipeline                                                     | A command line interface for user                                                                      |                                                              |


### Tentative timeline

| Week    | Objectives                                                                                                                                                                                                                                                                | Deliverables                                                                                    | Status                                                                                    |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |----------------------------------------------------------------------------------------------- |
| 1       | Preparing data for training POS model by extracting from the above dataset using conll-U parser and creating rules with the help of previous research papers and discussing with the language experts to take inputs as features                                          | Prepared sumerian data and rules to be worked with.                                             | Completed |
| 2       | Implementing Conditional Random Field(CRF) and Hidden Markov Models (HMMs) to train POS tagging model on the prepared dataset                                                                                                                                             | First POS tagging Model for sumerian language                                                   | Completed |
| 3       | Extracting monolingual sumerian data using regex according to our input and training Fast-text and Word2vec word embeddings for sumerian language. Preparing data to be used for Neural Network model                                                                     | Extracted monolingual sumerian data with word vectors to be used for training                   | Completed |
| 4       | Training Deep Neural Network Models for POS tagging with the variations in the model ( such as changing optimisers, word embeddings, etc.)                                                                                                           | Improvised POS tagging model based on Seq2seq modeling(Neural Network architecture)             | Completed |
| 5       | Preparing data to be used for NER, Creating rules with the help of previous research papers and language experts. Creating a Classification model as an experiment using RNNs for the second dataset [ Word, Tag ] to integrate that as input in our Probabilistic Model. | Prepared features and dataset to be worked with. Classification Model using second Dataset      | Completed  |
| 6       | Implementing NER model using Conditional Random Field(CRF) and Training Deep Neural Network model for Named entity recognition with the variations in the models                                                                                                                                                    | First Named Entity recognition model.                                                           | Completed |
| 7       | Parameter Tunning for Named entity recognition and language training FLAIR model for Both POS and NER                                                                                                                    | Flair Language Model for POS and NER   | Completed |
| 8       | Training BERT Language Model for both POS and NER model along with different word embeddings  | BERT language model for NER and POS tagging                                            | Completed |
| 9  | Fine Tunning FLAIR and BERT Language Model for both NER and POS, producing results   | Improved scores | Completed |
| 10  |Discussion with Machine translation student developer to understand their Models, combining and connecting different models (POS, NER, MT systems).                            | Understanding the whole pipeline processing and preparing basic connected pipeline architecture | Completed |
| 11 - 12 | Integrating all the models and deploying command line interface for the final pipeline to be used by the user  | Translation Pipeline for sumerian language  | Completed |


#### Additional Objectives

| \#  | Objectives| Associated Deliverables| status |
| --- | --------- | --------------------------------------------------- | -------- |
| 1   | Producing final POS and NER results in combined form in CDLI-CONLL format along with previously annotated morphological syntax  | Improved informational results   |   Completed       |
| 2   | Building Docker container and Web API for to provide user interface   |  User interface for easy access to Pipeline   |Completed |


#### To Do
| \#  | Objectives| Issues | status |
| --- | --------- | --------------------------------------------------- | -------- |
| 1   | Integrating web API and docker cotainer to CDLI framework  |  Backend knowledge of web servers and CDLI framework including PHP and Databse |    |

