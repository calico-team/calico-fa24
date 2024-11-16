#include <iostream>
#include <set>

using namespace std;

/**
 * Return the shape displayed by the picture represented by G of dimensions N x M
 *
 * G: a list of strings representing a picture
 * N: integer for number of rows
 * M: integer for number of columns
 */
string solve(int N, int M, char G[][100]) {
    set<int> row_count;
    for (int i = 0; i < N; i++) {
        int count = 0;
        for (int j = 0; j < M; j++) {
            if (G[i][j] == '#') {
                count++;
            }
        }
        if (count != 0) {
            row_count.insert(count);
        }
    }
    if (row_count.size() <= 1) {
        return "ferb";
    }
    return "phineas";
}

int main() {
    int T;
    cin >> T;
    for (int c = 0; c < T; c++) {
        int N, M;
        cin >> N >> M;
        char G[100][100];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                cin >> G[i][j];
            }
        }
        cout << solve(N, M, G) << '\n';
    }
}
