import time
from time import perf_counter

class union_find: # We create union-find class for kruskal algorithm

    def __init__(self, parent_node = {}):
        self.parent_node = parent_node # Implementation with dictionary, initialized empty
        self.rank = {}

    def make_set(self, u): # Initialization function 
        for i in u:
            self.parent_node[i] = i
            self.rank[i] = 0

    def find(self, k):
        if self.parent_node[k] == k:
            return k
        return self.find(self.parent_node[k])

    def op_union(self, x, y):
        root_of_x = self.find(x)
        root_of_y = self.find(y)
        if self.rank[root_of_x] < self.rank[root_of_y]:
            self.parent_node[root_of_x] = root_of_y
        elif self.rank[root_of_x] > self.rank[root_of_y]:
            self.parent_node[root_of_y] = root_of_x
        else:
            self.parent_node[root_of_y] = root_of_x
            self.rank[root_of_x] += 1



class Graph:

    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output

    
# Question 1

# We took the correction of the teacher because it was more clear than our version
# Graph_from_file is at the end, out of the class Graph
# Complexity in O(1)

    def add_edge(self, node1, node2, power_min, dist=1):
        if node1 not in self.graph: # We check if node1, and node2 after, are already in the graph and if not, we add the nodes
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append((node2, power_min, dist)) # We create the edge between node1 and node2
        self.graph[node2].append((node1, power_min, dist))
        self.nb_edges += 1


# Question 2
# The complexity of this algorithm is O(V+E) where V = number of nodes and E = number of edges

    def connected_components(self):
        components_list = []
        visited_nodes = {node : False for node in self.nodes} # We need to know if we already visited the nodes or not

        def exploration(node): # Depth first search algorithm
            component = [node]
            for neighbor in self.graph[node]:
                neighbor = neighbor[0]
                if not visited_nodes[neighbor]:
                    visited_nodes[neighbor] = True
                    component += exploration(neighbor) # If a node has not been visited, we add the neighbors of this node
            return component
        
        for node in self.nodes:
            if not visited_nodes[node]:
                components_list.append(exploration(node))

        return components_list


    def connected_components_set(self):
        return set(map(frozenset, self.connected_components()))


# Question 3
# Complexity in O(E * log(E))

    def get_path_with_power(self, src, dest, power):
        visited_nodes = {node : False for node in self.nodes} # We need to know which nodes have already been visited
        visited_nodes[src] = True
   
        def finding_a_path(node, path): # We need to have the path in argument for the recursivity
            if node == dest:
                return path
            for neighbor in self.graph[node]:
                neighbor, power_min, dist = neighbor[0], neighbor[1], neighbor[2]
                if not visited_nodes[neighbor] and power_min <= power: # We visit the neighbors of the node if they have not been visited yet and if power_min <= power
                    visited_nodes[neighbor] = True
                    result = finding_a_path(neighbor, path+[neighbor]) # We build the path recursively, keeping it in memory
                    if result is not None:
                        return result
            return None

        return finding_a_path(src, [src])
    

# Question 4 : Already made


# Question 5 : Bonus

    def Dijkstra(self,src,dest,power):
        infinity = 1000000000000
        distance_dic = {node : infinity for node in self.nodes} # Initialization : at the beginning, no nodes are reached
        distance_dic[src] = 0 # Except the source
        predecessor_dic = {None : node for node in self.nodes} # We need to know the predecessor to create the path at the end


        def finding_min(non_reached_nodes): # We find the node with the lowest distance among non visited nodes
            mini = infinity
            min_dts_node = -1
            for node in non_reached_nodes:
                if distance_dic[node] < mini:
                    mini = distance_dic[node]
                    min_dts_node = node
            if min_dts_node == -1:
                return None
            else:
                return min_dts_node

        def power_and_dist_between_nodes(self,node1,node2): # We update the distances if it is shorter and if the power_edge is lower than power_min
            for node in self.graph[node1]:
                if node[0] == node2:
                    return(node[1],node[2])

        def update_distances(node1,node2):
            power_of_edge,dist_of_edge = power_and_dist_between_nodes(self, node1, node2)
            if (distance_dic[node2] > distance_dic[node1] + dist_of_edge) and (power >= power_of_edge):
                distance_dic[node2] = distance_dic[node1] + dist_of_edge
                predecessor_dic[node2] = node1

        my_non_reached_nodes = [node for node in self.nodes]  # No nodes are reached at the beginning
        while my_non_reached_nodes != []: # We repeat that until all nodes are reached
            nearest_neighbor = finding_min(my_non_reached_nodes)
            if nearest_neighbor == None:
                my_non_reached_nodes = [] 
            else:
                my_non_reached_nodes.remove(nearest_neighbor) # We remove the node treated
                for neighbor_of_nearest_neighbor in self.graph[nearest_neighbor]:
                    neighbor_of_nearest_neighbor = neighbor_of_nearest_neighbor[0]
                    update_distances(nearest_neighbor, neighbor_of_nearest_neighbor) # We update all the distances
        shortest_path = []
        moving_node = dest
        while moving_node != src:
            if moving_node == None:
                return("Pas de chemin possible")
            shortest_path.insert(0,moving_node)
            moving_node = predecessor_dic[moving_node] # We build the path using the predecessors
        shortest_path.insert(0,src)
        return(shortest_path)


