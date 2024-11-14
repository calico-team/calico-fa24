#include <iostream>
#include <vector>
#include <string>

using namespace std;

/**
 * Return the minimum number of moves to get to E, or return 
 * -1 if it is impossible.
 * 
 * N: number of rows
 * M: number of columns
 * K: the length of Madeline’s dash
 * C: a list of N strings with M characters each, describing 
 * the maze Madeline is in.
 *    In each string:
 *     . denotes a space
 *     # denotes a wall.
 *     * denotes a dash crystal.
*/
int solve(int N, int M, int K, vector<string> C) {
    // YOUR CODE HERE
    return -1;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N, M, K;
        cin >> N >> M >> K;
        vector<string> C(N);
        for (int i = 0; i < N; ++i) {
            cin >> C[i];
        }
        cout << solve(N, M, K, C) << '\n';
    }
}
