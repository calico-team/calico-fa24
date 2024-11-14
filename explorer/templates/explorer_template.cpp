#include <iostream>

using namespace std;

int scan(int);
string submit(int);

/**
 * Perform scan queries and a submit query to find the length of the shortest
 * path from the vertex labeled 1 to the vertex labeled 1000 in the graph.
 */
void solve() {
    // YOUR CODE HERE
}

/**
 * Scan at the vertex labeled v. Returns the label of a random vertex that v is
 * connected to.
 */
int scan(int v) {
    cout << "SCAN " << v << endl;
    string response;
    cin >> response;
    if (response == "WRONG_ANSWER") {
        exit(0);
    }
    return stoi(response);
}

/**
 * Submit your guess for the length of the shortest path. Returns CORRECT if
 * your guess is correct and WRONG_ANSWER if your guess is wrong.
 */
string submit(int d) {
    cout << "SUBMIT " << d << endl;
    string response;
    cin >> response;
    if (response == "WRONG_ANSWER") {
        exit(0);
    }
    return response;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        solve();
    }
    return 0;
}
