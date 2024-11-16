#include <bits/stdc++.h>
using namespace std;

/**
 * Return the height H in which the danger is minimized and satisfies the budget constraints.
 *
 * B: a non-negative integer
 * N: a positive integer
 * S: an array of N integers
 */
long long solve(long long B, int N, long long S[]) {
    long long low = LLONG_MAX;
    long long high = 0;
    for (int i = 0; i < N; ++i) {
        low = min(low, S[i]);
        high = max(high, S[i]);
    }
    while (low < high) {
        long long mid = (low + high) / 2;
        long long cost = 0;
        long long danger = 0;
        for (int i = 0; i < N; i++) {
            if (S[i] < mid) {
                danger += mid - S[i];
            } else {
                cost += S[i] - mid;
            }
        }

        if (cost > B) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    return high;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        long long B;
        int N;
        cin >> B >> N;
        long long S[N];
        for (int j = 0; j < N; j++) {
            cin >> S[j];
        }
        cout << solve(B, N, S) << '\n';
    }
}
