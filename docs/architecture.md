# Architecture

HNEO is an application ontology for evidence-aware historical network research. It uses an event-centered historical core and keeps facts, source assertions, evidence, and project assessments distinct.

## Layers

1. **Conceptual design** — OntoUML/UFO patterns: identity-bearing kinds, roles, relators, events.
2. **Historical semantics** — CIDOC CRM-style actors, events, places, documents.
3. **Domain modules** — organizations, time, finance, intelligence, criminal-state interaction, cultural patronage, labor, private funding.
4. **Epistemic layer** — propositions, claims, evidence uses, inferences, theories, assessments.
5. **Provenance layer** — source derivation and assertion provenance.
6. **Validation layer** — SHACL constraints.
7. **Analytical projections** — temporal, multiplex, affiliation, funding, communication, and evidence-filtered networks.

## Core rule

The ontology distinguishes:
- what happened;
- what a source says happened;
- the evidence used for that proposition;
- how a researcher evaluates that proposition.

This permits contradictory claims to coexist without making the knowledge base logically inconsistent.

## Recommended storage partitions

- entity registry
- source graph
- assertion/nanopublication graphs
- evidence graph
- assessment graph
- argument graph
- derived graph
- analytic graph

## External alignments

HNEO is designed to align selectively with:
- CIDOC CRM
- CRMinf
- PROV-O
- W3C ORG
- OWL-Time
- FIBO
- SKOS
- SHACL

The project does not blindly import complete external ontologies. It maintains a constrained application profile so reasoning remains tractable.
