def solve(N: int, M: int, F: int, S: int, E: list[(int, int, int)]) -> int:
    """
    Return the minimum weight of a subset of E that fits the problem statement conditions.
    N : Number of vertices
    M : Number of edges
    F : France
    S : Spain
    E : Graph edges in the format (u, v, w)
    """
    # YOUR CODE HERE
    return -1


def main():
    T = int(input())
    for _ in range(T):
        N, M, F, S = map(int, input().split())
        E = [tuple(map(int, input().split())) for _ in range(M)]
        print(solve(N, M, F, S, E))


if __name__ == "__main__":
    main()
