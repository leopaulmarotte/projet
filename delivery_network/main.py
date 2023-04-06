from graph import  Graph, graph_from_file, time_estimation, union_find, bfs,  new_minpower_aux, knapsack2
from graph import  trucks_from_file, routes_from_file, optimized_truck, truck_affectation, truck_affectation_ks
from graph import knapsack1, node_objet, queue, knapsack3, knapSack, kruskal
import time
from time import perf_counter

#data_path = "input/"
#file_name = "routes.1.in"



#routes_from_file("input/routes.1.in")

g = graph_from_file("input/network.3.in")
kruskal(g)


list_routes = routes_from_file("input/routes.1.in")
list_routes1 = list_routes[:50]
list_trucks = trucks_from_file("input/trucks.1.in")
#t1 = time.perf_counter()
#truck = truck_affectation(g, list_routes, list_trucks)
#print(t)
#t2 = time.perf_counter()
#print(t2-t1)
#t3 = time.perf_counter()
#truck1 = truck_affectation_ks(truck)
#t4 = time.perf_counter()
#truck2 = truck1[:5]
#print(truck2)
#print(t4-t3)
#print(t1)
#n = len(truck1)
#t5 = time.perf_counter()
#print(knapsack2(truck2, 25*10**9, n))
#print(knapsack1(truck2, 25*10**9, t))
#print(knapsack3(truck2,25*10**9, t))
#t6 = time.perf_counter()
#print(t6 - t5)
#s = 0
#for i in truck2:
    #s = s + i[1]
    #print(s)
#t = []
#print(knapsack3(truck2, 25*10**9, t))

