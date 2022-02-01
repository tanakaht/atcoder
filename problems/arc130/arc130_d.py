import sys
import math


sys.setrecursionlimit(int(1e6))
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]
MOD = 998244353
g = [[] for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
for root in range(N):
    if len(g[root])==1:
        break

children = [[] for _ in range(N)]
parents = [None]*N
q = [(root, None)]
dfs_ord = []
while len(q) > 0:
    u, p = q.pop()
    dfs_ord.append(u)
    parents[u] = p
    for v in g[u]:
        if v != p:
            q.append((v, u))
            children[u].append(v)

# 再利用する時あらかじめN以下の計算しとく
kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, 2*N+10):
    tmp = (tmp*i) % MOD
    kaizyo.append(tmp)
    kaizyo_inv.append(pow(tmp, MOD - 2, MOD))


def comb(n, r):
    if n < r or n < 0:
        return 0
    elif n == r or r==0:
        return 1
    else:
        return (((kaizyo[n] * kaizyo_inv[r])%MOD) * kaizyo_inv[n - r])%MOD

def concat(pn, pm, flg):
    n, m = len(pn), len(pm)
    pm_ = [0]
    for p in pm:
        pm_.append((pm_[-1]+p)%MOD)
    if flg:
        pm_ = [pm_[-1]-x for x in pm_]
    ret = [0]*(n+m)
    for i in range(n+m):
        for x in range(max(0, i-m), min(i+1, n)):
            ret[i] = (ret[i] + (comb(i, x)*comb(n+m-(i+1), n-(x+1)))%MOD * (pn[x]*pm_[i-x])%MOD)%MOD
    return ret

ans = 0

# ptn1
q = [(root, None, 0)] # 今どこ、どっから来た、flg
node_flg = [None]*N
while len(q) > 0:
    u, p, flg = q.pop()
    node_flg[u] = flg
    for v in g[u]:
        if v != p:
            q.append((v, u, flg^1))

dp1 = [None]*N
def dfs1(u):
    if dp1[u] is not None:
        return dp1[u]
    ret = [1]
    for v in children[u]:
        ret = concat(ret, dfs1(v), node_flg[u])
    dp1[u] = ret
    return dp1[u]

for u in dfs_ord[::-1]:
    dfs1(u)
ans = ans + sum(dfs1(root))%MOD


#ptn2
node_flg = [i^1 for i in node_flg]

dp1 = [None]*N
for u in dfs_ord[::-1]:
    dfs1(u)
ans = ans + sum(dfs1(root))%MOD

print(ans)
