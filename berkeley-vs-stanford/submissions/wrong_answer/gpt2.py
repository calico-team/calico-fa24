def solve(N, M, B, S, E):
    from collections import deque

    # Build the auxiliary graph
    class Edge:
        def __init__(self, to, rev, capacity, cost):
            self.to = to
            self.rev = rev
            self.capacity = capacity
            self.cost = cost

    class Graph:
        def __init__(self, N):
            self.size = N
            self.graph = [[] for _ in range(N)]

        def add_edge(self, fr, to, capacity, cost):
            forward = Edge(to, len(self.graph[to]), capacity, cost)
            backward = Edge(fr, len(self.graph[fr]), 0, -cost)
            self.graph[fr].append(forward)
            self.graph[to].append(backward)

    INF = float('inf')

    # Node indices
    # For each node v, we have v_in and v_out
    node_indices = {}
    idx = 0
    for v in range(N):
        node_indices[(v, 'in')] = idx
        idx += 1
        node_indices[(v, 'out')] = idx
        idx += 1

    s = idx  # Super source
    idx += 1
    t = idx  # Super sink
    idx += 1

    total_nodes = idx
    graph = Graph(total_nodes)

    # Add edges from v_in to v_out with infinite capacity (except for B and S)
    for v in range(N):
        if v == B or v == S:
            capacity = 2  # We need to allow up to 2 units of flow (one to B, one to S)
        else:
            capacity = 2  # Each node can send up to 2 units of flow
        graph.add_edge(node_indices[(v, 'in')], node_indices[(v, 'out')], capacity, 0)

    # Add edges for the undirected edges in E
    for u, v, w in E:
        # Edge from u_out to v_in
        graph.add_edge(node_indices[(u, 'out')], node_indices[(v, 'in')], 1, w)
        graph.add_edge(node_indices[(v, 'out')], node_indices[(u, 'in')], 1, w)

    # Add edges from super source to all nodes except B and S
    for v in range(N):
        if v != B and v != S:
            # Each node has a demand of 2 units (one to B, one to S)
            graph.add_edge(s, node_indices[(v, 'out')], 2, 0)

    # Add edges from B_in and S_in to super sink
    graph.add_edge(node_indices[(B, 'in')], t, INF, 0)
    graph.add_edge(node_indices[(S, 'in')], t, INF, 0)

    # Remove edges to prevent flows passing through S when going to B, and vice versa
    # Remove edge S_in -> S_out when modeling flows to B
    # Remove edge B_in -> B_out when modeling flows to S

    # Implement Min-Cost Max-Flow algorithm (e.g., successive shortest augmenting path)
    def min_cost_max_flow(graph, s, t):
        flow = 0
        cost = 0
        potential = [0] * graph.size  # For reduced costs

        while True:
            dist = [INF] * graph.size
            prevv = [-1] * graph.size
            preve = [-1] * graph.size
            inqueue = [False] * graph.size
            dist[s] = 0

            queue = deque()
            queue.append(s)
            while queue:
                v = queue.popleft()
                inqueue[v] = False
                for i, e in enumerate(graph.graph[v]):
                    if e.capacity > 0:
                        to = e.to
                        rcost = e.cost + potential[v] - potential[to]
                        if dist[to] > dist[v] + rcost:
                            dist[to] = dist[v] + rcost
                            prevv[to] = v
                            preve[to] = i
                            if not inqueue[to]:
                                queue.append(to)
                                inqueue[to] = True

            if dist[t] == INF:
                break

            for v in range(graph.size):
                if dist[v] < INF:
                    potential[v] += dist[v]

            # Find the minimum capacity along the path
            d = INF
            v = t
            while v != s:
                d = min(d, graph.graph[prevv[v]][preve[v]].capacity)
                v = prevv[v]

            # Augment flow
            v = t
            while v != s:
                e = graph.graph[prevv[v]][preve[v]]
                e.capacity -= d
                graph.graph[v][e.rev].capacity += d
                v = prevv[v]
            flow += d
            cost += d * potential[t]

        return flow, cost

    flow, total_cost = min_cost_max_flow(graph, s, t)

    # Check if the total flow is equal to 2 * (N - 2) (since each node except B and S needs to send 2 units of flow)
    if flow < 2 * (N - 2):
        # Not all demands were met
        return -1

    return int(total_cost)


def main():
    T = int(input())
    for _ in range(T):
        N, M, B, S = map(int, input().split())
        E = [tuple(map(int, input().split())) for _ in range(M)]
        print(solve(N, M, B, S, E))


if __name__ == "__main__":
    main()
