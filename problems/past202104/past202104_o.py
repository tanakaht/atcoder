import sys
import math
from collections import deque
sys.setrecursionlimit(int(1e5))
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

input = sys.stdin.readline
N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
Q = int(input())
UV = [list(map(int, input().split())) for _ in range(Q)]
uf = UnionFind(N)
g = [[] for _ in range(N)]
rest_edge = []
for a, b in AB:
    a -= 1
    b -= 1
    if uf.find(a) == uf.find(b):
        rest_edge.append((a, b))
        continue
    uf.union(a, b)
    g[a].append(b)
    g[b].append(a)

children = [[] for _ in range(N)]
q = [(0, None)]
while q:
    u, p = q.pop()
    for v in g[u]:
        if v == p:
            continue
        children[u].append(v)
        q.append((v, u))

# Euler Tour の構築
S = []
F = [0]*N
depth = [0]*N
def dfs(v, d):
    F[v] = len(S)
    depth[v] = d
    S.append(v)
    for w in children[v]:
        dfs(w, d+1)
        S.append(v)
dfs(0, 0)

# 存在しない範囲は深さが他よりも大きくなるようにする
INF = (N, None)

# LCAを計算するクエリの前計算
M = 2*N
M0 = 2**(M-1).bit_length()
data = [INF]*(2*M0)
for i, v in enumerate(S):
    data[M0-1+i] = (depth[v], i)
for i in range(M0-2, -1, -1):
    data[i] = min(data[2*i+1], data[2*i+2])

# LCAの計算 (generatorで最小値を求める)
def _query(a, b):
    yield INF
    a += M0; b += M0
    while a < b:
        if b & 1:
            b -= 1
            yield data[b-1]
        if a & 1:
            yield data[a-1]
            a += 1
        a >>= 1; b >>= 1

# LCAの計算 (外から呼び出す関数)
def query(u, v):
    fu = F[u]; fv = F[v]
    if fu > fv:
        fu, fv = fv, fu
    return S[min(_query(fu, fv+1))[1]]

Ps = set()
for u, v in rest_edge:
    Ps.add(u)
    Ps.add(v)
    g[u].append(v)
    g[v].append(u)

dists = {i: [math.inf]*N for i in Ps}
for i in Ps:
    dists[i][i] = 0
    appeared = [False]*N
    appeared[i] = True
    q = deque([(i, 0)])
    while q:
        u, d = q.popleft()
        for v in g[u]:
            if appeared[v]:
                continue
            q.append((v, d+1))
            appeared[v] = True
            dists[i][v] = d+1

for u, v in UV:
    u -= 1
    v -= 1
    lca = query(u, v)
    ans = depth[u]+depth[v]-2*depth[lca]
    for i in Ps:
        ans = min(ans, dists[i][u]+dists[i][v])
    print(ans)
