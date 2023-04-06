import sys 
sys.path.append("delivery_network")
from graph import  Graph, graph_from_file, time_estimation, union_find, kruskal
from graph import  truck_from_file, route_from_file, optimized_truck,  only_useful_truck, truck_affectation
from graph import knapsack_cost, knapsack_efficiency
import time
from time import perf_counter

# we want to compare the results of knapsack_cost and knapsack_efficiency
# The goal is to optimize our profit by using a new function : knapsack_efficiency

