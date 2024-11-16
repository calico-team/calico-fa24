def solve(N: int, M: int, G: list[list[int]]) -> int:
    """
    Return the maximum number of islands.

    N: number of rows
    M: number of columns
    G: grid of heights
    """
    # YOUR CODE HERE
    return 0

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        G = [list(map(int, input().split())) for _ in range(N)]
        print(solve(N, M, G))

if __name__ == '__main__':
    main()
