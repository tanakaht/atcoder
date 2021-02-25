import sys
import math
import heapq

input = sys.stdin.readline
N, M, X, Y = map(int, input().split())
X -= 1
Y -= 1
ABTK = [list(map(int, input().split())) for _ in range(M)]
g = [[] for _ in range(N)]
for a, b, t, k in ABTK:
    a -= 1
    b -= 1
    g[a].append((b, t, k))
    g[b].append((a, t, k))

dist = [math.inf]*N
appeared = [False]*N
q = [(0, X)]
dist[X] = 0
while q:
    d, u = heapq.heappop(q)
    if appeared[u]:
        continue
    appeared[u] = True
    if u==Y:
        print(d)
        sys.exit(0)
    for v, t_, k_ in g[u]:
        if appeared[v]:
            continue
        d_ = math.ceil(d/k_)*k_ + t_
        if dist[v] <= d_:
            continue
        heapq.heappush(q, (d_, v))
        dist[v] = d_
print(-1)
