#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
typedef pair <int, int> pii;
typedef long long ll;
#define pb push_back
#define mp make_pair
#define f first
#define s second

const int maxn = 100010;

int n;
ll arr[maxn], diff[maxn], pre[maxn], suf[maxn], ps[maxn], ss[maxn];

ll gcd(ll a, ll b) {
    if (a < b) swap(a, b);
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
        diff[i] = arr[i] - arr[i - 1];
    }
    int q;
    cin >> q;
    while (q--) {
        string op;
        cin >> op;
        if (op[0] == 'U') {
            int l, r, x;
            cin >> l >> r >> x;
            diff[l] += x;
            diff[r + 1] -= x;
        }
        else {
            for (int i = 1; i <= n; i++) {
                arr[i] = arr[i - 1] + diff[i];
                pre[i] = gcd(pre[i - 1], arr[i]);
                ps[i] = ps[i - 1] + arr[i];
            }
            for (int i = n; i >= 1; i--) {
                suf[i] = gcd(suf[i + 1], arr[i]);
                ss[i] = ss[i + 1] + arr[i];
            }
            ll ans = 1e12;
            for (int i = 1; i < n; i++) {
                ans = min(ans, ps[i] / pre[i] + ss[i + 1] / suf[i + 1]);
            }
            cout << ans << '\n';
        }
    }
}