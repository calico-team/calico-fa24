#include <iostream>
#include <algorithm>

using namespace std;

// Fast floor division function from https://stackoverflow.com/a/4110620
int floorDiv(int a, int b) {
    return (a - (a<0 ? b-1 : 0)) / b;
}

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
    int numerator = floorDiv(D, S) * P - N;
    return numerator < 0 ? 0 : floorDiv(numerator, H - P * L) + 1;
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
