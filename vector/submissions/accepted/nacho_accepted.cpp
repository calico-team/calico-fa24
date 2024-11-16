#include <bits/stdc++.h>
using namespace std;
 
using ll = long long;
using db = long double; // or double, if TL is tight
using str = string; // yay python! //

// pairs
using pi = pair<int,int>;
using pl = pair<ll,ll>;
using pd = pair<db,db>;
#define mp make_pair
#define f first
#define s second

#define tcT template<class T
#define tcTU tcT, class U
// ^ lol this makes everything look weird but I'll try it
tcT> using V = vector<T>; 
tcT, size_t SZ> using AR = array<T,SZ>; 
using vi = V<int>;
using vb = V<bool>;
using vl = V<ll>;
using vd = V<db>;
using vs = V<str>;
using vpi = V<pi>;
using vpl = V<pl>;
using vpd = V<pd>;

// vectors
// oops size(x), rbegin(x), rend(x) need C++17
#define sz(x) int((x).size())
#define bg(x) begin(x)
#define all(x) bg(x), end(x)
#define rall(x) x.rbegin(), x.rend() 
#define sor(x) sort(all(x)) 
#define rsz resize
#define ins insert 
#define pb push_back
#define eb emplace_back
#define ft front()
#define bk back()

#define lb lower_bound
#define ub upper_bound
tcT> int lwb(V<T>& a, const T& b) { return int(lb(all(a),b)-bg(a)); }
tcT> int upb(V<T>& a, const T& b) { return int(ub(all(a),b)-bg(a)); }

// loops
#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define F0R(i,a) FOR(i,0,a)
#define ROF(i,a,b) for (int i = (b)-1; i >= (a); --i)
#define R0F(i,a) ROF(i,0,a)
#define rep(a) F0R(_,a)
#define each(a,x) for (auto& a: x)

const int MOD = (int)1e9+7; // 998244353;
const int INF = (int)1e9;
const int MX = (int)2e5+5;
const ll BIG = 1e18; // not too close to LLONG_MAX
const db PI = acos((db)-1);
const int dx[4]{1,0,-1,0}, dy[4]{0,1,0,-1}; // for every grid problem!!
mt19937 rng((uint32_t)chrono::steady_clock::now().time_since_epoch().count()); 
template<class T> using pqg = priority_queue<T,vector<T>,greater<T>>;

// bitwise ops
// also see https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html
constexpr int pct(int x) { return __builtin_popcount(x); } // # of bits set
constexpr int bits(int x) { // assert(x >= 0); // make C++11 compatible until USACO updates ...
	return x == 0 ? 0 : 31-__builtin_clz(x); } // floor(log2(x)) 
constexpr int p2(int x) { return 1<<x; }
constexpr int msk2(int x) { return p2(x)-1; }

ll cdiv(ll a, ll b) { return a/b+((a^b)>0&&a%b); } // divide a by b rounded up
ll fdiv(ll a, ll b) { return a/b-((a^b)<0&&a%b); } // divide a by b rounded down

tcT> bool ckmin(T& a, const T& b) {
	return b < a ? a = b, 1 : 0; } // set a = min(a,b)
tcT> bool ckmax(T& a, const T& b) {
	return a < b ? a = b, 1 : 0; } // set a = max(a,b)

tcTU> T fstTrue(T lo, T hi, U f) {
	++hi; assert(lo <= hi); // assuming f is increasing
	while (lo < hi) { // find first index such that f is true 
		T mid = lo+(hi-lo)/2;
		f(mid) ? hi = mid : lo = mid+1; 
	} 
	return lo;
}
tcTU> T lstTrue(T lo, T hi, U f) {
	--lo; assert(lo <= hi); // assuming f is decreasing
	while (lo < hi) { // find first index such that f is true 
		T mid = lo+(hi-lo+1)/2;
		f(mid) ? lo = mid : hi = mid-1;
	} 
	return lo;
}
tcT> void remDup(vector<T>& v) { // sort and remove duplicates
	sort(all(v)); v.erase(unique(all(v)),end(v)); }
tcTU> void erase(T& t, const U& u) { // don't erase
	auto it = t.find(u); assert(it != end(t));
	t.erase(it); } // element that doesn't exist from (multi)set


tcTU> inline ostream& operator << (ostream& o, pair<T, U> const& p);
tcT> inline ostream& operator << (ostream& o, V<T> const& v);

