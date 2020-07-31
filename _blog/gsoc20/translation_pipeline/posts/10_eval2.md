---
layout: page
title: translation_pipeline Eval#2
author: "Himanschu"
tags: ["eval","gsoc","gsoc2020","translation_pipeline","eval#2"]
---

## Summary
In the Second phase I focused on building the Named entity recognation models for sumerian to achive state of art result. I used different type of models which includes machine learning, rule based methods and neural network architecture. I also got the help from the mentors for the models evaluation and modified the models, updated them and they performed very well with at most 1 to 2 % error. I am very much ahead of the schedule, I have not only built the different NER models but also, almost completed the pipeline. I updated Updated the pipeline code by integrating the all the models. Moreover I have trained the flair language model which includes the combination of character and other word embeddings and fine tuned it to built NER and POS models.  I have updated the documentation, the code is easily integrable and ready for use. Also written a code to convert the POS and NER in conll version which was desired to store the results. The pipeline can be used and extended easily (https://github.com/cdli-gh/Sumerian-Translation-Pipeline)\
### To Use - \
Clone the Repo https://github.com/cdli-gh/Sumerian-Translation-Pipeline.git \
Install requirments by simply running requirments.sh file- \
Run pipeline.py file with the ATF input file, the results will be in ATF_OUTPUT folder 
```
git clone https://github.com/cdli-gh/Sumerian-Translation-Pipeline.git
cd Sumerian-Translation-Pipeline
sh requirments.sh
python3 pipeline.py -i ATF_INPUT/demo.atf -o ATF_OUTPUT
```

## Objectives and Deliverables

 Week    | Objectives | Deliverables  | Status  |
| ------- | ---------- | ------------- |-------  |
| 5       | Preparing data to be used for NER, Creating rules with the help of previous research papers and language experts. Creating a Classification model as an experiment using RNNs for the second dataset [ Word, Tag ] to integrate that as input in our Probabilistic Model. | Prepared features and dataset to be worked with. Classification Model using second Dataset  | Completed |
| 6       | Implementing NER model using Conditional Random Field(CRF), Spacy and other statistical machine translation techniques| First Named Entity recognition model. | Completed |
| 7       | Training Deep Neural Network model for Named entity recognition with the variations in the model ( such as changing optimisers, word embeddings etc.)| Second NER model based on Seq2seq modeling(Neural Network architecture) | Completed |
| 8       | Combining features of probabilistic approach with the Deep neural networks for both POS and NER model  | Improved Results for both NER and POS tagging models | Completed |


## Learning and Success
Successfully built the 3 POS tagging models to achive the state of art results. Updated the Sumerian-Translation-Pipeline integrating all POS and NER Models. New Machine Translation models are also updated. Code is tested and working pretty good. Learned about different Deep learning and machine learning architectures. As an experient trained Flair language model so learned about these new techniques. Learned Training and Fine tunning of language models and use of differnet word embeddings including character embeddings, word2vec, glove, fasttext and flair word embeddings. All these improved my understanding of Neural networks and related parameters. Also learned new concepts of git with the command line interface and using cloud servers.

## Difficulties
Limited dataset, tried text augmentation. Less data to train and Fine Tune language Model.

## Plan update
Mostly ahead of schedule, almost integrated the pipeline and ready for use, tested now will traing BERT language model and update the documentation deploy an API to use the model at backend and work on reasearch paper for EACL conference.
