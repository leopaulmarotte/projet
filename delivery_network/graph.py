class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
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
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        
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
        noeud_visite = {noeud:False for noeud in self.nodes}

        def recherche_de_chemin(noeud, chemin):
            if noeud == dest :
                return chemin
            for voisin in self.graph[noeud]:
                voisin, power_min, dist = voisin
                if not noeud_visite[voisin] and power_min <= power:
                    noeud_visite[voisin] = True
                    resultat = recherche_de_chemin(voisin, chemin + [voisin])
                    if resultat is not None :
                        return resultat
            return None
        return recherche_de_chemin(src, [src])

  
   


    
        
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
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
    
    



        return set(map(frozenset, self.connected_components()))
    
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        
        def get_path_with_power(self, src, dest, power):
            noeud_visite = {noeud:False for noeud in self.nodes}

            def recherche_de_chemin(noeud, chemin):
                if noeud == dest :
                    return chemin
                for voisin in self.graph[noeud]:
                    voisin, power_min, dist = voisin
                    if not noeud_visite[voisin] and power_min <= power:
                        noeud_visite[voisin] = True
                        resultat = recherche_de_chemin(voisin, chemin + [voisin])
                        if resultat is not None :
                            return resultat
                return None
            return recherche_de_chemin(src, [src])



        puissances = []
        for noeuds in self.nodes :
            for noeuds1 in self.graph[noeuds] :
                puissances.append(noeuds1[1])
        

        

        puissances = frozenset(puissances)
        puissances = list(puissances)
        puissances = sorted(puissances)

        print(puissances)

    
        a = 0
        b = len(puissances) - 1
        if get_path_with_power(self, src, dest, puissances[b]) is None:
            return None
        
        else :
            while a < b:
                m = (a + b) // 2
                print(m)
                if get_path_with_power(self,src, dest, puissances[m]) is None:
                    
                    a = m + 1
                    print(a,b)
                
                else : 
                    
                    b = m 
                    print(a,b)
        m = b
        print(a,b)
        print(m)
        print(puissances[m] )         
                
            

        return (get_path_with_power(self, src, dest, puissances[m]), puissances[m])



def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    G: Graph
        An object of the class Graph with the graph from file_name.
    """
   
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


    