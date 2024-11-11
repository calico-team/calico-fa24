def solve(N: int, M: int, G: list[list[int]]) -> int:
    """
    Return the maximum number of islands.

    N: number of rows
    M: number of columns
    G: grid of heights
    """
    mx_g = 0
    for row in G:
        mx_g = max(mx_g, max(row))

    vis = []
    def dfs(i, j):
        vis[i][j] = True
        for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if not vis[i + di][j + dj]:
                dfs(i + di, j + dj)
    
    mx_islands = 0
    for H in range(mx_g + 1):
        islands = 0
        # Marking submerged cells and borders as "visited" for convenience
        vis = [[True] * (M + 2) for _ in range(N + 2)]
        for i in range(N):
            for j in range(M):
                vis[i + 1][j + 1] = G[i][j] < H
        for i in range(N):
            for j in range(M):
                if not vis[i + 1][j + 1]:
                    islands += 1
                    dfs(i + 1, j + 1)
        mx_islands = max(mx_islands, islands)

    return mx_islands

def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        N, M = int(temp[0]), int(temp[1])
        G = []
        for _ in range(N):
            G.append([int(x) for x in input().split()])
        print(solve(N, M, G))

if __name__ == '__main__':
    main()
