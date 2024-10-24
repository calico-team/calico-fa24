#include <iostream>

using namespace std;

/**
 * Return the number of healing items the player needs to use.
 *
 * N: starting health
 * H: amount of healing
 * D: distance out of the storm in meters
 * S: running speed in meters per second
 * P: storm damage per second
 * L: length of heal in seconds
 */
int solve(int N, int H, int D, int S, int P, int L) {
    // YOUR CODE HERE
    return -1;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, H, D, S, P, L;
        cin >> N >> H >> D >> S >> P >> L;
        cout << solve(N, H, D, S, P, L) << '\n';
    }
}
