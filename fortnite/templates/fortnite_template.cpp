#include <iostream>

using namespace std;

/**
 * Return the sum of A and B.
 *
 * N: starting health
 * H: amount of healing
 * D: distance out of the storm in meters
 * S: running speed in meters per second
 * P: storm damage per second
 * T: time to heal
 */
int solve(int N, int H, int D, int S, int P, int T) {
    // YOUR CODE HERE
    return -1;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, H, D, S, P, T;
        cin >> N >> H >> D >> S >> P >> T;
        cout << solve(N, H, D, S, P, T) << '\n';
    }
}
