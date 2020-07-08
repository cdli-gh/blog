---
layout: page
title: "API: First Evaluation"
author: "Lars Willighagen"
tags: ["eval","gsoc","gsoc2020","eval#1"]
---

## Summary
In phase 1, spanning the past 4 weeks, I worked on implementing the Bibliography
API, both the internal one and the public-facing REST API. I also documented how
this API and others should be implemented, to ensure consistency between
implementations.

Bibliography exports can now be fetched with file extensions (for BibTeX and
[RIS](https://dev.to/citation-js/creating-a-ris-mapping-from-the-original-specification-1kfo))
and with `Accept` HTTP headers. Although this is currently implemented for only
artifacts and publications, the code for processing the request parameters is
extracted into a component which, when loaded, automatically adds bibliography
export support to any given controller.

```bash
# run the app locally
./cdlidev up

# fetch example data
curl -H 'Accept: application/x-bibtex' http://127.0.0.1:2354/artifacts/1
```

The data is formatted on Docker container with a NodeJS server running
[Citation.js](https://citation.js.org), a library that I developed. The container
running CakePHP then communicates with the internal server to input data and
respond with the output. This communication is abstracted away by a helper. The
helper's implementation however, requires a configuration change that still needs
to be discussed.

## Deliverables

This phase concludes\* objective A2.

| Week | Objectives | Deliverables | Status |
|-----:|------------|--------------|--------|
|    1 | Prepare non-PHP scripts | Documentation on how to call external scripts from CakePHP | Most of the documentation was complete in the first week, the rest followed in week 3. |
|    2 | Setup Bibliography API | Functional internal Bibliography API | Complete* |
|    3 | Finish Bibliography API | Functional Component and REST API | Complete* |
|    4 | Prepare data for catalogue API | Prepared ATF and CONLL files | Already completed; the files are represented in newer versions of the database. |

\*: The merge request is not yet merged, as the framework needs to be updated
    and that updated image needs to be published.

## Learning and success
Working with PHP and the CakePHP framework has been a blast, even though I am
new to both. Not only is the code I wrote functional, it also looks nice, in my
opinion anyway. Implementing functionality with my own software library (used for
the bibliography exports) also helps me see the perspective of an application
developer, instead of the library author.

## Difficulties
The merge request containing most of my work of the past 4 weeks is stuck because
we need to update the framework version. This is taking a while, but I hope I
can address it in this week's meeting and fix things before Friday.

The processes of working together, e.g. merging code and adhering to coding
styles, has been a bit difficult for me. Everyone's interpretation is a bit
different resulting in code that I would have written differently myself.
However, when reviewing such code I need to provide constructive criticism, not
push my personal opinions. I think that is going well though.

## Plan update
I hope that, after this phase is completed, I can carry on without much
difficulty. I am more or less on schedule with my side of things, and though
there are some challenging objectives on my path I believe I can complete them.
Additionally, now that the university semester is done, I can spend more time on
this project.
