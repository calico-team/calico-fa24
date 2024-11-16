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
double solve(double N, double H, double D, double S, double P) {
    double time_to_escape = D / S;
        double damage_taken_to_escape = P * time_to_escape;
        if (damage_taken_to_escape > N) {
            if (P >= H) {
                return -1.0;
            }
            double extra_health_needed = damage_taken_to_escape - N;
            double time_to_heal = extra_health_needed / (H - P);
            time_to_escape += time_to_heal;
        }
        return time_to_escape;
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
