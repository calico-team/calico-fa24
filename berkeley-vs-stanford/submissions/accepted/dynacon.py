"""
Dynamic Connectivity for graphs.
Based on https://github.com/yosupo06/library-checker-problems/blob/master/graph/dynamic_graph_vertex_add_component_sum/sol/correct.cpp
"""


class EulerTourTreeNode:
    def __init__(self, l=0, r=0):
        self.ch = [None, None]
        self.p = None
        self.l = l
        self.r = r
        self.sz = int(l == r)
        self.sz2 = 0
        self.exact = True
        self.child_exact = l < r
        self.edge_connected = False

    def is_root(self) -> bool:
        return not self.p


class EulerTourTree:
    def __init__(self, N):
        self.ptr = [{i: EulerTourTreeNode(i, i)} for i in range(N)]
        self.N = N

    def _get_node(self, l, r):
        if r not in self.ptr[l]:
            self.ptr[l][r] = EulerTourTreeNode(l, r)
        return self.ptr[l][r]

    def _root(self, t):
        if not t:
            return t
        while t.p:
            t = t.p
        return t

    def _same(self, s, t):
        if s:
            self._splay(s)
        if t:
            self._splay(t)
        return self._root(s) == self._root(t)

    def _reroot(self, t):
        u, v = self._split(t)
        return self._merge(v, u)

    def _split(self, s):
        self._splay(s)
        t = s.ch[0]
        if t:
            t.p = None
        s.ch[0] = None
        return t, self._update(s)

    def _split2(self, s):
        self._splay(s)
        t, u = s.ch
        if t:
            t.p = None
        s.ch[0] = None
        if u:
            u.p = None
        s.ch[1] = None
        return t, u

    def _split3(self, s, t):
        u = self._split2(s)
        if self._same(u[0], t):
            r = self._split2(t)
            return r[0], r[1], u[1]
        else:
            r = self._split2(t)
            return u[0], r[0], r[1]

    def _merge(self, *args):
        def _merge_two(s, t):
            if not s:
                return t
            if not t:
                return s
            while s.ch[1]:
                s = s.ch[1]
            self._splay(s)
            s.ch[1] = t
            if t:
                t.p = s
            return self._update(s)

        ans = None
        for s in args:
            s = _merge_two(ans, s)

    def _size(self, t):
        return 0 if not t else t.sz

    def _size2(self, t):
        return 0 if not t else t.sz2

    def _update(self, t):
        t.sz = self._size(t.ch[0]) + int(t.l == t.r) + self._size(t.ch[1])
        t.sz2 = self._size2(t.ch[0]) + int(t.edge_connected) + self._size2(t.ch[1])
        t.child_exact = (
                (t.ch[0] and t.ch[0].child_exact)
                or (t.l < t.r and t.exact)
                or (t.ch[1] and t.ch[1].child_exact)
        )
        return t

    def _rot(self, t, b):
        x = t.p
        y = x.p
        b = int(b)
        x.ch[1 - b] = t.ch[b]
        if x.ch[1 - b]:
            t.ch[b].p = x
        t.ch[b] = x
        x.p = t
        self._update(x)
        self._update(t)
        t.p = y
        if t.p:
            if y.ch[0] == x:
                y.ch[0] = t
            if y.ch[1] == x:
                y.ch[1] = t
            self._update(y)

    def _splay(self, t):
        while not t.is_root():
            q = t.p
            if q.is_root():
                self._rot(t, q.ch[0] == t)
            else:
                r = q.p
                b = r.ch[0] == q
                if q.ch[1 - int(b)] == t:
                    self._rot(q, b)
                    self._rot(t, b)
                else:
                    self._rot(t, not b)
                    self._rot(t, b)

    """ Declaration of public methods """

    def size(self, s):
        t = self._get_node(s, s)
        self._splay(t)
        return t.sz

    def same(self, s, t):
        return self._same(self._get_node(s, s), self._get_node(t, t))

    def set_size(self, sz):
        while len(self.ptr) < sz:
            self.ptr.append({len(self.ptr): EulerTourTreeNode(len(self.ptr), len(self.ptr))})

    def edge_connected_update(self, s, b):
        t = self._get_node(s, s)
        self._splay(t)
        t.edge_connected = b
        self._update(t)

    def link(self, l, r):
        if self.same(l, r):
            return False
        self._merge(
            self._reroot(self._get_node(l, l)),
            self._get_node(l, r),
            self._reroot(self._get_node(r, r)),
            self._get_node(r, l),
        )
        return True

    def cut(self, l, r):
        if r not in self.ptr[l]:
            return False
        s, t, u = self._split3(self._get_node(l, r), self._get_node(r, l))
        self._merge(s, u)
        p, q = self.ptr[l][r], self.ptr[r][l]
        del self.ptr[l][r]
        del self.ptr[r][l]
        return True

    def edge_update(self, s, g):
        t = self._get_node(s, s)
        self._splay(t)

        def dfs(t):
            assert t
            if t.l < t.r and t.exact:
                self._splay(t)
                t.exact = False
                self._update(t)
                g(t.l, t.r)
                return
            if t.ch[0] and t.ch[0].child_exact:
                dfs(t.ch[0])
            else:
                dfs(t.ch[1])

        while t and t.child_exact:
            dfs(t)
            self._splay(t)

    def try_reconnect(self, s, f):
        t = self._get_node(s, s)
        self._splay(t)

        def dfs(t, idx):
            assert t
            if t.edge_connected and self._size2(t.ch[0]) == idx:
                self._splay(t)
                return f(t.l)
            if idx < self._size(t.ch[0]):
                return dfs(t.ch[0], idx)
            else:
                return dfs(t.ch[1], idx - self._size2(t.ch[0]) - int(t.edge_connected))

        while self._size2(t):
            if dfs(t, 0):
                return True
            self._splay(t)

        return False


