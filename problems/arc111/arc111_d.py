from collections import defaultdict
import sys
import math
sys.setrecursionlimit(3000)

input = sys.stdin.readline
N, M = map(int, input().split())
ab = []
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ab.append((a, b))
c = list(map(int, input().split()))


ans = [None]*M
g = [[] for _ in range(N)]
for i, (a, b) in enumerate(ab):
    if c[a] > c[b]:
        ans[i] = '->'
    elif  c[a] < c[b]:
        ans[i] = '<-'
    else:
        g[a].append((i, b))
        g[b].append((i, a))

appeared = [False]*N
ord = [math.inf]*N
def dfs(v, p, k):
    appeared[v] = True
    ord[v] = k
    for i, u in g[v]:
        if u == p:
            continue
        if not appeared[u]:
            dfs(u, v, k+1)
            if ab[i][0] == v:
                ans[i] = '->'
            else:
                ans[i] = '<-'
        else:
            if ord[v] > ord[u]:
                if ab[i][0] == v:
                    ans[i] = '->'
                else:
                    ans[i] = '<-'

for v in range(N):
    if appeared[v]:
        continue
    appeared[v] = True
    if len(g[v])==0:
        continue
    dfs(v, None, 0)

for i in ans:
    print(i)
