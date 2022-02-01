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

N = int(input())
UV = [list(map(int, input().split())) for _ in range(N-1)]
MOD = 998244353
g = [[] for _ in range(N)]
for a, b in UV:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

depthes = [None]*N
q = [(0, None, 0)]  # u, p, depth
while len(q) > 0:
    v, p, depth = q.pop()
    depthes[v] = depth
    for u in g[v]:
        if u != p:
            q.append((u, v, depth+1))
root = 0
D = 0
for u in range(N):
    if D < depthes[u]:
        root = u
        D = depthes[u]

depthes = [None]*N
children = [[] for _ in range(N)]
parents = [None]*N
q = [(root, None, 0)]
dfs_ord = []
while len(q) > 0:
    v, p, depth = q.pop()
    dfs_ord.append(v)
    parents[v] = p
    depthes[v] = depth
    for u in g[v]:
        if u != p:
            q.append((u, v, depth+1))
            children[v].append(u)
D = max(depthes)
dp1 = [None]*N
def dfs1(u):
    if dp1[u] is not None:
        return dp1[u]
    ret = int(depthes[u] == D)
    for v in children[u]:
        ret = ret+dfs1(v)
    dp1[u] = ret
    return dp1[u]

for u in dfs_ord[::-1]:
    dfs1(u)
if D%2==1:
    print(dfs1(root))
    sys.exit(0)

grps = [1]
for u in range(N):
    if depthes[u]==D//2:
        for v in children[u]:
            grps.append(dfs1(v))
        break
ans = 1
for cnt in grps:
    ans = (ans*(cnt+1))%MOD
print((ans-sum(grps)-1)%MOD)
