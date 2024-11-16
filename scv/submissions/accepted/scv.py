def solve(N: int, M: int, G: list [str]) -> str:
    """
    Return the shape displayed by the picture represented by G of dimensions N x M
    
    G: a list of strings representing a picture
    N: integer for number of rows
    M: integer for number of columns
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
        N, M = map(int, input().split())
        G = []
        for _ in range(N):
            row = list(input().strip())
            G.append(row)
        print(solve(N, M, G))

if __name__ == '__main__':
    main()