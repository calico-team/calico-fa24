from typing import List

def solve(B: int, N: int, S: List[int]) -> int:
    '''
    Implements addition with Python's arbitary precision arithmetic.
    '''
    return 0


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        B, N = int(temp[0]), int(temp[1])
        S:int = []
        for _ in range(N):
            S.append(int(input()))
        print(solve(B, N, S))


if __name__ == '__main__':
    main()
