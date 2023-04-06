from graphe2 import Graph

g2 = Graph([1, 2, 3, 4, 5])


g2.add_edge(1,2,2)
g2.add_edge(1,3,1)
g2.add_edge(2,3,3)
g2.add_edge(3,4,2)
g2.add_edge(4,5,1)
print(g2)
#print(g2.kruskal())



#en gros ça renvoie une liste de listes : première sous-liste = node 1, deuxième sous-liste : nod 2 etc...
