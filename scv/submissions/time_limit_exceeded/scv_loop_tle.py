def solve(N: int, M: int, G: list) -> str:
    """
    Infinite loop TLE
    
    G: a string representing an ASCII picture
    N: integer for number of rows
    M: integer for number of columns
    """
    c = 0
    while True:
        c += 1

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        G = []
        for _ in range(N):
            row = list(input().strip())
            G.append(row)
        print(solve(N, M, G))

if __name__ == '__main__':
    main()