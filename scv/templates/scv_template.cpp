#include <iostream>

using namespace std;

/**
 * Return the shape of displayed by ASCII string S of dimensions M x N
 *
 * S: a string representing an ASCII picture
 * M: integer for number of rows
 * N: integer for number of columns
 */
String solve(int M, int N, char G[100][100]) {
    // YOUR CODE HERE
    return -1;
}

int main() {
    int T;
    cin >> T;
    for (int c = 0; c < T; c++) {
        int M, N;
        char G[100][100]
        cin >> M >> N;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                cin >> G[i][j];
            }
        }
        cout << solve(M, N, G) << '\n';
    }
}
