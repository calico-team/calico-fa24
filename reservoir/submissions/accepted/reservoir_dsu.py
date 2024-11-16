from typing import List, Tuple, Dict
from collections import defaultdict

class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.r = [0] * n

    def get(self, a: int) -> int:
        if a != self.p[a]:
            self.p[a] = self.get(self.p[a])
        return self.p[a]

    def uni(self, a: int, b: int):
        a, b = self.get(a), self.get(b)
        if a == b:
            return
        if self.r[b] < self.r[a]:
            a, b = b, a
        if self.r[b] == self.r[a]:
            self.r[b] += 1
        self.p[a] = b
        global islands
        islands -= 1

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solve(N: int, M: int, G: List[List[int]]) -> int:
    global islands
    # Extend grid with borders (-1 for always-submerged border cells)
    Gp = [[-1] * (M + 2) for _ in range(N + 2)]
    for i in range(N):
        for j in range(M):
            Gp[i + 1][j + 1] = G[i][j]

    # Mapping height to list of cells at that height
    m = {}
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            key = Gp[i][j]
            if key not in m:
                m[key] = []
            m[key].append((i, j))

    dsu = DSU((N + 2) * (M + 2))
    mx_islands = 0
    islands = 0
    for h, cells in sorted(m.items())[::-1]:
        islands += len(cells)
        for i, j in cells:
            for di, dj in DIRS:
                ip, jp = i + di, j + dj
                if Gp[ip][jp] >= h:
                    dsu.uni(i * (M + 2) + j, ip * (M + 2) + jp)
        mx_islands = max(mx_islands, islands)

    return mx_islands

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        G = [list(map(int, input().split())) for _ in range(N)]
        print(solve(N, M, G))

if __name__ == "__main__":
    main()
