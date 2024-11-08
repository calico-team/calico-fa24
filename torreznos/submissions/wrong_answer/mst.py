class UnionFind:
    def __init__(self, n):
        self.n = n
        self.p = [-1 for _ in range(n)]

    def find(self, x):
        if self.p[x] < 0:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.p[x] > self.p[y]:
            x, y = y, x
        self.p[x] += self.p[y]
        self.p[y] = x
        return True

def solve(N: int, M: int, B: int, S: int, E: list[(int, int, int)]) -> int:
    """ Just return a min spanning tree of the graph without checking condition """
    dsu = UnionFind(N)
    E.sort(key=lambda e: e[2])
    ans = 0
    for e in E:
        if dsu.union(e[0], e[1]):
            ans += e[2]
    return ans



def main():
    T = int(input())
    for _ in range(T):
        N, M, F, S = map(int, input().split())
        E = [tuple(map(int, input().split())) for _ in range(M)]
        print(solve(N, M, F, S, E))


if __name__ == "__main__":
    main()