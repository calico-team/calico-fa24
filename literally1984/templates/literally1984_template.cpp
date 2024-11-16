#include <iostream>

using namespace std;

/**
 * Return a length 2 vector containing the coordinates x and y for the given address N.
 * 
 * N: a positive integer, the address of your house
 */
vector<int> solve(int N) {
    // YOUR CODE HERE
    
    return vector<int>({-1, -1});
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        vector<int> ans = solve(N);
        cout << ans[0] << ' ' << ans[1] << '\n';
    }
}
