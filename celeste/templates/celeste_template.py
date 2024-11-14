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
    # YOUR CODE HERE
    return -1


def main():
    T = int(input())
    for _ in range(T):
        N, M, K = [int(x) for x in input().split()]
        C = [str(input().strip()) for x in range(N)]
        print(solve(N, M, K, C))


if __name__ == '__main__':
    main()
