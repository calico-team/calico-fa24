"""
experimenting with different implementations/optimizations to see what
thresholds are viable

this file uses a variant of the problem where querying gives a single random
edge instead of all edges
"""

import collections
import heapq
import random

import numpy as np
import networkx as nx
import pyperclip as pc

D = 3
N = 500

class DungeonGraph:
    def __init__(self, n=N, d=D):
        self.n = n
        self.d = d
        
        self.queries = 0
        self.random = random.Random(random.random())
        
        self._graph = None
        while not (self._graph and nx.is_connected(self._graph)):
            self._graph = nx.random_regular_graph(d, n)
    
    def query(self, node):
        self.queries += 1
        return self.random.choice(list(self._graph.neighbors(node - 1))) + 1
    
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

def solve_prebuilt_bfs(dg):
    adj_list = [[]]
    for i in range(1, dg.n + 1):
        adj_list.append(set())
        while len(adj_list[i]) < dg.d:
            adj_list[i].add(dg.query(i))
    
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

def solve_smart_prebuilt_bfs(dg):
    adj_list = [set() for _ in range(dg.n + 1)]
    for i in range(1, dg.n + 1):
        while len(adj_list[i]) < dg.d:
            v = dg.query(i)
            adj_list[i].add(v)
            adj_list[v].add(i)
    
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
    adj_list = [set() for _ in range(dg.n + 1)]
    def query(i):
        while len(adj_list[i]) < dg.d:
            v = dg.query(i)
            adj_list[i].add(v)
            adj_list[v].add(i)
        return adj_list[i]
    
    q = collections.deque([1])
    dists = {1: 0}
    while True:
        curr_node = q.popleft()
        if curr_node == dg.n:
            return dists[curr_node]
        for adj in query(curr_node):
            if adj not in dists:
                dists[adj] = dists[curr_node] + 1
                q.append(adj)

def solve_early_return_bfs(dg):
    adj_list = [set() for _ in range(dg.n + 1)]
    def query(i):
        while len(adj_list[i]) < dg.d:
            v = dg.query(i)
            adj_list[i].add(v)
            adj_list[v].add(i)
        return adj_list[i]
    
    q = collections.deque([1])
    dists = {1: 0}
    while True:
        curr_node = q.popleft()
        for adj in query(curr_node):
            if adj == dg.n:
                return dists[curr_node] + 1
            if adj not in dists:
                dists[adj] = dists[curr_node] + 1
                q.append(adj)

def solve_unoptimized_bidirectional_bfs(dg):
    def query(i):
        s = set()
        while len(s) < dg.d:
            v = dg.query(i)
            s.add(v)
        return s
    
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

def solve_bidirectional_bfs(dg):
    adj_list = [set() for _ in range(dg.n + 1)]
    def query(i):
        while len(adj_list[i]) < dg.d:
            v = dg.query(i)
            adj_list[i].add(v)
            adj_list[v].add(i)
        return adj_list[i]
    
    q_from_1 = collections.deque([1])
    q_from_n = collections.deque([dg.n])

    visited_from_1 = {1}
    visited_from_n = {dg.n}

    dist_estimate = 0

    while True:
        dist_estimate += 1
        for _ in range(len(q_from_1)):
            curr_node = q_from_1.popleft()
            for adj in query(curr_node):
                if adj not in visited_from_1:
                    visited_from_1.add(adj)
                    q_from_1.append(adj)

                    if adj in visited_from_n:
                        return dist_estimate

        dist_estimate += 1
        for _ in range(len(q_from_n)):
            curr_node = q_from_n.popleft()
            for adj in query(curr_node):
                if adj not in visited_from_n:
                    visited_from_n.add(adj)
                    q_from_n.append(adj)

                    if adj in visited_from_1:
                        return dist_estimate

def solve_picky_bidirectional_bfs(dg):
    adj_list = [set() for _ in range(dg.n + 1)]
    def query(i):
        while len(adj_list[i]) < dg.d:
            v = dg.query(i)
            adj_list[i].add(v)
            adj_list[v].add(i)
        return adj_list[i]
    
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

def solve_single_bidirectional_bfs(dg):
    adj_list = [set() for _ in range(dg.n + 1)]
    
    boundary_from_1 = [(0, 1)]
    visited_from_1 = {1}
    
    dist_estimate = 0
    while True:
        dist_estimate += 1
        # print('new est', dist_estimate)
        
        new_boundary = []
        while boundary_from_1:
            # print('scanning new boundary')
            known_edges, curr = heapq.heappop(boundary_from_1)
            
            # make sure entry is not outdated
            while known_edges != len(adj_list[curr]):
                # print('outdated entry found')
                heapq.heappush(boundary_from_1, (len(adj_list[curr]), curr))
                known_edges, curr = heapq.heappop(boundary_from_1)
            
            # if we scanned all neighbors, we're done
            if known_edges == dg.d:
                continue
            
            # scan until we get a new neighbor
            adj = dg.query(curr)
            while adj in adj_list[curr]:
                adj = dg.query(curr)
            
            # update adj_list
            adj_list[curr].add(adj)
            adj_list[adj].add(curr)
            
            visited_from_1.add(adj)
            new_boundary.append(adj)
            
            heapq.heappush(boundary_from_1, (len(adj_list[curr]), curr))

            if adj == dg.n:
                return dist_estimate
        
        boundary_from_1 = [(len(adj_list[u]), u) for u in new_boundary]


