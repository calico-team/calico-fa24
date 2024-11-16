#include <bits/stdc++.h>
using namespace std;
typedef pair <int, int> pii;
typedef long long ll;
#define pb push_back
#define mp make_pair
#define f first
#define s second

const int maxn = 100010;
const int CHEESE = 30;

// Try to cheese it without using a segment tree for gcd.
// I'll use the same segment tree for sums just for commodity, but can be changed to a fenwick tree for example.

int n, q;
ll sum[maxn * 4], add[maxn * 4], pref_gcd[maxn], suf_gcd[maxn];

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

ll sum_query(int ql, int qr, int t = 1, int l = 1, int r = n) {
    if (ql > qr) return 0;
    if (l > qr || r < ql) return 0;
    if (ql <= l && r <= qr) return sum[t];
    push_down(t, l, r);
    int lc = t << 1, rc = t << 1 | 1, mid = (l + r) >> 1;
    return sum_query(ql, qr, lc, l, mid) + sum_query(ql, qr, rc, mid + 1, r);
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n;
    int arr[n + 1];
    arr[0] = 0;
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
        sum_update(i, i, arr[i]);
    }
    // Create prefix gcd and suffix gcd arrays.
    pref_gcd[0] = suf_gcd[n + 1] = 1; // Dont want to divide by 0
    pref_gcd[1] = arr[1];
    for (int i = 2; i <= n; ++i) {
        pref_gcd[i] = gcd(pref_gcd[i-1], arr[i]);
    }
    suf_gcd[n] = arr[n];
    for (int i = n - 1; i; --i) {
        suf_gcd[i] = gcd(suf_gcd[i+1], arr[i]);
    }
    ll last_pref, val_pref = pref_gcd[1], last_suf, val_suf = suf_gcd[1];
    for (int i = 1; i <= n; ++i) {
	    if (pref_gcd[i] == val_pref) {
		    last_pref = i;
	    }
    }

    for (int i = n; i; --i) {
	    if (suf_gcd[i] == val_suf) {
		    last_suf = i;
		    val_suf = suf_gcd[1];
	    }
    };
    cin >> q;
    while (q--) {
        string op;
        cin >> op;
        if (op[0] == 'U') {
            int l, r, x;
            cin >> l >> r >> x;
            sum_update(l, r, x); // We update sum as the other version
            // GCD update is different. Let's try to cheese it.
	    int cnt = 0;
	    int cnt_repeated = 0;
	    for (int i = l; i <= r; ++i) {
		    pref_gcd[i] = (i == 1 ? sum_query(1, 1) : gcd(pref_gcd[i - 1], sum_query(i, i)));
		    // Say CHEEEEEEESEEEEEEE
		    if (pref_gcd[i] == pref_gcd[i - 1]) {
			    ++cnt_repeated;
			    if (cnt_repeated == CHEESE) {
				    break;
			    }
		    } else {
			    cnt_repeated = 0;
		    }
	    }
	    	    

	    for (int i = r; i >= l; --i) {
		    suf_gcd[i] = (i == n ? sum_query(n, n) : gcd(suf_gcd[i + 1], sum_query(i, i)));
		    // Do something to break and not process every number in the segment.
		    if (suf_gcd[i] == val_suf) {
			    ++cnt;
			    if (cnt == CHEESE) {
				    break;
			    }
		    } else if (suf_gcd[i] < val_suf) {
			    cnt = 0;
			    val_suf = gcd(val_suf, suf_gcd[i]);
		    }
	    }
        }
        else {
            ll ans = ll(1e18);
            int pre = 1;
	    ll val = sum_query(1, 1);
            while (pre <= n) {
                int l = pre, r = n + 1;
                while (l + 1 < r) {
                    int mid = (l + r) / 2;
                    if (pref_gcd[mid] == val) l = mid;
                    else r = mid;
                }
                val = pref_gcd[l + 1];
                ans = min(ans, sum_query(1, l) / pref_gcd[l] + sum_query(l + 1, n) / suf_gcd[l + 1]);
                pre = l + 1;
            }
            int suf = n;
            val = sum_query(n, n);
            while (suf > 0) {
                int l = 0, r = suf;
                while (l + 1 < r) {
                    int mid = (l + r) / 2;
                    if (suf_gcd[mid] == val) r = mid;
                    else l = mid;
                }
                val = suf_gcd[r - 1];
                ans = min(ans, sum_query(r, n) / suf_gcd[r] + sum_query(1, r - 1) / pref_gcd[r-1]);
                suf = r - 1;
            }
            cout << ans << '\n';
        }
    }
}
