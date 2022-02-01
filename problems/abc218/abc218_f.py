import sys
from collections import deque
import math

N, M = map(int, input().split())
ST = [list(map(int, input().split())) for _ in range(M)]
g=[[] for _ in range(N)]
ginv=[[] for _ in range(N)]
for i, (s, t) in enumerate(ST):
    g[s-1].append((i, t-1))
    ginv[t-1].append((i, s-1))

# bfs
q = deque([(0, 0)]) # 今どこ, 距離
dist = [math.inf]*N
dist[0] = 0
while q:
    u, d = q.popleft()
    if u==N-1:
        break
    for i, v in g[u]:
        d_ = d+1
        if d_<dist[v]:
            dist[v] = d_
            q.append((v, d_))

keiro = []
u, d = N-1, dist[-1]
if d == math.inf:
    for _ in range(M):
        print(-1)
    sys.exit(0)
while u!=0:
    for i, v in ginv[u]:
        if dist[v]==d-1:
            d -= 1
            u = v
            keiro.append(i)
            break


anss = [dist[-1]]*M
for cantuse in keiro:
    q = deque([(0, 0)]) # 今どこ, 距離
    dist = [math.inf]*N
    dist[0] = 0
    while q:
        u, d = q.popleft()
        if u==N-1:
            break
        for i, v in g[u]:
            if i==cantuse:
                continue
            d_ = d+1
            if d_<dist[v]:
                dist[v] = d_
                q.append((v, d_))
    anss[cantuse] = dist[-1]

for i in anss:
    print(i if i!=math.inf else -1)
