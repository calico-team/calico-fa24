def solve(B: int, N: int, S:list) -> int:
    '''
    Implements addition with Python's arbitary precision arithmetic.
    '''

    
    return B

def danger_and_cost(H: int, N: int, S: list) -> tuple:
    danger = 0
    cost = 0

    for x in range(0, N-1):
        danger += max(0, S[x] - H)
        cost += max(0, H - S[x])
    
    return danger, cost

def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        B, N = int(temp[0]), int(temp[1])
        S = [int(x) for x in input().split()]
        print(solve(B, N, S))


if __name__ == '__main__':
    main()