# Question 6

    def min_power(self, src, dest):

        def binary_search(self,L): #L is a list
            left,right = 0,(len(L)-1)
            while left != right:
                middle = (left+right)//2
                path = self.get_path_with_power( src, dest, L[middle])
                if path == None:
                    left = middle+1
                else:
                    right = middle
            return(path,L[left])

        power_list = []
        for node in self.nodes:
            for neighbor in self.graph[node]:
                power_list.append(neighbor[1])
        F = frozenset(power_list)
        power_list = sorted(list(F))
        power_max = power_list[-1]
        if self.get_path_with_power(src, dest, power_max) == None: #to avoid the case where there is no path
            return None
        else:
            return binary_search(self,power_list)



# Question 12

    def kruskal(self):
        g_mst = Graph(range(1,self.nb_nodes+1)) # Initialization of our mst
        mst_union_find = union_find({})
        mst_union_find.make_set(list(self.nodes)) # Initialization of our union-find structure to know if another edge create a cycle or not
        edge_list = []
        for node1 in self.graph:
            for node2 in self.graph[node1]:
                node2,power_1_2 = node2[0],node2[1]
                edge = [power_1_2,min(node1,node2),max(node1,node2)]
                if not edge in edge_list:
                    edge_list.append(edge)  
        sorted_edge_list = sorted(edge_list) # We have collected all the edges and make sure we did not take a edge twice, and sorted them by power
        for edge in sorted_edge_list:
            power,node1,node2 = edge
            if mst_union_find.find(node1) != mst_union_find.find(node2): # We added the edges only if it does not create a cycle
                g_mst.add_edge(node1, node2, power)
                mst_union_find.op_union(node1, node2)
        return(g_mst)


# Question 13

# There are already 2 tests implemented
# g.kruskal() instead of doing kruskal(g) as it was previously computed
# We implemented a new graph "my_network.06.py" whish successfuly passed the test


# Question 14

    def min_power_optimized(self, src, dest):
       
       
       
       
        
        
        
        
        
        
        g_mst = self.kruskal()
        return g_mst.min_power(src,dest) # We know that it only works with small graphs : we will improve it

# Question 1 

# Second part with Graph_from_file

def graph_from_file(filename):

    with open(filename, "r") as file:
        n, m = map(int, file.readline().split())
        g = Graph(range(1, n+1))
        for _ in range(m):
            edge = list(map(int, file.readline().split()))
            if len(edge) == 3:
                node1, node2, power_min = edge
                g.add_edge(node1, node2, power_min) # will add dist=1 by default
            elif len(edge) == 4:
                node1, node2, power_min, dist = edge
                g.add_edge(node1, node2, power_min, dist)
            else:
                raise Exception("Format incorrect")
    return g

    
# Question 10 

def time_estimation(n):
    with open("input/routes." + str(n) + ".in","r") as file:
        time_est = 0
        src = []
        dest = []
        a = map(int, file.readline().split()) # We save the amount of itineraries
        for i in range(10): # Average with 10 itineraries
            node1,node2,p = map(int, file.readline().split())
            g = graph_from_file("input/network." + str(n) + ".in")
            t1 = time.perf_counter()

            opti = g.min_power_optimized(node1,node2)
            t2 = time.perf_counter()
            time_est += (t2-t1)
            print(time_est)
    return(((list(a)[0])/10)*time_est)


    # def bfs(g, root): #breadth-first search algorithm
        # depth = {} #http://www.monlyceenumerique.fr/nsi_terminale/a/a1_algo_arbre.php#e3 + wikipedia parcours en largeur



