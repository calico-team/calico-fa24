#include <iostream>

using namespace std;

/**
 * Return the minimum time needed for you to exit the storm.
 * 
 * N: starting health
 * H: healing per second
 * D: distance out of the storm in meters
 * S: running speed in meters per second
 * P: storm damage per second
 */
long long solve(long long N, long long H, long long D, long long S, long long P) {
    // YOUR CODE HERE
    return -1;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, H, D, S, P;
        cin >> N >> H >> D >> S >> P;
        cout << solve(N, H, D, S, P) << '\n';
    }
}
