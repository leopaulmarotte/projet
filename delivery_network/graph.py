class union_find:

    def __init__(self, parent_node = {}):
        self.parent_node = parent_node

    def make_set(self, u):
        for i in u:
            self.parent_node[i] = i

    def find(self, k):
        if self.parent_node[k] == k:
            return k
        return self.find(self.parent_node[k])

    def op_union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        self.parent_node[x] = y


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

    
    
    def add_edge(self, node1, node2, power_min, dist=1):
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min, dist))
        self.nb_edges += 1


    def get_path_with_power(self, src, dest, power):
        visited_nodes = {node : False for node in self.nodes}
        visited_nodes[src] = True
   
        def finding_a_path(node, path):
            if node == dest:
                return path
            for neighbor in self.graph[node]:
                neighbor, power_min, dist = neighbor[0], neighbor[1], neighbor[2]
                if not visited_nodes[neighbor] and power_min <= power:
                    visited_nodes[neighbor] = True
                    result = finding_a_path(neighbor, path+[neighbor])
                    if result is not None:
                        return result
            return None

        return finding_a_path(src, [src])

        raise NotImplementedError
    

    def connected_components(self):
        components_list = []
        visited_nodes = {node : False for node in self.nodes}

        def exploration(node):
            component = [node]
            for neighbor in self.graph[node]:
                neighbor = neighbor[0]
                if not visited_nodes[neighbor]:
                    visited_nodes[neighbor] = True
                    component += exploration(neighbor)
            return component
        
        for node in self.nodes:
            if not visited_nodes[node]:
                components_list.append(exploration(node))

        return components_list

        raise NotImplementedError


    def connected_components_set(self):
        return set(map(frozenset, self.connected_components()))
    

    def min_power(self, src, dest):
        power_list = []

        
        def binary_search(self,L): #L is a liste
            left,right = 0,(len(L)-1)
            while left != right:
                middle = (left+right)//2
                path = self.get_path_with_power( src, dest, L[middle])
                if path == None:
                    left = middle+1
                else:
                    right = middle
            return(path,L[left])

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

    def Dijkstra(self,src,dest,power):
        infinity = 1000000000000
        distance_dic = {node : infinity for node in self.nodes}
        distance_dic[src] = 0
        predecessor_dic = {None : node for node in self.nodes}

        def finding_min(non_reached_nodes):
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

        def power_and_dist_between_nodes(self,node1,node2):
            for node in self.graph[node1]:
                if node[0] == node2:
                    return(node[1],node[2])

        def update_distances(node1,node2):
            power_of_edge,dist_of_edge = power_and_dist_between_nodes(self, node1, node2)
            if (distance_dic[node2] > distance_dic[node1] + dist_of_edge) and (power >= power_of_edge):
                distance_dic[node2] = distance_dic[node1] + dist_of_edge
                predecessor_dic[node2] = node1

        my_non_reached_nodes = [node for node in self.nodes]
        while my_non_reached_nodes != []:
            nearest_neighbor = finding_min(my_non_reached_nodes)
            if nearest_neighbor == None:
                my_non_reached_nodes = []
            else:
                my_non_reached_nodes.remove(nearest_neighbor)
                for neighbor_of_nearest_neighbor in self.graph[nearest_neighbor]:
                    neighbor_of_nearest_neighbor = neighbor_of_nearest_neighbor[0]
                    update_distances(nearest_neighbor, neighbor_of_nearest_neighbor)
        shortest_path = []
        moving_node = dest
        while moving_node != src:
            if moving_node == None:
                return("Pas de chemin possible")
            shortest_path.insert(0,moving_node)
            moving_node = predecessor_dic[moving_node]
        shortest_path.insert(0,src)
        return(shortest_path)

    def kruskal(self):

        def del_occur(L):
            LL = []
            for i in L:
                if not i in LL:
                    LL.append(i)
            return(LL)
        
        nb_nodes = self.nb_nodes
        mst = Graph(range(1,nb_nodes+1))
        
        mst_union_find = union_find({})
        mst_union_find.make_set(list(self.nodes))
        edge_list = []
        for node1 in self.nodes:
            for node2 in self.graph[node1]:
                node2,power_1_2 = node2[0],node2[1]
                edge_list.append([power_1_2,max(node1,node2),min(node1,node2)])
        edge_list_sorted_unic = del_occur(sorted(edge_list))
        final_edge_list = []
        for edge in edge_list_sorted_unic:
            edge.reverse()
            final_edge_list.append(edge)
        
        for edge in final_edge_list:
            node1,node2,power = edge
            if mst_union_find.find(node1) != mst_union_find.find(node2):
                mst.add_edge(node1, node2, power)
                mst_union_find.op_union(node1, node2)
        
        return(mst)
    
    def f1(self, src, dest):
        g = self.kruskal()
        t = g.min_power(src, dest)
        return t



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


