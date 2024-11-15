def solve(B: int, N: int, S: list) -> int:
    low = min(S)
    high = max(S)
    while low < high:
        mid = (high + low) // 2
        cost = 0
        danger = 0
        for h in S:
            danger += max(mid - h, 0)
            cost += max(h - mid, 0)
        if cost > B:
            low = mid + 1
        else:
            high = mid
    return low


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        B, N = int(temp[0]), int(temp[1])
        S = [int(x) for x in input().split()]
        print(solve(B, N, S))


if __name__ == "__main__":
    main()
