def solve(N: int, H: int, D: int, S: int, P: int) -> int:
    """
    Return the minimum time needed for you to exit the storm.
    
    N: starting health
    H: healing per second
    D: distance out of the storm in meters
    S: running speed in meters per second
    P: storm damage per second
    """
    # YOUR CODE HERE
    return -1


def main():
    T = int(input())
    for _ in range(T):
        N, H, D, S, P = map(int, input().split())
        print(solve(N, H, D, S, P))

if __name__ == '__main__':
    main()
