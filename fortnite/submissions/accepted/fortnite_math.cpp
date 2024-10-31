#include <iostream>
#include <algorithm>

using namespace std;

// Fast floor division function from https://stackoverflow.com/a/4110620
long long floorDiv(long long a, long long b) {
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
long long solve(long long N, long long H, long long D, long long S, long long P, long long L) {
    return max(floorDiv(floorDiv(D, S) * P - N, H - P * L) + 1, 0LL);
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        long long N, H, D, S, P, L;
        cin >> N >> H >> D >> S >> P >> L;
        cout << solve(N, H, D, S, P, L) << '\n';
    }
}
