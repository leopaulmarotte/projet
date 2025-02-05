import sys 
sys.path.append("delivery_network")
from graph import  Graph, graph_from_file, time_estimation, union_find, kruskal, bfs, new_minpower_aux, new_minpower
from graph import  truck_from_file, route_from_file, optimized_truck,  only_useful_truck, truck_affectation
from graph import knapsack_cost, knapsack_efficiency
import time
from time import perf_counter
def new_time_estimation(n):
    with open("input/routes." + str(n) + ".in","r") as file:
        time_est = 0
        a = int(file.readline()) # We save the amount of itineraries
        g = graph_from_file("input/network." + str(n) + ".in")
        g1 = kruskal(g)
        for i in range(10): # Average with 10 itineraries
            node1,node2,p = map(int, file.readline().split())
            t1 = time.perf_counter()
            opti = new_minpower_aux(g1, node1, node2)
            t2 = time.perf_counter()
            time_est += (t2-t1)
    print((a/10)*time_est)   

new_time_estimation(2)

# we do it for the second routes, with a function similar to the one used in 
# test_q10 and we obtain the result in 82041 seconds
# therefore we reduced of around 30% the time to calculate the min_power for all the routes