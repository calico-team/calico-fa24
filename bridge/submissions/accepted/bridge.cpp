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
    int low = 0;
    int high = 1000000000;
    while (low < high) {
        int mid = (low + high) / 2;
        int cost = 0;
        int danger = 0;
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
