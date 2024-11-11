def solve(M: int, N: int, G: list) -> str:
    """
    Return the shape of displayed by ASCII string G of dimensions M x N
    
    G: a string representing an ASCII picture
    M: integer for number of rows
    N: integer for number of columns
    """

    list_of_lengths = []

    
    for i in G:
        hashtag = i.count("#")
        list_of_lengths.append(hashtag)
    unique_set = set(list_of_lengths)
    if len(unique_set) > 2:
        return "Built like Phineas head"
    if len(unique_set) == 2:
        return "wow, its a square"
    


def main():
    T = int(input())
    for _ in range(T):
        M, N = map(int, input().split())
        G = []
        for _ in range(M):
            row = list(input().strip())
            G.append(row)
        solve(M, N, G)

if __name__ == '__main__':
    main()