tcTU> inline ostream& operator << (ostream& o, pair<T, U> const& p) {
	return o << '(' << p.f << ", " << p.s << ')';
}

tcT> inline ostream& operator << (ostream& o, V<T> const& v) {
	F0R(i, sz(v) - 1) o << v[i] << ' ';
	if (sz(v)) o << v.back();
	return o;
}

const int MAX_N = 100010;

int n, q;
ll sum[MAX_N * 4], add[MAX_N * 4], diff[MAX_N * 4];

void push_down(int t, int l, int r) {
    int lc = t << 1, rc = t << 1 | 1, mid = (l + r) >> 1;
    add[lc] += add[t];
    add[rc] += add[t];
    sum[lc] += add[t] * (mid - l + 1);
    sum[rc] += add[t] * (r - mid);
    add[t] = 0;
}

void sum_update(int ql, int qr, int v, int t = 1, int l = 1, int r = n) {
    if (l > qr || r < ql) return;
    if (ql <= l && r <= qr) {
        add[t] += v;
        sum[t] += (ll)(r - l + 1) * v;
        return;
    }
    push_down(t, l, r);
    int lc = t << 1, rc = t << 1 | 1, mid = (l + r) >> 1;
    sum_update(ql, qr, v, lc, l, mid);
    sum_update(ql, qr, v, rc, mid + 1, r);
    sum[t] = sum[lc] + sum[rc];
}

void diff_update(int p, int v, int t = 1, int l = 1, int r = n) {
    if (l > p || r < p) return;
    if (l == p && r == p) {
        diff[t] += v;
        return;
    }
    int lc = t << 1, rc = t << 1 | 1, mid = (l + r) >> 1;
    diff_update(p, v, lc, l, mid);
    diff_update(p, v, rc, mid + 1, r);
    diff[t] = gcd(diff[lc], diff[rc]);
}

ll sum_query(int ql, int qr, int t = 1, int l = 1, int r = n) {
    if (ql > qr) return 0;
    if (l > qr || r < ql) return 0;
    if (ql <= l && r <= qr) return sum[t];
    push_down(t, l, r);
    int lc = t << 1, rc = t << 1 | 1, mid = (l + r) >> 1;
    return sum_query(ql, qr, lc, l, mid) + sum_query(ql, qr, rc, mid + 1, r);
}

ll diff_query(int ql, int qr, int t = 1, int l = 1, int r = n) {
    if (ql > qr) return 0;
    if (l > qr || r < ql) return 0;
    if (ql <= l && r <= qr) return diff[t];
    int lc = t << 1, rc = t << 1 | 1, mid = (l + r) >> 1;
    return gcd(diff_query(ql, qr, lc, l, mid), diff_query(ql, qr, rc, mid + 1, r));
}

ll gcd_query(int l, int r) {
    if (l > r) return 1;
    return gcd(sum_query(l, l), diff_query(l + 1, r));
}

signed main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n;
    ll arr[n + 1];
    arr[0] = 0;
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
        sum_update(i, i, arr[i]);
        diff_update(i, arr[i] - arr[i - 1]);
    }
    cin >> q;
    while (q--) {
        string op;
        cin >> op;
        if (op[0] == 'U') {
            int l, r, x;
            cin >> l >> r >> x;
            sum_update(l, r, x);
            diff_update(l, x);
            diff_update(r + 1, -x);
        }
        else {
            ll ans = LLONG_MAX;
            ll pre = 1, val = sum_query(1, 1);
            while (pre < n) {
                int l = pre, r = n;
                while (l < r) {
                    int mid = (l + r + 1) / 2;
                    if (gcd_query(1, mid) == val) l = mid;
                    else r = mid - 1;
                }
                ans = min(ans, sum_query(1, l) / val + sum_query(l + 1, n) / gcd_query(l + 1, n));
                val = gcd_query(1, l + 1);
                pre = l + 1;
            }
            int suf = n;
            val = sum_query(n, n);
            while (suf > 1) {
                int l = 1, r = suf;
                while (l < r) {
                    int mid = (l + r) / 2;
                    if (gcd_query(mid, n) == val) r = mid;
                    else l = mid + 1;
                }
                ans = min(ans, sum_query(r, n) / val + sum_query(1, r - 1) / gcd_query(1, r - 1));
                val = gcd_query(r - 1, n);
                suf = r - 1;
            }
            cout << ans << '\n';
        }
    }
}