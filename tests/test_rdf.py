from rdflib import Graph, ConjunctiveGraph, Namespace, RDF

HNEO = Namespace("https://example.org/hneo/")

def load():
    g = ConjunctiveGraph()
    g.parse("ontology/hneo.ttl", format="turtle")
    g.parse("vocab/hneo-vocab.ttl", format="turtle")
    g.parse("examples/historical-network.trig", format="trig")
    return g

def test_example_parses():
    g = load()
    assert len(g) > 100

def test_contradiction_model_present():
    g = load()
    q = """
    PREFIX hneo: <https://example.org/hneo/>
    ASK {
      ?c1 a hneo:Claim ; hneo:proposition ?p ; hneo:beliefValue hneo:BeliefTrue .
      ?c2 a hneo:Claim ; hneo:proposition ?p ; hneo:beliefValue hneo:BeliefFalse .
    }
    """
    assert bool(g.query(q).askAnswer)

def test_unresolved_assessment_present():
    g = load()
    assert any(True for _ in g.triples((None, HNEO.assessmentStatus, HNEO.Unresolved)))
