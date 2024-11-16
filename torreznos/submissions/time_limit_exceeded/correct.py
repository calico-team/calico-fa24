def solve(N: int, M: int, F: int, S: int, E: list[(int, int, int)]) -> int:
    ans = int(2e9)
    for i in range(1 << M):
        G = [[] for _ in range(N)]
        sum_weights = 0
        for j in range(M):
            if i & (1 << j):
                G[E[j][0]].append(E[j][1])
                G[E[j][1]].append(E[j][0])
                sum_weights += E[j][2]

        if sum_weights > ans:
            continue

        def dfs(u, t):
            vis.add(u)
            ret = 1
            for v in G[u]:
                if v != t and v not in vis:
                    ret += dfs(v, t)
            return ret

        vis = set()
        if dfs(S, F) != N - 1:
            continue
        vis = set()
        if dfs(F, S) != N - 1:
            continue
        ans = min(ans, sum_weights)

    return ans


def main():
    T = int(input())
    for _ in range(T):
        N, M, F, S = map(int, input().split())
        E = [tuple(map(int, input().split())) for _ in range(M)]
        print(solve(N, M, F, S, E))


if __name__ == "__main__":
    main()
