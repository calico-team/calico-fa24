#include <bits/stdc++.h>
using namespace std;

#define size(x) ((int)(x.size()))

class Matroid {
	protected:
		int n;
		set<int> iset, gset, cset;
	
	public:
		Matroid(int _n) : n(_n) {
			for (int i = 0; i < n; ++i) {
				gset.insert(i);
				cset.insert(i);
			}
		}

		virtual bool independent() {
			assert(false); // Subclasses must implement this method.
		}

		virtual void insert(int e) {
			iset.insert(e);
			cset.erase(e);
		}

		virtual void erase(int e) {
			iset.erase(e);
			cset.insert(e);
		}

		virtual bool find(int e) {
			return iset.find(e) != end(iset);
		}

		virtual set<int> ground_set() {
			return gset;
		}

		virtual set<int> current_set() {
			return iset;
		}

		virtual set<int> complement_set() {
			return cset;
		}

		virtual vector<vector<int>> compute_all_circuits() {
			vector<vector<int>> answers(n);
			for (auto y : complement_set()) {
				insert(y);
				if (independent()) {
					erase(y);
					continue;
				}
				for (auto x : current_set()) {
					erase(x);
					if (independent()) {
						answers[y].push_back(x);
					}
					insert(x);
				}
				erase(y);
			}
			return answers;
		}
};

// Example matroid implementations

class UniformMatroid : public Matroid {
	private:
		int rank;
	public:
		UniformMatroid(int _n, int _rank) : Matroid(_n), rank(_rank) {}
		bool independent() {
			return size(iset) <= rank;
		}
};


// Weighted Matroid Intersection Algorithm

using U = int;
U weighted_matroid_intersection(int n, Matroid& F1, Matroid& F2, vector<U> const& c) {
	vector<bool> iset(n, false);
	vector<U> c1 = c, c2(n, 0);
	int k = 0;
	U total_weight = 0;
	U max_total_weight = 0;
	vector<U> answers;
	vector<bool> best_iset(n, false);
	vector<vector<int>> C1, C2;
	vector<pair<int, int>> A1, A2;
	vector<int> S, T;

	bool initialized = false;

	while (true) {
		if (!initialized) { // Do this at most O(E) times with O(E^2) cost
			initialized = true;
			C1 = F1.compute_all_circuits();
			C2 = F2.compute_all_circuits();
			A1.clear();
			A2.clear();
			S.clear();
			T.clear();

			for (int y = 0; y < n; ++y) if (!iset[y]) {
				for (auto x : C1[y]) {
					if (x != y) {
						A1.emplace_back(x, y);
					}
				}
				for (auto x : C2[y]) {
					if (x != y) {
						A2.emplace_back(y, x);
					}
				}
				F1.insert(y);
				if (F1.independent()) {
					S.push_back(y);
				}
				F1.erase(y);
				F2.insert(y);
				if (F2.independent()) {
					T.push_back(y);
				}
				F2.erase(y);
			}
		}

		U m1 = numeric_limits<U>::min();
		set<int> barS;

		for (auto y : S)
			m1 = max(m1, c1[y]);

		for (auto y : S)
			if (c1[y] == m1)
				barS.insert(y);
		
		U m2 = numeric_limits<U>::min();
		set<int> barT;

		for (auto y : T)
			m2 = max(m2, c2[y]);
		
		for (auto y : T)
			if (c2[y] == m2)
				barT.insert(y);
		
		vector<pair<int, int>> barA1, barA2;

		for (auto& [x, y] : A1)
			if (c1[x] == c1[y])
				barA1.emplace_back(x, y);
		
		for (auto& [y, x] : A2)
			if (c2[y] == c2[x])
				barA2.emplace_back(y, x);
		
		vector<vector<int>> G(n);
		for (auto& [x, y] : A1)
			G[x].push_back(y);
		
		for (auto& [y, x] : A2)
			G[y].push_back(x);
		
		vector<int> parents(n, -1); // An element u is in R iff parents[u] != -1
		int found = -1;
		queue<int> q;
		for (auto y : barS) {
			parents[y] = -2;
			q.push(y);
		}

		while (!q.empty()) {
			int u = q.front();
			q.pop();
			if (barT.count(u)) {
				found = u;
				break;
			}
			for (auto v : G[u]) {
				if (parents[v] == -1) {
					parents[v] = u;
					q.push(v);
				}
			}
		}

		// Augmentation or Weight Adjustment

		if (found != -1) {
			// Path augmentation
			while (found >= 0) {
				if (iset[found]) {
					// Erase found from iset
					iset[found] = false;
					F1.erase(found);
					F2.erase(found);
					total_weight -= c[found];
				} else {
					// Insert found to iset
					iset[found] = true;
					F1.insert(found);
					F2.insert(found);
					total_weight += c[found];
				}
				found = parents[found];				
			}
			answers.push_back(total_weight);
			max_total_weight = max(max_total_weight, total_weight);
			if (total_weight == max_total_weight) {
				best_iset = iset;
			}
			++k;
			initialized = false;
		} else {
			// Weight adjustment
			U eps1 = numeric_limits<U>::max(), eps2 = eps1, eps3 = eps1, eps4 = eps1;
			for (auto& [x, y] : A1) {
				if (parents[x] != -1 and parents[y] == -1) {
					eps1 = min(eps1, c1[x] - c1[y]);
				}
			}
			for (auto& [y, x] : A2) {
				if (parents[y] != -1 and parents[x] == -1) {
					eps2 = min(eps2, c2[x] - c2[y]);
				}
			}
			for (auto y : S) {
				if (parents[y] == -1) {
					eps3 = min(eps3, m1 - c1[y]);
				}
			}
			for (auto y : T) {
				if (parents[y] != -1) {
					eps4 = min(eps4, m2 - c2[y]);
				}
			}
			U eps = min({eps1, eps2, eps3, eps4});

			if (eps == numeric_limits<U>::max()) {
				break; // No more augmentation can be done
			} else {
				for (int x = 0; x < n; ++x) if (parents[x] != -1) {
					c1[x] -= eps;
					c2[x] += eps;
				}
			}
		}

	}

	return max_total_weight;

}

