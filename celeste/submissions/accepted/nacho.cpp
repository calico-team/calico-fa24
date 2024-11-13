#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define mp make_pair

using pi = pair<int, int>;

template<typename T> ostream& operator << (ostream& o, vector<T> const& v);
template<typename T1, typename T2> ostream& operator << (ostream& o, pair<T1, T2> const& p);

template<typename T> ostream& operator << (ostream& o, vector<T> const& v) {
	for (auto& x : v) o << x << ' ';
	return o;
}
template<typename T1, typename T2> ostream& operator << (ostream& o, pair<T1, T2> const& p) {
	return o << "(" << p.first << ", " << p.second << ")";
}

const int dx[4] = { 0, 1, 0, -1 };
const int dy[4] = { 1, 0, -1, 0 };
const int INF = 1000000000;

int N, M, K;

bool ok(int x, int y) {
	return x >= 0 and x < N and y >= 0 and y < M;
}

void solveCase() {
	cin >> N >> M >> K;
	vector<string> grid(N);
	for (int i = 0; i < N; ++i)
		cin >> grid[i];
	pi S, E;
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < M; ++j)
			if (grid[i][j] == 'S')
				S = mp(i, j);
			else if (grid[i][j] == 'E')
				E = mp(i, j);
	vector<vector<vector<int>>> dist(N, vector<vector<int>>(M, vector<int>(2, -1)));

	// Precalculate this to use BinarySearch
	vector<vector<int>> rowsLeft(N), rowsRight(N), columnsDown(M), columnsUp(M);
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			if (grid[i][j] == '#')
				rowsLeft[i].push_back(j);
		}
		rowsRight[i] = rowsLeft[i];
		reverse(begin(rowsRight[i]), end(rowsRight[i]));
	}

	for (int j = 0; j < M; ++j) {
		for (int i = 0; i < N; ++i) {
			if (grid[i][j] == '#')
				columnsDown[j].push_back(i);
		}
		columnsUp[j] = columnsDown[j];
		reverse(begin(columnsUp[j]), end(columnsUp[j]));
	}

	vector<vector<int>> prefixRows(N, vector<int>(M, 0)), prefixColumns(M, vector<int>(N, 0));
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			if (j) prefixRows[i][j] = prefixRows[i][j - 1];
			if (i) prefixColumns[j][i] = prefixColumns[j][i - 1];
			if (grid[i][j] == '*') {
				++prefixRows[i][j];
				++prefixColumns[j][i];
			}
		}
	}

	// cout << "rowsRight = " << rowsRight << endl;
	// cout << "rowsLeft = " << rowsLeft << endl;
	// cout << "columnsDown = " << columnsDown << endl;
	// cout << "columnsUp = " << columnsUp << endl;

	queue<pair<pi, int>> q;
	q.push(mp(S, 1));
	dist[S.f][S.s][1] = 0;

	while (!q.empty()) {
		auto p = q.front(); q.pop();
		int x = p.f.f, y = p.f.s, z = p.s;
		// cout << "x = " << x << " y = " << y << " z = " << z << endl;
		// We try to move 1 block
		for (int k = 0; k < 4; ++k) {
			int xx = x + dx[k], yy = y + dy[k];
			if (ok(xx, yy) and grid[xx][yy] != '#') { // In bounds and not a wall
				int zz = z | (grid[xx][yy] == '*'); // Either we had red hair or we walk into a crystal
				if (dist[xx][yy][zz] == -1) {
					dist[xx][yy][zz] = dist[x][y][z] + 1;
					q.push(mp(mp(xx, yy), zz));
				}
			}
		}
		if (!z)
			continue; // We can't dash
		// Now we try to dash
		// Dash to the left?
		
		int y_left = *upper_bound(begin(rowsRight[x]), end(rowsRight[x]), y, greater<int>()) + 1; // Guaranteed to be inside
		if (y_left < y - K)
			y_left = y - K;
		int z_left = prefixRows[x][y - 1] != prefixRows[x][y_left - 1];
		if (dist[x][y_left][z_left] == -1) {
			dist[x][y_left][z_left] = dist[x][y][z] + 1;
			q.push(mp(mp(x, y_left), z_left));
		}

		// Dash to the right?
		int y_right = *upper_bound(begin(rowsLeft[x]), end(rowsLeft[x]), y) - 1; // Guaranteed to be inside
		if (y_right > y + K)
			y_right = y + K;
		int z_right = prefixRows[x][y_right] != prefixRows[x][y];
		if (dist[x][y_right][z_right] == -1)  {
			dist[x][y_right][z_right] = dist[x][y][z] + 1;
			q.push(mp(mp(x, y_right), z_right));
		}

		// Dash down?
		int x_down = *upper_bound(begin(columnsDown[y]), end(columnsDown[y]), x) - 1;
		if (x_down > x + K)
			x_down = x + K;
		int z_down = prefixColumns[y][x_down] != prefixColumns[y][x];
		if (dist[x_down][y][z_down] == -1) {
			dist[x_down][y][z_down] = dist[x][y][z] + 1;
			q.push(mp(mp(x_down, y), z_down));
		}

		// Dash up?
		int x_up = *upper_bound(begin(columnsUp[y]), end(columnsUp[y]), x, greater<int>()) + 1;
		if (x_up < x - K)
			x_up = x - K;
		int z_up = prefixColumns[y][x_up - 1] != prefixColumns[y][x - 1];
		if (dist[x_up][y][z_up] == -1) {
			dist[x_up][y][z_up] = dist[x][y][z] + 1;
			q.push(mp(mp(x_up, y), z_up));
		}
	}
	
	int answer1 = dist[E.f][E.s][0], answer2 = dist[E.f][E.s][1];
	if (answer1 == -1)
		cout << answer2 << '\n';
	else if (answer2 == -1)
		cout << answer1 << '\n';
	else
		cout << min(answer1, answer2) << '\n';

}


int main() {
	cin.tie(0)->sync_with_stdio(0);
	int tc;
	cin >> tc;
	while (tc--)
		solveCase();
	return 0;
}
