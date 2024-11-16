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
    // YOUR CODE HERE
    return -1;
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
