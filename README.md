# MAVE Minimum Information Model

[![arXiv](https://img.shields.io/badge/arXiv-2306.15113-b31b1b.svg)](https://arxiv.org/abs/2306.15113)
[![DOI](https://zenodo.org/badge/634403007.svg)](https://zenodo.org/badge/latestdoi/634403007)

JSON Schema for validating MAVE experiment metadata

*Purpose:* To provide an overarching organization and definitions for terms relevant to tech development and data
repositories associated with the [Atlas of Variant Effects Alliance](https://www.varianteffect.org).
This "controlled vocabulary" and standard is intended to give structure to minimum required information for data and
meta-data sharing for scientists using variant effect mapping technology.

## How to use this repository

This repository contains an implementation of the schema described in the
[Atlas of Variant Effects Alliance](https://www.varianteffect.org) minimum information model for describing a
multiplexed assay experiment.

Overall, it is felt that minimum standard reporting should include information on
(1) means and characteristics of genetic perturbation,
(2) details of the phenotypic assay employed to identify variant effects,
(3) information on the cellular and environmental context(s) in which the assays were carried out, and
(4) details of sequencing strategy for variant-effect associations.

The schema defines a set of required and optional fields and possible values that can be used to validate a minimum
information document.
The implementation is found in the [schema](schema/) directory.

In addition to the structure of the minimum information model, the schema also defines controlled vocabulary terms for
describing one of these experiments.

The [examples](examples/) directory contains examples of this type of document describing real experiments, as well as a simple
Python script that will run the schema validation using [jsonschema](https://pypi.org/project/jsonschema/).
Many other implementations of the JSON Schema standard are available in other languages (see
[here](https://json-schema.org/implementations.html)).

Please note that although we are using the JSON Schema standard, the schema source file is written in YAML format for ease in human
reading/writing, and processed to JSON using the provided [Makefile](schema/Makefile).

## Reading the schema

The [schema](schema/) directory contains JSON and YAML representations of the minimum information standard and controlled vocabulary
expressed as JSON Schema. There are multiple levels of required information that can be browsed hierarchically.
Most fields include a description that details the intention of that field and the type of information that is to be provided.

For many fields, there is an enumerated list of valid values corresponding to the controlled vocabulary terms that must
be used to describe the experiment.

The general schema structure and terms are also described below. The YAML documents in the [schema](schema/) directory should be
considered the authoritative structure and source of information where discrepancies exist.

### Applying the schema to your datasets

Unless you are an experienced YAML user who is able to read the [schema/experiment.yml](schema/experiment.yml) file yourself, we recommend
choosing the most closely-related example file as a starting point and modifying it as needed.

The repository currently contains three examples:

- [examples/Findlay_2018.yml](examples/Findlay_2018.yml) describes a saturation genome editing (SGE) experiment on BRCA1, involving CRISPR-based
editing of the endogenous locus and measuring cell survival in HAP1 cells
([PubMed reference](https://pubmed.ncbi.nlm.nih.gov/30209399/))
- [examples/Matreyek_2018.yml](examples/Matreyek_2018.yml) describes a deep mutational scan of PTEN, expressed using a designed construct integrated
into the genome using a landing pad system and measuring cell fluorescence, also known as VAMP-seq
([PubMed reference](https://pubmed.ncbi.nlm.nih.gov/29785012/))
- [examples/Seuma_2022.yml](examples/Seuma_2022.yml) describes a deep mutatational scan of amyloid beta, expressed episomally and measuring the
effect on yeast growth ([PubMed reference](https://pubmed.ncbi.nlm.nih.gov/36400770/))

The schema starts with some descriptive metadata, such as the title and abstract.
The title and abstract should reflect the experimental dataset reflected in a study (which may optionally reference a published document that may
have a differing title).
The `title` and `abstract` are required properties.

The next section (`document`) describes a publication associated with the experiment (if any).
This part of the schema is optional, but if used, must minimally include a `ref` property with a URI (such as a [DOI](https://www.doi.org/))
linking to the publication.

The [variantLibrary](#variant-library) and [phenotypicAssay](#phenotypic-assay) describe the experiment that was performed and both are required.
Each has several subsections that provide structure for detailing the important experimental design decisions captured by the schema.
We refer users to the examples and the list of [controlled vocabulary terms](#controlled-vocabulary-terms) below to help complete this section,
as it will be different for each experiment.

*Note:* We anticipate that the standard will be adopted by established resources such as [MaveDB](https://www.mavedb.org) that will provide
users with the ability to download a minimum information file after data deposition.

### Generating sequence identifiers

Some examples (e.g. `examples/Seuma_2022.yml`) include target sequence identifiers and hashes.
These values were generated according to the [GA4GH VRS v1.3](https://vrs.ga4gh.org/) and [refGet](http://samtools.github.io/hts-specs/refget.html)
standards (see [here](https://vrs.ga4gh.org/en/stable/impl-guide/computed_identifiers.html) for details).

Generating these stable identifiers is not required but is recommended, particularly for in-vitro construct libraries.

## Controlled vocabulary terms

### Overview of ontologies and identifiers

Concept codes used by the schema follow the `Coding` model, which describes concepts as objects with a `code` and `label` used by a
`system` (or `version` of a `system`).

For describing assay readouts, we recommend the use of terms from the
[Ontology for Biomedical Investigations](https://obi-ontology.org/).

For describing human diseases relevant to the assay, we recommend using terms from [OMIM](https://www.omim.org/) or
the [Mondo Disease Ontology](https://mondo.monarchinitiative.org/).

For describing human cell lines, we use terms from the [Cell Line Ontology](http://obofoundry.org/ontology/clo.html),
where available.

We encourage users to provide an [NCBI Taxonomy ID](https://www.ncbi.nlm.nih.gov/taxonomy) that specifically denotes
the organism (including strain, where applicable).

### Variant Library

This section describes the scope and characteristics of a variant library: a collection of sequence variants for a MAVE experiment
that are derived from a common target sequence.

#### Target sequences

A collection of sequences used as references from which all variants in the library are defined. This collection is defined as a
set of `ReferenceSequence` objects, each defined by the following properties:

`id`: an identifier for the sequence.
`sha512t24u`: the GA4GH `SQ.` identifier (see [here](https://vrs.ga4gh.org/en/stable/impl-guide/computed_identifiers.html) for
details).
`sequence`: the literal sequence as a string of [IUPAC single character codes](https://www.bioinformatics.org/sms/iupac.html).
`sequenceAlphabet`: one of `na` (nucleic acids) or `aa` (amino acids) for interpreting IUPAC character codes in the `sequence`.

#### Library scope

The variant library should be defined by the functional scope of DNA elements introduced into the library.
DNA elements can have known or unknown functions. Example functions include a gene, an exon or set of exons included in a
transcript, a set of enhancers, a set of repressors, etc.

We define the scope type using the following controlled vocabulary terms:

- coding
- intronic
- non-coding, regulatory
- non-coding, other

Libraries may be further described with `description`. The `description` field must be populated for any
library of type `non-coding, other` (e.g. tRNA libraries).

#### Library generation method

The methods used to generate the library. A library may create and integrate an *in vitro* construct or directly edit an
endogenous locus. The library generation method is defined by its `type`, which may be one of:

- in-vitro construct library
- endogenous locus library

##### In-vitro construct library method

A methodology for generating and integrating an exogenous variant library.

For *in-vitro* constructs, `system` is one of the following controlled vocabulary terms:

- oligo-directed mutagenic PCR
- error-prone PCR
- nicking mutagenesis
- microarray synthesis
- site-directed mutagenesis
- doped oligo synthesis
- oligo pool synthesis
- proprietary method
- other

In addition, `integration` refers to the mechanism for integration or expression of an exogenous construct and is one of
the following controlled vocabulary terms:

- native locus replacement
- extra-local construct insertion
- random locus viral integration
- episomal delivery
- plasmid (not integrated)
- transfection of RNA

`system` and `integration` are required properties. `description` may be used to further describe the generation method
`system` and `integration` parameters, and is required if the `system` is set to `other`.

##### Endogenous locus library method

A methodology for generating a variant library at an endogenous locus.

For endogenous editing, `system` refers to the CRISPR/Cas system used, and is one of the following controlled vocabulary terms:

- SpCas9
- SaCas9
- AsCas12a
- RfsCas13d

In addition, `mechanism` is used to define the functional mechanism of the method, and is one of the following controlled vocabulary
terms:

- nuclease
- base editor
- prime editor

`system` and `mechanism` are required properties. `description` may be used to further describe the generation method
`system` and `mechanism` parameters.

#### Delivery method

The delivery method specifies how the variant induction machinery and/or construct was delivered to the cell/organism
(e.g. viral transduction, electroporation, transfection and MOI).

The delivery method is specified by the `type` property and must be one of the following controlled vocabulary terms:

- electroporation
- nucleofection
- chemical-based transfection
- adeno-associated virus transduction
- lentivirus transduction
- chemical or heat shock transformation
- other

The `type` property is required. Additional detail about the delivery method may be provided with the `description` property.

### Phenotypic assay

A physical adjudication of model system that allows for systematic interrogation of a functional read-out for a large
amount of genetic variants (e.g. cell size and mode of adjudication, action potential characteristic(s) and mode of
measurement, expression of a particular factor and mode of measurement (FACS, sc-RNA-seq), or transcript expression
(bulk RNA-seq)).

#### Dimensionality

Dimensionality defines how many phenotypes and of what complexity are included in the map.

Dimensionality is primarily defined by its `type`, which must be one of the following controlled vocabulary terms:

- single-dimensional data
- high-dimensional data
- combined functional data

where `single-dimensional data` refers to experiments with a single dimension (e.g. FACS fluorescence from a single protein was used),
`high-dimensional data` refers to experiments with multiple dimensions (e.g. ML/AI enabled cell imaging/classification), and
`combined functional data` refers to experiments where multiple phenotypic assays were combined to make a map.

The `type` property is required. Additional information about the `dimensionality` of an experiment may be provided using the
`description` property.

#### Replication

Assay replication work performed is defined by its `type`, which must be one of the following controlled vocabulary terms:

- biological
- technical
- biological and technical
- no replication

The `type` property is required. Additional detail about the replication method may be provided with the `description` property.

#### Method

The assay method, defining the molecular properties interrogated by the experiment. Terms are derived from OBI subtree with root
[OBI_0000070: “assay”](http://purl.obolibrary.org/obo/OBI_0000070) where appropriate. Term mappings to OBI concept identifiers
are available in the controlled vocabulary definitions file. The method is specified by the `type` property, which must be one of
the following controlled vocabulary terms:

- promoter activity detection by reporter gene assay
- bulk RNA-sequencing
- single-cell RNA sequencing assay
- fluorescence in-situ hybridization (FISH) assay
- flow cytometry assay
- imaging mass cytometry assay
- systematic evolution of ligands by exponential enrichment assay
- single cell imaging
- multiplexed fluorescent antibody imaging
- binding assay
- cell proliferation assay
- survival assessment assay
- other

#### Relevance

The disease or biological processes the assay is relevant to. Relevance is specified by an array of `Coding` objects (see
[note](#overview-of-ontologies-and-identifiers)). We recommend relevance to be described by terms from [OMIM](https://www.omim.org/)
or the [Mondo Disease Ontology](https://mondo.monarchinitiative.org/).

#### Model system

The model system context that influences expression of the phenotype. The model system is specified by the `type` property and must 
be one of the following controlled vocabulary terms:

- immortalized human cells
- murine primary cells
- induced pluripotent stem cells from human male
- induced pluripotent stem cells from human female
- patient derived primary cells (e.g. T-cells, adipocytes)
- yeast
- bacteria
- bacteriophage
- molecular display
- other

We recommend that cell lines are further described by relevant concepts using the `codings` array of `Coding` objects (see
[note](#overview-of-ontologies-and-identifiers)). We recommend that cell lines are described using the Cell Line Ontology
where applicable. Some commonly used cell lines and model systems are listed below:

| Cell | CLO Term | NCBI Taxonomy ID |
|------|----------|------------------|
| Yeast | n/a | 4932 |
| HEK293T | 37372 or 37373 | 9606 |
| HAP1 | missing | 9606 |
| HeLa | 3684 | 9606 |
| *E. coli* | n/a | 562 |
| iPSC-derived | 37308 | 9606 |
| *C. elegans* | n/a | 6239 |
| *C. savignyi* | n/a | 51511 |
| *D. melanogaster* | n/a | 7227 |
| HepG2 | 3704 | 9606 |
| Human hepatocytes | 182 | 9606 |
| K562 | 7050 | 9606 |
| Mouse embryonic stem cells | 37317 | 10090 |
| NIH3T3 | missing | 10090 |
| Bacteriophage | n/a | 38018 |
| Cell-free | n/a | n/a |

The `type` property is required. Additional detail about the model system may be provided with the `description` property.

**Environmental variables** – variance of environmental factors included in the experiment
(e.g. addition of specific compounds to cell media, temperature controls, time course, CRISPR interference by KRAB,
KRAB-MeCP2, CRISPR activation by VPR, SAM, or SunTag, etc.)

Controlled vocabulary terms (select one):

- Yes - If yes, please describe this in detail in the free text methods describing your assay.
- No

#### Variant sequencing characteristics

This section details the method for accurately capturing variant frequency associated with outcome of phenotypic assay.

**Library profiling strategy** – approach used to quantify variants in the population

Controlled vocabulary terms (select one):

- Direct sequencing
- Shotgun sequencing
- Barcode sequencing

Controlled vocabulary terms (select one):

- Single segment (short read)
- Single segment (long read)
- Multi-segment
