import sys 
sys.path.append("delivery_network")
from graph import Graph, union_find, graph_from_file

#on crée un grapghe nous-mêmes car les graghes donnés sont soit trop simples, soit trop compliqués

g = Graph([1, 2, 3, 4, 5])

g.add_edge(1,2,2)
g.add_edge(1,3,1)
g.add_edge(2,3,3)
g.add_edge(3,4,2)
g.add_edge(4,5,1)

print(g)
print(g.kruskal())

#le résultat est cohérent


def time_estimation(n):
    with open("input/routes." + str(n) +  ".in", "r") as file:
        time_est = 0
        src = []
        dest = []
        a = map(int, file.readline().split())
        for i in range(10): 
            node1,node2,p = map(int, file.readline().split())
            g = graph_from_file("input/network." +str(n) +".in")
            t1 = time.perf_counter()
           
            opti = g.min_power_optimized(node1,node2)
            t2 = time.perf_counter()
            time_est += (t2 - t1)
            print(time_est)
        
            
    return (((list(a)[0])/10)* time_est)
