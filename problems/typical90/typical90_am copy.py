import sys
from collections import defaultdict

sys.setrecursionlimit(int(1e6))

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]
g = [[] for _ in range(N)]
for a, b in AB:
    g[a-1].append(b-1)
    g[b - 1].append(a - 1)

children = [[] for _ in range(N)]
parents = [None]*N
q = [(0, None)]
while len(q) > 0:
    v, p = q.pop()
    parents[v] = p
    for u in g[v]:
        if u != p:
            q.append((u, v))
            children[v].append(u)


dp1 = [None]*N # (部分木のノード数, 子孫とのdistのsum)
def dfs1(u):
    if dp1[u] is not None:
        return dp1[u]
    ret = [1, 0]
    for v in children[u]:
        n, s = dfs1(v)
        ret[0] += n
        ret[1] += s+n
    dp1[u] = ret
    return dp1[u]


dfs_order = []
appeared = [False]*N
q = [0]
while q:
    u = q.pop()
    if appeared[u]:
        continue
    appeared[u] = True
    dfs_order.append(u)
    for v in g[u][::-1]:
        if appeared[v]:
            continue
        q.append(v)

dfs1(0)

dp2 = [None]*N
dp2[0] = dfs1(0)[1]
def dfs2(u):
    if dp2[u] is not None:
        return dp2[u]
    pans = dfs2(parents[u])
    n, s = dfs1(u)
    ret = pans - n + (N-n)
    dp2[u] = ret
    return dp2[u]

for i in dfs_order[::-1]:
    dfs2(i)

print(sum(dp2)//2)
