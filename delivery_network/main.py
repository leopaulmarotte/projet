from graph import Graph, graph_from_file, Kruskal
import time
from time import perf_counter


data_path = "input/"
file_name = "routes.2.in"

#with open(data_path + file_name, "r") as file:
 #   src = []
 #   dest = []
 #    
 #   a = map(int, file.readline().split())

 #   for i in range(10):
 #       n,m,c = map(int, file.readline().split())
  #      src.append(n)
   #     dest.append(m)
    #

g = graph_from_file("input/" + "network.00.in")

#t1 = time.perf_counter()
#
#for i in range(10):
 #   g.min_power(src[i], dest[i])

#t2 = time.perf_counter()
#print(list(a)[0]* (t2 - t1))



Kruskal(g)
