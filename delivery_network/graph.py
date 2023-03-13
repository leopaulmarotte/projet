class Graph:
   

    def __init__(self, nodes=[]):
      
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
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
            self.nb_nodes +=1
        if node2 not in self.graph:
            self.graph[nodes2] = []
            self.nb_nodes +=1
        
        self.nb_edges +=1
        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min, dist))
       

    

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

  
   


    
        
    def connected_components(self):
        liste_composante = []
        noeud_visite = {noeud:False for noeud in self.nodes}

        def dfs(noeud):
            composante = [noeud]
            for voisin in self.graph[noeud]:
                voisin = voisin[0]
                if not noeud_visite[voisin]:
                    noeud_visite[voisin] = True
                    composante += dfs(voisin)
            return composante
        
        for noeud in self.nodes:
            if not noeud_visite[noeud]:
                liste_composante.append(dfs(noeud))

        return liste_composante
            

        


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
        infini = 10^9
        distance_list = [infini for node in self.nodes]
        distance_list[src] = 0
        predecessor = [infini for node in self.nodes]

        def finding_min(non_reached_nodes):
            mini = infini
            vertex = -1
            for node in non_reached_nodes:
                if distance_list[node] < mini:
                    mini = distance_list[node]
                    vertex = node
            return(vertex)

        def dist(node1,node2):
            for neighbor in self.graph[node1]:
                if neighbor[0] == node2:
                    return neighbor[2]
            return("Erreur")

        def power_fct(node1,node2):
            for neighbor in self.graph[node1]:
                if neighbor[0] == node2:
                    return neighbor[1]
            return("Erreur")

        def distance_update(node1,node2):
            if (distance_list[node2] > distance_list[node1] + dist(node1,node2)) and (power_fct((node1),node(2)) < power) :
                distance_list[node2] = distance_list[node1] + dist(node1,node2)
                predecessor[node2] = node1

        my_non_reached_node = (self.nodes).remove(src)
        while my_non_reached_node != []:
            node_min = finding_min(my_non_reached_node)
            my_non_reached_node.remove(node_min)
            for neighbor in self.graph[node_min]:
                neighbor = neighbor[0]
                distance_update(node_min, neighbor)
        moving_node = dest
        min_path = []
        while moving_node != src:
            min_path = [moving_node] + min_path
            moving_node = predecessor[moving_node]
        min_path = [src] + min_path
        return(min_path)


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

class DisjointSet:
    parent = {}
 
    # effectue l'opération MakeSet
    def makeSet(self, n):
        # créer `n` ensembles disjoints (un pour chaque sommet)
        for i in range(n):
            self.parent[i] = i
 
    # Trouver la racine de l'ensemble auquel appartient l'élément `k`
    def find(self, k):
        # si `k` est racine
        if self.parent[k] == k:
            return k
 
        # se reproduisent pour le parent jusqu'à ce que nous trouvions la racine
        return self.find(self.parent[k])
 
    # Perform Union de deux sous-ensembles
    def union(self, a, b):
        # trouver la racine des ensembles auxquels appartiennent les éléments `x` et `y`
        x = self.find(a)
        y = self.find(b)
 
        self.parent[x] = y
 
 
# Fonction pour construire MST en utilisant l'algorithme de Kruskal
def Kruskal(g):
 
    # stocke les arêtes présentes dans MST
    MST = []
    n = g.nb_nodes
    # Initialise la classe `DisjointSet`.
    # Créer un ensemble singleton pour chaque élément de l'univers.
    ds = DisjointSet()
    ds.makeSet(n)
 
    index = 0

    edges = []
    for i in g.nodes :
        for t in g.graph[i]:
        
        
            edges.append((t[1],min([i,t[0]]),max([i,t[0]])))
        
    print(edges)
    edges = sorted(edges)
    F = frozenset(edges)
    edges = list(F)
    
    print(edges)
        
        
 
    #there are n nodes, so our MST must have n - 1 edges
    while len(MST) != n - 1:
 
        # considère le bord suivant avec un poids minimum du graph
        (src, dest, power) = edges[index]
        index = index + 1
 
        # 
        x = ds.find(src)
        y = ds.find(dest)
 
        # si les deux points de terminaison ont des parents différents, ils appartiennent à
        # différents composants connectés et peuvent être inclus dans MST
        if x != y:
            MST.append((src, dest, power))
            ds.union(x, y)
 
    return MST
 
    