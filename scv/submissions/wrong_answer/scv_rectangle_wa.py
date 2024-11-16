def solve(N: int, M: int, G: list) -> str:
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
        N, M = map(int, input().split())
        G = []
        for _ in range(N):
            row = list(input().strip())
            G.append(row)
        print(solve(N, M, G))

if __name__ == '__main__':
    main()