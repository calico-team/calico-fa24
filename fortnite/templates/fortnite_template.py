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
    # YOUR CODE HERE
    return -1

def main():
    T = int(input())
    for _ in range(T):
        N, H, D, S, P, T = map(int, input().split())
        print(solve(N, H, D, S, P, T))

if __name__ == '__main__':
    main()