"""
experimenting with different implementations/optimizations to see what
thresholds are viable
"""


import collections
import heapq
import random

import numpy as np
import networkx as nx
import pyperclip as pc

D = 5
N = 500

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

def test_solve_func(solve_func, t, n=N, d=D):
    random.seed(1337)
    np.random.seed(69420)
    
    queries_list = []
    for _ in range(t):
        dg = DungeonGraph(n, d)
        solve_func(dg)
        queries_list.append(dg.queries)
    return queries_list

def get_stats(queries_list):
    print('benchmarking', solver.__name__)
    
    print('mean', np.mean(queries_list))
    print('std', np.std(queries_list))
    print('median', np.median(queries_list))
    
    pc.copy(f'histogram({queries_list}, {N // 10})')
    print('desmos histogram copied to clipboard')
    
    print()

def verify_solve_funcs(solve_funcs, t, n=N, d=D):
    random.seed(1337)
    np.random.seed(69420)
    
    for _ in range(t):
        dg = DungeonGraph(n, d)
        answers = [solve_func(dg) for solve_func in solve_funcs]
        assert len(set(answers)) == 1
    
    print('all solvers concur!')

################################################################################

def solve_stupid_bfs(dg):
    adj_list = [[]]
    for i in range(1, dg.n + 1):
        adj_list.append(dg.query(i))
    
    q = collections.deque([1])
    dists = {1: 0}
    while True:
        curr_node = q.popleft()
        if curr_node == dg.n:
            return dists[curr_node]
        for adj in adj_list[curr_node]:
            if adj not in dists:
                dists[adj] = dists[curr_node] + 1
                q.append(adj)

def solve_wikipedia_bfs(dg):    
    q = collections.deque([1])
    dists = {1: 0}
    while True:
        curr_node = q.popleft()
        if curr_node == dg.n:
            return dists[curr_node]
        for adj in dg.query(curr_node):
            if adj not in dists:
                dists[adj] = dists[curr_node] + 1
                q.append(adj)

def solve_early_return_bfs(dg):    
    q = collections.deque([1])
    dists = {1: 0}
    while True:
        curr_node = q.popleft()
        for adj in dg.query(curr_node):
            if adj == dg.n:
                return dists[curr_node] + 1
            if adj not in dists:
                dists[adj] = dists[curr_node] + 1
                q.append(adj)

def solve_bidirectional_bfs(dg):    
    q_from_1 = collections.deque([1])
    q_from_n = collections.deque([dg.n])
    
    visited_from_1 = {1}
    visited_from_n = {dg.n}
    
    dist_estimate = 0
    
    while True:
        dist_estimate += 1
        for _ in range(len(q_from_1)):
            curr_node = q_from_1.popleft()
            for adj in dg.query(curr_node):
                if adj not in visited_from_1:
                    visited_from_1.add(adj)
                    q_from_1.append(adj)
                    
                    if adj in visited_from_n:
                        return dist_estimate
        
        dist_estimate += 1
        for _ in range(len(q_from_n)):
            curr_node = q_from_n.popleft()
            for adj in dg.query(curr_node):
                if adj not in visited_from_n:
                    visited_from_n.add(adj)
                    q_from_n.append(adj)
                    
                    if adj in visited_from_1:
                        return dist_estimate

def solve_picky_bidirectional_bfs(dg):
    q_from_1 = collections.deque([1])
    q_from_n = collections.deque([dg.n])
    
    visited_from_1 = {1}
    visited_from_n = {dg.n}
    
    dist_estimate = 0
    
    while True:
        if len(q_from_1) <= len(q_from_n):
            dist_estimate += 1
            for _ in range(len(q_from_1)):
                curr_node = q_from_1.popleft()
                for adj in dg.query(curr_node):
                    if adj not in visited_from_1:
                        visited_from_1.add(adj)
                        q_from_1.append(adj)
                        
                        if adj in visited_from_n:
                            return dist_estimate
        else:
            dist_estimate += 1
            for _ in range(len(q_from_n)):
                curr_node = q_from_n.popleft()
                for adj in dg.query(curr_node):
                    if adj not in visited_from_n:
                        visited_from_n.add(adj)
                        q_from_n.append(adj)
                        
                        if adj in visited_from_1:
                            return dist_estimate

def solve_optimized_bidirectional_bfs(dg):
    cache = [set() for _ in range(dg.n + 1)]
    def query(node):
        if len(cache[node]) < dg.d:
            cache[node].update(dg.query(node))
            assert len(cache[node]) == dg.d
            for adj in cache[node]:
                cache[adj].add(node)
        else:
            print('cache hit!')
        
        return sorted(cache[node])
    
    q_from_1 = collections.deque([1])
    q_from_n = collections.deque([dg.n])
    
    visited_from_1 = {1}
    visited_from_n = {dg.n}
    
    dist_estimate = 0
    
    while True:
        if len(q_from_1) <= len(q_from_n):
            dist_estimate += 1
            for _ in range(len(q_from_1)):
                curr_node = q_from_1.popleft()
                for adj in query(curr_node):
                    if adj not in visited_from_1:
                        visited_from_1.add(adj)
                        q_from_1.append(adj)
                        
                        if adj in visited_from_n:
                            return dist_estimate
        else:
            dist_estimate += 1
            for _ in range(len(q_from_n)):
                curr_node = q_from_n.popleft()
                for adj in query(curr_node):
                    if adj not in visited_from_n:
                        visited_from_n.add(adj)
                        q_from_n.append(adj)
                        
                        if adj in visited_from_1:
                            return dist_estimate

solvers = [
    solve_stupid_bfs,
    solve_wikipedia_bfs,
    solve_early_return_bfs,
    solve_bidirectional_bfs,
    # solve_picky_bidirectional_bfs,
    # solve_optimized_bidirectional_bfs,
]

verify_solve_funcs(solvers, 100)

for solver in solvers:
    get_stats(test_solve_func(solver, 1000))
