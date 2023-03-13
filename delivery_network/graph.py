class UnionFind:
    def __init__(self, n):
        """
        Initialise la structure de données Union-Find avec n éléments,
        chacun étant initialement dans sa propre partition.
        """
        self.parent = [k for k in range(n)] #tableau qui contient le parent de chaque élément, initialisé à lui-même
        self.rank = [0]*n #stocke la hauteur (=le rang) de chaque arbre

    def find(self, x): #trouver l'ensemble auquel x appartient en remontant la chaine de parents
        if self.parent[x] != x: #si x n'est pas la racine, on continue 
            self.parent[x] = self.find(self.parent[x]) #récursivité + on comprime pour être plus efficace
        return self.parent[x]

    def union(self, x, y): #relier les arbres
        root_x, root_y = self.find(x), self.find(y) #on trouve les racines de x et y
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y #on relie l'arbre de hauteur inférieur à la racine de l'arbre de rang supérieur 
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x #si même rang, on les relie + on augmete le rang 
            self.rank[root_x] += 1


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

    
      
    
    def f1(self, src, dest):
        g = self.kruskal()
        t = g.min_power(src, dest)
        return t

def kruskal(g):

        edges=[]
        sorted_edges=[]
        for node in g.graph:
            for connected_node, power, dist in g.graph[node]:
                edges.append((power,node,connected_node))
        sorted_edges=sorted(edges, key=lambda l: l[0]) #on trie les arêtes par poids croissant
        uf = UnionFind(g.nb_nodes + max(g.nodes)) #on crée une structure d'unionfind, on rajoute le dernier sinon on est out of range dans la suite de la fonction
        g_mst = Graph() #on va créer l'arbre couvrant de poids minimal
        for power, node1, node2 in sorted_edges:
            if uf.find(node1)!= uf.find(node2): #on vérifie si ça ne crée pas de cycle 
                g_mst.add_edge(node1, node2, power) #on l'ajoute à l'arbre couvrant 
                uf.union(node1, node2) #on les lie 
        return g_mst 

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


