import sys 
sys.path.append("delivery_network")
from graph import  Graph, graph_from_file, time_estimation, union_find, kruskal
from graph import  truck_from_file, route_from_file, optimized_truck,  only_useful_truck, truck_affectation
from graph import knapsack_cost, knapsack_efficiency
import time
from time import perf_counter

B = 25*(10**9)

g = graph_from_file("input/network.3.in")
g = kruskal(g)

list_routes = route_from_file("input/routes.1.in")
list_routes1 = list_routes[:20]                 # we have some issues with the amount of time truck_affectation takes
                                                # therefore we will only work with a truncated list for the big networks
                                                
list_trucks = truck_from_file("input/trucks.1.in")
print(len(list_trucks))
list_trucks = only_useful_truck(list_trucks)
print(len(list_trucks)) # we can notice that there was in fact a useless truck in list_trucks : it is a truck more expensive  
                        # than another more powerful truck
t1 = time.perf_counter()
t = truck_affectation(g, list_routes1, list_trucks) # we notice that it takes around 11 seconds
t2 = time.perf_counter()                            # to calculate truck_affectation
print(t2-t1)                                        # it is consistent with what we established before
                                                    # since the function truck_affectation uses the the function new_minpower_aux
                                                    # and it has been found before that it takes around 0.5 seconds for this function
                                                    # to calculte the minimal power for each route.
                                                


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
# it is logical that they are the same since our budget is way bigger than the cost of the trucks
# therefore we are not limited by it and we can find a truck for each routes



