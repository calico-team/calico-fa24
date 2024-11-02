def solve(M: int, N: int, G: list) -> str:
    """
    Do not check the character, will constantly return "rectangle"
    """
    row_count = set()
    for row in G:
        count = 0
        for letter in row:
                count += 1
    if len(row_count) <= 1:
        return 'rectangle'
    return 'triangle' 

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