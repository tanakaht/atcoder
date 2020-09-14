import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline
N = int(input())


def get_id(i, j):
    if j < i:
        i, j = j, i
    return i * N + j


g = [[] for _ in range(N * N)]
S = []
for i in range(N):
    pre = None
    for j in map(int, input().split()):
        j -= 1
        id_ = get_id(i, j)
        if pre is None:
            S.append(id_)
        else:
            g[pre].append(id_)
        pre = id_


dp = [-1] * (N * N)
visited = [False] * (N * N)


def dfs(v):
    visited[v] = True
    if dp[v] != -1:
        return dp[v]
    for u in g[v]:
        if dp[u] != -1:
            res = dp[u]
        else:
            if visited[u]:
                raise ValueError('find loop!')
            res = dfs(u)
        dp[v] = max(dp[v], res + 1)
    if len(g[v]) == 0:
        dp[v] = 1
    return dp[v]


ans = 0
try:
    for s in S:
        ans = max(ans, dfs(s))
    print(ans)
except ValueError:
    print(-1)
