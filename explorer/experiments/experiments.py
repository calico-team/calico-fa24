import collections
import heapq

import numpy as np
import networkx as nx
import pyperclip as pc

D = 5
N = 10000

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
        return [adj + 1 for adj in self._graph.neighbors(node - 1)]
    
    def print(self):
        for u, v in self._graph.edges:
            print(u + 1, v + 1)

def test_solve_func(solve_func, t, n=N, d=D):
    queries_list = []
    for _ in range(t):
        dg = DungeonGraph(n, d)
        solve_func(dg)
        queries_list.append(dg.queries)
    return queries_list

def get_stats(queries_list):
    print('mean', np.mean(queries_list))
    print('std', np.std(queries_list))
    print('median', np.median(queries_list))
    
    pc.copy(f'histogram({queries_list}, {N // 10})')
    print('desmos histogram copied to clipboard')

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

def solve_double_bfs(dg):
    q_from_1 = collections.deque([1])
    q_from_n = collections.deque([dg.n])
    dists_from_1 = {1: 0}
    dists_from_n = {dg.n: 0}
    while True:
        curr_node = q_from_1.popleft()
        for adj in dg.query(curr_node):
            if adj in dists_from_n:
                return dists_from_1[curr_node] + 1 + dists_from_n[adj]
            if adj not in dists_from_1:
                dists_from_1[adj] = dists_from_1[curr_node] + 1
                q_from_1.append(adj)
        
        curr_node = q_from_n.popleft()
        for adj in dg.query(curr_node):
            if adj in dists_from_1:
                return dists_from_n[curr_node] + 1 + dists_from_1[adj]
            if adj not in dists_from_n:
                dists_from_n[adj] = dists_from_n[curr_node] + 1
                q_from_n.append(adj)

def solve_cached_double_bfs(dg):
    cache = [set() for _ in range(dg.n + 1)]
    def query(node):
        if len(cache[node]) != 3:
            cache[node].update(dg.query(node))
            for adj in cache[node]:
                cache[adj].add(node)
        return cache[node]
    
    q_from_1 = collections.deque([1])
    q_from_n = collections.deque([dg.n])
    dists_from_1 = {1: 0}
    dists_from_n = {dg.n: 0}
    while True:
        curr_node = q_from_1.popleft()
        for adj in query(curr_node):
            if adj in dists_from_n:
                return dists_from_1[curr_node] + 1 + dists_from_n[adj]
            if adj not in dists_from_1:
                dists_from_1[adj] = dists_from_1[curr_node] + 1
                q_from_1.append(adj)
        
        curr_node = q_from_n.popleft()
        for adj in query(curr_node):
            if adj in dists_from_1:
                return dists_from_n[curr_node] + 1 + dists_from_1[adj]
            if adj not in dists_from_n:
                dists_from_n[adj] = dists_from_n[curr_node] + 1
                q_from_n.append(adj)

def solve_cached_priority_double_bfs(dg):
    cache = [set() for _ in range(dg.n + 1)]
    def query(node):
        if len(cache[node]) != 3:
            cache[node].update(dg.query(node))
            for adj in cache[node]:
                cache[adj].add(node)
        return cache[node]
    
    q_from_1 = [(0, 0, 1)]
    q_from_n = [(0, 0, dg.n)]
    dists_from_1 = {1: 0}
    dists_from_n = {dg.n: 0}
    while True:
        curr_dist, curr_known_edges, curr_node = heapq.heappop(q_from_1)
        while curr_known_edges != len(cache[curr_node]):
            heapq.heappush(q_from_1, (curr_dist, len(cache[curr_node]), curr_node))
            curr_dist, curr_known_edges, curr_node = heapq.heappop(q_from_1)
        for adj in query(curr_node):
            if adj in dists_from_n:
                return dists_from_1[curr_node] + 1 + dists_from_n[adj]
            if adj not in dists_from_1:
                dists_from_1[adj] = dists_from_1[curr_node] + 1
                heapq.heappush(q_from_1, (dists_from_1[adj], len(cache[adj]), adj))
        
        curr_dist, curr_known_edges, curr_node = heapq.heappop(q_from_n)
        while curr_known_edges != len(cache[curr_node]):
            heapq.heappush(q_from_n, (curr_dist, len(cache[curr_node]), curr_node))
            curr_dist, curr_known_edges, curr_node = heapq.heappop(q_from_n)
        for adj in query(curr_node):
            if adj in dists_from_1:
                return dists_from_n[curr_node] + 1 + dists_from_1[adj]
            if adj not in dists_from_n:
                dists_from_n[adj] = dists_from_n[curr_node] + 1
                heapq.heappush(q_from_n, (dists_from_n[adj], len(cache[adj]), adj))

# 
# def solve_gigachad_bfs(dg):
#     adj_list = [[] for _ in range(dg.n + 1)]
# 
#     # (distance from start, number of known neighbors, node)
#     q = [(0, 0, 1)]
#     dists = {0: 0}
# 
#     while True:
#         curr_dist, curr_neighbors, curr_node = heapq.heappop(q)
#         if curr_neighbors != len(adj_list[curr_node]):
#             heapq.heappush((dist, len(adj_list[curr_node]), curr_node))
# 
#         if curr_node == dg.n:
#             return dist
# 
# 
#         for adj in dg.query(node):
#             if adj not in dists:
#                 dists[adj] = dist
# 
#         else if :
#             dist1[] = dist
# 
# 
#             if node1 not in seen1:
#                 seen1[node1] = dist1
#                 for adj1 in dg.query(node1):
#                     if adj1 in seen2:
#                         return dist1 + 1 + seen2[adj1]
#                     q1.append((adj1, dist1 + 1))
# 
#         node2, dist2 = q2.popleft()
#         if node2 not in seen2:
#             seen2[node2] = dist2
#             for adj2 in dg.query(node2):
#                 if adj2 in seen1:
#                     return dist2 + 1 + seen1[adj2]
#                 q2.append((adj2, dist2 + 1))


get_stats(test_solve_func(solve_double_bfs, 100))
get_stats(test_solve_func(solve_cached_priority_double_bfs, 100))
