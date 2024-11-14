#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
#include <fstream>
#include <iomanip>
#include <random>
#include <stack>
#include <set>
#include <random>
 
using namespace std;
 
#define pb push_back
#define mp make_pair
#define rep(i, n) for (int i = 0 ; i < n ; i++)
#define rrep(i, a, n) for (int i = a ; i < n ; i++)
#define per(i, n) for (int i = n - 1 ; i >= 0 ; i--)
#define all(x) begin(x), end(x)
#define int long long
#define sz(x) (int) (x).size()
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef tuple<int, int, int> iii;
typedef vector<iii> viii;
typedef priority_queue<int> pqi;
typedef priority_queue<ii> pqii;
typedef map<int, int> mii;
typedef map<int, string> mis;
typedef map<string, int> msi;
typedef map<ll, ll> mll;
typedef queue<int> qi;
typedef queue<ii> qii;
typedef pair<ll, ll> iil;
typedef vector<iil> viil;
typedef vector<vi> vvi;
 
ll MOD = 1000000007;
ll INF = 1LL * 2000000000 * 2000000000;
 
double PI = 3.1415926535897932;
 
mt19937_64 mt;

void solve() {
    /*
     5 9 5
     #########
     #...S..*#
     ######..#
     #.E....*#
     #########
     */
    
    int n, m, k;
    cin >> n >> m >> k;
        
    char mat[n][m];
    rep(i, n) {
        string s;
        cin >> s;
        
        rep(j, m) {
            mat[i][j] = s[j];
        }
    }
    
    int dx[4] = {0, 0, -1, 1};
    int dy[4] = {-1, 1, 0, 0};
    
    vector<pair<ii, int>> adj[n][m][2];
    
    int last_wall[n][m][4];
    int last_crystal[n][m][4];
    
    rep(i, n) {
        last_wall[i][0][0] = -1;
        last_crystal[i][0][0] = -1;
        
        rrep(j, 1, m) {
            if (mat[i][j - 1] == '#') {
                last_wall[i][j][0] = j - 1;
            }
            else {
                last_wall[i][j][0] = last_wall[i][j - 1][0];
            }
            
            if (mat[i][j - 1] == '*') {
                last_crystal[i][j][0] = j - 1;
            }
            else {
                last_crystal[i][j][0] = last_crystal[i][j - 1][0];
            }
            
            if (i == 1 && j == 1) {
    //            cout << mat[i][j - 1] << " " << last_wall[i][j][0] << "  " << last_crystal[i][j][0] << endl;
            }
        }
        
        
        
        last_wall[i][m - 1][1] = -1;
        last_crystal[i][m - 1][1] = -1;

        for (int j = m - 2 ; j >= 0 ; j--) {
           
            if (mat[i][j + 1] == '#') {
                last_wall[i][j][1] = j + 1;
            }
            else {
                last_wall[i][j][1] = last_wall[i][j + 1][1];
            }
            /*
             5 7 5
             #########
             #...S..*#
             ######..#
             #.E....*#
             #########
             */
            if (mat[i][j + 1] == '*') {
                last_crystal[i][j][1] = j + 1;
            }
            else {
                last_crystal[i][j][1] = last_crystal[i][j + 1][1];
            }
            
            if ( j== 1 && i == 1) {
             //   cout << last_wall[i][j][1] << endl;
            }
        }
    }
    
    rep(j, m) {
        last_wall[0][j][2] = -1;
        last_crystal[0][j][2] = -1;

        rrep(i, 1, n) {
            if (mat[i - 1][j] == '#') {
                last_wall[i][j][2] = i - 1;
            }
            else {
                last_wall[i][j][2] = last_wall[i - 1][j][2];
            }
            
            if (mat[i - 1][j] == '*') {
                last_crystal[i][j][2] = i - 1;
            }
            else {
                last_crystal[i][j][2] = last_crystal[i - 1][j][2];
            }
        }
        
        last_wall[n - 1][j][3] = -1;
        last_crystal[n - 1][j][3] = -1;

        for (int i = n - 2 ; i >= 0 ; i--) {
            if (mat[i + 1][j] == '#') {
                last_wall[i][j][3] = i + 1;
            }
            else {
                last_wall[i][j][3] = last_wall[i + 1][j][3];
            }
            
            if (mat[i + 1][j] == '*') {
                last_crystal[i][j][3] = i + 1;
            }
            else {
                last_crystal[i][j][3] = last_crystal[i + 1][j][3];
            }
        }
    }
    
    ii start;
    ii end;
        
    rep(i, n) {
        rep(j, m) {
            if (mat[i][j] == '#') continue;
            
            if (mat[i][j] == 'S') {
                start = {i, j};
            }
            
            if (mat[i][j] == 'E') {
                end = {i, j};
            }
            
            rep(l, 4) {
                int lw = last_wall[i][j][l];
                int lc = last_crystal[i][j][l];
                
                if (i == 1 && j == 7 && l == 3) {
              //      cout << "lc: " << lc << endl;
                }
                
                bool crystal_in_dash;
                ii next_dash;
                
                if (l == 0) {
                    next_dash = {i, max(j - k, lw + 1)};
                    crystal_in_dash = (lc > lw);
                }
                else if (l == 1) {
                    next_dash = {i, min(j + k, lw - 1)};
                    crystal_in_dash = (lc < lw);
                }
                else if (l == 2) {
                    next_dash = {max(i - k, lw + 1), j};
                    crystal_in_dash = (lc > lw);
                }
                else {
                    next_dash = {min(i + k, lw - 1), j};
                    crystal_in_dash = (lc < lw);
                }
                
                if (lc == -1) {
                    crystal_in_dash = false;
                }
                
                if (i == 3 && j == 16 && l == 2) {
               //     cout << "c: " << crystal_in_dash << " " << lc << " " << lw << " " << next_dash.first << " " << next_dash.second << endl;
                }
                //dash
                if (crystal_in_dash) {
                    adj[i][j][1].pb({next_dash, 1});
                }
                else {
                    adj[i][j][1].pb({next_dash, 0});
                }
                
                //walk
                int nx = i + dx[l];
                int ny = j + dy[l];
                
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && mat[nx][ny] != '#') {
                    if (mat[nx][ny] == '*') {
                        adj[i][j][1].pb({{nx, ny}, 1});
                        adj[i][j][0].pb({{nx, ny}, 1});
                    }
                    else {
                        adj[i][j][1].pb({{nx, ny}, 1});
                        adj[i][j][0].pb({{nx, ny}, 0});
                    }
                }
            }
        }
    }
    
    queue<pair<ii, ii>> q;
    
    q.push({{0, 1}, start});
    
    bool vis[n][m][2];
    memset(vis, false, sizeof vis);
    
    int dist[n][m][2];
    rep(i, n) {
        rep(j, m) {
            rep(k, 2) dist[i][j][k] = -1;
        }
    }
    
    int ct = 0;
    
    while (q.size()) {
        ct++;
        pair<ii, ii> inf = q.front();
        int ds = inf.first.first;
        int dash = inf.first.second;
        int i = inf.second.first;
        int j = inf.second.second;
        
        q.pop();
                
        if (vis[i][j][dash]) continue;
        if (i < 0 || j < 0 || i >= n || j >= m) continue;
        
        vis[i][j][dash] = true;
        dist[i][j][dash] = ds;
        
        //cout << i << " " << j << " " << dash << " " << adj[i][j][dash].size() << endl;
        
        for (pair<ii, int> a : adj[i][j][dash]) {
            if (!vis[a.first.first][a.first.second][a.second]) {
                if (a.first.first == 6 && a.first.second == 16) {
           //         cout << i << " " << j << " " << dash <<  " " << ds << endl;
                }
                q.push({{ds + 1, a.second}, a.first});
            }
        }
    }
    
    /*rep(i, n) {
        rep(j, m) {
            cout << dist[i][j][0] << " ";
        }
        cout << endl;
    }
    
    cout << endl;
    rep(i, n) {
        rep(j, m) {
            cout << dist[i][j][1] << " ";
        }
        cout << endl;
    }
    */
    
    cout << min(dist[end.first][end.second][0], dist[end.first][end.second][1]) << '\n';
}

void querySolve() {
    int t;
    cin >> t;
    
    rep(i, t) {
        solve();
    }
}

int32_t main() {
    querySolve();
}
