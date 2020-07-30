---
layout: page
title: "API Week #8: More Linked Data"
author: "Lars Willighagen"
tags: ["week","gsoc","gsoc2020","api","eval#2","week#8"]
---

Deliverable: Finish links to journal system\*

\* Journal system may not be ready for that yet

Other deliverables to complete:
  - Functional API for linked data (RDF and JSON-LD)
  - Documentation and URIs for the schema of RDF, XML and JSON-LD files
  - Functional API for inscriptions and annotations (see [!149](https://gitlab.com/cdli/framework/-/merge_requests/149))

## Week Summary

### Linked data

This week I made linked data exports (not in a merge request yet). The first step
was to make JSON-LD based on the existing database structures in PHP. This is
currently done by taking database columns as fields. Because column names are not
globally unique, the fields have to be prefixed by the table name, separated by
a hyphen. Type URIs are just the table name, without hyphen or field. Both URI
types are prefixed with `https://cdli.ucla.edu/docs/schema/1.0#`, where `1.0` is
the schema version.

Entity URIs are all prefixed with `https://cdli.ucla.edu/`. In case of artifacts,
the ID is the CDLI number. This produces the same type of URLs as are currently
used to cite and permalink to artifacts. Other entities like publications and
materials have URIs like `https://cdli.ucla.edu/publications/1#this` and
`https://cdli.ucla.edu/materials/1#this` respectively.

Different representations of the linked data were easily produced with the
[EasyRDF](https://www.easyrdf.org/) library. The supported formats are JSON-LD,
N-Triples, [Turtle](https://www.w3.org/TR/turtle/), XML-RDF and [RDF-JSON](https://www.easyrdf.org/docs/rdf-formats-json).
The JSON-LD is written in such a way that it doubles as a regular JSON export,
just with some added properties (`@id`, `@type` and `@context`) in each entity.

Example publication:

```turtle
@prefix cdli: <https://cdli.ucla.edu/docs/schema/1.0#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://cdli.ucla.edu/publications/1#this>
  a cdli:publication ;
  cdli:publication-bibtexkey "Abusch1981"^^xsd:string ;
  cdli:publication-book_title "In Honor of Ernest R. Lacheman on His Seventy-fifth Birthday, April 29, 1981"^^xsd:string ;
  cdli:publication-entry_type <https://cdli.ucla.edu/entry-types/7#this> ;
  cdli:publication-entry_type_id 7 ;
  cdli:publication-id 1 ;
  cdli:publication-pages "1-9"^^xsd:string ;
  cdli:publication-publisher "Eisenbrauns: Winona Lake"^^xsd:string ;
  cdli:publication-series "SCCNH"^^xsd:string ;
  cdli:publication-title "Notes on a Pair of Matching Texts: A Shepherd&rsquo;s Bulla and an Owner&rsquo;s Receipt"^^xsd:string ;
  cdli:publication-volume "1"^^xsd:string .
```

Example artifact (shortened):

```turtle
@prefix cdli: <https://cdli.ucla.edu/docs/schema/1.0#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://cdli.ucla.edu/P000001>
  a cdli:artifact ;
  cdli:artifact-ark_no "21198/zz001q0dtm"^^xsd:string ;
  cdli:artifact-artifact_type <https://cdli.ucla.edu/artifact-types/4#this> ;
  cdli:artifact-artifacts_composites <https://cdli.ucla.edu/artifacts-composites/8369#this> ;
  cdli:artifact-artifacts_seals <https://cdli.ucla.edu/artifacts-seals/1#this> ;
  cdli:artifact-collections <https://cdli.ucla.edu/artifacts-collections/1#this> ;
  cdli:artifact-designation "CDLI Lexical 000002, ex. 065"^^xsd:string ;
  cdli:artifact-excavation_no "W 06435,a"^^xsd:string ;
  cdli:artifact-findspot_comments "auf Hügeloberfläche in der Nähe des Südbaues"^^xsd:string ;
  cdli:artifact-findspot_square "M XVIII,?"^^xsd:string ;
  cdli:artifact-genres <https://cdli.ucla.edu/artifacts-genres/1#this> ;
  cdli:artifact-languages <https://cdli.ucla.edu/artifacts-languages/1#this> ;
  cdli:artifact-materials <https://cdli.ucla.edu/artifacts-materials/1621#this> ;
  cdli:artifact-museum_no "VAT 01533"^^xsd:string ;
  cdli:artifact-period <https://cdli.ucla.edu/periods/4#this> ;
  cdli:artifact-provenience <https://cdli.ucla.edu/proveniences/105#this> ;
  cdli:artifact-publications <https://cdli.ucla.edu/artifacts-publications/1#this>, <https://cdli.ucla.edu/artifacts-publications/221241#this>, <https://cdli.ucla.edu/artifacts-publications/555708#this>, <https://cdli.ucla.edu/artifacts-publications/890248#this>, <https://cdli.ucla.edu/artifacts-publications/1224788#this>, <https://cdli.ucla.edu/artifacts-publications/1559328#this>, <https://cdli.ucla.edu/artifacts-publications/1559329#this> ;
  cdli:artifact-thickness 18 ;
  cdli:artifact-width 61 .
```

[Full examples can be found here](https://gitlab.com/cdli/framework/-/issues/126#note_384123352).

With a short script and a structure-only SQL export I could generate documentation
for the fields and types, to be placed under the URIs used in the RDF files.
Complex fields (any field linking to other entities) were produced by output of
a short PHP script going through the table registry and listing all associations.

```php
// <?php

use Cake\DataSource\ConnectionManager;
use Cake\ORM\TableRegistry;
use Cake\ORM\Association\BelongsToMany;

$tables = [];

foreach (ConnectionManager::get('default')->schemaCollection()->listTables() as $name) {
    $table = TableRegistry::get($name);
    $associations = [];
    foreach ($table->associations() as $association) {
        $associations[] = [
            $association->getProperty(),
            $association->type(),
            $association instanceof BelongsToMany
                ? $association->junction()->getEntityClass()
                : $association->getTarget()->getEntityClass()
        ];
    }
    $tables[$name] = $associations;
}

echo json_encode($tables);
```

For compatibility, some (or many) fields may need to be mapped to more common
schemas, genera; ones like schema.org, Dublin Core and more field-specific ones
as well.

### Other progress

Additionally, the merge request involving the updated database models was merged,
which cleared the way for the tabular export merge request to be merged as well.
Next will be the Inscription API, which will have to wait until the relevant
people can review.

### Journal bibliographies

On the deliverable of this week:

  - There is a tracking issue for linking bibliographies to the publication
    database ([#229](https://gitlab.com/cdli/framework/-/issues/229)). Already,
    there is a table that links articles to their publications which can be used
    in the future.
  - I have not found how articles currently look like online, and how the
    bibliographies could be added.
  - Exporting _articles_ as citations should be possible as well, though I need
    to add the relevant components and add support for article metadata in the
    backend.

Ergo, the links are mostly in place but not yet connected.

## Daily Work Update

| # | Day | Date       | A short description of the work done |
|---|-----|------------|--------------------------------------|
| 1 | Mon | 2020/07/20 | Make JSON API, research XML and JSON-LD/RDF APIs |
| 2 | Tue | 2020/07/21 | Make XML API |
| 3 | Wed | 2020/07/22 | Make all linked-data APIs, generate schema documentation |
| 4 | Thu | 2020/07/23 | Have [!134](https://gitlab.com/cdli/framework/-/merge_requests/134) merged; update WIP merge request ([!146](https://gitlab.com/cdli/framework/-/merge_requests/146)) |
| 5 | Fri | 2020/07/24 | Have [!146](https://gitlab.com/cdli/framework/-/merge_requests/146) merged |
| 6 | Sat | 2020/07/25 |  |
| 7 | Sun | 2020/07/26 | Start reviewing [!156](https://gitlab.com/cdli/framework/-/merge_requests/156) |
