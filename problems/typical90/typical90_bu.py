import sys

sys.setrecursionlimit(int(1e6))

N = int(input())
C = input().split()
AB = [list(map(int, input().split())) for _ in range(N-1)]
MOD = int(10**9+7)
g=[[] for _ in range(N)]
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

dp = [None]*N
def solve(u):
    if dp[u] is not None:
        return dp[u]
    ret = [0, 0, 0]
    if C[u]=='a':
        ret[0] = 1
    else:
        ret[1] = 1
    for v in children[u]:
        a_, b_, ab_ = ret
        a, b, ab = solve(v)
        ret[0] = (a_*(a+ab))%MOD
        ret[1] = (b_*(b+ab))%MOD
        ret[2] = ((a_+b_+ab_)*(a+b+ab)-(a*a_+b*b_)+ab_*ab)%MOD
    dp[u] = ret
    return ret

dfs_order = []
q = [0]
while q:
    u = q.pop()
    dfs_order.append(u)
    # 探索先を追加
    for v in children[u][::-1]:
        q.append(v)
for u in dfs_order[::-1]:
    solve(u)
print(dp[0][-1])
