class EulerTourTreeNode:
    def __init__(self, l=0, r=0):
        self.ch = [None, None]
        self.p = None
        self.l = l
        self.r = r
        self.sz = int(l == r)
        self.sz2 = 0
        self.exact = True
        self.child_exact = l < r
        self.edge_connected = False

    def is_root(self) -> bool:
        return not self.p


class EulerTourTree:
    def __init__(self, N):
        self.ptr = [{i: EulerTourTreeNode(i, i)} for i in range(N)]
        self.N = N

    def _get_node(self, l, r):
        if r not in self.ptr[l]:
            self.ptr[l][r] = EulerTourTreeNode(l, r)
        return self.ptr[l][r]

    def _root(self, t):
        if not t:
            return t
        while t.p:
            t = t.p
        return t

    def _same(self, s, t):
        if s:
            self._splay(s)
        if t:
            self._splay(t)
        return self._root(s) == self._root(t)

    def _reroot(self, t):
        u, v = self._split(t)
        return self._merge(v, u)

    def _split(self, s):
        self._splay(s)
        t = s.ch[0]
        if t:
            t.p = None
        s.ch[0] = None
        return t, self._update(s)

    def _split2(self, s):
        self._splay(s)
        t, u = s.ch
        if t:
            t.p = None
        s.ch[0] = None
        if u:
            u.p = None
        s.ch[1] = None
        return t, u

    def _split3(self, s, t):
        u = self._split2(s)
        if self._same(u[0], t):
            r = self._split2(t)
            return r[0], r[1], u[1]
        else:
            r = self._split2(t)
            return u[0], r[0], r[1]

    def _merge(self, *args):
        def _merge_two(s, t):
            if not s:
                return t
            if not t:
                return s
            while s.ch[1]:
                s = s.ch[1]
            self._splay(s)
            s.ch[1] = t
            if t:
                t.p = s
            return self._update(s)

        ans = None
        for s in args:
            s = _merge_two(ans, s)

    def _size(self, t):
        return 0 if not t else t.sz

    def _size2(self, t):
        return 0 if not t else t.sz2

    def _update(self, t):
        t.sz = self._size(t.ch[0]) + int(t.l == t.r) + self._size(t.ch[1])
        t.sz2 = self._size2(t.ch[0]) + int(t.edge_connected) + self._size2(t.ch[1])
        t.child_exact = (
            (t.ch[0] and t.ch[0].child_exact)
            or (t.l < t.r and t.exact)
            or (t.ch[1] and t.ch[1].child_exact)
        )
        return t

    def _rot(self, t, b):
        x = t.p
        y = x.p
        b = int(b)
        x.ch[1 - b] = t.ch[b]
        if x.ch[1 - b]:
            t.ch[b].p = x
        t.ch[b] = x
        x.p = t
        self._update(x)
        self._update(t)
        t.p = y
        if t.p:
            if y.ch[0] == x:
                y.ch[0] = t
            if y.ch[1] == x:
                y.ch[1] = t
            self._update(y)

    def _splay(self, t):
        while not t.is_root():
            q = t.p
            if q.is_root():
                self._rot(t, q.ch[0] == t)
            else:
                r = q.p
                b = r.ch[0] == q
                if q.ch[1 - int(b)] == t:
                    self._rot(q, b)
                    self._rot(t, b)
                else:
                    self._rot(t, not b)
                    self._rot(t, b)

    """ Declaration of public methods """

    def size(self, s):
        t = self._get_node(s, s)
        self._splay(t)
        return t.sz

    def same(self, s, t):
        return self._same(self._get_node(s, s), self._get_node(t, t))

    def set_size(self, sz):
        while len(self.ptr) < sz:
            self.ptr.append({len(self.ptr): EulerTourTreeNode(len(self.ptr), len(self.ptr))})

    def edge_connected_update(self, s, b):
        t = self._get_node(s, s)
        self._splay(t)
        t.edge_connected = b
        self._update(t)

    def link(self, l, r):
        if self.same(l, r):
            return False
        self._merge(
            self._reroot(self._get_node(l, l)),
            self._get_node(l, r),
            self._reroot(self._get_node(r, r)),
            self._get_node(r, l),
        )
        return True

    def cut(self, l, r):
        if r not in self.ptr[l]:
            return False
        s, t, u = self._split3(self._get_node(l, r), self._get_node(r, l))
        self._merge(s, u)
        p, q = self.ptr[l][r], self.ptr[r][l]
        del self.ptr[l][r]
        del self.ptr[r][l]
        return True

    def edge_update(self, s, g):
        t = self._get_node(s, s)
        self._splay(t)
        def dfs(t):
            assert t
            if t.l < t.r and t.exact:
                self._splay(t)
                t.exact = False
                self._update(t)
                g(t.l, t.r)
                return
            if t.ch[0] and t.ch[0].child_exact:
                dfs(t.ch[0])
            else:
                dfs(t.ch[1])
        while t and t.child_exact:
            dfs(t)
            self._splay(t)

    def try_reconnect(self, s, f):
        t = self._get_node(s, s)
        self._splay(t)
        def dfs(t, idx):
            assert t
            if t.edge_connected and self._size2(t.ch[0]) == idx:
                self._splay(t)
                return f(t.l)
            if idx < self._size(t.ch[0]):
                return dfs(t.ch[0], idx)
            else:
                return dfs(t.ch[1], idx - self._size2(t.ch[0]) - int(t.edge_connected))

        while self._size2(t):
            if dfs(t, 0):
                return True
            self._splay(t)

        return False

