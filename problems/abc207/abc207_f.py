from itertools import zip_longest

MOD = int(10**9+7)

def add_(a, b):
    return [(x+y)%MOD for x, y in zip_longest(a, b, fillvalue=0)]

def sub_(a, b):
    return [(x-y)%MOD for x, y in zip_longest(a, b, fillvalue=0)]

def convolve(a, b):
    ret = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            ret[i+j] = (ret[i+j]+x*y)%MOD
    return ret

def roll(a):
    return [0]+a[:-1]

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
    u, p = q.pop()
    parents[u] = p
    dfs_ord.append(u)
    for v in g[u]:
        if v != p:
            q.append((v, u))
            children[u].append(v)

dp = [None]*N
def dfs(u: int):
    if dp[u] is not None:
        return dp[u]
    # 0: 監視なし, 1: 監視あり(置かれてない), 2: 監視あり(置かれている)
    tmp0, tmp1, tmp2 = [1, 0], [0, 1], [0, 1]
    for v in children[u]:
        if v == parents[u]:
            continue
        v0, v1, v2 = dfs(v)
        tmp0 = convolve(tmp0, add_(v0, v1))
        tmp1 = convolve(tmp1, add_(add_(v0, v1), v2))
        tmp2 = convolve(tmp2, add_(add_(roll(v0), v1), v2))
    ret = [tmp0, sub_(tmp1, roll(tmp0)), tmp2]
    dp[u] = ret
    return dp[u]

for u in dfs_ord[::-1]:
    dfs(u)
for i, j, k in zip(*dp[0]):
    print((i+j+k)%MOD)
