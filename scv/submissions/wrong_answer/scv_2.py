def solve(N: int, M: int, G: list) -> str:
    """
    Return the shape of displayed by ASCII string G of dimensions N x M
    
    G: a string representing an ASCII picture
    N: integer for number of rows
    M: integer for number of columns
    """

    list_of_lengths = []

    
    for i in G:
        hashtag = i.count("#")
        list_of_lengths.append(hashtag)
    unique_set = set(list_of_lengths)
    if len(unique_set) > 2:
        return "triangle"
    if len(unique_set) == 2:
        return "rectangle"
    


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