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
    def __init__(self, v, edges, source, sink):
        super().__init__(len(edges))
        self._v = v
        self._edges = edges
        self._source = source
        self._sink = sink
        self.g = {i: [] for i in range(v)}
        for i, e in enumerate(edges):
            self.g[e[0]].append((i, e[1]))
            self.g[e[1]].append((i, e[0]))

    def independent(self):
        """
        Returns true if all vertices (aside from sink) are reachable from source without going through sink
        """
        visited = set()
        q = deque()
        q.append(self._source)
        visited.add(self._source)

        while q:
            u = q.popleft()
            for i, v in self.g[u]:
                # In bond matroid we have the graph and take away edges if they are in the independent set.
                if i not in self._iset and v != self._sink and v not in visited:
                    visited.add(v)
                    q.append(v)
        assert self._sink not in visited
        return len(visited) == self._v - 1


def solve(N: int, M: int, F: int, S: int, E: list[(int, int, int)]) -> int:
    F1 = SpecialBondMatroid(N, E, F, S)
    F2 = SpecialBondMatroid(N, E, S, F)
    total_weight = sum(e[2] for e in E)
    weights = {i: e[2] for i, e in enumerate(E)}
    max_weight, answers = WeightedMatroidIntersection(M, F1, F2, weights)
    return total_weight - max_weight


def main():
    T = int(input())
    for _ in range(T):
        N, M, F, S = map(int, input().split())
        E = [tuple(map(int, input().split())) for _ in range(M)]
        print(solve(N, M, F, S, E))


if __name__ == "__main__":
    main()