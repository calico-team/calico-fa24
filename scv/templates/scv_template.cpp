#include <iostream>

using namespace std;

/**
 * Return the shape displayed by the picture represented by G of dimensions N x M
 *
 * S: a string representing an ASCII picture
 * N: integer for number of rows
 * M: integer for number of columns
 */
string solve(int N, int M, char G[][100]) {
    // YOUR CODE HERE
    return "";
}

int main() {
    int T;
    cin >> T;
    for (int c = 0; c < T; c++) {
        int N, M;
        cin >> N >> M;
        char G[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                cin >> G[i][j];
            }
        }
        cout << solve(N, M, G) << '\n';
    }
}
