def solve(B: int, N: int, S:list) -> int:
    '''
    Return the height H in which the danger is minimized and satisfies the budget constraints.
    '''
    # YOUR CODE HERE
    return -1


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        B, N = int(temp[0]), int(temp[1])
        S = [int(x) for x in input().split()]
        print(solve(B, N, S))


if __name__ == '__main__':
    main()
