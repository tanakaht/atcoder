import math
import heapq

N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]
g = [[] for _ in range(N)]
for a, b, c in ABC:
    a -= 1
    b -= 1
    g[a].append((b, c))

for i in range(N):
    g[i] = sorted(g[i], key=lambda x: x[1])

ans = [-1]*N
for i in range(N):
    dist = [math.inf]*N
    appeared = [False]*N
    q = []
    for u, d in g[i]:
        q.append((d, u))
        dist[u] = min(d, dist[u])
    heapq.heapify(q)
    while q:
        d, u = heapq.heappop(q)
        if appeared[u]:
            continue
        if u == i:
            ans[i] = d
            break
        appeared[u] = True
        for v, d_ in g[u]:
            if dist[v] <= d+d_ or v==u:
                continue
            dist[u] = d+d_
            heapq.heappush(q, (d+d_, v))
print('\n'.join(map(str, ans)))
