---
layout: page
title: numerals Eval#1 Week#1
author: "Logan Born"
tags: ["week","gsoc","gsoc2020","numerals","eval#1","week#1"]
---

## Week Summary

**Numeral Conversion**
- added code to handle dates written using \|ASZxDISZ\|
- added test cases from Edzard 2003
- merge PR from Willis to change testing framework
- document frequency of known bugs to determine which to prioritize

**Commodity ID**
- created flask API to query the commodity module
- setup wordnet for experiments with hypernyms
- experiment with using states from existing HMM to label commodities. Accuracy is too low, but the state is somewhat informative and could be used as a feature in a predictive model down the line.
- begin experimenting with wordnet to identify commodities based on hypernyms of the english translation.


## Daily Work Update

|\#|Day|Date|A short description of the work done|  
|---	|---	|---	|---	|  
|1   	| Monday 	|   2020/06/01	| Refine numeral conversion (handle dates; add test cases from Edzard 2003) and commodity id (check coverage of existing rules, add JSON formatted output).  	|  
|2   	| Tuesday  	|   2020/06/02	| Check how common known issues are: not common enough to focus on at this point. Meet with Max. Documentation and cleaning existing code. Update objective sheet and issues on github  	|  
|3   	| Wednesday  	|  2020/06/03 	| Make flask API to query commodify module. Coordinate with Rachit and Himanshu re. numeral conversion module.   	|  
|4   	| Thursday  	|   2020/06/04	| Weekly meeting. Share and discuss sample data on slack. HMM experiments: check whether existing HMM states are accurate enough for use in commodity ID (they aren't). 	|  
|5   	| Friday  	|   2020/06/05	| Setup wordnet. Start work on hypernym experiments (fetch hypernym chain and start filtering useless word senses). 	|  
|6   	| Saturday  	|   2020/06/06	|   	|  
|7   	| Sunday  	|   2020/06/07	|   	|  
