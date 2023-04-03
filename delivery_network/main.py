from graph import Graph, graph_from_file, time_estimation, union_find, trucks_from_file, routes_from_file, optimized_truck, truck_affectation, truck_affectation_ks
import time
from time import perf_counter

#data_path = "input/"
#file_name = "routes.1.in"



#routes_from_file("input/routes.1.in")

g = graph_from_file("input/network.1.in")
g1 = g.kruskal()

list_routes = routes_from_file("input/routes.1.in")
list_trucks = trucks_from_file("input/trucks.2.in")
t = truck_affectation(g1, list_routes, list_trucks)

#print(truck_affectation_ks(t))
