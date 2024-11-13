"""
chatpgt is garbage at writing bidirectional bfs lmfao this implementation is
just straight up wrong :skull:
"""


from collections import deque

import random

import numpy as np
import networkx as nx


N = 1000
D = 3

def bidirectional_bfs(graph, source=0, target=N-1):
    if source == target:
        return 0  # If the source and target are the same, no path is needed
    
    # Initialize queues for the forward and backward BFS
    queue_source = deque([source])
    queue_target = deque([target])
    
    # Initialize distances for both searches
    distance_from_source = {source: 0}
    distance_from_target = {target: 0}
    
    # Initialize explored sets for both searches
    visited_from_source = {source}
    visited_from_target = {target}
    
    # Perform bidirectional BFS
    while queue_source and queue_target:
        # Step 1: Expand from source side
        if queue_source:
            current_node = queue_source.popleft()
            current_distance = distance_from_source[current_node]
            
            # Explore neighbors
            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited_from_source:
                    visited_from_source.add(neighbor)
                    distance_from_source[neighbor] = current_distance + 1
                    queue_source.append(neighbor)
                    
                    # Check if the node is visited by the target-side search
                    if neighbor in visited_from_target:
                        return distance_from_source[neighbor] + distance_from_target[neighbor]
        
        # Step 2: Expand from target side
        if queue_target:
            current_node = queue_target.popleft()
            current_distance = distance_from_target[current_node]
            
            # Explore neighbors
            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited_from_target:
                    visited_from_target.add(neighbor)
                    distance_from_target[neighbor] = current_distance + 1
                    queue_target.append(neighbor)
                    
                    # Check if the node is visited by the source-side search
                    if neighbor in visited_from_source:
                        return distance_from_source[neighbor] + distance_from_target[neighbor]

    # If no path exists
    return -1

def bfs(graph, source=0, target=N-1):
    if source == target:
        return 0  # If source and target are the same, no path is needed
    
    # Initialize BFS structures
    queue = deque([source])
    distance = {source: 0}  # Distance from source to each node
    
    while queue:
        current_node = queue.popleft()
        current_distance = distance[current_node]
        
        # Explore neighbors of the current node
        for neighbor in graph.neighbors(current_node):
            if neighbor not in distance:  # Node not visited yet
                distance[neighbor] = current_distance + 1
                queue.append(neighbor)
                
                # If we reach the target node, return the distance
                if neighbor == target:
                    return distance[neighbor]
    
    # If no path exists, return -1
    return -1

class DungeonGraph:
    def __init__(self, n=N, d=D):
        self.n = n
        self.d = d
        
        self.queries = 0
        
        self._graph = None
        while not (self._graph and nx.is_connected(self._graph)):
            self._graph = nx.random_regular_graph(d, n)
    
    def query(self, node):
        self.queries += 1
        return sorted(adj + 1 for adj in self._graph.neighbors(node - 1))
    
    def print(self):
        for u, v in self._graph.edges:
            print(u + 1, v + 1)

def verify_solve_funcs(solve_funcs, t, n=N, d=D):
    random.seed(1337)
    np.random.seed(69420)
    
    for _ in range(t):
        dg = DungeonGraph(n, d)
        answers = [solve_func(dg._graph) for solve_func in solve_funcs]
        print(answers)
        assert len(set(answers)) == 1
    
    print('all solvers concur!')

verify_solve_funcs([bfs, bidirectional_bfs], 100)
