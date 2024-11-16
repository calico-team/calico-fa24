#include <bits/stdc++.h>
#include <tuple>
using namespace std;
using ll = long long;
using vll = vector<ll>;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using vvl = vector<vector<ll>>;
using pii = pair<int, int>;

struct state {
	int i;
	int j;
	bool dash = true;
	ll dist = 0;

	auto tuple() {
		return make_tuple(i, j, dash, dist);
	}
};

const ll INF = 1e18+100;

int solve(int N, int M, int K, vector<string> C) {
	vector<int> dxs = {1, -1, 0, 0};
	vector<int> dys = {0, 0, 1, -1};
	state s;
	state e;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (C[i][j] == 'S') s = state{i, j};
			if (C[i][j] == 'E') e = state{i, j};
		}
	}

	queue<state> q;
	vector<vvl> dist(N, vvl(M, vll(2, INF)));

	q.push(s);
	while (!q.empty()) {
		int i, j, d;
		bool dash;
		tie(i, j, dash, d) = q.front().tuple();
		q.pop();
		// We already processed this state
		if (C[i][j] == '#' || dist[i][j][dash] != INF) {
			continue;
		}
		dist[i][j][dash] = d;
		for (int id = 0; id < 4; id++) {
			int dx = dxs[id];
			int dy = dys[id];
			bool newDash = dash;
			if (C[i][j] == '*') newDash = true;
			q.push({ i+dx, j+dy, newDash, d+1 });
			if (!newDash) continue;

			// Dash move
			int curx = i;
			int cury = j;
			newDash = false;
			for (int rep = 0; rep < K; rep++) {
				if (rep > 0 && C[curx][cury] == '*') newDash = true;
				if (C[curx+dx][cury+dy] == '#') break;
				curx += dx;
				cury += dy;
			}
			if (C[curx][cury] == '*') newDash = true;
			// cout << i << ' ' << j << ' ' << curx << ' ' << cury << ' ' << newDash << '\n';
			q.push({curx, cury, newDash, d+1});
		}
	}
    ll ans = min(dist[e.i][e.j][0], dist[e.i][e.j][1]);
	return ans == INF ? -1: ans;
}

/*
alias csafe='g++ -std=c++17 -Wshadow -Wall -DLOCAL -fsanitize=address -fsanitize=undefined -D_GLIBCXX_DEBUG -g'
*/

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N, M, K;
        cin >> N >> M >> K;
        vector<string> C(N);
        for (int i = 0; i < N; ++i) {
            cin >> C[i];
        }
        cout << solve(N, M, K, C) << '\n';
    }
}
