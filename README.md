# MAVE Minimum Information Model

[![arXiv](https://img.shields.io/badge/arXiv-2306.15113-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2306.15113)

JSON Schema for validating MAVE experiment metadata

*Purpose:* To provide an overarching organization and definitions for terms relevant to tech development and data repositories associated with the [Atlas of Variant Effects Alliance](https://www.varianteffect.org).

## How to use this repository

This repository contains an implementation of the schema described in the [Atlas of Variant Effects Alliance](https://www.varianteffect.org) minimum information model for describing a multiplexed assay experiment.

The schema defines a set of required and optional fields and possible values that can be used to validate a minimum information document.
The implementation is found in the `schema` directory.

In addition to the structure of the minimum information model, the schema also defines controlled vocabulary terms for describing one of these experiments.

The `examples` directory contains examples of this type of document describing real experiments, as well as a simple Python script that will run the schema validation using [jsonschema](https://pypi.org/project/jsonschema/).
Many other implementations of the JSON Schema standard are available in other languages (see [here](https://json-schema.org/implementations.html)).

Please note that although we are using the JSON Schema standard, the files here are in YAML format because it is more human-readable.

## Reading the schema

The `schema` directory contains a YAML representation of the minimum information standard and controlled vocabulary.
There are multiple levels of required information that can be browsed hierarchically.
Most fields include a description that details the intention of that field and the type of information that is to be provided.

For many fields, there is an enumerated list of valid values corresponding to the controlled vocabulary terms that can be used to describe the experiment.

The schema structure and terms are also described below, although the YAML documents in the `schema` directory should be considered the authoritative source of information if there are discrepancies.

## Controlled vocabulary terms

