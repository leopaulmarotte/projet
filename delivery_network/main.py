from graph import Graph, graph_from_file, time_estimation, union_find
from graph import  trucks_from_file, routes_from_file, optimized_truck, truck_affectation, truck_affectation_ks
from graph import knapsack
import time
from time import perf_counter

#data_path = "input/"
#file_name = "routes.1.in"



#routes_from_file("input/routes.1.in")

g = graph_from_file("input/network.4.in")
g.kruskal


list_routes = routes_from_file("input/routes.1.in")
list_trucks = trucks_from_file("input/trucks.1.in")
t1 = ti
t = truck_affectation(g, list_routes, list_trucks)
print(t)
#t1 = truck_affectation_ks(t)




#print(knapsack(t1, 25*10**9))

