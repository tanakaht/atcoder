import sys
from collections import defaultdict

sys.setrecursionlimit(int(1e6))
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]
g = [[] for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
children = [[] for _ in range(N)]
parents = [None]*N
q = [(0, None)]
dfs_ord = []
while len(q) > 0:
    v, p = q.pop()
    parents[v] = p
    dfs_ord.append(v)
    for u in g[v]:
        if u != p:
            q.append((u, v))
            children[v].append(u)

n_children_ = [None]*N
def n_children(u):
    if n_children_[u] is not None:
        return n_children_[u]
    ret = 1
    for v in children[u]:
        ret = ret+n_children(v)
    n_children_[u] = ret
    return n_children_[u]

dp1 = [None]*N
def dfs1(u):
    if dp1[u] is not None:
        return dp1[u]
    ret = 0
    for v in children[u]:
        ret = ret+dfs1(v)+n_children(v)
    dp1[u] = ret
    return dp1[u]

dp2 = [None]*N
def dfs2(u):
    if dp2[u] is not None:
        return dp2[u]
    ret = dfs1(u)
    p = parents[u]
    if p is not None:
        ret += dfs2(p)-(dfs1(u)+n_children(u))+N-n_children(u)
    dp2[u] = ret
    return dp2[u]


for u in dfs_ord[::-1]:
    n_children(u)
    dfs1(u)
for u in dfs_ord:
    dfs2(u)
print(*dp2, sep='\n')
