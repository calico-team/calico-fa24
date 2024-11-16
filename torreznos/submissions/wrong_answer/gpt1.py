def solve(N, M, B, S, E):
    # Helper class for Union-Find (Disjoint Set Union)
    class UnionFind:
        def __init__(self, size):
            self.parent = list(range(size))
            self.rank = [0] * size

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])  # Path compression
            return self.parent[x]

        def union(self, x, y):
            xroot = self.find(x)
            yroot = self.find(y)
            if xroot == yroot:
                return False  # Already connected
            # Union by rank to keep tree shallow
            if self.rank[xroot] < self.rank[yroot]:
                self.parent[xroot] = yroot
            else:
                self.parent[yroot] = xroot
                if self.rank[xroot] == self.rank[yroot]:
                    self.rank[xroot] += 1
            return True

    # Function to build MST edges excluding a specific node
    def get_mst_edges(exclude_node, required_node):
        uf = UnionFind(N)
        mst_edges = set()
        # Sort edges by weight (ascending)
        sorted_edges = sorted(E, key=lambda x: x[2])
        for u, v, w in sorted_edges:
            if u == exclude_node or v == exclude_node:
                continue  # Skip edges connected to the excluded node
            if uf.union(u, v):
                # Store edges as sorted tuples to handle undirected edges
                if u < v:
                    mst_edges.add((u, v, w))
                else:
                    mst_edges.add((v, u, w))
        # Verify connectivity: all nodes (except excluded) must be connected to the required node
        root = uf.find(required_node)
        for node in range(N):
            if node == exclude_node:
                continue
            if uf.find(node) != root:
                return None  # Not all nodes are connected
        return mst_edges

    # Build MST1: Connectivity to B excluding S
    mst1 = get_mst_edges(S, B)
    # Build MST2: Connectivity to S excluding B
    mst2 = get_mst_edges(B, S)

    # If either MST cannot be formed, return -1 indicating no valid subset exists
    if mst1 is None or mst2 is None:
        return -1

    # Identify overlapping edges between MST1 and MST2
    overlap = mst1.intersection(mst2)
    # Identify unique edges in MST1 and MST2
    unique_mst1 = mst1 - overlap
    unique_mst2 = mst2 - overlap

    # Calculate the total weight: overlapping edges counted once
    total_weight = sum(edge[2] for edge in overlap) + \
                   sum(edge[2] for edge in unique_mst1) + \
                   sum(edge[2] for edge in unique_mst2)

    return total_weight


def main():
    T = int(input())
    for _ in range(T):
        N, M, F, S = map(int, input().split())
        E = [tuple(map(int, input().split())) for _ in range(M)]
        print(solve(N, M, F, S, E))


if __name__ == "__main__":
    main()