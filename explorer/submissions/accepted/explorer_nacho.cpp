#include <bits/stdc++.h>
using namespace std;

mt19937 rng(20241116);

int main() {
	int tc; cin >> tc;
	while (tc--) {
		vector<set<int>> g(501);
		vector<vector<int>> d(501, vector<int>(2, -1));
		d[1][0] = d[500][1] = 0;
		queue<pair<int, int>> q;
		pair<int, int> source = {1,0}, sink = {500,1};
		if (rng() % 2) swap(source, sink);
		q.push(source);
		q.push(sink);
		int ans = -1;

		while (ans == -1) {
			int u = q.front().first;
			int s = q.front().second;
			q.pop();

			while (size(g[u]) != 3) {
				int v;
				cout << "SCAN " << u << endl;
				cin >> v;
				g[u].insert(v);
				g[v].insert(u);
			}
			for (int v : g[u]) {
				if (d[v][s] != -1)
					continue;
				else if (d[v][1-s] != -1) {
					ans = d[u][s] + d[v][1-s] + 1;
					break;
				}
				else {
					d[v][s] = d[u][s] + 1;
					q.emplace(v, s);
				}
			}
		}
		cout << "SUBMIT " << ans << endl;
		string xd;
		cin >> xd;
	}
	return 0;
}
				
