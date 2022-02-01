import math
import heapq
import sys

N, M = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(M)]
g = [[] for _ in range(N)]
for a, b, c, d in ABCD:
    a -= 1
    b -= 1
    g[a].append((b, c, d))
    g[b].append((a, c, d))

def best_time(t, c, d):
    ret = t+c+d//(t+1)
    tmp = int(math.sqrt(d))
    for t_ in [tmp-1, tmp]:
        if t_>=t:
            ret = min(ret, t_+c+d//(t_+1))
    return ret

q = [(0, 0)]
dist = [math.inf]*N
while q:
    t, u = heapq.heappop(q)
    if u == N-1:
        print(t)
        sys.exit(0)
    if dist[u] < t:
        continue
    for v, c, d in g[u]:
        t_ = best_time(t, c, d)
        if dist[v] > t_:
            heapq.heappush(q, (t_, v))
            dist[v] = t_
print(-1)
