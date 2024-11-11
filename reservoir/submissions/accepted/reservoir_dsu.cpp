#include <bits/stdc++.h>

using namespace std;
typedef vector<int> vi;

/**
 * Return the height H Evbo should choose.
 *
 * N: number of rows
 * M: number of columns
 * G: grid of heights
 */
int solve(int N, int M, vector<vector<int>> &G) {
    set<int> heights;
    for (vi v: G) for (int x: v) heights.push_back(x);
    sort(heights.begin(), heights.end());



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
