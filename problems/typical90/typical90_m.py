import math
import heapq

N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]
g = [[] for _ in range(N)]
for a, b, c in ABC:
    a -= 1
    b -= 1
    g[a].append((b, c))
    g[b].append((a, c))

dists_0 = [math.inf]*N
appeared = [False]*N
dists_0[0] = 0
q = [(0, 0)]
while q:
    d, u = heapq.heappop(q)
    if appeared[u]:
        continue
    appeared[u] = True
    for v, c in g[u]:
        if dists_0[v] > d+c:
            heapq.heappush(q, (d+c, v))
            dists_0[v] = d+c

dists_N = [math.inf]*N
appeared = [False]*N
dists_N[N-1] = 0
q = [(0, N-1)]
while q:
    d, u = heapq.heappop(q)
    if appeared[u]:
        continue
    appeared[u] = True
    for v, c in g[u]:
        if dists_N[v] > d+c:
            heapq.heappush(q, (d+c, v))
            dists_N[v] = d+c
for k in range(N):
    print(dists_0[k]+dists_N[k])
