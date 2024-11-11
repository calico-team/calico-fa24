#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;
typedef vector<int> vi;
typedef vector<vi> v2i;
typedef pair<int, int> pi2;
typedef vector<pi2> vp;

int islands;

struct DSU {
	vi p, r; // Parents and ranks/depths of elements

	DSU(int n) {
		for (int i = 0; i < n; i++) p.push_back(i);
		r.resize(n);
	}
	
	int get(int a) {
		return p[a] = a == p[a] ? a : get(p[a]);
	}
	void uni(int a, int b) {
		a = get(a), b = get(b);
		if (a == b) return;
		if (r[b] < r[a]) swap(a, b);
		if (r[b] == r[a]) r[b]++;
		p[a] = b;
		islands--;
	}
};

const int DIRS[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

/**
 * Return the maximum number of islands.
 *
 * N: number of rows
 * M: number of columns
 * G: grid of heights
 */
int solve(int N, int M, vector<vector<int>> &G) {
    // G' is G with borders (-1 will make the cell always submerged)
    v2i Gp(N + 2, vi(M + 2, -1));
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            Gp[i + 1][j + 1] = G[i][j];

    map<int, vp> m; // Maps each height to the set of cells at that height
    for (int i = 1; i <= N; i++)
        for (int j = 1; j <= M; j++)
            // Using negative height to help us iterate in reverse later 
            m[-Gp[i][j]].emplace_back(i, j);
    
    // DSU in reverse
    DSU dsu((N + 2) * (M + 2));
    int mx_islands = 0;
    islands = 0;
    for (pair<int, vp> p: m) {
        int h = -p.first;
        vp cells = p.second;
        islands += cells.size();
        for (pi2 cell: cells) {
            int i = cell.first, j = cell.second;
            for (auto d: DIRS) {
                int ip = i + d[0], jp = j + d[1];
                if (Gp[ip][jp] >= h)
                    dsu.uni(i * (M + 2) + j, ip * (M + 2) + jp);
            }
        }
        mx_islands = max(mx_islands, islands);
    }

    return mx_islands;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N, M;
        cin >> N >> M;
        vector<vector<int>> G(N, vector<int>(M));
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                cin >> G[i][j];
        cout << solve(N, M, G) << '\n';
    }
}
