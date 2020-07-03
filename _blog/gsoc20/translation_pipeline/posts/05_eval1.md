---
layout: page
title: translation_pipeline Eval#1
author: "Himanschu"
tags: ["eval","gsoc","gsoc2020","translation_pipelinel#1"]
---

## Summary
Worked on building First sumerian Translation pipeline which includes the extraction of part of speech tag, named entity recognation and translating the text into english. In the first phase I focused on building the part of speech model for sumerian to achive state of art result. I used different type of models which includes machine learning, rule based methods and neural network architecture. I also got the help from the mentors for the models evaluation and got to know that it performed very well with at most 2 to 3 % error. As I enjoyed working on the project I moved ahead of the schedule and also built the first named entity recognation model and built the basic pipeline. Updated the pipeline code by integrating the current models. The current pipeline can be used and extended easily.Pipeline can be used after cloning (https://github.com/cdli-gh/Sumerian-Translation-Pipeline)\  
```
usage: pipeline.py [-h] [-i INPUT]
                   [-p {POS_CRF,POS_HMM,POS_Bi_LSTM,POS_Bi_LSTM_CRF}]
                   [-n {NER_CRF,NER_Bi_LSTM,NER_Bi_LSTM_CRF}]
                   [-t {Transformer}] [-o OUTPUT]
                   
  -i INPUT,
          Location of the Input ATF File
  -p {POS_CRF,POS_HMM,POS_Bi_LSTM,POS_Bi_LSTM_CRF}
                        POS Model to be used out of the above choices 
  -n {NER_CRF,NER_Bi_LSTM,NER_Bi_LSTM_CRF}
                        NER Model to be used from above the choices
  -t {Transformer}
                        Machine Translation Model to be used from above choices 
  -o OUTPUT
                        Location of output Directory/Folder
```

## Deliverables
| Week    | Objectives | Deliverables  | Status  |
| ------- | ---------- | ------------- |-------  |
| 1       | Preparing data for training POS model by extracting from the above dataset using conll-U parser and creating rules with the help of previous research papers and discussing with the language experts to take inputs as features | Prepared sumerian data and rules to be worked with.  | Completed |
| 2       | Implementing Conditional Random Field(CRF) and Hidden Markov Models (HMMs) to train POS tagging model on the prepared dataset  | First POS tagging Model for sumerian language | Completed |
| 3       | Extracting monolingual sumerian data using regex according to our input and training Fast-text and Word2vec word embeddings for sumerian language. Preparing data to be used for Neural Network model   | Extracted monolingual sumerian data with word vectors to be used for training | Completed |
| 4       | Training Deep Neural Network Models for POS tagging with the variations in the model ( such as changing optimisers, word embeddings, architectures etc.)  | Improvised POS tagging model based on Seq2seq modeling(Neural Network architecture)  | Completed |



## Learning and Success
Successfully built the 4 POS tagging models to achive the state of art results. Built the basic Sumerian-Translation-Pipeline integrating POS, NER and Machine Translation model. Produced results are pretty good as reviewed by the Mentor(s). Learned about different rule based and and machine learning architectures. The dependence of these models on probabilistic approach and the integration of deep learning and machine learning models. It improved my understanding of Neural networks and related parameters. I also learned new concepts of git with the command line interface. 

## Difficulties
Hard to get context of the sentence as the phrases were too small, although models are working pretty well with the limited datasets.  

## Plan update
Pretty much ahead of the schedule, so planning to work on producing POS and NER results in Conll-U format. Will work on the remaining NER model to achieve state of art results. Integrate the pipeline with the remaining models and try to improve the translation accuracy of the Machine translation model.  
