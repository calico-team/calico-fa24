def solve(M: int, N: int, G: list) -> str:
    """
    Return the shape of displayed by ASCII string G of dimensions N x M
    
    G: a string representing an ASCII picture
    N: integer for number of rows
    M: integer for number of columns
    """
    # YOUR CODE HERE
    return ''
    

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        G = []
        for _ in range(N):
            row = list(input().strip())
            G.append(row)
        solve(N, M, G)

if __name__ == '__main__':
    main()