def solve(M: int, N: int, G: list) -> str:
    """
    Infinite loop TLE
    
    G: a string representing an ASCII picture
    M: integer for number of rows
    N: integer for number of columns
    """
    c = 0
    while True:
        c += 1

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