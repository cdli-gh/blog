---
layout: page
title: numerals
author: "Logan Born"
tags: ["project","gsoc","gsoc2020","numerals","eval#1","week#2"]
---

## Analysis of Accounting Corpora
This project seeks to produce exploratory visualizations of CDLI accounting corpora. The final product will comprise a pipeline which identifies counted objects in a corpus and converts the associated count from Sumerian to arabic numerals. A Flask API will return a summary data file listing all of the counted objects in the corpus, all of the counts associated with each object, and all of the collocations between counted objects. An online visualization will display this information to readers in an accessible format, with options to filter the visualization to focus on objects or relationships of interest.

The goal is to present the information from these corpora in an accessible manner to facilitate exploration of the ancient economy and society.

Code available [here](https://github.com/MrLogarithm/cdli-accounting-viz)

### Objectives and Deliverables

#### Essential Objectives

|\#|Objectives|Associated Deliverables|Notes|issue(s)|  
|---	|---	|---	|---	|---	|  
|1   	| Numeral conversion   	| ~~i. Python script to convert transliterated cuneiform numerals into arabic numerals (e.g. *1(disz) 1(u) gin2* &#8614; 1.167)~~ <br/><br/> ~~ii. API endpoint to access this script~~ 	| **API is ready but not hosted anywhere yet.** <br/><br/> NB notations can be ambiguous: if user does not specify a number system to use, the script returns a list of possible readings. <br/><br/> ~~Update to handle variant spellings (e.g. *disz* vs *di&#353;*)~~ <br/><br/> ~~To-do: What is the meaning of \|ASZxDISZ\|?~~ 	| [#1](https://github.com/MrLogarithm/cdli-accounting-viz/issues/1) [#2](https://github.com/MrLogarithm/cdli-accounting-viz/issues/2) [#3](https://github.com/MrLogarithm/cdli-accounting-viz/issues/3) [#4](https://github.com/MrLogarithm/cdli-accounting-viz/issues/4) [#5](https://github.com/MrLogarithm/cdli-accounting-viz/issues/5)	|  
|2   	| Entry segmentation  	| ~~i. Python script to segment documents into entries.~~  	| Script segments a text using numerals as delimiters. This works except for the final entry: during objective 3, when totals are recorded (*... dur 1(disz) ...*) remember that *dur* "total" must be removed as it is not a counted object. (More generally, descriptors and explanations will have to be stripped: consider e.g. *1(asz@c)-ta szu ba-ti ezem sze gu7 {d}nansze-ka sa6-sa6 dam URU-KA-gi-na lugal lagasz{ki}-ka-ke4 e-ne-ba 2(\|ASZxDISZ@t\|)*)	|	|  
|3   	| Commodity identification  	| ~~i. Python script which uses a rule-based system to identify and label counted objects in an entry.~~ 	| Depends on #2 <br/><br/> A heuristic, rule-based approach will miss some counted objects and will probably label some objects incorrectly. Any extra time in the project should go towards refining this component as much as possible (see [optional objectives](#additional-objectives)). <br/><br/> <b>Done so far:</b> heuristics based on common determinatives and POS projection (based on English definitions from ePSD). High recall, middling precision: next step should be manual pruning to improve precision (e.g. *lugal* is not a commodity) and some consideration of morphology to improve recall.	| 	|  
|4   	| Data extraction  	| i. Python script which produces JSON summary of counted object frequencies and number of times goods co-occur. <br/><br/> ii. API endpoint to serve this JSON data.  	| Depends on #3 <br/><br/> To ensure the API returns accurate data, must always fetch the most recent version of the corpus.  	|	|  
|5   	| Visualizations  	| i. Static HTML page with interactive, exploratory visualizations of the extracted data. <br/><br/> ii. Filtering options, implemented as standalone scripts to permit later integration with CDLI search. 	| Depends on #4 <br/><br/> See details [below](#visualization-details). 	|	|  
|6   	| Framework integration  	| Integrate the preceding deliverables into the existing CDLI framework wherever possible.  	|   	|	|  

##### Visualization Details
Feedback from prospective users will guide the exact format of the visualizations. Information to be visualized includes:
* Summaries of item frequency 
* Measures of central tendency and variation in an item's counts; if possible, identifying items with multimodal distributions
* Item collocations
* Similarity between item distributions

#### Additional Objectives

|\#|Objectives|Associated Deliverables|Notes|issue(s)|  
|---	|---	|---	|---	|---	|  
|1   	| Improved commodity identification  	| Extend objective 3 (commodity identification) to use POS tags and NER to identify and label counted objects in an entry. 	| If POS tagging is not available at this point in the project, we can align and project annotations from English until a better system comes along.  	|	|  
|2   	| Extra languages  	| Extend all components to include support for additional scripts and languages (e.g. Akkadian, proto-cuneiform, proto-Elamite).  	| Resources are more limited for languages which are not Sumerian.  	|	|  

<!--
<br/><br/> Very long term (likely beyond the scope of the summer of code) some form of dependency parsing would be helpful to disambiguate owners from owned objects, and to identify adjectival modifiers (e.g. to distinguish whole fish from filleted fish). Is there data available to train such a model?
-->

### Tentative timeline  

**Month 1:** complete pipeline to extract data from the corpus and API to serve as JSON

**Month 2:** first batch of visualizations complete, from sketches through filtering tools to final demo

**Month 3**: all visualizations complete, and final integration with CDLI framework

| Week  |Objectives |Deliverables |  
|---|---|---|  
|1| ~~Entry segmentation~~ & Commodity identification   |   Scripts for ~~(i) segmentation~~; ~~(ii) commodity labeling~~ (done in most basic form, needs refinement) |  
|2| Data extraction  | Script to convert corpus text file into JSON data  |  
|3| Full pipeline complete  | API endpoint which fetches most recent corpus and serves extracted data  |  
|4| Sketches and feedback; start filtering tools  | Sketches delivered to prospective users  |  
|5| Filtering tools  | Script implementing filtering tools: query &#8614; list of matching texts  |  
|6| Start Viz Work | Demo  |  
|7| Viz  | Demo  |  
|8| Viz  | Demo  |  
|9| Finalize Viz | Final Demo  |  
|10| Test cross-browser compatibility & visual polish  |   |  
|11| User guide, begin framework integration  |   |  
|12| Integration with CDLI framework  |   |

