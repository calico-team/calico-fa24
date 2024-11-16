def solve(n, arr, q, queries):
    from math import gcd

    # Initialize arrays
    diff = [0] * (n + 1)
    pre = [0] * (n + 1)
    suf = [0] * (n + 2)  # Extra for boundary handling
    ps = [0] * (n + 1)
    ss = [0] * (n + 2)  # Extra for boundary handling

    # Compute initial differences
    for i in range(1, n + 1):
        diff[i] = arr[i - 1] - (arr[i - 2] if i > 1 else 0)

    results = []
    for query in queries:
        op = query[0]
        if op == 1:
            l, r, x = query[1], query[2], query[3]
            diff[l] += x
            if r + 1 <= n:
                diff[r + 1] -= x
        else:
            for i in range(1, n + 1):
                arr[i - 1] = (arr[i - 2] if i > 1 else 0) + diff[i]
                pre[i] = gcd(pre[i - 1], arr[i - 1])
                ps[i] = ps[i - 1] + arr[i - 1]

            for i in range(n, 0, -1):
                suf[i] = gcd(suf[i + 1], arr[i - 1])
                ss[i] = ss[i + 1] + arr[i - 1]

            ans = float('inf')
            for i in range(1, n):
                if pre[i] > 0 and suf[i + 1] > 0:  # To avoid division by zero
                    ans = min(ans, ps[i] // pre[i] + ss[i + 1] // suf[i + 1])

            results.append(ans)

    return results
