#include <iostream>

using namespace std;

/**
 * TODO
 */
int scan(int v) {
    // Simulate the scan function
    cout << "SCAN " << v << endl;
    int result;
    cin >> result;
    return result;
}

/**
 * TODO
 */
int solve() {
    // TODO return answer
    return 0;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int d = solve();
        cout << "SUBMIT " << d << endl;
    }
    return 0;
}
