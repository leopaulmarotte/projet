from graphe2 import Graph

graph = Graph(9)
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 7)
graph.add_edge(1, 2, 11)
graph.add_edge(1, 3, 9)
graph.add_edge(1, 5, 20)
graph.add_edge(2, 5, 1)
graph.add_edge(3, 6, 6)
graph.add_edge(3, 4, 2)
graph.add_edge(4, 6, 10)
graph.add_edge(4, 8, 15)
graph.add_edge(4, 7, 5)
graph.add_edge(4, 5, 1)
graph.add_edge(5, 7, 3)
graph.add_edge(6, 8, 5)
graph.add_edge(7, 8, 12)
print(graph.m_graph)

print(graph.kruskals_mst())

#en gros ça renvoie une liste de listes : première sous-liste = node 1, deuxième sous-liste : nod 2 etc...
