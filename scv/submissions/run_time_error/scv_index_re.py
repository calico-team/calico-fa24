def solve(M: int, N: int, G: list) -> str:
    """
    Index out of bound RE
    
    G: a string representing an ASCII picture
    M: integer for number of rows
    N: integer for number of columns
    """
    return G[len(G)]

def main():
    T = int(input())
    for _ in range(T):
        M, N = map(int, input().split())
        G = []
        for _ in range(M):
            row = list(input().strip())
            G.append(row)
        print(solve(M, N, G))

if __name__ == '__main__':
    main()