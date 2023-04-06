import sys 
sys.path.append("delivery_network")
from graph import  Graph, graph_from_file, time_estimation, union_find, kruskal
from graph import  truck_from_file, route_from_file, optimized_truck,  only_useful_truck, truck_affectation
from graph import knapsack_cost, knapsack_efficiency
import time
from time import perf_counter

B = 25*(10**9)
B2 = 1000000

# we complete the code written in test_q18_0 

g = graph_from_file("input/network.3.in")
g = kruskal(g)

list_routes = route_from_file("input/routes.1.in")
list_routes1 = list_routes[:20]                 
                                                
list_trucks = truck_from_file("input/trucks.2.in")
list_trucks = only_useful_truck(list_trucks)

                                            
t3 = time.perf_counter()
h = knapsack_cost(g, list_trucks, list_routes1, B)      # the function knapsack takes 11 seconds too, because
                                                        # it uses the function truck_affectation.
t4 = time.perf_counter()
print(h)    # we display the results 
print(t4 - t3)

profit = h[-1]
print(profit)
s = 0
for i in  list_routes1: # this iterative function calculates the maximum profit we can make 
                        # with the different routes we have
    s = s + i[2]
print(s)

# the last term in the list returned by our function knapsack_cost is the profit
# we compare it with the maximum profit we can make
# the profit returned by knapsack_cost is 106930
# it is logical that they are the same since our budget is way bigger than the cost of the trucks
# therefore we are not limited by it and we can find a truck for each routes

h2 = knapsack_cost(g, list_trucks, list_routes1, B2)
print(h2)

# we try the function knapsack with a budget around the trucks prices scale
# this time the profit returned by knapsasck_cost is 26460
# we can see the profit is smaller than the maximul profit, since we don't have enourgh money
# to buy all the trucks we need

