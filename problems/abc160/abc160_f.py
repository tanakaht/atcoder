import sys
from collections import defaultdict

sys.setrecursionlimit(int(1e6))
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]
P = int(1e9+7)
kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, N+2):
    tmp = (tmp*i) % P
    kaizyo.append(tmp)
    kaizyo_inv.append(pow(tmp, P - 2, P))

def comb(n, r):
    if n < r or n < 0:
        return 0
    elif n == r or r==0:
        return 1
    else:
        return (((kaizyo[n] * kaizyo_inv[r])%P) * kaizyo_inv[n - r])%P

g = [[] for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
children = [[] for _ in range(N)]
parent = [None]*N
q = [(0, None)]
while q:
    u, p = q.pop()
    for v in g[u]:
        if v == p:
            continue
        children[u].append(v)
        parent[v] = u
        q.append((v, u))

e = (1, 0)
def op(a, b):
    a1, a2 = a
    b1, b2 = b
    return (((a1*b1)%P)*comb(a2+b2, a2)%P, a2+b2)

dp1 = [None]*N
def dfs1(u, p):
    if dp1[u] is not None:
        return dp1[u]
    ret = e
    for v in children[u]:
        if v == p:
            continue
        ret = op(ret, dfs1(v, u))
    dp1[u] = (ret[0], ret[1]+1)
    return dp1[u]

dp2 = [defaultdict(lambda: None) for _ in range(N)]
def dfs2(u, p, d):
    if dp2[u][d] is not None:
        return dp2[u][d]
    lcums = [e]
    rcums = [e, e]
    for v in g[u]:
        if v == p:
            val = dfs2(v, parent[v], u)
        else:
            val = dfs1(v, u)
        lcums.append(op(lcums[-1], val))
    for v in g[u][::-1]:
        if v == p:
            val = dfs2(v, parent[v], u)
        else:
            val = dfs1(v, u)
        rcums.append(op(rcums[-1], val))
    for i, v in enumerate(g[u]):
        tmp = op(lcums[i], rcums[-(i+2)])
        dp2[u][v] = (tmp[0], tmp[1]+1)
    tmp = lcums[-1]
    dp2[u][-1] = (tmp[0], tmp[1]+1)
    return dp2[u][d]

for i in range(N):
    print(dfs2(i, parent[i], -1)[0])
