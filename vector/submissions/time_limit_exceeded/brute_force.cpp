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
ll arr[maxn];

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
    }
    int q;
    cin >> q;
    while (q--) {
        string op;
        cin >> op;
        if (op[0] == 'U') {
            int l, r, x;
            cin >> l >> r >> x;
            for (int i = l; i <= r; i++) arr[i] += x;
        }
        else {
            ll ans = 1e12;
            for (int k = 1; k < n; k++) {
                int v1 = arr[1];
                ll sum1 = arr[1];
                for (int i = 2; i <= k; i++) {
                    v1 = gcd(v1, arr[i]);
                    sum1 += arr[i];
                }
                int v2 = arr[n];
                ll sum2 = arr[n];
                for (int i = n - 1; i > k; i--) {
                    v2 = gcd(v2, arr[i]);
                    sum2 += arr[i];
                }
                ans = min(ans, sum1 / v1 + sum2 / v2);
            }
            cout << ans << endl;
        }
    }
}