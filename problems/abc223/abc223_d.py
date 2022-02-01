import sys
import heapq

input = sys.stdin.readline
N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
g = [[] for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].append(b)

ans = []
cnts = [0]*N
for u in range(N):
    for v in g[u]:
        cnts[v] += 1
removed = [False]*N
rmq = []
for u in range(N):
    if cnts[u]==0:
        heapq.heappush(rmq, u)
while rmq:
    u = heapq.heappop(rmq)
    ans.append(u+1)
    removed[u] = True
    for v in g[u]:
        cnts[v] -= 1
        if cnts[v] == 0:
            heapq.heappush(rmq, v)
if len(ans)!=N:
    print(-1)
else:
    print(*ans)
