import sys
from collections import defaultdict

sys.setrecursionlimit(int(1e6))

N = int(input())
UVW = [list(map(int, input().split())) for _ in range(N-1)]
MOD = int(1e9+7)

g=[[] for _ in range(N)]
for a, b, w in UVW:
    g[a-1].append((b-1, w))
    g[b - 1].append((a - 1, w))

children = [[] for _ in range(N)]
parents = [None]*N
q = [(0, None, 0)]
while len(q) > 0:
    v, p, w = q.pop()
    parents[v] = (p, w)
    for u, w in g[v]:
        if u != p:
            q.append((u, v, w))
            children[v].append((u, w))


dp1 = [None]*N # (部分木のnode数, xorの集計array)
def dfs1(u):
    if dp1[u] is not None:
        return dp1[u]
    ret = [1, [0]*60]
    for v, w in children[u]:
        n, v = dfs1(v)
        ret[0] += n
        for i in range(60):
            if (w>>i)&1:
                ret[1][i] += n-v[i]
            else:
                ret[1][i] += v[i]
    dp1[u] = ret
    return dp1[u]

dfs_order = []
appeared, withdrawed = [False]*N, [False]*N
t = 0
q = [0]
while q:
    u = q.pop()
    if appeared[u]:
        continue
    appeared[u] = True
    # 入った時の処理
    # 記録
    dfs_order.append(u)
    # 探索先を追加
    for v, w in g[u][::-1]:
        if appeared[v]:
            continue
        q.append(v)
for u in dfs_order[::-1]:
    dfs1(u)

ans = 0
for u in range(N):
    n, v = dfs1(u)
    v = [x for x in v]
    for c, w in children[u]:
        nc, vc = dfs1(c)
        for i in range(60):
            if (w>>i)&1:
                v[i] -= nc-vc[i]
            else:
                v[i] -= vc[i]
        n -= nc
        for i in range(60):
            n0, n1 = n-v[i], v[i]
            nc0, nc1 = nc-vc[i], vc[i]
            if (w>>i)&1:
                ans = (ans+((n0*nc0+n1*nc1)<<i))%MOD
            else:
                ans = (ans+((n0*nc1+n1*nc0)<<i))%MOD
print(ans)
