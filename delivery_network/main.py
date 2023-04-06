from graph import  Graph, graph_from_file, time_estimation, union_find, kruskal
from graph import  truck_from_file, route_from_file, optimized_truck,  only_useful_truck, truck_affectation
from graph import knapsack_cost, knapsack_efficiency
import time
from time import perf_counter


data_path = "input/"
file_name = "routes.1.in"

g = graph_from_file("input/network.3.in")
kruskal(g)
