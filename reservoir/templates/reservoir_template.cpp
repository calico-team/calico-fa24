#include <iostream>

using namespace std;

/**
 * Return the maximum number of islands.
 *
 * N: number of rows
 * M: number of columns
 * G: grid of heights
 */
int solve(int N, int M, vector<vector<int>> &G) {
    return 0;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N, M;
        cin >> N >> M;
        vector<vector<int>> G(N, vector<int>(M));
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                cin >> G[i][j];
        cout << solve(N, M, G) << '\n';
    }
}
