# Historical Network & Evidence Ontology (HNEO)

HNEO is an evidence-aware ontology and knowledge-graph framework for historical networks, organizations, events, claims, provenance, and competing interpretations.

The project is designed for domains where the historical record contains a mixture of established facts, disputed allegations, mutually contradictory testimony, institutional findings, investigative hypotheses, and later synthetic theories. It therefore separates **world entities and events** from **claims about them**, **evidence used for those claims**, and **project assessments**.

## Design

HNEO uses:

- **OntoUML/UFO** as a conceptual design discipline for identity, roles, relators, and events.
- **CIDOC CRM-style event semantics** for historical actors, events, places, and information objects.
- **CRMinf-style epistemic structures** for propositions, claims, evidence, inference, and belief.
- **PROV-O** for provenance.
- **W3C ORG** for organizational structure.
- **OWL-Time** for temporal modeling.
- **FIBO-aligned concepts** for finance and business.
- **SKOS** for controlled vocabularies.
- **SHACL** for validation.
- **Nanopublication patterns** for source-bounded assertions.

## Core modeling rule

Do not collapse these:

1. what happened;
2. what a source says happened;
3. what evidence supports or contradicts that proposition;
4. what the project currently assesses.

This makes contradictory claims representable without making the graph inconsistent.

## Repository structure

- `ontology/hneo.ttl` — application ontology
- `ontology/hneo-shapes.ttl` — SHACL validation shapes
- `vocab/hneo-vocab.ttl` — controlled vocabulary
- `examples/historical-network.trig` — integrated worked example
- `docs/` — architecture, epistemology, modeling, source policy, historical domains
- `queries/` — SPARQL examples
- `scripts/` — parse/validation helpers
- `tests/` — RDF and epistemic-behavior tests

## Historical example

The worked example covers the major areas discussed during initial design:

- Operation Underworld and wartime organized-crime cooperation
- CIA-Mafia anti-Castro activity
- The Company / Bluegrass Conspiracy
- Black Tuna
- Watergate political intelligence
- Moorer-Radford
- Cultural Cold War organizations
- anti-communist labor and WACL networks
- CAT / Air America proprietary patterns
- Iran-Contra and its private support infrastructure
- private donor and nonprofit financing
- BCCI and offshore-finance patterns
- INSLAW / PROMIS / Wackenhut-Cabazon allegations
- institutional-capture hypotheses
- Hougan, Casolaro, Brussell, and Emory-style synthetic interpretations

Large theories such as Casolaro's "Octopus" are modeled as **theories containing component propositions**, not as automatically established organizations.

## Quick start

```bash
python -m pip install -e .
python scripts/validate.py
pytest
```

Optional full SHACL validation can use `pyshacl`.

## Epistemic example

Instead of asserting:

```
Wackenhut -> modified -> PROMIS
```

HNEO records:

- a proposition stating that relationship;
- the claimant who asserts it;
- source fragments used as evidence;
- claims that support or deny it;
- a separate project assessment such as `Unresolved`.

See `docs/epistemology.md`.

## Status

This is a synthetic first-pass ontology and example dataset. It is meant to establish a rigorous modeling framework before large-scale historical ingestion. The next development phase should add source-specific nanopublications, archival identifiers, richer temporal intervals, entity-resolution workflows, and automated analytic graph projections.

## License

MIT.
