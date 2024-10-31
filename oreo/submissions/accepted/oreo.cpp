#include <iostream>

using namespace std;

void solve(string S) {
    for (int i = 0; i < S.length(); i++) {
        if (S[i] == 'O') {
            cout << "[###OREO###]\n";
        } 
        else if (S[i] == 'R') {
            cout << " [--------]\n";
        }
        else if (S[i] == '&') {
            cout << '\n';
        }
    }
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
