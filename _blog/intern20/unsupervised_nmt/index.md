---
title: unsupervised_nmt
layout: page
author: "Rachit"
tags: ["project","research","internship", "unsupervised", "nmt"]
---

## Project X name
Short description here.

### Objectives and Deliverables
Objectives are separated in two categories: essential and additional, they are also listed in pririty order. 
#### Essential Objectives

|\#|Objectives|Associated Deliverables|issue(s)|  
|---	|---	|---	|---	|  
|1   	|   	|   	|   	|  
|2   	|   	|   	|   	|  
|3   	|   	|   	|   	|  
|4   	|   	|   	|   	|  
|5   	|   	|   	|   	|  
|6   	|   	|   	|   	|  

#### Additional Objectives

|\#|Objectives|Associated Deliverables|issue(s)|  
|---	|---	|---	|---	|  
|1   	|   	|   	|   	|  
|2   	|   	|   	|   	|  
|3   	|   	|   	|   	|  
|4   	|   	|   	|   	|  
|5   	|   	|   	|   	|  
|6   	|   	|   	|   	|  

### Tentative timeline  

| Week  |Objectives |Deliverables |  
|---|---|---|  
|1| Preparing the parallel and monolingual texts for final usage by using Regular Expressions along with methods like BPE and BBPE to tokenize the text <br> Working on the discussed method of handling special characters and placeholders | English and Sumerian Data prepared to be worked with.  |  
|2| Implementing the Vanilla Transformer for Sumerian to English as well as English to Sumerian and training on the parallel corpora while saving weights for future use (for Back Translation). | Tranined Tranformer on English to Sumerian as well as Sumerian to English|  
|3| Compiling the results of Vanilla Transformer, performing experiments with various sets of hyper parameters and analysing the results in comparison to previously used models. <br> Doing further experiments solely on the parallel corpora using techniques like Transfer Learning by using pre-trained weights on other language sets. | More experiments on Parallel Data |
|4| Implementing the XLM Encoder <br> Training the XLM on Masked Language Modelling (MLM), Translational Language Modelling (TLM) and Causal Language Modelling (CLM) tasks on some part of the parallel and monolingual data to obtain the PLT (Positional, Language and Token) embeddings for both English and Sumerian languages. | Pre-trained XLM Encoder and PLT Embeddings |  
|5| Training the XLM Encoder along with a Transformer Decoder on English $\leftrightarrow$ Sumerian Translation and saving the weights. | Fully trained XLM Encoder |  
|6| Back translating sentences from Sumerian monolingual corpus by using the saved Sumerian to English Tranformer model thus creating synthetic parallel data, re-training Encoder-Decoder models using this synthetic data for English to Sumerian translation task. Doing the same for Sumerian to English by back translating sentences from English monolingual corpus. | Back Translation |
|7| Implementing Model-Level Dual Learning using tied Transformer Encoder-Decoder pairs. Alternating the training on parallel and monolingual corpora. | Dual Learning |  
|8| Investigating the performance variation in Dual Learning with different Encoder-Decoder models such as LSTMs, Vanilla Transformer and XLM, and the effect with various combinations of hyper-parameters. Comparing the results. | Further experimentations on Dual Learning |  
|9-10| Experimenting with Back Translation by studying the effect of sampling methods, amount of parallel data and model hyper-parameters on the translation quality. | Further experimentations on Back Translation |  
|11-12| Working on completely Unsupervised NMT Systems based on Language Models, trained on Sumerian Monolingual Data | Experiments on completely Unsupervised NMT Models |
