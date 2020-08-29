---
layout: page
title: "API: Third Evaluation"
author: "Lars Willighagen"
tags: ["eval","gsoc","gsoc2020","api","eval#3"]
---

## Summary
The most interesting work that got completed in this phase was the Linked Data API,
planned for last phase. All entities in the core catalog now support exports in
linked data formats, and except for very specific, redundant fields all data is
covered. Most of the catalog is described with the [CIDOC-CRM ontology](https://www.cidoc-crm.org/)
(Doerr&nbsp;et&nbsp;al.,&nbsp;2020; ICOM/CIDOC,&nbsp;2011),
though other schemas are used for bibliographical, archaeological, geospatial and
linguistic information.

The linguistic information is generated with (Chiarcos & Fäth, 2017)
and linked based on the work described in (Chiarcos et al., 2018). In fact, the
entire model is mostly compatible with that work, except for some discrepancies
caused by the ontological difference between physical artifacts and conceptual
composites.

The general final blog post will contain more information on the contents of the
linked data specifically.

I have also worked on smaller things, finishing previous objectives and working
on the relatively smaller objectives of this phase.

### Bibliography

Chiarcos, C., & Fäth, C. (2017). CoNLL-RDF: Linked Corpora Done in an NLP-Friendly Way. In J. Gracia, F. Bond, J. P. McCrae, P. Buitelaar, C. Chiarcos, & S. Hellmann (Eds.), Language, Data, and Knowledge (pp. 74–88). Springer International Publishing. https://doi.org/10.1007/978-3-319-59888-8_6

Chiarcos, C., Pagé-Perron, É., Khait, I., Schenk, N., & Reckling, L. (2018, May). Towards a Linked Open Data Edition of Sumerian Corpora. Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018). https://www.aclweb.org/anthology/L18-1387

Doerr, M., Light, R., & Hiebel, G. (2020, January). Implementing the CIDOC Conceptual Reference Model in RDF. 45th joint meeting of the CIDOC CRM SIG and SO/TC46/SC4/WG9; 38th FRBR – CIDOC CRM Harmonization, Heraklion. http://www.cidoc-crm.org/Issue/ID-443-implementing-the-cidoc-conceptual-reference-model-in-rdf

ICOM/CIDOC Documentation Standards Group, & CIDOC CRM Special Interest Group. (2011). Definition of the CIDOC Conceptual Reference Model. CIDOC-CRM. http://www.cidoc-crm.org/html/5.0.4/cidoc-crm.html

## Objectives and Deliverables
| Week | Objectives | Deliverables | Status |
|-----:|------------|--------------|--------|
|  9   | Setup search API | Functional search API for the catalogue | partially complete |
| 10   | Annotate HTML pages | HTML pages with microdata and metadata | partially complete |
| 11   | Document APIs | API documentation | complete |
| 12   | Quality assurance and/or SDK | Integration tests, simple SDK | partially complete |

## Learning and Success
I really enjoyed working on the linked data. In total I spent at least two weeks
working on the final model, discussing with people inside and outside the project
along the way. In the end I think I have good results, too.

## Difficulties
Two deliverables are, as of writing, partially or completely blocked by other
students' deliverables. In some cases I *could* implement my functionality, but
at this point in the project I do not want to cause merge conflicts, interfering
with *their* work.

Getting non-PHP libraries to work from PHP was a bit of a hassle, but combined
with a local cache my ideas from earlier in the project turned out to be good
enough to be applied here as well.

I could unfortunately not compare my interpretation of the CIDOC-CRM ontology
because the only major implementations I could find information about, the British
Museum and the French MoDyCo, seem to have no actual information available since
at least 2018. I asked the British Museum about this at the end of July, but they
have not gotten back to me, nor acknowledged my message in any way. In fact, there
is [a Twitter bot made in October 2018](https://twitter.com/bm_lod_status)
that tweets a variation of "no" every 10 hours or so, answering the simple question
"Is the British Museum’s endpoint working?" Little to no hope there.
