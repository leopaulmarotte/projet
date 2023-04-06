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

class node_objet:

    def __init__(self, value):
        self.value = value
        self.next = None

class queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return not self.head

    def enqueue(self, new_node):
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "You queue is empty"
        else:
            deleted_element = self.head.value
            self.head = self.head.next
            return(deleted_element)


class Graph:

    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.list_edges = []
    

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
        self.list_edges.append((node1, node2, power_min))


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

    def dijkstra(self,src,dest,power):
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

# Question 14

    def min_power_optimized(g, src, dest):
        g_mst = kruskal(g)
        return g_mst.min_power(src,dest)


# Question 12

def kruskal(G):
    list_edges = G.list_edges
    i = 0
    g_mst = Graph(range(1,G.nb_nodes+1)) # Initialization of our mst
    mst_union_find = union_find({})
    mst_union_find.make_set(list(G.nodes)) # Initialization of our union-find structure to know if another edge create a cycle or not
    list_edges.sort(key=lambda l : l[2]) # We have collected all the edges and make sure we did not take a edge twice, and sorted them by power
    while g_mst.nb_edges != G.nb_nodes-1:
        node1,node2,power = list_edges[i]
        i += 1
        if mst_union_find.find(node1) != mst_union_find.find(node2): # We added the edges only if it does not create a cycle
            g_mst.add_edge(node1, node2, power)
            mst_union_find.op_union(node1, node2)
    return(g_mst)


# Question 13

# There are already 2 tests implemented
# g.kruskal() instead of doing kruskal(g) as it was previously computed
# We implemented a new graph "my_network.06.py" which successfuly passed the test



# Question 16

# We do first a breadth-first search using a queue-structure in order to give a depth to each node of the mst
def bfs(G):
    deep_state = {node : None for node in G.nodes} # depth of each node using a dictionary
    marked_node = {node : False for node in G.nodes} #We need to know which nodes have already been visited
    father_power = {node : (None,1000000) for node in G.nodes} # We will need to know the fathers to build the path
    root = G.nodes[0] # We take the first element as the root
    marked_node[root] = True
    deep_state[root] = 0
    root = node_objet(root) # We convert the root as an element of our queue
    Q = queue()
    Q.enqueue(root)
    while not Q.is_empty(): # while the queue is not empty, we wil add the neigbors in the queue if they are not marked
        node = Q.dequeue()
        for neighbor in G.graph[node]:
            neighbor,power = neighbor[0],neighbor[1]
            if not marked_node[neighbor]:
                deep_state[neighbor] = deep_state[node] + 1 # the depth of a node is the one from the father + 1
                father_power[neighbor] = node,power
                Q.enqueue(node_objet(neighbor))
                marked_node[neighbor] = True # We don't forget to mark the nodes
    return(deep_state,father_power) # We return both the depth of each nodes and their fathers as well as the power between them


def new_minpower_aux(g_mst, src, dest): #main function but with the g_mst so that we only calculate hime once for all the routes
    power_min = 0 # power_min will be the max of the power on the path because a truck will need to have a higher power than each edges
    deep_level,father_power = bfs(g_mst)
    if deep_level[src] < deep_level[dest]: # We choose to have the source the deeper
        src,dest = dest,src
    path_src_father = [src] # We creater 2 paths we will concatenate after : src->father and father->dest
    path_father_dest = [dest]
    moving_node_src,moving_node_dest = src,dest # The moving nodes will be the different fathers until a common father
    while deep_level[moving_node_src] != deep_level[dest]: # first, we run from the source (the deeper) until a node as deep as the dest
        moving_node_src,power = father_power[moving_node_src]
        power_min = max(power_min,power)
        path_src_father.append(moving_node_src)
    while moving_node_src != moving_node_dest: # Then, we take the fathers of each sides until we got the same (the root in the worst case)
        moving_node_src,power_src = father_power[moving_node_src]
        moving_node_dest,power_dest = father_power[moving_node_dest]
        path_src_father.append(moving_node_src)
        path_father_dest.append(moving_node_dest)
        power_min = max(power_min,power_dest,power_src)
    path_src_father = path_src_father[0:len(path_src_father)-1] #the common ancestor is present once in each list, we remove it from the first list
    path_father_dest.reverse() # we had dest-> father while we need father->dest
    path = path_src_father + path_father_dest # src->father->dest = src->dest which is our path
    return(path,power_min) #We return the path and the power_min needed for that path
    
def new_minpower(G,src,dest): #The final function
    g_mst = kruksal(G)
    return new_minpower_aux(g_mst, src, dest)

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
        a = int(file.readline()) # We save the amount of itineraries
        g = graph_from_file("input/network." + str(n) + ".in")
        for i in range(10): # Average with 10 itineraries
            node1,node2,p = map(int, file.readline().split())
            t1 = time.perf_counter()
            opti = g.min_power(node1, node2)
            t2 = time.perf_counter()
            time_est += (t2-t1)
    print((a/10)*time_est)
    
 

# Séance 4




# Question 18

def route_from_file(filename):
    itineraries = []
    with open(filename, "r") as file:
        nb_itinerary = int(file.readline())
        for _ in range(nb_itinerary):
            src,dest,profit = map(int, file.readline().split())
            itineraries.append((src,dest,profit))
    return(itineraries)

def truck_from_file(filename):
    trucks = []
    with open(filename, "r") as file:
        nb_models = int(file.readline())
        for _ in range(nb_models):
            power,cost = map(int, file.readline().split())
            trucks.append((power,cost))
    return(trucks)

