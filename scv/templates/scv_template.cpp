#include <iostream>

using namespace std;

/**
 * Return the shape of displayed by ASCII string S of dimensions R x C
 *
 * S: a string representing an ASCII picture
 * R: integer for number of rows
 * C: integer for number of columns
 */
String solve(int R, int C, String S) {
    // YOUR CODE HERE
    return -1;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int R, C;
        String S;
        cin >> R >> C;
        cin >> S;
        cout << solve(R, C, S) << '\n';
    }
}
