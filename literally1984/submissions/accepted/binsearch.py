# Preprocessing
MAX_M = 60427 # Precalculated value such that totient_sum[MAX_M - 1] > 1E9

euler_sieve = [i for i in range(MAX_M)] # Euler sieve
primes = [[] for i in range(MAX_M)] # Prime factors
for i in range(2, MAX_M):
    if euler_sieve[i] == i:
        for j in range(i, MAX_M, i):
            euler_sieve[j] = euler_sieve[j] * (i - 1) // i
            primes[j].append(i)
totient_sum = [0 for _ in range(MAX_M)] # Start from 2 in this problem since we dont have 0/1
for i in range(2, MAX_M):
    totient_sum[i] = totient_sum[i-1] + euler_sieve[i]


def num_coprimes(m, M):
    coprime = m
    for i in range(1, 1 << len(primes[M])): # dont take away 1 nor the whole number i think
            bits, num = 0, 1
            for j in range(len(primes[M])):
                if i & (1 << j) != 0:
                    bits += 1
                    num *= primes[M][j]
            coprime += m // num * (1 if bits % 2 == 0 else -1)
    return coprime


def solve(N: int) -> list[int]:
    """
    Return a tuple containing the coordinates X and Y.

    N: a positive integer, the address of your house
    """
    # First we find the M-th diagonal i.e. the least M such that totient_sum[M] >= N
    l, r, M = 0, MAX_M - 1, MAX_M - 1
    while l <= r:
        m = (l + r) // 2
        if totient_sum[m] >= N:
            M = m
            r = m - 1
        else:
            l = m + 1
    i = N - totient_sum[M - 1]
    # Now we want to find the i-th number in the M-th diagonal

    l, r, ans = 1, M, 1
    while l <= r:
        m = (l + r) // 2
        # Check how many numbers coprime with M are in [1..m]
        coprime = num_coprimes(m, M)
        if coprime >= i:
            ans = m
            r = m - 1
        else:
            l = m + 1
                    
    return [ans, M - ans]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(*solve(N))


if __name__ == "__main__":
    main()
