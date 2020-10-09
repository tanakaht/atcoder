import sys
import heapq
import math

input = sys.stdin.readline
N, M = map(int, input().split())
uv = [list(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

g = [[] for _ in range(3*N)]
for a, b in uv:
    g[a-1].append(b-1+N)
    g[a-1+N].append(b-1+2*N)
    g[a - 1 + 2 * N].append(b - 1)

# bfsでよかった
hq = [(0, S-1)]
costs = [math.inf] * 3 * N
while len(hq) > 0:
    c, u = heapq.heappop(hq)
    if u == T - 1:
        print(c // 3)
        sys.exit()
    costs[u] = c
    for v in g[u]:
        if costs[v] > c+1:
            heapq.heappush(hq, (c + 1, v))
        costs[v] = min(costs[v], c+1)

print(-1)