class DynamicConnectivity:
    def __init__(self, sz):
        self.sz = sz
        self.dep = 1
        self.ett = []
        self.edges = []
        self.ett.append(EulerTourTree(sz))
        self.edges.append([set() for _ in range(sz)])

    def link(self, s, t):
        if s == t:
            return False
        if self.ett[0].link(s, t):
            return True
        self.edges[0][s].add(t)
        self.edges[0][t].add(s)
        if len(self.edges[0][s]) == 1:
            self.ett[0].edge_connected_update(s, True)
        if len(self.edges[0][t]) == 1:
            self.ett[0].edge_connected_update(t, True)
        return False

    def same(self, s, t):
        return self.ett[0].same(s, t)

    def size(self, s):
        return self.ett[0].size(s)

    def cut(self, s, t):
        if s == t:
            return False
        for i in range(self.dep):
            self.edges[i][s].discard(t)
            self.edges[i][t].discard(s)
            if len(self.edges[i][s]) == 0:
                self.ett[i].edge_connected_update(s, False)
            if len(self.edges[i][t]) == 0:
                self.ett[i].edge_connected_update(t, False)

        for i in range(self.dep - 1, -1, -1):
            if self.ett[i].cut(s, t):
                if self.dep - 1 == i:
                    self.dep += 1
                    self.ett.append(EulerTourTree(self.sz))
                    self.edges.append([set() for _ in range(self.sz)])
                return not self.try_reconnect(s, t, i)

        return 0

    def try_reconnect(self, s, t, k):
        for i in range(k):
            self.ett[i].cut(s, t)
        for i in range(k, -1, -1):
            if self.ett[i].size(s) > self.ett[i].size(t):
                s, t = t, s

            def g(s, t):
                self.ett[i + 1].link(s, t)

            self.ett[i].edge_update(s, g)

            def f(x):
                for y in list(self.edges[i][x]):
                    self.edges[i][x].discard(y)
                    self.edges[i][y].discard(x)
                    if len(self.edges[i][x]) == 0:
                        self.ett[i].edge_connected_update(x, False)
                    if len(self.edges[i][y]) == 0:
                        self.ett[i].edge_connected_update(y, False)
                    if self.ett[i].same(x, y):
                        self.edges[i + 1][x].add(y)
                        self.edges[i + 1][y].add(x)
                        if len(self.edges[i + 1][x]) == 1:
                            self.ett[i + 1].edge_connected_update(x, True)
                        if len(self.edges[i + 1][y]) == 1:
                            self.ett[i + 1].edge_connected_update(y, True)

                    else:
                        for j in range(i + 1):
                            self.ett[j].link(x, y)
                        return True

                return False

            if self.ett[i].try_reconnect(s, f):
                return True

        return False


