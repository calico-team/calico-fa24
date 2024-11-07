def solve(B: int, N: int, S:list) -> int:
    low = 0
    high = 1e9
    while low<high:
        mid = low + (high-low)//2
        cost = 0
        danger = 0
        for h in S:
            if (h<mid):
                danger+=mid-h
            elif (h>mid):
                cost += h - mid
        if cost>B:
            low = mid+1
        else:
            high = mid
    return int(low)


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        B, N = int(temp[0]), int(temp[1])
        S = [int(x) for x in input().split()]
        print(solve(B, N, S))


if __name__ == '__main__':
    main()
