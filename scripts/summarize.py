from rdflib import ConjunctiveGraph

g = ConjunctiveGraph()
g.parse("examples/historical-network.trig", format="trig")
print(f"quads={len(g)}")
print(f"contexts={len(list(g.contexts()))}")