struct SpecialBondMatroid : public Matroid {
	int V, E;
	vector<pair<int, int>> edges;
	int source, sink;
	vector<vector<pair<int, int>>> g;

	SpecialBondMatroid(int _v, vector<pair<int, int>> _edges, int _source, int _sink) : Matroid(size(_edges)), V(_v), E(size(_edges)), edges(_edges), source(_source), sink(_sink), g(_v) {
		for (int i = 0; i < E; ++i) {
			g[edges[i].first].emplace_back(i, edges[i].second);
			g[edges[i].second].emplace_back(i, edges[i].first);
		}
	}

	bool independent() {
		vector<int> visited(V, 0);
		queue<int> q;
		q.push(source);
		visited[source] = 1;

		while (!q.empty()) {
			int u = q.front(); q.pop();
			for (auto& [i, v] : g[u]) {
				if (!iset.count(i) && v != sink && !visited[v]) {
					visited[v] = 1;
					q.push(v);
				}
			}
		}
		assert(!visited[sink]);
		return accumulate(begin(visited), end(visited), 0) == V - 1;
	}

};


/**
 * Return the minimum weight of a subset of E that fits the problem statement conditions.
 * N: Number of vertices
 * M: Number of edges
 * B: Berkeley
 * S: Stanford
 * E: Graph edges in the format [u, v, w].
 */
int solve(int N, int M, int B, int S, vector<vector<int>> E) {
	vector<pair<int, int>> edges(M);
	for (int i = 0; i < M; ++i) {
		edges[i] = make_pair(E[i][0], E[i][1]);
	}
	SpecialBondMatroid F1(N, edges, B, S), F2(N, edges, S, B);
	vector<int> weights(M);
	for (int i = 0; i < M; ++i) {
		weights[i] = E[i][2];
	}
	int total_weight = accumulate(begin(weights), end(weights), 0);
	int answer = weighted_matroid_intersection(M, F1, F2, weights);
	return total_weight - answer;
}

int main() {
	int T;
	cin >> T;
	for (int tc = 0; tc < T; ++tc) {
		int N, M, B, S;
		cin >> N >> M >> B >> S;
		vector<vector<int>> E(M, vector<int>(3));
		for (int i = 0; i < M; ++i)
			for (int j = 0; j < 3; ++j)
				cin >> E[i][j];
		cout << solve(N, M, B, S, E) << '\n';
	}
	return 0;
}


