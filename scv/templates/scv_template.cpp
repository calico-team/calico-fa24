#include <iostream>

using namespace std;

/**
 * Return the shape of displayed by ASCII string S of dimensions M x N
 *
 * S: a string representing an ASCII picture
 * N: integer for number of rows
 * M: integer for number of columns
 */
String solve(int N, int M, char G[M][N]) {
    // YOUR CODE HERE
    return -1;
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
