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
use_edgeclass = True

# 入力生成の何番目で作られたedgeか調べる
if use_edgeclass:
    edge_class = [[None]*N for _ in range(N)]
    edges_tmp = []
    for u in range(N):
        ux, uy = XY[u]
        for v in range(u+1, N):
            vx, vy = XY[v]
            d = round(math.sqrt((ux-vx)**2+(uy-vy)**2))
            edges_tmp.append((d, u, v))
    edges_tmp = sorted(edges_tmp)
    is_used = [False]*(len(edges_tmp))
    for i in range(5):
        uf_tmp = UnionFind(N)
        for j ,(d, u, v) in enumerate(edges_tmp):
            if is_used[j] or (uf_tmp.find(u)==uf_tmp.find(v)):
                continue
            uf_tmp.union(u, v)
            is_used[j] = True
            edge_class[u][v] = i
            edge_class[v][u] = i

class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v
        self.ux, self.uy = XY[u]
        self.vx, self.vy = XY[v]
        self.d = round(math.sqrt((self.ux-self.vx)**2+(self.uy-self.vy)**2))
        self.used = None
        self.uf = uf_main
        if use_edgeclass:
            self.edge_class = edge_class[u][v]

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
cnt = 0
sikoukaisuu = 1
g_base = [[] for _ in range(N)]
for i, edge in list(enumerate(edges)):
    d = int(input())
    u, v = edge.u, edge.v
    if not edge.is_useful():
        edge.unuse()
        continue
    # 10^3~10^4くらいまでok
    ok_cnt = 0
    if time()-ts>1.65:
        sikoukaisuu=0
    for _ in range(sikoukaisuu):
        g_tmp = [[x for x in g_base[nodeid]] for nodeid in range(N)]
        for edge_ in edges[1:]:
            d_ = random.randint(edge_.d, edge_.d*3)
            u_, v_ = edge_.u, edge_.v
            if d_<d:
                g_tmp[u_].append(v_)
                g_tmp[v_].append(u_)
        # uからdfs
        start_node = u
        appeared = [False]*N
        q = [start_node]
        while q:
            x = q.pop()
            if appeared[x]:
                continue
            appeared[x] = True
            # 入った時の処理
            if x==v:
                ok_cnt += 1
                break
            # 探索先を追加
            for y in g_tmp[x]:
                if appeared[y]:
                    continue
                q.append(y)
        if time()-ts>1.65:
            break
    if ok_cnt*2<=sikoukaisuu:
        edge.use()
        g_base[u].append(v)
        g_base[v].append(u)
        cnt += 1
    else:
        edge.unuse()
    edges = [e for e in edges[1:] if e.is_useful()]
print(time()-ts, file=sys.stderr)
