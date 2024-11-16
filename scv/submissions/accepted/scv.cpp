#include <iostream>
#include <set>

using namespace std;

/**
 * Return the shape displayed by the picture represented by G of dimensions M x N
 *
 * G: a list of strings representing a picture
 * M: integer for number of rows
 * N: integer for number of columns
 */
string solve(int M, int N, char G[][100]) {
    set<int> row_count;
    for (int i = 0; i < M; i++) {
        int count = 0;
        for (int j = 0; j < N; j++) {
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
        int M, N;
        cin >> M >> N;
        char G[100][100];
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                cin >> G[i][j];
            }
        }
        cout << solve(M, N, G) << '\n';
    }
}
