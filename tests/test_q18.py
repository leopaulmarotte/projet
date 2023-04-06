import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file, time_estimation, union_find, bfs,  new_minpower_aux
from graph import  trucks_from_file, routes_from_file, optimized_truck, truck_affectation, truck_affectation_ks
from graph import  node_objet, queue, knapsack2
import time
from time import perf_counter



#routes_from_file("input/routes.1.in")

g = graph_from_file("input/network.1.in") # on 
print(g)
print(g.kruskal())
#print(g)


list_routes = routes_from_file("input/routes.1.in")
#list_routes1 = list_routes[:50]

list_trucks = trucks_from_file("input/trucks.1.in")

t1 = time.perf_counter()
t = truck_affectation(g, list_routes, list_trucks)
#print(t)
t2 = time.perf_counter()
#print(t2-t1)
t3 = time.perf_counter()
t1 = truck_affectation_ks(t)
t4 = time.perf_counter()
#print(t4-t3)

#print(len(t1))
t5 = time.perf_counter()
#print(knapsack2(t1, 25*10**9, len(t1)))
#print(knapsack(t1, 25*10**9))
t6 = time.perf_counter()
#print(t6 - t5)
s = 0
for i in  list_routes:
    s = s + i[2]
#print(s)

#cohérent


