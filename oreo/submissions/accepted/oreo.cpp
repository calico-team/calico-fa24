#include <iostream>

using namespace std;

/**
 * Print out an Oreo
 *
 * S: a string
 */
void solve(string S) {
    // YOUR CODE HERE
    for (int i = 0; i < S.length(); i++) {
        if (S[i] == 'O') {
            cout << "[###OREO###]" << endl;
        } 
        else if (S[i] == 'R') {
            cout << " [--------] " << endl;
        }
        else if (S[i] == '&') {
            cout << '\n';
        }
    }
    cout << '\n';

}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string S;
        cin >> S;
        solve(S);
    }
}
