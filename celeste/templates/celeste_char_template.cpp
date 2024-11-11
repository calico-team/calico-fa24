#include <iostream>

using namespace std;

/**
 * Return the minimum number of moves to get to E, or print 
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
int solve(int N, int M, int K, char mat[N][M]) {
    // YOUR CODE HERE
    return -1;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N, M, K;
        cin >> N >> M >> K;
        char mat[N][M];
        for (int i = 0 ; i < N ; ++i) {
            string s;
            cin >> s;
            for (int j = 0 ; j < M ; ++j) {
                mat[i][j] = s[j];
            }
        }
    
        cout << solve(N, M, K, mat) << '\n';
    }
}
