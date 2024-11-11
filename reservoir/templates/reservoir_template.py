def solve(N: int, M: int, G: list[list[int]]) -> int:
    """
    Return the height H Evbo should choose.

    N: number of rows
    M: number of columns
    G: grid of heights
    """
    # YOUR CODE HERE
    return 0

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