def optimized_truck(liste_truck, power_min): # liste_truck is sorted by power : we process by dichotomic search
    left, right = 0, (len(liste_truck)-1)
    while left != right:
        middle = (left+right)//2
        truck_applicant = liste_truck[middle]
        if truck_applicant[0] >= power_min:
            right = middle
        else:
            left = middle + 1
    if liste_truck[right][0] >= power_min:
        return(liste_truck[right])
    else:
        return([None,None])
    
def only_useful_truck(list_trucks): # To remove useless trucks : those with higher cost thant other but less powerful
    list_trucks.sort(key=lambda only_useful_truck : only_useful_truck[1]) #We sort the list_truck by cost
    useful_trucks = []
    moving_power = 0 #it will be the power of the different truck
    for truck in list_trucks:
        if moving_power < truck[0]: #We don't take the truck if the power is lower than the former one (whose the cost whose lower due to the sort)
            useful_trucks.append(truck)
            moving_power = truck[0]
    return(useful_trucks)



def truck_affectation(G,list_route,list_trucks):

#INPUT : 
#G = a graph from the class graph
#liste_route = a list with 3-uplets coding each road : a source, a destination and #a profit/utility : [[src1, dest1, profit1], … , [srcn, destin, profitn]]
#liste_trucks : a list with 2-uplets coding a truck : the power and the cost
#[[power1, cost1], … , [powern, costn]]

#OUTPUT : 
#list_truck_affected which is a list with 3 elements : 
#the good truck coding with the 2-uplet like before
#the route coding with the 3-uplet like before
#the value of the power_min for the route

    list_trucks.sort() #We sort the trucks by the first argument which is the power
    list_powermin = []
    list_trucks_affected = []
    list_trucks = only_useful_truck(list_trucks)
    kruskal(G)
    for route in list_route: #For each route, we will identify the cheapest truck to do it
        src,dest,profit = route
        path,power_min = new_minpower_aux(G, src, dest)
        list_powermin.append(power_min)
    for i in range(len(list_powermin)):
        good_truck = optimized_truck(list_trucks, list_powermin[i])
        list_trucks_affected.append([good_truck, list_route[i], list_powermin[i]])
    return(list_trucks_affected)


def knapsack_cost(G,list_trucks, list_route, my_B):

#INPUT : 
#G, list_trucks, list_route : exactly the same as in truck_affection
#my_B which is an integer coding our budget

#OUTPUT : 
#selected_itineraries : a list of the selected itineraries coding exactly as in #truck_affection : a 3-uplet with 
                      # the good truck (a 2-uplet), the route (a 3-uplet) #and an integer for the power_min

#not_selected_itineraries :  which is a list of the itineraries that have not #been selected by our 
                            # algorithm : the elements are coding exactly like in #the selected_itineraries
#2 integers : the total_cost which is the amount of money spent to buy #our trucks and total_profit which is 
                # the profit made by doing the #selected itineraries.

    list_trucks = only_useful_truck(list_trucks)
     #We have our budjet, to not delete the initial value
    total_cost = 0 #At the beginning, nothing was buy so our total cost is null
    list_trucks_affected = truck_affectation(G, list_route, list_trucks) #for each route, we associate it the truck with the less power but enough powerful to do it (which is by doing so the cheapest truck thanks to only_useful_truck)
    list_trucks_affected.sort(key=lambda l : l[0][1], reverse=True)
    selected_itineraries = [] #only the routes with the highest efficency will be selected
    not_selected_itineraries = []
    list_profit = []
    for index_itinerary in range(len(list_trucks_affected)):
        cost = list_trucks_affected[index_itinerary][0][1]
        association = list_trucks_affected[index_itinerary]
        profit = association[1][2]
        if cost + total_cost < my_B: #We add a route by descending efficency and only if it is in our budget : maybe there is further a route with a lower profit but which need a truck which is still in our budget
            selected_itineraries.append(association) 
            list_profit.append(profit)
            total_cost += cost #We actualize our spendings
        else:
            selected_itineraries.append(None)
            not_selected_itineraries.append(association)
            list_profit.append(0)
    total_profit = sum(list_profit)
    return(selected_itineraries, not_selected_itineraries, total_cost, total_profit)


def knapsack_efficiency(G,list_trucks, list_route, my_B):
    list_trucks = only_useful_truck(list_trucks)
     #We have our budjet, to not delete the initial value
    total_cost = 0 #At the beginning, nothing was buy so our total cost is null
    list_trucks_affected = truck_affectation(G, list_route, list_trucks) #for each route, we associate it the truck with the less power but enough powerful to do it (which is by doing so the cheapest truck thanks to only_useful_truck)
    list_efficiency = [] #a list of efficency corresponding to the quotient of the profit of a route by the cost of the associated truck
    selected_itineraries = [] #only the routes with the highest efficency will be selected
    list_profit = []
    not_selected_itineraries = []
    for association in list_trucks_affected: #We create the list of efficency
        utility, cost, profit = association[1][2],association[0][1],association[1][2]
        efficiency = utility/cost
        list_efficiency.append((efficiency,association))
    list_efficiency.sort(reverse=True) #We sort it by descending in order to have the highest efficency at the beginning
    for index_itinerary in range(len(list_efficiency)):
        if list_efficiency[index_itinerary][0] != [None,None]:
            cost = list_efficiency[index_itinerary][1][0][1]
            association = list_efficiency[index_itinerary][1][0:3]
            profit = association[1][2]
            if cost + total_cost < my_B: #We add a route by descending efficency and only if it is in our budget : maybe there is further a route with a lower profit but which need a truck which is still in our budget
                selected_itineraries.append(association) 
                list_profit.append(profit)
                total_cost += cost #We actualize our spendings
            else:
                selected_itineraries.append(None) 
                not_selected_itineraries.append(association)
                list_profit.append(0)
    total_profit = sum(list_profit)
    return(selected_itineraries,not_selected_itineraries, total_cost, total_profit)