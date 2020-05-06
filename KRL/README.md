# Knowledge Embeddings and Knowledge Representation Learning

## Introduction

Definition: Knowledge Graphs/Bases describes real-world *entities* and their *relations*, organized in a *graph*.

A graph consists of a RDF triplet `(Subject or Head, Relation, Object or Tail)`. 

There are three elements within a knowledge graph:
- **Entities**: Named objects in the world
- **Properties**: Relationships between two entities
- **Types**: Sets or classes of entities
    - Entity types (attributes)
    - Relationship types

TODO: ABox (assertion) vs. TBox (terminology)

![](https://i.imgur.com/RgdX0El.png)

> [Google's Introduction of Knowledge Graph](https://www.youtube.com/watch?v=mmQl6VGvX-c&feature=emb_title)

## Fields of Interest
- Knowledge Graph Completion
- Knowledge Extraction
- Knowledge Graph Refinement
- Error Detection

## Challenges of scaled KGs
![](https://i.imgur.com/51QT3UU.png)

## Knowledge Extraction Process
1. Information Retrieval
2. Information Extraction
    - Dependency Parsing, Part of Speech, Named Entity Recognition (Entity Extraction)
    - Document Coreference Resolution
    - Entity Resolution, Entity Linking, Relation Extraction

## Problems in Information Extraction
The below problems could be solved via supervised(manual), semi-supervised, unsupervised, which has a precision and recall trade-off.
1. Defining domain: Define subset of types, discover new types, nouns as entities and verbs as relation
2. Learning extractors: Create examples, find patterns
3. Scoring candidate facts: human defined, multiple iterations, confidence threshold

## RDF Parsers/Serializers
- Notation3 (.n3)
- Turtle (.ttl)
- N-Triples (.nt)

## Open KGs/Datasets
- [Freebase Dumps](https://developers.google.com/freebase) (`.nt`)
- [Wikidata Dumps](https://www.wikidata.org/wiki/Wikidata:Database_download) (`.json`, `.ttl`, `.nt`, `.xml`)
- [DBpedia](https://wiki.dbpedia.org/develop/datasets) (`.ttl`)
- [YAGO](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/yago-naga/yago/downloads/) (`.ttl`, `.tsv`)
- [KB Datasets](https://github.com/villmow/datasets_knowledge_embedding)

## Glossary

RDF: Resource Description Framework is a standard model for interchanging data on the web even if the underlying schemas differ.

Semantic Web: is a vision of a web of linked data proposed by Tim Berners-Lee. It is thought of as an extention of the current World Wide Web in which applications are connected to form a consistent logical web of data and information is given a well-defined meaning (semantics), making it readable not only to humans, but also machines

Ontology: (Metaphysics, Philosophy) a study of the nature of existence and the structure of reality. (Semantic Web) Ontology investigates the categories of things that exist or may exist in a particular domain. Ontologies are used to refer to the semantic understanding, the conceptual framework of knowledge, shared by individuals who participate in a given domain. 

OWL: is a semantic web language designed to represent rich and complex knowledge about things, groups of things, and relations between things.




