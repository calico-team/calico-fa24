#include <iostream>

using namespace std;

/**
 * Return the sum of A and B.
 *
 * A: a non-negative integer
 * B: another non-negative integer
 */
int solve(int B, int N, int[] S) {
    // YOUR CODE HERE
    return -1;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int B, N;
        cin >> B >> N;
        int[] S = new int[N];
        for (int j = 0; j < N; j++) {
            cin >> S[j];
        }
        cout << solve(B, N, S) << '\n';
    }
}
