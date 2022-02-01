import sys
import math
import random
from time import time
ts = time()

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


N, M = 400, 1995
XY = [list(map(int, input().split())) for _ in range(N)]
UV = [list(map(int, input().split())) for _ in range(M)]
uf_main = UnionFind(N)

class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v
        self.ux, self.uy = XY[u]
        self.vx, self.vy = XY[v]
        self.d = round(math.sqrt((self.ux-self.vx)**2+(self.uy-self.vy)**2))
        self.used = None
        self.uf = uf_main

    def is_useful(self, uf=None):
        if uf is not None:
            return uf.find(self.u)!=uf.find(self.v)
        else:
            return self.uf.find(self.u)!=self.uf.find(self.v)

    def use(self, uf=None):
        if uf is not None:
            uf.union(self.u, self.v)
        else:
            self.uf.union(self.u, self.v)
            self.used = True
            print(1)

    def unuse(self, uf=None):
        if uf is not None:
            pass
        else:
            self.used = False
            print(0)

edges = [Edge(u, v) for u, v in UV]
expected_v = [[math.inf]*N for _ in range(M)]
for i, edge in list(enumerate(edges))[::-1]:
    d, u, v = edge.d, edge.u, edge.v
    if i<M-1:
        for j in range(N):
            expected_v[i][j] = [i+1][j]
    for x in [u, v]:
        m = expected_v[i][x]
        if m<=d:
            pass
        elif d<m<3*d:
            expected_v[i][x] = (m-d)*(d+m)/(4*d) + (3*d-m)*m/(2*d)
        else:
            expected_v[i][x] = 2*d
for i, edge in list(enumerate(edges))[::-1]:
    d, u, v = edge.d, edge.u, edge.v
    d_gt = int(input())
    if not edge.is_useful():
        edge.unuse()
        continue
    # 10^3~10^4くらいまでok
    is_saiyo = False
    # uの連結成分からの期待値
    E_u = math.inf
    E_v = math.inf
    for edge_ in edges[i+1:][::-1]:
        d_ = edge_.d
        if u in [edge_.u, edge_.v]:
            if E_u<=d_:
                pass
            elif d_<E_u<3*d_:
                E_u = (E_u-d_)*(d_+E_u)/(4*d_) + (3*d_-E_u)*E_u/(2*d_)
            else:
                E_u = 2*d_
        if v in [edge_.u, edge_.v]:
            if E_v<=d_:
                pass
            elif d_<E_v<3*d_:
                E_v = (E_v-d_)*(d_+E_v)/(4*d_) + (3*d_-E_v)*E_v/(2*d_)
            else:
                E_v = 2*d_
    is_saiyo = i==M-1 or expected_v[i+1][u]>d_gt-1 or expected_v[i+1][v]>d_gt-1
    if is_saiyo:
        edge.use()
    else:
        edge.unuse()
    edges = [e for e in edges[1:] if e.is_useful()]
print(time()-ts, file=sys.stderr)
