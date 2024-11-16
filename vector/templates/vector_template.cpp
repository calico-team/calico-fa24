#include <iostream>
#include <vector>

using namespace std;

/**
 * Read N, S, Q, and queries.
 *
 * For each Find query, output a single line containing an integer denoting the sum of b
 */
int solve() {
    int N;
    cin >> N;
    vector<long long> S(N);
    for (auto &x: S) {
        cin >> x;
    }

    int Q;
    cin >> Q;
    while (Q--) {
        string q_type;
        cin >> q_type;
        if (q_type == "UPDATE") {
            int L, R;
            long long V;
            cin >> L >> R >> V;
            // perform ADD queries
            // YOUR CODE HERE
        } else { // q_type == "FIND"
            // perform FIND queries
            // YOUR CODE HERE
        }
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
}
