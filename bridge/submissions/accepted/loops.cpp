#include <iostream>

using namespace std;

/**
 * Return the sum of A and B.
 *
 * B: a non-negative integer
 * N: a positive integer
 * S: an array of N integers
 */
long long solve(long long B, int N, long long S[]) {
    int H;
    int mn = 101;
    for (int i = 0; i < N; ++i)
        mn = min(mn, (int)S[i]);
    for (H = 100; H >= mn; --H) {
        long long current_layer = 0;
        for (int i = 0; i < N; ++i)
            if (S[i] > H) current_layer++;
        if (current_layer > B) break;
        B -= current_layer;
    }
    return H + 1;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int B, N;
        cin >> B >> N;
        long long S[N];
        for (int j = 0; j < N; j++) {
            cin >> S[j];
        }
        cout << solve(B, N, S) << '\n';
    }
}
