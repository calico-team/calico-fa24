#include <bits/stdc++.h>
using namespace std;

class Matroid {
  public:
    Matroid(int n) : _n(n), _iset(n, false) {}
    // Returns if S+x is independent
    virtual bool independent(int x);
    // For y not in S, returns all x in S such that x is in S+y, S+y is not independent and (S+y)-x is an independent set.
    virtual vector<int> circuit(int y);
    // Adds x to S for S+x independent set
    virtual void insert(int x);
    // Removes x from S
    virtual void erase(int x);
    // Computes all circuits for all n elements in the matroid.
    vector<set<int>> compute_all_circuits() {
      vector<set<int>> answers(n);
      for (int x = 0; x < n; ++x) {
        if (!_iset[x]) continue;
        erase(x);
        for (int y = 0; y < n; ++y) {
          if (x != y && !_iset[y] && independent(y))
            answers[y].insert(x);
        }
        insert(x);
      }
      return answers;
    }

  private:
    int _n;
    vector<bool> _iset;

};

template<typename T>
vector<T> weighted_matroid_isect(int n, Matroid& F1, Matroid& F2, vector<T>& c) {
  assert((int)(c.size()) == n);
  vector<bool> iset(n, false);
  vector<T> c1(n), c2(n);
  for (int k = 0; k < n; ++k) {
    for (int e = 0; e < n; ++e) {
      c1[e] = c[e];
      c2[e] = c[e];
    }
    vector<set<int>> C1 = F1.compute_all_circuits(), C2 = F2.compute_all_circuits();
    set<int> A1, A2;
    for (int y = 0; y < n; ++y) {
      if (iset[y]) continue;
      for (int 
  }
}
