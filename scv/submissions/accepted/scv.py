def solve(M: int, N: int, G: list [str]) -> str:
    """
    Return the shape displayed by the picture represented by G of dimensions M x N
    
    G: a list of strings representing a picture
    M: integer for number of rows
    N: integer for number of columns
    """
    row_count = set()
    for row in G:
        count = 0
        for letter in row:
            if letter == '#':
                count += 1
        if count != 0:
            row_count.add(count)
    if len(row_count) <= 1:
        return 'ferb'
    return 'phineas' 

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