class DynamicConnectivity:
    def __init__(self, sz):
        self.sz = sz
        self.dep = 1
        self.ett = []
        self.edges = []
        self.ett.append(EulerTourTree(sz))
        self.edges.append([set() for _ in range(sz)])

    def link(self, s, t):
        if s == t:
            return False
        if self.ett[0].link(s, t):
            return True
        self.edges[0][s].add(t)
        self.edges[0][t].add(s)
        if len(self.edges[0][s]) == 1:
            self.ett[0].edge_connected_update(s, True)
        if len(self.edges[0][t]) == 1:
            self.ett[0].edge_connected_update(t, True)
        return False

    def same(self, s, t):
        return self.ett[0].same(s, t)

    def size(self, s):
        return self.ett[0].size(s)

    def cut(self, s, t):
        if s == t:
            return False
        for i in range(self.dep):
            self.edges[i][s].discard(t)
            self.edges[i][t].discard(s)
            if len(self.edges[i][s]) == 0:
                self.ett[i].edge_connected_update(s, False)
            if len(self.edges[i][t]) == 0:
                self.ett[i].edge_connected_update(t, False)

        for i in range(self.dep - 1, -1, -1):
            if self.ett[i].cut(s, t):
                if self.dep - 1 == i:
                    self.dep += 1
                    self.ett.append(EulerTourTree(self.sz))
                    self.edges.append([set() for _ in range(self.sz)])
                return not self.try_reconnect(s, t, i)


        return 0


    def try_reconnect(self, s, t, k):
        for i in range(k):
            self.ett[i].cut(s, t)
        for i in range(k, -1, -1):
            if self.ett[i].size(s) > self.ett[i].size(t):
                s, t = t, s
            def g(s, t):
                self.ett[i + 1].link(s, t)
            self.ett[i].edge_update(s, g)
            def f(x):
                for y in list(self.edges[i][x]):
                    self.edges[i][x].discard(y)
                    self.edges[i][y].discard(x)
                    if len(self.edges[i][x]) == 0:
                        self.ett[i].edge_connected_update(x, False)
                    if len(self.edges[i][y]) == 0:
                        self.ett[i].edge_connected_update(y, False)
                    if self.ett[i].same(x, y):
                        self.edges[i + 1][x].add(y)
                        self.edges[i + 1][y].add(x)
                        if len(self.edges[i + 1][x]) == 1:
                            self.ett[i + 1].edge_connected_update(x, True)
                        if len(self.edges[i + 1][y]) == 1:
                            self.ett[i + 1].edge_connected_update(y, True)

                    else:
                        for j in range(i + 1):
                            self.ett[j].link(x, y)
                        return True

                return False

            if self.ett[i].try_reconnect(s, f):
                return True

        return False



def main():
    g = DynamicConnectivity(3)
    print(g.link(0,1))
    print(g.link(0,2))
    print(g.link(1,2))
    print(g.size(0))
    print(g.size(1))
    print(g.size(2))
    print(g.same(0,2))
    print(g.same(0,1))



if __name__ == '__main__':
    main()




