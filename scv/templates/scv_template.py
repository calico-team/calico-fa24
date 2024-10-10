def solve(M: int, N: int, G: list) -> str:
    """
    Return the shape of displayed by ASCII string S of dimensions R x C
    
    S: a string representing an ASCII picture
    R: integer for number of rows
    C: integer for number of columns
    """
    # YOUR CODE HERE
    return 0


def main():
    T = int(input())
    for _ in range(T):
        M, N = map(int, input().split())
        G = []
        for _ in range(M):
            row = list(input().strip())
            G.append(row)
        print(G)
        solve(M, N, G)

if __name__ == '__main__':
    main()