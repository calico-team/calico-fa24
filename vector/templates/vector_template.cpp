#include <iostream>
#include <vector>

using namespace std;

/**
 * TODO
 */
int solve() {
    int N;
    cin >> N;
    vector<long long> v(N);
    for (auto &x: v) {
        cin >> x;
    }

    int Q;
    cin >> Q;
    while (Q--) {
        int q_type;
        cin >> q_type;
        if (q_type == 1) {
            int l, r;
            long long x;
            cin >> l >> r >> x;
            // perform ADD queries
            // YOUR CODE HERE
        } else { // q_type = 2
            // perform FIND queries
            // YOUR CODE HERE
        }
    }
    return -1;
}

int main() {
    solve();
}
