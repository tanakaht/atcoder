import sys
from collections import defaultdict

sys.setrecursionlimit(int(1e6))
N = int(input())
ABC = [list(map(int, input().split())) for _ in range(N-1)]
D = list(map(int, input().split()))

g = [[] for _ in range(N)]
for a, b, c in ABC:
    a -= 1
    b -= 1
    g[a].append((b, c))
    g[b].append((a, c))

children = [[] for _ in range(N)]
parents = [None]*N
dfs_ord = []
q = [(0, None)]
while len(q) > 0:
    v, p = q.pop()
    dfs_ord.append(v)
    parents[v] = p
    for u, c in g[v]:
        if u != p:
            q.append((u, v))
            children[v].append((u, c))

dp1 = [None]*N
def dfs1(u):
    if dp1[u] is not None:
        return dp1[u]
    ret = 0
    for v, c in children[u]:
        ret = max(ret, dfs1(v)+c, D[v]+c)
    dp1[u] = ret
    return dp1[u]

dp2 = [defaultdict(lambda: None) for _ in range(N)]
def dfs2(u, d):
    if dp2[u][d] is not None:
        return dp2[u][d]
    lcums = [0]
    rcums = [0, 0]
    for v, c in g[u]:
        if v == parents[u]:
            val = dfs2(v, u)
        else:
            val = dfs1(v)
        lcums.append(max(lcums[-1], val+c, D[v]+c))
    for v, c in g[u][::-1]:
        if v == parents[u]:
            val = dfs2(v, u)
        else:
            val = dfs1(v)
        rcums.append(max(rcums[-1], val+c, D[v]+c))
    for i, (v, c) in enumerate(g[u]):
        dp2[u][v] = max(lcums[i], rcums[-(i+2)])
    dp2[u][-1] = lcums[-1]
    return dp2[u][d]

for u in dfs_ord[::-1]:
    dfs1(u)
for u in dfs_ord:
    dfs2(u, -1)
print(*[dfs2(u, -1) for u in range(N)], sep='\n')
