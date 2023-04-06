import sys 
sys.path.append("delivery_network")
from graph import  Graph, graph_from_file, time_estimation, union_find, kruskal
from graph import  truck_from_file, route_from_file, optimized_truck,  only_useful_truck, truck_affectation
from graph import knapsack_cost, knapsack_efficiency
import time
from time import perf_counter


# we create a simple graph to easily test the kruskal function

g2 = Graph([1, 2, 3, 4, 5])


g2.add_edge(1,2,2)
g2.add_edge(1,3,1)
g2.add_edge(2,3,3)
g2.add_edge(3,4,2)
g2.add_edge(4,5,1)
print(g2)
print(kruskal(g2))


g = graph_from_file("input/network.2.in")

# we can easily verify that the result is correct
# and it is


g1 = graph_from_file("input/network.9.in")

t11 = time.perf_counter()
print(g1) #
t22 = time.perf_counter()
print(t22-t11) 

t111 = time.perf_counter()
print(kruskal(g1))
t222 = time.perf_counter()
print(t22-t11)
print(t222 - t111)      # it takes 0.5 more seconds to display the kruskal of a graph than to 
                        # just display the graph, which can be considered quick enough



