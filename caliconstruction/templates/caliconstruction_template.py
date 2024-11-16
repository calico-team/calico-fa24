def solve(S: str) -> int:
    """
    Return the minimum number of sets of CALICO blocks needed to
    form S, or -1 if it is impossible.

    S: a string
    """
    return 1


def main():
    T = int(input())
    for _ in range(T):
        S = input()
        print(solve(S))


if __name__ == '__main__':
    main()
