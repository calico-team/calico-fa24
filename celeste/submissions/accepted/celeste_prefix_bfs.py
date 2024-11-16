def solve(N: int, M: int, K: int, C: list[str]) -> int:
    """
    Return the minimum number of moves to get to E, or return 
    -1 if it is impossible.

    N: number of rows
    M: number of columns
    K: the length of Madeline’s dash
    C: a list of N strings with M characters each, describing 
    the maze Madeline is in.
       In each string:
        . denotes a space
        # denotes a wall.
        * denotes a dash crystal.

    """
    UP, DOWN, LEFT, RIGHT = "U", "D", "L", "R"
    dirs = [UP, DOWN, LEFT, RIGHT]

    # dash_distance[r][c][dir] => (d = distance dashed, p = passes over crystal)
    dash_distance = [[{} for _ in range(M)] for _ in range(N)]

    def init_dash_distance():
        # Initialize p = True if (r, c) is a space and a crystal exists one step in the specified direction
        crystal_adjacent_condition = {
            UP: lambda r, c : (r > 0) and (C[r - 1][c] == '*'),
            DOWN: lambda r, c : (r < N - 1) and (C[r + 1][c] == '*'),
            LEFT: lambda r, c : (c > 0) and (C[r][c - 1] == '*'),
            RIGHT: lambda r, c : (c < M - 1) and (C[r][c + 1] == '*')
        }

        # Begin initializing dash_distance with placeholder values
        for dir in dirs:
            for r in range(N):
                for c in range(M):
                    dash_distance[r][c][dir] = (-1, C[r][c] != '#' and crystal_adjacent_condition[dir](r, c))
    
    init_dash_distance()

    for r in range(N):
        for c in range(M):
            if C[r][c] == '#':
                continue

            dash_distance[r][c][UP] = (
                min(K, 1 + dash_distance[r - 1][c][UP]),
                (r > 0) and (C[r - 1][c] == '*')
            )

            dash_distance[r][c][LEFT] = (
                min(K, 1 + dash_distance[r][c - 1][LEFT]),
                (c > 0) and (C[r][c - 1] == '*')
            )
    
    for r in range(N - 1, -1, -1):
        for c in range(M - 1, -1, -1):
            if C[r][c] == '#':
                continue
            
            dash_distance[r][c][DOWN] = (
                min(K, 1 + dash_distance[r + 1][c][DOWN]),
                (r < N - 1) and (C[r + 1][c] == '*')
            )
            
            dash_distance[r][c][RIGHT] = (
                min(K, 1 + dash_distance[r][c + 1][RIGHT]),
                (c < M - 1) and (C[r][c + 1] == '*')
            )




def main():
    T = int(input())
    for _ in range(T):
        N, M, K = [int(x) for x in input().split()]
        C = [str(input().strip()) for x in range(N)]
        print(solve(N, M, K, C))


if __name__ == '__main__':
    main()
