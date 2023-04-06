class Graph:
    
    def __init__(self, nodes=[]):
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    
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
    # Finds the root node of a subtree containing node `i`
     def find(self, k):
        if self.parent_node[k] == k:
            return k
        return self.find(self.parent_node[k])

    # Connects subtrees containing nodes `x` and `y`
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

    def connect_subtrees(self, parent, subtree_sizes, x, y):
        xroot = self.find_subtree(parent, x)
        yroot = self.find_subtree(parent, y)
        if subtree_sizes[xroot] < subtree_sizes[yroot]:
            parent[xroot] = yroot
        elif subtree_sizes[xroot] > subtree_sizes[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            subtree_sizes[xroot] += 1

    def kruskals_mst(self):
        # Resulting tree
        result = dict([(n, []) for n in self.nodes])
        # Iterator
        i = 0
        # Number of edges in MST
        e = 0
        # Sort edges by their weight
        self.m_graph = sorted(self.m_graph, key=lambda item: item[2])

        # Auxiliary arrays
        parent = []
        subtree_sizes = []

        # Initialize `parent` and `subtree_sizes` arrays
        for node in range(self.nb_nodes):
            parent.append(node)
            subtree_sizes.append(0)

        # Important property of MSTs
        # number of egdes in a MST is
        # equal to (m_num_of_nodes - 1)
        while e < (self.nb_nodes - 1):
            # Pick an edge with the minimal weight
            t = self.graph[i]
            for j in t:
                node1, node2, weight = j
                i = i + 1

                x = self.find_subtree(parent, node1)
                y = self.find_subtree(parent, node2)

                if x != y:
                    e = e + 1
                    result[].append([node1, node2, weight])
                    self.connect_subtrees(parent, subtree_sizes, x, y)
        return result