from collections import deque

class Matroid:
    def __init__(self, n: int, ground_set=None):
        self._iset = set()
        self._n = n
        if ground_set is not None:
            self._ground_set = set(ground_set)
            if len(self._ground_set) != n:
                raise ValueError(
                    f"Mismatch between n={n} and the size of the ground set {ground_set}"
                )
        else:
            self._ground_set = set(range(n))
        self._complement = self._ground_set - self._iset

    def independent(self):
        """
        Check if the given subset is independent.
        Must be implemented specifically for each matroid.
        """
        raise NotImplementedError("This method should be implemented by subclasses")

    def add(self, element):
        self._iset.add(element)
        self._complement.discard(element)

    def remove(self, element):
        self._iset.discard(element)
        self._complement.add(element)

    def contains(self, element):
        return element in self._iset

    def ground_set(self):
        return self._ground_set

    def current_set(self):
        return self._iset.copy()

    def compute_all_circuits(self):
        """
        Returns a dictionary of int to set computing all C(X, y)
        """
        answers = {y: set() for y in self._complement}
        complement = self._complement.copy()
        for y in complement:
            self.add(y)
            if self.independent():
                self.remove(y)
                continue
            for x in self.current_set():
                self.remove(x)
                if self.independent():
                    answers[y].add(x)
                self.add(x)
            self.remove(y)
        return answers


# Example Matroid Implementations
class UniformMatroid(Matroid):
    def __init__(self, n: int, rank: int):
        super().__init__(n)
        self.rank = rank

    def independent(self):
        return len(self._iset) <= self.rank


class PartitionMatroid(Matroid):
    def __init__(self, n: int, partition, capacities):
        super().__init__(n)
        self.partition = partition
        self.capacities = capacities

    def independent(self):
        counts = {}
        for e in self._iset:
            cls = self.partition[e]
            counts[cls] = counts.get(cls, 0) + 1
            if counts[cls] > self.capacities[cls]:
                return False
        return True


