#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <cstring>
#include <cassert>
using namespace std;
typedef pair <int, int> pii;
typedef long long ll;
#define pb push_back
#define mp make_pair
#define f first
#define s second

const int maxn = 100010;

int n, q;
ll sum[maxn * 4], add[maxn * 4], diff[maxn * 4];

ll gcd(ll a, ll b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    if (a < b) swap(a, b);
    if (b == 0) return a;
    return gcd(b, a % b);
}

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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
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
        int op;
        cin >> op;
        if (op == 1) {
            int l, r, x;
            cin >> l >> r >> x;
            sum_update(l, r, x);
            diff_update(l, x);
            diff_update(r + 1, -x);
        }
        else {
            ll ans = 1e18;
            ll pre = 1, val = sum_query(1, 1);
            while (pre <= n) {
                int l = pre, r = n + 1;
                while (l + 1 < r) {
                    int mid = (l + r) / 2;
                    if (gcd_query(1, mid) == val) l = mid;
                    else r = mid;
                }
                val = gcd_query(1, l + 1);
                ans = min(ans, sum_query(1, l) / gcd_query(1, l) + sum_query(l + 1, n) / gcd_query(l + 1, n));
                pre = l + 1;
            }
            int suf = n;
            val = sum_query(n, n);
            while (suf > 0) {
                int l = 0, r = suf;
                while (l + 1 < r) {
                    int mid = (l + r) / 2;
                    if (gcd_query(mid, n) == val) r = mid;
                    else l = mid;
                }
                val = gcd_query(r - 1, n);
                ans = min(ans, sum_query(r, n) / gcd_query(r, n) + sum_query(1, r - 1) / gcd_query(1, r - 1));
                suf = r - 1;
            }
            cout << ans << endl;
        }
    }
}