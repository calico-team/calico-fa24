#include <iostream>

using namespace std;

/**
 * Return the sum of A and B.
 *
 * B: a non-negative integer
 * N: a positive integer
 * S: an array of N integers
 */
int solve(int B, int N, int S[]) {
    int low = 1000000000;
    int high = 0;
    for (int i = 0; i < N; ++i) {
        low = min(low, S[i]);
        high = max(high, S[i]);
    }
    while (low < high) {
        int mid = (low + high) / 2;
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
        int B, N;
        cin >> B >> N;
        int S[N];
        for (int j = 0; j < N; j++) {
            cin >> S[j];
        }
        cout << solve(B, N, S) << '\n';
    }
}
