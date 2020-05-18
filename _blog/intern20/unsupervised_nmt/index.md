---
title: unsupervised_nmt
layout: page
author: "Rachit"
tags: ["project","research","internship", "unsupervised", "nmt"]
---

## Unsupervised Neural Machine Translation for English-Sumerian
Previous models that have been used to carry out English-Sumerian Translation have only made use of the available parallel corpora. [Presently](https://github.com/cdli-gh/Unsupervised-NMT-for-Sumerian-English) we have only about 50K extracted sentences for both languages in the parallel corpora, whereas around 1.47M sentences in the Sumerian monolingual corpus. This huge amount of monolingual data can be used to improve the NMT system by combining it with techniques like Back Translation and Dual Learning which have proved specially useful for Low-Resource languages like Sumerian which have a limited amount of parallel data. Studies on Back Translation have shown that using the synthetic sentences on the source side proves more effective and thus to accomplish English to Sumerian translation, the Sumerian monolingual data can be used extensively. The limitless English monolingual data too can be used to assist Sumerian to English translation, further the two models can be made to complement each other, thus moving onto an Iterative form of Back Translation or Dual Learning.

Recently methods have been proposed to accomplish completely Unsupervised Neural Machine Translation, they rely on Language Modelling and then combining the hidden states of the two LMs. Though they are still very limited to similar language pairs, it would be interesting to experiment with it for our task.

Before moving onto using monolingual data, it would be wise to create a solid baseline by using the self-attention based Transformer architecture purely on the parallel data, first. Moreover, additional techniques like Transfer Learning  wherein weights from a High Resource Language (HRL) Pair are fine-tuned for the Low Resource Language (LRL) Translation have shown considerable improvement in performance and can be employed along with a model like XLM, which hasn’t been tested on such a framework before.

**GitHub Repository: [cdli-gh/Unsupervised-NMT-for-Sumerian-English](https://github.com/cdli-gh/Unsupervised-NMT-for-Sumerian-English)**

### Objectives and Deliverables
Objectives are separated in two categories: essential and additional, they are also listed in pririty order. 
#### Essential Objectives

|\#|Objectives|Associated Deliverables|issue(s)|  
|---	|---	|---	|---	|  
|1   	|  Training the Transformer Seq2Seq on both English to Sumerian and Sumerian to English 	| Improved performance over the current SOTA of LSTMs	|   	|  
|2   	|  Using Cross-Lingual Language Modellings (XLM)	|  Equal/Better performance than Vanilla Transformers 	|   	|  
|3   	|  Performing Back Translation (BT) using previously saved models and complete (parallel + mono) data 	| Comparable performance to the completely supervised models 	|   	|  
|4   	|  Perfmorming Dual Learning using various Seq2Seq models on the complete data 	| Comparable performance to the completely supervised models and BT 	|   	|

#### Additional Objectives

|\#|Objectives|Associated Deliverables|issue(s)|  
|---	|---	|---	|---	|  
|1   	|  Implementing and Training (very recently introduced) completely Unsupervised Models 	|  Extended and more thorough experimentations as well as comparable performance 	|   	|

### Tentative timeline  

| Week  |Objectives |Deliverables |  
|---|---|---|  
|1| Preparing the parallel and monolingual texts for final usage by using Regular Expressions along with methods like BPE and BBPE to tokenize the text <br> Working on the discussed method of handling special characters and placeholders | English and Sumerian Data prepared to be worked with.  |  
|2| Implementing the Vanilla Transformer for Sumerian to English as well as English to Sumerian and training on the parallel corpora while saving weights for future use (for Back Translation). | Tranined Transformer on English to Sumerian as well as Sumerian to English|  
|3| Compiling the results of Vanilla Transformer, performing experiments with various sets of hyper parameters and analysing the results in comparison to previously used models. <br> Doing further experiments solely on the parallel corpora using techniques like Transfer Learning by using pre-trained weights on other language sets. | More experiments on Parallel Data |
|4| Implementing the XLM Encoder <br> Training the XLM on Masked Language Modelling (MLM), Translational Language Modelling (TLM) and Causal Language Modelling (CLM) tasks on some part of the parallel and monolingual data to obtain the PLT (Positional, Language and Token) embeddings for both English and Sumerian languages. | Pre-trained XLM Encoder and PLT Embeddings |  
|5| Training the XLM Encoder along with a Transformer Decoder on English-Sumerian Translation and saving the weights. | Fully trained XLM Encoder |  
|6| Back translating sentences from Sumerian monolingual corpus by using the saved Sumerian to English Transformer model thus creating synthetic parallel data, re-training Encoder-Decoder models using this synthetic data for English to Sumerian translation task. Doing the same for Sumerian to English by back translating sentences from English monolingual corpus. | Back Translation |
|7| Implementing Model-Level Dual Learning using tied Transformer Encoder-Decoder pairs. Alternating the training on parallel and monolingual corpora. | Dual Learning |  
|8| Investigating the performance variation in Dual Learning with different Encoder-Decoder models such as LSTMs, Vanilla Transformer and XLM, and the effect with various combinations of hyper-parameters. Comparing the results. | Further experimentations on Dual Learning |  
|9-10| Experimenting with Back Translation by studying the effect of sampling methods, amount of parallel data and model hyper-parameters on the translation quality. | Further experimentations on Back Translation |  
|11-12| Working on completely Unsupervised NMT Systems based on Language Models, trained on Sumerian Monolingual Data | Experiments on completely Unsupervised NMT Models |
