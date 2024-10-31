from math import gcd

maxn = 10010

def solve(n, arr, q, queries):

    # Ensure arr has the correct length (1-indexed)
    arr = [0] + arr  # Prepend a zero to make the array 1-indexed
    ret = []
    for t in range(q):
        # Read op, l, r, x in one line (if op == 1)
        line = queries[t]
        
        op = line[0]
        
        if op == 1:
            l, r, x = line[1], line[2], line[3]
            for i in range(l, r + 1):
                arr[i] += x
                
        else:
            ans = 1e12
            for k in range(1, n):
                v1 = arr[1]
                sum1 = arr[1]
                for i in range(2, k + 1):
                    v1 = gcd(v1, arr[i])
                    sum1 += arr[i]
                    
                v2 = arr[n]
                sum2 = arr[n]
                for i in range(n - 1, k, -1):
                    v2 = gcd(v2, arr[i])
                    sum2 += arr[i]
                    
                ans = min(ans, sum1 // v1 + sum2 // v2)

            ret.append(ans)
    return ret
