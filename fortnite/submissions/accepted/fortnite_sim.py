def solve(N: int, H: int, D: int, S: int, P: int, L: int) -> int:
    """
    Return the number of healing items the player needs to use.
    
    N: starting health
    H: amount of healing
    D: distance out of the storm in meters
    S: running speed in meters per second
    P: storm damage per second
    L: time to heal
    """
    heal_count = 0
    while (True):
        D -= S
        if D < 0:
            break
        while N - P * (L + 1) <= 0:
            N += H - P * L
            heal_count += 1
        N -= P 
    return heal_count

def main():
    T = int(input())
    for _ in range(T):
        N, H, D, S, P, L = map(int, input().split())
        print(solve(N, H, D, S, P, L))

if __name__ == '__main__':
    main()