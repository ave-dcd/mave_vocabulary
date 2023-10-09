# MAVE Minimum Information Model

[![arXiv](https://img.shields.io/badge/arXiv-2306.15113-b31b1b.svg)](https://arxiv.org/abs/2306.15113)
[![DOI](https://zenodo.org/badge/634403007.svg)](https://zenodo.org/badge/latestdoi/634403007)

JSON Schema for validating MAVE experiment metadata

*Purpose:* To provide an overarching organization and definitions for terms relevant to tech development and data 
repositories associated with the [Atlas of Variant Effects Alliance](https://www.varianteffect.org).

## How to use this repository

This repository contains an implementation of the schema described in the 
[Atlas of Variant Effects Alliance](https://www.varianteffect.org) minimum information model for describing a 
multiplexed assay experiment.

The schema defines a set of required and optional fields and possible values that can be used to validate a minimum 
information document.
The implementation is found in the `schema` directory.

In addition to the structure of the minimum information model, the schema also defines controlled vocabulary terms for 
describing one of these experiments.

The `examples` directory contains examples of this type of document describing real experiments, as well as a simple 
Python script that will run the schema validation using [jsonschema](https://pypi.org/project/jsonschema/).
Many other implementations of the JSON Schema standard are available in other languages (see 
[here](https://json-schema.org/implementations.html)).

Please note that although we are using the JSON Schema standard, the files here are in YAML format because it is more 
human-readable.

## Reading the schema

The `schema` directory contains a YAML representation of the minimum information standard and controlled vocabulary.
There are multiple levels of required information that can be browsed hierarchically.
Most fields include a description that details the intention of that field and the type of information that is to be 
provided.

For many fields, there is an enumerated list of valid values corresponding to the controlled vocabulary terms that can 
be used to describe the experiment.

The general schema structure and terms are also described below. 
The YAML documents in the `schema` directory should be considered the authoritative structure and source of information 
where there are discrepancies.

### Generating sequence identifiers

Some examples (e.g. `examples/Seuma_2018.yml`) include target sequence identifiers and hashes.
These values were generated according to the [GA4GH VRS](https://vrs.ga4gh.org/) standard (see 
[here](en/stable/impl-guide/computed_identifiers.html)) for details.

Generating these stable identifiers is not required but is recommended, particularly for in-vitro construct libraries.

## Controlled vocabulary terms

### Important acronyms

#### Multiplexed Assays of Variant Effects (MAVEs)

Experimental assays involving scaled, pooled genetic perturbation of a naturally occurring or synthetic DNA element 
followed by multiplexed high-throughput phenotyping (potentially multiple phenotypic modalities).

#### Variant Effect Map (VEM)

A dataset that reports the effects of variation in a DNA element (a gene, transcript, set of regulatory regions, etc.) 
on a single or multiplexed set of phenotypes.

#### Atlas of Variant Effects (AVE) ###

A combined resource for variant effects measured across model systems and contexts applicable to the study of the 
structure and function of the genome and its products, as well as the consequences of its perturbation in health and 
disease.

### Experimental vocabulary (genetic perturbation, phenotype and context)

#### Genetic perturbation

This section describes the scope and characteristics of variant introduction.

**Library scope** – the collection of DNA elements introduced into the library. 
DNA elements can have known (e.g. a gene, an exon or set of exons included in a transcript, a set of enhancers, 
repressors, etc), or unknown functions. 
For a given DNA element we distinguish the mode of variant programming/engineering 
(e.g. all SNV, indels, ClinVar variants etc).

Controlled vocabulary terms (one or many):
- Coding
- Intronic
- Non-coding regulatory
- Non-coding other (eg tRNA)
	
**Variant Library characteristics** – methods used to generate the library

*Variant generation method* – how was the variant library created 
(e.g. doped oligo, mutagenic PCR, primer-based, base editor)

Controlled vocabulary categorical term (can pick both category options):
- Editing at endogenous locus
- In vitro variant construct generation

*In vitro construct generation method* (if applicable)
- Oligo-directed mutagenic PCR (e.g. NNK PCR) 
- Error-prone PCR
- Nicking mutagenesis
- Microarray synthesis
- Site-directed mutagenesis
- Doped oligo synthesis
- Oligo pool synthesis
- Proprietary method
- Other (please describe)

*Integration/expression of exogenous construct* (if applicable)
- Entire element replacement at the native locus (e.g. with integrases, not base editing)

*Integration of extra-local construct* (e.g. with landing pad; if applicable)
- Viral Integration
- Episomal delivery
- Transfection of RNA

*Endogenous genome editing* (if applicable)
- CRISPR/Cas system
- SpCas9
- SaCas9
- AsCas12a
- RfxCas13d
- CRISPR/Cas system functionality
    - Wildtype nuclease
    - Base Editor
    - Prime Editor

**Delivery method** – how the variant induction machinery and/or construct was delivered to the cell/organism 
(e.g. viral transduction, electroporation, transfection and MOI)

Controlled vocabulary terms (one or many):
- Electroporation
- Lipofection
- Nucleofection
- Microinjection
- Chemical-based transfection
- Transduction: AAV
- Transduction: lentivirus
- Transformation: chemical or heat shock
- Other (please specify)

#### Phenotypic assay

A physical adjudication of model system that allows for systematic interrogation of a functional read-out for a large 
amount of genetic variants (e.g. cell size and mode of adjudication, action potential characteristic(s) and mode of 
measurement, expression of a particular factor and mode of measurement (FACS, sc-RNA-seq), or transcript expression 
(bulk RNA-seq)).

**Dimensionality of phenotyping assays** – how many phenotypes and of what complexity are included in the map

Controlled vocabulary terms (select one):
- Single functional read-out
- Single dimension (e.g. FACS fluorescence from a single protein was used)
- High-dimensional data (e.g. ML/AI enabled cell imaging/classification)
- The outcomes of multiple phenotypic assays were combined to make this map

**Phenotypic assay examines** – terms selected from OBI subtree with root 
[OBI_0000070: “assay”](http://purl.obolibrary.org/obo/OBI_0000070)

- DNA 
    - OBI_0000913 Promoter activity reporter gene assay RNA
    - “Other”, e.g. structure, methylation

- RNA
    - OBI_0001177 Bulk RNA-sequencing
    - OBI_0002631 Single cell RNA-sequencing and single cell combinatorial index RNA-sequencing assay
    - OBI_0003094 Fluorescence in-situ hybridization (FISH) assay
    - “Other”

- Protein 
    - OBI_0000916 Flow cytometry assay 
    - OBI_0003096  Imaging Mass Cytometry assay
    - OBI_0002161 Evolution of ligands by exponential enrichment assay 
    - “Other”

- Morphology & Function
    - OBI_0002119 Single cell imaging 
    - OBI_0003091 Multiplexed fluorescent antibody imaging
    - OBI_0001146 Binding assays
    - OBI_0000891 Cell Proliferation Assay, including fluorescence image-based cell proliferation assay
    - OBI_0000699 Survival assessment assay
    - “Other”

**Disease/biological process relevance** – choose terms from [OMIM](https://www.omim.org/) or 
[https://mondo.monarchinitiative.org/](https://mondo.monarchinitiative.org/)

#### Context - Characteristics of the model system that influence expression of phenotype

**Cellular model system and genetic background** – genetically encoded characteristics of the model system that 
potentially affect the outcome of the assay (e.g. species, animal strain, genetic ancestry, biological sex)

Controlled vocabulary terms (one or many):
- Immortalized human cells (e.g. HEK293, HeLa cells; please specify below)
- Murine primary cells
- Induced pluripotent stem cells from male
- Induced pluripotent stem cells from female
- Patient derived primary cells (e.g. T-cells, adipocytes)
- Yeast
- E. coli
- Other bacteria
- Bacteriophage
- Molecular display (e.g. ribosome display)
- Other (please specify - includes all other OBI ontology terms)

Commonly used cell lines and model systems

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
