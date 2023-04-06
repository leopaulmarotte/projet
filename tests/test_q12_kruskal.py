import sys 
sys.path.append("delivery_network")
from graph import Graph, graph_from_file, time_estimation, union_find
from graph import  trucks_from_file, routes_from_file, optimized_truck, truck_affectation, truck_affectation_ks, new_minpower_aux
import time
from time import perf_counter

#on crée un grapghe nous-mêmes car les graghes donnés sont soit trop simples, soit trop compliqués

g2 = Graph([1, 2, 3, 4, 5])


g2.add_edge(1,2,2)
g2.add_edge(1,3,1)
g2.add_edge(2,3,3)
g2.add_edge(3,4,2)
g2.add_edge(4,5,1)
print(g2)
print(g2.kruskal())


#résultat cohérent


g1 = graph_from_file("input/network.9.in")
g1.kruskal
t11 = time.perf_counter()
#print(g1) # Quel que soit le volume du fichier, le graphe kruskal s'affiche en quelques secondes
t22 = time.perf_counter()
#print(t22-t11) # 10,44 secondes pour calculer le kruskal

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
            opti = new_minpower_aux(g, node1, node2)
            t2 = time.perf_counter()
            time_est += (t2-t1)
    #print((a/10)*time_est)       

#new_time_estimation(4)
# on met au max 1 seconde pour calculer la puissance minimale qu'il faut pour un trajet donné, quelle que soit la base de données.



