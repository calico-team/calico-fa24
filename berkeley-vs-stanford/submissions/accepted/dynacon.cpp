#include <bits/stdc++.h>
using namespace std;

/**
 * Dynamic Connectivity in O(lg^2n) using Euler Tour Trees
 * Source: https://github.com/yosupo06/library-checker-problems/blob/master/graph/dynamic_graph_vertex_add_component_sum/sol/correct.cpp
 */
template<typename T>
class dynamic_connectivity{
	class euler_tour_tree{
		public:
		struct node;
		using np=node*;
		using lint=long long;
		struct node{
			np ch[2]={nullptr,nullptr};
			np p=nullptr;
			int l,r,sz,sz2;
			T val=et,sum=et;
			bool exact=1;
			bool child_exact;
			bool edge_connected=0;
			node(){}
			node(int l,int r):l(l),r(r),sz(l==r),sz2(0),child_exact(l<r){}
			bool is_root() {
				return !p;
			}
		};
		vector<unordered_map<int,np>>ptr;
		np get_node(int l,int r){
			if(ptr[l].find(r)==ptr[l].end())ptr[l][r]=new node(l,r);
			return ptr[l][r];
		}
		np root(np t){
			if(!t)return t;
			while(t->p)t=t->p;
			return t;
		}
		bool same(np s,np t){
			if(s)splay(s);
			if(t)splay(t);
			return root(s)==root(t);
		}
		np reroot(np t){
			auto s=split(t);
			return merge(s.second,s.first);
		}
		pair<np,np> split(np s){
			splay(s);
			np t=s->ch[0];
			if(t)t->p=nullptr;
			s->ch[0]=nullptr;
			return {t,update(s)};
		}
		pair<np,np> split2(np s){
			splay(s);
			np t=s->ch[0];
			np u=s->ch[1];
			if(t)t->p=nullptr;
			s->ch[0]=nullptr;
			if(u)u->p=nullptr;
			s->ch[1]=nullptr;
			return {t,u};
		}
		tuple<np,np,np> split(np s,np t){
			auto u=split2(s);
			if(same(u.first,t)){
				auto r=split2(t);
				return make_tuple(r.first,r.second,u.second);
			}else{
				auto r=split2(t);
				return make_tuple(u.first,r.first,r.second);
			}
		}
		template<typename First, typename... Rest>
		np merge(First s,Rest... t){
			return merge(s,merge(t...));
		}
		np merge(np s,np t){
			if(!s)return t;
			if(!t)return s;
			while(s->ch[1])s=s->ch[1];
			splay(s);
			s->ch[1]=t;
			if(t)t->p=s;
			return update(s);
		}
		int size(np t){return t?t->sz:0;}
		int size2(np t){return t?t->sz2:0;}
		np update(np t){
			t->sum=et;
			if(t->ch[0])t->sum=fn(t->sum,t->ch[0]->sum);
			if(t->l==t->r)t->sum=fn(t->sum,t->val);
			if(t->ch[1])t->sum=fn(t->sum,t->ch[1]->sum);
			t->sz=size(t->ch[0])+(t->l==t->r)+size(t->ch[1]);
			t->sz2=size2(t->ch[0])+(t->edge_connected)+size2(t->ch[1]);
			t->child_exact=(t->ch[0]?t->ch[0]->child_exact:0)|(t->l<t->r&&t->exact)|(t->ch[1]?t->ch[1]->child_exact:0);
			return t;
		}
		// void push(np t){
		// 	//遅延評価予定
		// }
		void rot(np t,bool b){
			np x=t->p,y=x->p;
			if((x->ch[1-b]=t->ch[b]))t->ch[b]->p=x;
			t->ch[b]=x,x->p=t;
			update(x);update(t);
			if((t->p=y)){
				if(y->ch[0]==x)y->ch[0]=t;
				if(y->ch[1]==x)y->ch[1]=t;
				update(y);
			}
		}
		void splay(np t){
			//push(t);
			while(!t->is_root()){
				np q=t->p;
				if(q->is_root()){
					//push(q), push(t);
					rot(t,q->ch[0]==t);
				}else{
					np r=q->p;
					//push(r), push(q), push(t);
					bool b=r->ch[0]==q;
					if(q->ch[1-b]==t)rot(q,b),rot(t,b);
					else rot(t,1-b),rot(t,b);
				}
			}
		}
		void debug(np t){
			if(!t)return;
			debug(t->ch[0]);
			cerr<<t->l<<"-"<<t->r<<" ";
			debug(t->ch[1]);
		}
		constexpr static T et=T();
		constexpr static T fn(T s,T t){
			return s+t;
		}
		public:
		euler_tour_tree(){}
		euler_tour_tree(int sz){
			ptr.resize(sz);
			for(int i=0;i<sz;i++)ptr[i][i]=new node(i,i);
		}
		int size(int s){
			np t=get_node(s,s);
			splay(t);
			return t->sz;
		}
		bool same(int s,int t){
			return same(get_node(s,s),get_node(t,t));
		}
		void set_size(int sz){
			ptr.resize(sz);
			for(int i=0;i<sz;i++)ptr[i][i]=new node(i,i);
		}
		void update(int s,T x){
			np t=get_node(s,s);
			splay(t);
			t->val=fn(t->val,x);
			update(t);
		}
		void edge_update(int s,function<void(int,int)> g){
			np t=get_node(s,s);
			splay(t);
			function<void(np)>dfs=[&](np t){
				assert(t);
				if(t->l<t->r&&t->exact){
					splay(t);
					t->exact=0;
					update(t);
					g(t->l,t->r);
					return;
				}
				if(t->ch[0]&&t->ch[0]->child_exact)dfs(t->ch[0]);
				else dfs(t->ch[1]);
			};
			while(t&&t->child_exact){
				dfs(t);
				splay(t);
			}
		}
		bool try_reconnect(int s,function<bool(int)> f){
			np t=get_node(s,s);
			splay(t);
			function<bool(np,int)>dfs=[&](np t,int idx)->bool{
				assert(t);
				if(t->edge_connected&&(size2(t->ch[0])==idx)){
					splay(t);
					return f(t->l);
				}
				if(idx<size2(t->ch[0]))return dfs(t->ch[0],idx);
				else return dfs(t->ch[1],idx-size2(t->ch[0])-(t->edge_connected));
			};
			while(size2(t)){
				if(dfs(t,0))return 1;
				splay(t);
			}
			return 0;
		}
		void edge_connected_update(int s,bool b){
			np t=get_node(s,s);
			splay(t);
			t->edge_connected=b;
			update(t);
		}
		bool link(int l,int r){
			if(same(l,r))return 0;
			merge(reroot(get_node(l,l)),get_node(l,r),reroot(get_node(r,r)),get_node(r,l));
			return 1;
		}
		bool cut(int l,int r){
			if(ptr[l].find(r)==ptr[l].end())return 0;
			np s,t,u;
			tie(s,t,u)=split(get_node(l,r),get_node(r,l));
			merge(s,u);
			np p=ptr[l][r];
			np q=ptr[r][l];
			ptr[l].erase(r);
			ptr[r].erase(l);
			delete p;delete q;
			return 1;
		}
		T get_sum(int p,int v){
			cut(p,v);
			np t=get_node(v,v);
			splay(t);
			T res=t->sum;
			link(p,v);
			return res;
		}
		T get_sum(int s){
			np t=get_node(s,s);
			splay(t);
			return t->sum;
		}
	};
	int dep=1;
	vector<euler_tour_tree> ett;
	vector<vector<unordered_set<int>>>edges;
	int sz;
	public:
	dynamic_connectivity(int sz):sz(sz){
		ett.emplace_back(sz);
		edges.emplace_back(sz);
	}
	bool link(int s,int t){
		if(s==t)return 0;
		if(ett[0].link(s,t))return 1;
		edges[0][s].insert(t);
		edges[0][t].insert(s);
		if(edges[0][s].size()==1)ett[0].edge_connected_update(s,1);
		if(edges[0][t].size()==1)ett[0].edge_connected_update(t,1);
		return 0;
	}
	bool same(int s,int t){
		return ett[0].same(s,t);
	}
	int size(int s){
		return ett[0].size(s);
	}
	vector<int>get_vertex(int s){
		return ett[0].vertex_list(s);
	}
	void update(int s,T x){
		ett[0].update(s,x);
	}
	T get_sum(int s){
		return ett[0].get_sum(s);
	}
	bool cut(int s,int t){
		if(s==t)return 0;
		for(int i=0;i<dep;i++){
			edges[i][s].erase(t);
			edges[i][t].erase(s);
			if(edges[i][s].size()==0)ett[i].edge_connected_update(s,0);
			if(edges[i][t].size()==0)ett[i].edge_connected_update(t,0);
		}
		for(int i=dep-1;i>=0;i--){
			if(ett[i].cut(s,t)){
				if(dep-1==i){
					dep++;
					ett.emplace_back(sz);
					edges.emplace_back(sz);
				}
				return !try_reconnect(s,t,i);
			}
		}
		return 0;
	}
	bool try_reconnect(int s,int t,int k){
		for(int i=0;i<k;i++){
			ett[i].cut(s,t);
		}
		for(int i=k;i>=0;i--){
			if(ett[i].size(s)>ett[i].size(t))swap(s,t);
			function<void(int,int)> g=[&](int s,int t){ett[i+1].link(s,t);};
			ett[i].edge_update(s,g);
			function<bool(int)> f=[&](int x)->bool{
				for(auto itr=edges[i][x].begin();itr!=edges[i][x].end();){
					auto y=*itr;
					itr=edges[i][x].erase(itr);
					edges[i][y].erase(x);
					if(edges[i][x].size()==0)ett[i].edge_connected_update(x,0);
					if(edges[i][y].size()==0)ett[i].edge_connected_update(y,0);
					if(ett[i].same(x,y)){
						edges[i+1][x].insert(y);
						edges[i+1][y].insert(x);
						if(edges[i+1][x].size()==1)ett[i+1].edge_connected_update(x,1);
						if(edges[i+1][y].size()==1)ett[i+1].edge_connected_update(y,1);
					}else{
						for(int j=0;j<=i;j++){
							ett[j].link(x,y);
						}
						return 1;
					}
				}
				return 0;
			};
			if(ett[i].try_reconnect(s,f))return 1;
		}
		return 0;
	}
};


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
		for (auto& [x, y] : barA1)
			G[x].push_back(y);
		
		for (auto& [y, x] : barA2)
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
	dynamic_connectivity<int> g;

	SpecialBondMatroid(int _v, vector<pair<int, int>> _edges, int _source, int _sink) : Matroid(size(_edges)), V(_v), E(size(_edges)), edges(_edges), source(_source), sink(_sink), g(_v) {
		for (int i = 0; i < E; ++i) {
			if (edges[i].first != sink && edges[i].second != sink) {
                g.link(edges[i].first, edges[i].second);
            }
		}
        for (int i = 0; i < V; ++i)
            g.update(i, 1);
	}

    void insert(int e) {
        // Adding edge to current set is equivalent to taking it away from the graph
        Matroid::insert(e);
        if (edges[e].first != sink && edges[e].second != sink) {
            g.cut(edges[e].first, edges[e].second);
        }
    }

    void erase(int e) {
        if (!iset.count(e)) return;
        // Erasing edge from current set is equivalent to adding it to the graph
        Matroid::erase(e);
        if (edges[e].first != sink and edges[e].second != sink) {
            g.link(edges[e].first, edges[e].second);
        }
    }

	bool independent() {
		return g.size(source) == V - 1;
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
