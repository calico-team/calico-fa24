def solve(N: int, M: int, B: int, S: int, E: list[(int, int, int)]) -> int:
    """ TODO: Implement your solution"""


def main():
    T = int(input())
    for _ in range(T):
        N, M, B, S = map(int, input().split())
        E = [tuple(map(int, input().split())) for _ in range(M)]
        print(solve(N, M, B, S, E))


if __name__ == "__main__":
    main()
