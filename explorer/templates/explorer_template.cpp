#include <iostream>

using namespace std;

int scan(int);
string submit(int);

/**
 * Perform scan queries to find the length of the shortest path from the vertex
 * labeled 1 to the vertex labeled 500 in the graph. Return the length to
 * perform the submit query to submit your answer.
 */
int solve() {
    // YOUR CODE HERE
    return 0;
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

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cout << "SUBMIT " << solve() << endl;
        string response;
        cin >> response;
        if (response == "WRONG_ANSWER") {
            exit(0);
        }
    }
    return 0;
}
