import sys
import math
import heapq

N, M = map(int, input().split())
UVL = [list(map(int, input().split())) for _ in range(M)]
g = [[] for _ in range(N)]
dist = [[math.inf]*N for _ in range(N)]
for i in range(N):
    dist[i][i] = 0
for a, b, l in UVL:
    a -= 1
    b -= 1
    g[a].append((b, l))
    g[b].append((a, l))
    if 0 not in [a, b]:
        dist[a][b] = l
        dist[b][a] = l
for k in range(len(dist)):
    for i in range(len(dist)):
        for j in range(len(dist)):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = math.inf
for i , li in g[0]:
    for j, lj in g[0]:
        if i!=j:
            ans = min(ans, li+lj+dist[i][j])
if ans==math.inf:
    print(-1)
else:
    print(ans)
