import sys 
sys.path.append("delivery_network")
from graph import  Graph, graph_from_file, time_estimation, union_find, kruskal, bfs, new_minpower_aux, new_minpower
from graph import  truck_from_file, route_from_file, optimized_truck,  only_useful_truck, truck_affectation
from graph import knapsack_cost, knapsack_efficiency
import time
from time import perf_counter

# we want to compare the results of knapsack_cost and knapsack_efficiency
# The goal is to optimize our profit by using a new function : knapsack_efficiency
# we complete the code written in test_q18_1

B = 25*(10**9)
B2 = 1000000

g = graph_from_file("input/network.3.in")
g = kruskal(g)

list_routes = route_from_file("input/routes.1.in")
list_routes1 = list_routes[:20]                 
                                                
list_trucks = truck_from_file("input/trucks.2.in")
list_trucks = only_useful_truck(list_trucks)

                                            
t3 = time.perf_counter()
h1 = knapsack_cost(g, list_trucks, list_routes1, B2)
t4 = time.perf_counter()     
h2 = knapsack_efficiency(g, list_trucks, list_routes1, B2)
t5 = time.perf_counter()

print(h1)
print(h2)

# we compare the profit found by the two functions
# knapsack_cost finds a way to make a profit of 26640 (it is the same result as found in test_q18_1 since we used the same parameters)
# knapsack_efficiency finds a way to make a profit of 63556
# it seems that the optimization of our knapsack algorithm is effectiuve since we have almost tripled our profit.







