import sys 
sys.path.append("delivery_network")
from graph import  Graph, graph_from_file, time_estimation, union_find, kruskal
from graph import  truck_from_file, route_from_file, optimized_truck,  only_useful_truck, truck_affectation
from graph import knapsack_cost, knapsack_efficiency
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
print(kruskal(g2))


g = graph_from_file("input/network.2.in")

#résultat cohérent


#g1 = graph_from_file("input/network.9.in")

t11 = time.perf_counter()
#print(g1) # Quel que soit le volume du fichier, le graphe kruskal s'affiche en quelques secondes
t22 = time.perf_counter()
#print(t22-t11) # 10,44 secondes pour calculer le kruskal

def new_time_estimation(n):
    with open("input/routes." + str(n) + ".in","r") as file:
        time_est = 0
        a = int(file.readline()) # We save the amount of itineraries
        g = graph_from_file("input/network." + str(n) + ".in")
        g1 = kruskal(g)
        for i in range(10): # Average with 10 itineraries
            node1,node2,p = map(int, file.readline().split())
            t1 = time.perf_counter()
            #print(t1)
            opti = new_minpower_aux(g1, node1, node2)
            t2 = time.perf_counter()
            time_est += (t2-t1)
    print((a/10)*time_est)       

new_time_estimation(4)
# on met au max 1 seconde pour calculer la puissance minimale qu'il faut pour un trajet donné, quelle que soit la base de données.