# def solve_optimized_bidirectional_bfs(dg):
#     adj_list = [set() for _ in range(dg.n + 1)]
#     def query(i):
#         while len(adj_list[i]) < dg.d:
#             v = dg.query(i)
#             adj_list[i].add(v)
#             adj_list[v].add(i)
#         return adj_list[i]
# 
#     boundary_from_1 = [(0, 1)]
#     boundary_from_n = [(0, dg.n)]
# 
#     visited_from_1 = {1}
#     visited_from_n = {dg.n}
# 
#     dist_estimate = 0
# 
#     while True:
#         dist_estimate += 1
# 
#         if len(q_from_1) <= len(q_from_n):
#             new_boundary = []
#             while boundary_from_1:
#                 known_edges, curr = heapq.heappop(q_from_1)
# 
#                 # make sure entry is not outdated
#                 while known_edges != len(adj_list[curr]):
#                     heapq.heappush(q_from_1, (len(adj_list[curr]), curr))
#                     priority, curr = heapq.heappop(q_from_1)
# 
#                 # if we scanned all neighbors, we're done
#                 if known_edges == dg.d:
#                     continue
# 
#                 # scan until we get a new neighbor
#                 v = dg.query(curr)
#                 while v in adj_list[curr]:
#                     v = dg.query(curr)
# 
#                 # update adj_list
#                 adj_list[i].add(v)
#                 adj_list[v].add(i)
# 
#                 visited_from_1.add(adj)
#                 new_boundary.append(adj)
# 
#                 if adj in visited_from_n:
#                     return dist_estimate
#         else:
#             for _ in range(len(q_from_n)):
#                 curr_node = q_from_n.popleft()
#                 for adj in query(curr_node):
#                     if adj not in visited_from_n:
#                         visited_from_n.add(adj)
#                         q_from_n.append(adj)
# 
#                         if adj in visited_from_1:
#                             return dist_estimate

def solve_optimized_bidirectional_bfs(dg):
    adj_list = [set() for _ in range(dg.n + 1)]
    
    boundary_from_1 = [(0, 1)]
    boundary_from_n = [(0, dg.n)]
    
    visited_from_1 = {1}
    visited_from_n = {dg.n}
    
    dist_estimate = 0
    while True:
        dist_estimate += 1
        # print('new est', dist_estimate)
        # print(len(boundary_from_1))
        # print(len(boundary_from_1))
        
        new_boundary = []
        
        if len(boundary_from_1) <= len(boundary_from_n):
            while boundary_from_1:
                # print('scanning new boundary')
                known_edges, curr = heapq.heappop(boundary_from_1)
                
                # make sure entry is not outdated
                while known_edges != len(adj_list[curr]):
                    # print('outdated entry found')
                    heapq.heappush(boundary_from_1, (len(adj_list[curr]), curr))
                    known_edges, curr = heapq.heappop(boundary_from_1)
                
                # if we scanned all neighbors, we're done
                if known_edges == dg.d:
                    continue
                
                # scan until we get a new neighbor
                adj = dg.query(curr)
                while adj in adj_list[curr]:
                    adj = dg.query(curr)
                
                # update adj_list
                adj_list[curr].add(adj)
                adj_list[adj].add(curr)
                
                visited_from_1.add(adj)
                new_boundary.append(adj)
                
                heapq.heappush(boundary_from_1, (len(adj_list[curr]), curr))

                if adj in visited_from_n:
                    return dist_estimate
            
            
                boundary_from_1 = [(len(adj_list[u]), u) for u in new_boundary]
        else:
            while boundary_from_n:
                # print('scanning new boundary')
                known_edges, curr = heapq.heappop(boundary_from_n)
                
                # make sure entry is not outdated
                while known_edges != len(adj_list[curr]):
                    # print('outdated entry found')
                    heapq.heappush(boundary_from_n, (len(adj_list[curr]), curr))
                    known_edges, curr = heapq.heappop(boundary_from_n)
                
                # if we scanned all neighbors, we're done
                if known_edges == dg.d:
                    continue
                
                # scan until we get a new neighbor
                adj = dg.query(curr)
                while adj in adj_list[curr]:
                    adj = dg.query(curr)
                
                # update adj_list
                adj_list[curr].add(adj)
                adj_list[adj].add(curr)
                
                visited_from_n.add(adj)
                new_boundary.append(adj)
                
                heapq.heappush(boundary_from_n, (len(adj_list[curr]), curr))

                if adj in visited_from_1:
                    return dist_estimate
            
            
                boundary_from_n = [(len(adj_list[u]), u) for u in new_boundary]

solvers = [
    # solve_prebuilt_bfs,
    # solve_smart_prebuilt_bfs,
    solve_wikipedia_bfs,
    solve_early_return_bfs,
    solve_unoptimized_bidirectional_bfs,
    # solve_single_bidirectional_bfs,
    # solve_bidirectional_bfs,
    solve_picky_bidirectional_bfs,
    # solve_optimized_bidirectional_bfs,
]

# verify_solve_funcs(solvers, 100)

# for solver in solvers:
#     get_stats(test_solve_func(solver, 3000))
