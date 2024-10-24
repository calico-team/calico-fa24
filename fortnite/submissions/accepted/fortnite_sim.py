def solve(N: int, H: int, D: int, S: int, P: int, T: int) -> int:
    """
    Return the shape of displayed by ASCII string G of dimensions M x N
    
    N: starting health
    H: amount of healing
    D: distance out of the storm in meters
    S: running speed in meters per second
    P: storm damage per second
    T: time to heal
    """
    heal_count = 0
    while D > 0:
        if N - P * (T + 1) <= 0:
            N += H - P * T
            heal_count += 1
        D -= S
        N -= P 
    return heal_count

def main():
    T = int(input())
    for _ in range(T):
        N, H, D, S, P, T = map(int, input().split())
        print(solve(N, H, D, S, P, T))

if __name__ == '__main__':
    main()