def solve(N: int, H: int, D: int, S: int, P: int) -> float:
    """
    Return the minimum time for you to escape the storm
    
    N: starting health
    H: healing per second
    D: distance out of the storm in meters
    S: running speed in meters per second
    P: storm damage per second
    """
    time_to_escape = D / S
    damage_taken_to_escape = P * time_to_escape

    if damage_taken_to_escape > N:
        if P >= H:
            return -1.0
        extra_health_needed = damage_taken_to_escape - N
        time_to_heal = extra_health_needed / (H - P)
        time_to_escape += time_to_heal
        
    return time_to_escape

def main():
    T = int(input())
    for _ in range(T):
        N, H, D, S, P = map(int, input().split())
        print(solve(N, H, D, S, P))

if __name__ == '__main__':
    main()