def solve(M: int, N: int, G: list) -> str:
    """
    Return the shape displayed by the picture represented by G of dimensions M x N
    
    G: a list of strings representing a picture
    M: integer for number of rows
    N: integer for number of columns
    """
    # YOUR CODE HERE
    return ''
    

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