def WeightedMatroidIntersection(n: int, F1: Matroid, F2: Matroid, c: dict):
    E = set(range(n))  # Ground set
    X = set()  # Current independent set
    c1 = {e: c[e] for e in E}  # Adjusted weights c1
    c2 = {e: 0 for e in E}  # Adjusted weights c2
    k = 0
    total_weight = 0
    max_total_weight = 0
    answers = []
    bestX = set()
    C1, C2 = None, None
    while True:
        # Step 2: Compute C_i(X_k, y) if they haven't been computed
        if C1 is None:
            C1 = F1.compute_all_circuits()
            C2 = F2.compute_all_circuits()

            # Step 3: Compute A^1, A^2, S, T
            A1, A2, S, T = set(), set(), set(), set()
            for y in E - X:
                for x in C1[y]:
                    if x != y:
                        A1.add((x, y))
                for x in C2[y]:
                    if x != y:
                        A2.add((y, x))
                F1.add(y)
                if F1.independent():
                    S.add(y)
                F1.remove(y)
                F2.add(y)
                if F2.independent():
                    T.add(y)
                F2.remove(y)

        # Step 4: Compute m1, m2, barS, barT, barA1, barA2
        if not S:
            m1 = float("-inf")
            barS = set()
        else:
            m1 = max(c1[y] for y in S)
            barS = {y for y in S if c1[y] == m1}
        if not T:
            m2 = float("-inf")
            barT = set()
        else:
            m2 = max(c2[y] for y in T)
            barT = {y for y in T if c2[y] == m2}

        barA1 = {(x, y) for (x, y) in A1 if c1[x] == c1[y]}
        barA2 = {(y, x) for (y, x) in A2 if c2[x] == c2[y]}

        G = {e: [] for e in E}
        for x, y in barA1:
            G[x].append(y)
        for y, x in barA2:
            G[y].append(x)

        # Step 5: Apply BFS to compute R
        R = set(barS)
        parents = {e: None for e in E}
        found = None
        queue = deque(list(barS))

        while queue:
            u = queue.popleft()
            if u in barT:
                found = u
                break
            for v in G[u]:
                if v not in R:
                    R.add(v)
                    parents[v] = u
                    queue.append(v)

        # Step 6: Augmentation of Weight Adjustment

        if found is not None:
            # Augment along the path from found back to start
            path = []
            current = found
            while current is not None:
                path.append(current)
                current = parents[current]
            path.reverse()

            # Update X
            for idx, e in enumerate(path):
                if idx % 2 == 0:
                    # Add to X
                    X.add(e)
                    F1.add(e)
                    F2.add(e)
                    total_weight += c[e]
                else:
                    # Remove from X
                    X.remove(e)
                    F1.remove(e)
                    F2.remove(e)
                    total_weight -= c[e]

            answers.append(total_weight)
            max_total_weight = max(max_total_weight, total_weight)
            if total_weight == max_total_weight:
                bestX = X
            k += 1
            C1, C2 = None, None

        else:
            # Compute epsilon values
            epsilon1 = float("inf")
            for x, y in A1:
                if x in R and y not in R:
                    epsilon1 = min(epsilon1, c1[x] - c1[y])

            epsilon2 = float("inf")
            for y, x in A2:
                if y in R and x not in R:
                    epsilon2 = min(epsilon2, c2[x] - c2[y])

            epsilon3 = float("inf")
            for y in S - R:
                epsilon3 = min(epsilon3, m1 - c1[y])

            epsilon4 = float("inf")
            for y in T & R:
                epsilon4 = min(epsilon4, m2 - c2[y])
            epsilon = min(epsilon1, epsilon2, epsilon3, epsilon4)

            if epsilon == float("inf"):
                break
            else:
                # Adjust weights
                for x in R:
                    c1[x] -= epsilon
                    c2[x] += epsilon

    return max_total_weight, answers


class SpecialBondMatroid(Matroid):
    def __init__(self, v, edges, S, B):
        super().__init__(len(edges))
        self._v = v
        self._edges = edges
        self._source = S
        self._sink = B
        self.g = DynamicConnectivity(v)
        for e in self._edges:
            if self._sink not in e[0:2]:
                self.g.link(e[0], e[1])

    def independent(self):
        """
        Returns true if all vertices (aside from sink) are reachable from source without going through sink
        """
        return self.g.size(self._source) == self._v - 1

    def add(self, element):
        super().add(element)
        e = self._edges[element]
        if self._sink not in e[0:2]:
            self.g.cut(e[0], e[1])

    def remove(self, element):
        super().remove(element)
        e = self._edges[element]
        if self._sink not in e[0:2]:
            self.g.cut(e[0], e[1])

def solve(N: int, M: int, B: int, S: int, E: list[(int, int, int)]) -> int:
    F1 = SpecialBondMatroid(N, E, B, S)
    F2 = SpecialBondMatroid(N, E, S, B)
    total_weight = sum(e[2] for e in E)
    weights = {i: e[2] for i, e in enumerate(E)}
    max_weight, answers = WeightedMatroidIntersection(M, F1, F2, weights)
    return total_weight - max_weight


def main():
    tc = int(input())
    for _ in range(tc):
        n, m, b, s = map(int, input().split())
        edges = [tuple(map(int, input().split())) for _ in range(m)]
        print(solve(n, m, b, s, edges))


if __name__ == "__main__":
    main()
