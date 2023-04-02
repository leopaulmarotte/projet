import sys 
sys.path.append("delivery_network")
from graph import Graph, union_find, graph_from_file, node_objet, queue, bfs, new_minpower
import time
from time import perf_counter

#on crée un grapghe nous-mêmes car les graghes donnés sont soit trop simples, soit trop compliqués

g = Graph([1, 2, 3, 4, 5])

g.add_edge(1,2,2)
g.add_edge(1,3,1)
g.add_edge(2,3,3)
g.add_edge(3,4,2)
g.add_edge(4,5,1)



#g1 = graph_from_file("input/network.1.in")

#print(new_minpower(g, 1, 4))

#le résultat est cohérent

def new_time_estimation(n):
    with open("input/routes." + str(n) + ".in","r") as file:
        time_est = 0
        a = int(file.readline()) # We save the amount of itineraries
        g = graph_from_file("input/network." + str(n) + ".in")
        g.kruskal
        for i in range(10): # Average with 10 itineraries
            node1,node2,p = map(int, file.readline().split())
            t1 = time.perf_counter()
            print(t1)
            opti = new_minpower(g, node1, node2)
            t2 = time.perf_counter()
            time_est += (t2-t1)
    print((a/10)*time_est)       

new_time_estimation(9)



