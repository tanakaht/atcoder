import sys
from collections import defaultdict

sys.setrecursionlimit(int(1e6))
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        d = {root: [] for root in self.roots()}
        for i in range(self.n):
            d[self.find(i)].append(i)
        return d

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


T = int(input())
MOD = 1000000007
for caseid in range(1, T+1):
    N = int(input())
    ABC = [list(map(int, input().split())) for _ in range(N-1)]
    g=[[] for _ in range(N)]
    weights = defaultdict(dict)
    for a, b, c in ABC:
        g[a-1].append((b-1, c))
        g[b-1].append((a-1, c))
        weights[a-1][b-1] = c
        weights[b-1][a-1] = c

    uf = UnionFind(N)
    base = 0
    for a, b, c in sorted(ABC, key=lambda x: -x[2]):
        a -= 1
        b -= 1
        if uf.find(a)==uf.find(b):
            continue
        base = (base+c*uf.size(a)*uf.size(b))%MOD
        uf.union(a, b)


    children = [[] for _ in range(N)]
    parents = [None]*N
    q = [(0, None)]
    dfs_ord = []
    while len(q) > 0:
        v, p = q.pop()
        dfs_ord.append(v)
        parents[v] = p
        for u, c in g[v]:
            if u != p:
                q.append((u, v))
                children[v].append((u, c))

    e = [0]*21
    def op(a, b):
        return [a[i]+b[i] for i in range(21)]

    dp1 = [None]*N
    def dfs1(u, p):
        if dp1[u] is not None:
            return dp1[u]
        ret = e
        for v, c in children[u]:
            if v == p:
                continue
            val = dfs1(v, u)
            val = [x for x in val]
            val[c] = sum(val[c:])+1
            for i in range(c+1, 21):
                val[i] = 0
            ret = op(ret, val)
        dp1[u] = ret
        return dp1[u]

    dp2 = [defaultdict(lambda: None) for _ in range(N)]
    def dfs2(u, p, d):
        if dp2[u][d] is not None:
            return dp2[u][d]
        lcums = [e]
        rcums = [e, e]
        for v, c in g[u]:
            if v == p:
                val = dfs2(v, parents[v], u)
            else:
                val = dfs1(v, u)
            val = [x for x in val]
            val[c] = sum(val[c:])+1
            for i in range(c+1, 21):
                val[i] = 0
            lcums.append(op(lcums[-1], val))
        for v, c in g[u][::-1]:
            if v == p:
                val = dfs2(v, parents[v], u)
            else:
                val = dfs1(v, u)
            val = [x for x in val]
            val[c] = sum(val[c:])+1
            for i in range(c+1, 21):
                val[i] = 0
            rcums.append(op(rcums[-1], val))
        for i, (v, c) in enumerate(g[u]):
            dp2[u][v] = op(lcums[i], rcums[-(i+2)])
        dp2[u][-1] = lcums[-1]
        return dp2[u][d]

    ans = 1
    for u in dfs_ord[::-1]:
        dfs1(u, parents[u])

    for u in dfs_ord:
        x = 0
        if parents[u] is None:
            continue
        c = weights[u][parents[u]]
        v1 = [x for x in dfs1(u, parents[u])]
        v2 = [x for x in dfs2(parents[u], parents[parents[u]], u)]
        v1[c] = sum(v1[c:])+1
        for i in range(c+1, 21):
            v1[i] = 0
        v2[c] = sum(v2[c:])+1
        for i in range(c+1, 21):
            v2[i] = 0
        for i in range(21):
            cnt = v1[i]*sum(v2[i:])+v2[i]*sum(v1[i:])-v1[i]*v2[i]
            x += i*cnt
        dfs2(u, parents[u], parents[u])
        ans = (ans*(base-x))%MOD

    print(f'Case #{caseid}: {ans}')
