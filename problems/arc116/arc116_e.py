import sys
import math

sys.setrecursionlimit(int(1e7))
input = sys.stdin.readline
N, K = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

children = [[] for _ in range(N)]
parent = [None]*N
q = [(0, None)]
while q:
    u, p = q.pop()
    parent[u] = p
    for v in g[u]:
        if v==p:
            continue
        children[u].append(v)
        q.append((v, u))


def is_ok(time_limit):
    dp1 = [None]*N # 貪欲にやって子の部分木に何個必要？
    dp2 = [None]*N # おや何個ぶんまでに必要？
    def dfs(u):
        if dp1[u] is not None:
            return dp1[u], dp2[u]
        ret = [0, time_limit]
        if children[u]:
            highest = -1
            for v in children[u]:
                i, j = dp1[v], dp2[v]
                ret[0] += i
                highest = max(highest, j-1)
                ret[1] = min(ret[1], j-1)
            kyori = 2*time_limit+1-highest
            if ret[1] >= kyori:
                ret[1] = highest
            if ret[1] == 0:
                ret[0] += 1
                ret[1] = 2*time_limit+1
        dp1[u] = ret[0]
        dp2[u] = ret[1]
        return ret

    dfsord = []
    q = [0]
    while q:
        u = q.pop()
        dfsord.append(u)
        for v in children[u]:
            q.append(v)
    for u in dfsord[::-1]:
        dfs(u)
    res = dfs(u)
    return res[0]+(res[1]<time_limit+1) <= K

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(bisect(0, N+1))
