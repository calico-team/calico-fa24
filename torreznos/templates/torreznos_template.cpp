#include <iostream>
#include <vector>
using namespace std;

/**
 * Return the minimum weight of a subset of E that fits the problem statement conditions.
 * N: Number of vertices
 * M: Number of edges
 * F: France
 * S: Spain
 * E: Graph edges in the format [u, v, w].
 */
int solve(int N, int M, int F, int S, vector<vector<int>> E) {
	// TODO: Write your code here.
	return 0;
}

int main() {
	int T;
	cin >> T;
	for (int tc = 0; tc < T; ++tc) {
		int N, M, F, S;
		cin >> N >> M >> F >> S;
		vector<vector<int>> E(M, vector<int>(3));
		for (int i = 0; i < M; ++i)
			for (int j = 0; j < 3; ++j)
				cin >> E[i][j];
		cout << solve(N, M, F, S, E);
	}
	return 0;
}
