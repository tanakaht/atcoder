import math
import heapq

N, M = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]

dist = [[math.inf]*N for _ in range(N)]
for i in range(N):
    dist[i][i] = 0
for a, b, c in ABC:
    dist[a-1][b-1] = c

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            if dist[i][j] != math.inf:
                ans += dist[i][j]
print(ans)
