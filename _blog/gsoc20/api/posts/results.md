---
layout: page
title: "API: Final Report"
author: "Lars Willighagen"
tags: ["gsoc","gsoc2020","api"]
---

This post evaluates the results of the entire API project. For information on
the project itself, see [the index page](../).

## Objectives and Deliverables

### Essential Objectives

| \# | Objectives | Associated Deliverables | Status |
|----|------------|-------------------------|--------|
| A1 | Make CDLI framework API | An API for artifact data and inscriptions | ✔️ |
| A2 | Make publication metadata API | An API for bibliographical data | ✔️ |
| A3 | Convert database to new schema | Richer data to be used for the APIs | partial |
| A4 | Define and document URIs for linked data | i. URI schema for database fields ii. Documentation at those URIs | ✔️ |
| A5 | Make CDLI framework search API | An API for search results | partial |
| A6 | Use publication metadata API in journal system | Journal system were references can be linked to the general database for display | ❌ |

#### A1: Make CDLI framework API

Status complete. The catalog supports three types of exports:

  - JSON
  - Tabular exports
  - Linked data

On all entities in the catalog, both requesting individual entities and paginating
through the entire list is supported. The pagination is achieved by using the
`Link` HTTP header. For more details, see [the post of Week 11](13_week11). The
JSON format is a slightly modified representation of the data as used internally.
This format is documented in the framework. The tabular exports are designed to
be compatible with the format used for importing data.

The linked data is a different story. I started out with getting as much data out
there, in as many different formats available ([week 8](9_week8)). This meant
that the actual schema was entirely based on the database fields, and so neither
stable nor meaningful. If I was going to solve the first one I might as well
solve the second one, so after I was pointed to earlier work (Chiarcos et al., 2018)
I started working on mapping the database to CIDOC-CRM (ICOM/CIDOC et al., 2011).

For archaeological data I used (Bekiari, 2014; Definition of the CRMarchaeo, 2019).
For bibliographical data, which was already stored in the BibTeX format, an
existing URI for BibTeX was used. I covered various concepts that were relatively
specific to the CDLI catalog by defining a number of our own classes. These are
documented in the framework as well, and available as OWL in RDF and Turtle.

To represent the CIDOC-CRM ontology I had to make some decisions regarding data
primitives defined by both RDF standards and the ontology. These decisions, and
others regarding the use of CIDOC-CRM in RDF-like linked data were guided by
(Doerr et al., 2020).

Specific to inscriptions is the inscription API, which supports export in the
formats ATF, CDLI-CoNLL and CoNLL-U. The CoNLL is also represented in the
linked data of the inscription, in the form of CoNLL-RDF (Chiarcos & Fäth, 2017).

#### A2: Make publication metadata API

Status complete. Implemented as a thin wrapper around [Citation.js](https://citation.js.org), though some custom converters were made for internal representations
of the data.

#### A3: Convert database to new schema

I have written down a number of changes to the database to make working with the
data easier, but these changed have not been applied to the existing database yet.

#### A4: Define and document URIs for linked data

Complete; see objective A1 above.

#### A5: Make CDLI framework search API

Since pagination is supported and given the way the APIs are implemented adding
API results to the search pages is relatively trivial. However, given the search
pages are still being worked on as of writing, the APIs are not yet added.

#### A6: Use publication metadata API in journal system

The API for returning bibliographies based on the linked metadata is complete.
The functionality for linking articles and publications was added by Nisheal and
Ajit. However, as of writing the combined functionality has not been added to the
user interface.

### Additional Objectives

| \# | Objectives | Associated Deliverables | Status |
|----|------------|-------------------------|--------|
| B1 | Make API for conversion services | An API for conversion services related to inscription and/or metadata formats | ❌ |
| B2 | Add (linked) data to (artifact) pages | Pages with Schema.org/Dublin Core annotations | partial |
| B3 | Document progress | Technical documentation for API use, use of data, etc. | ✔️ |
| B4 | Extend publication metadata API to journal system | Journal system where citations of articles can be exported | partial |
| B5 | Make a SDK for the API | An SDK to consume the new API (in R?) | partial |

#### B1: Make API for conversion services

Although I added internal support for a number of conversion services and developer
documentation on how to add more, there is no public-facing API for that at the
moment.

#### B2: Add (linked) data to (artifact) pages

I added OpenGraph annotations to pages but given the low number of pages where
Schema.org and DublinCore are actually relevant I decided to give priority to
other tasks

#### B3: Document progress

Status complete. I added documentation on how the APIs work internally, for
developers to use. I also added documentation for how the OpenGraph annotations
work. Additionally, documentation for the public API is also available.

#### B4: Extend publication metadata API to journal system

Partially complete, as in the back-end is complete but not the UI.

#### B5: Make a SDK for the API

I started making a [basic API client](https://github.com/cdli-gh/framework-api-client),
but it does not have much functionality yet.

### Bibliography

Bekiari, C. (2014, September 6). CRMarchaeo: Modelling Context, Stratigraphic Unit, Excavated Matter [Tutorial]. CIDOC 2014, Dresden.

Chiarcos, C., & Fäth, C. (2017). CoNLL-RDF: Linked Corpora Done in an NLP-Friendly Way. In J. Gracia, F. Bond, J. P. McCrae, P. Buitelaar, C. Chiarcos, & S. Hellmann (Eds.), Language, Data, and Knowledge (pp. 74–88). Springer International Publishing. https://doi.org/10.1007/978-3-319-59888-8_6

Chiarcos, C., Pagé-Perron, É., Khait, I., Schenk, N., & Reckling, L. (2018, May). Towards a Linked Open Data Edition of Sumerian Corpora. Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018). https://www.aclweb.org/anthology/L18-1387

Definition of the CRMarchaeo: An Extension of CIDOC CRM to support the archaeological excavation process. (2019). PIN, University of Florence, Italy.

Doerr, M., Light, R., & Hiebel, G. (2020, January). Implementing the CIDOC Conceptual Reference Model in RDF. 45th joint meeting of the CIDOC CRM SIG and SO/TC46/SC4/WG9; 38th FRBR – CIDOC CRM Harmonization, Heraklion. http://www.cidoc-crm.org/Issue/ID-443-implementing-the-cidoc-conceptual-reference-model-in-rdf

ICOM/CIDOC Documentation Standards Group, & CIDOC CRM Special Interest Group. (2011). Definition of the CIDOC Conceptual Reference Model. CIDOC-CRM. http://www.cidoc-crm.org/html/5.0.4/cidoc-crm.html

## Code

See my contributions [here](https://gitlab.com/cdli/framework/-/merge_requests?scope=all&utf8=%E2%9C%93&state=merged&author_username=larsgw).
For future visitors: be sure to look at the merge requests merged before the 6th
of September 2020, since I might have opened new ones after.
