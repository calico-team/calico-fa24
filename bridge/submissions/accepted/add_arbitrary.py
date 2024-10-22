def solve(B: int, N: int, S:list) -> int:
    '''
    Implements addition with Python's arbitary precision arithmetic.
    '''

    
    return B


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        B, N = int(temp[0]), int(temp[1])
        S = [int(x) for x in input().split()]
        print(solve(B, N, S))


if __name__ == '__main__':
    main()
