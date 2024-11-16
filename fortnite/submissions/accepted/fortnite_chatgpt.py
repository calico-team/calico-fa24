# File: fortnite_escape.py

def minimum_time_to_escape(test_cases):
    results = []
    for N, H, D, S, P in test_cases:
        # Compute the minimum time directly running if possible
        straight_run_time = D / S
        health_remaining = N - straight_run_time * P
        
        if health_remaining >= 0:
            # Running straight out works
            results.append(round(straight_run_time, 5))
            continue
        
        # Otherwise, use a simulation to check running and healing alternately
        left, right = 0, 10**6  # Upper bound for binary search
        best_time = -1.0
        
        while right - left > 1e-6:
            mid = (left + right) / 2
            time_used, health, distance = 0, N, D
            
            while distance > 0 and health > 0:
                # If running straight can cover remaining distance
                run_time = distance / S
                if time_used + run_time <= mid:
                    damage_taken = run_time * P
                    if health - damage_taken >= 0:
                        time_used += run_time
                        distance = 0
                        break
                # Otherwise, try healing
                heal_time = min(mid - time_used, (P * (mid - time_used) - health) / (H - P))
                if heal_time <= 0:
                    break
                time_used += heal_time
                health += heal_time * H
                health -= heal_time * P
            
            if distance == 0 and health > 0:
                best_time = mid
                right = mid
            else:
                left = mid
        
        if best_time == -1.0:
            results.append(-1.0)
        else:
            results.append(round(best_time, 5))
    
    return results


# Input Handling
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    test_cases = [tuple(map(int, line.split())) for line in data[1:T + 1]]
    
    results = minimum_time_to_escape(test_cases)
    for result in results:
        print(result)
