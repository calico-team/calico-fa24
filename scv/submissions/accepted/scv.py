def solve(M: int, N: int, G: list) -> str:
    numbers = set()
    
    for row in G:
        counter = row.count('#') 
        if counter > 0:
            numbers.add(counter)
    
    if len(numbers  ) == 1:
        return "rectangle"
    else: 
        return "triangle"


def main():
    ans = []
    T = int(input())
    for _ in range(T):
        M, N = map(int, input().split())
        G = []
        for _ in range(M):
            row = input().strip()  
            G.append(row)
        
        result = solve(M, N, G)
        ans.append(result)
    
    for answer in ans:
        print(answer)


if __name__ == '__main__':
    main()
