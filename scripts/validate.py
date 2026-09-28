from pathlib import Path
from rdflib import Graph, ConjunctiveGraph

FILES = [
    ("ontology/hneo.ttl", "turtle"),
    ("ontology/hneo-shapes.ttl", "turtle"),
    ("vocab/hneo-vocab.ttl", "turtle"),
]

for path, fmt in FILES:
    g = Graph()
    g.parse(path, format=fmt)
    print(f"OK {path}: {len(g)} triples")

cg = ConjunctiveGraph()
cg.parse("examples/historical-network.trig", format="trig")
print(f"OK examples/historical-network.trig: {len(cg)} quads")

for q in Path("queries").glob("*.rq"):
    query = q.read_text()
    list(cg.query(query))
    print(f"OK query: {q}")
