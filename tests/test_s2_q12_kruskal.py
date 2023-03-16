import sys 
sys.path.append("delivery_network")
from graph import Graph, union_find, graph_from_file

#on crée un grapghe nous-mêmes car les graghes donnés sont soit trop simples, soit trop compliqués

g = Graph([1, 2, 3, 4, 5])

g.add_edge(1,2,2)
g.add_edge(1,3,1)
g.add_edge(2,3,3)
g.add_edge(3,4,2)
g.add_edge(4,5,1)

print(g)
print(g.kruskal())

#le résultat est cohérent
