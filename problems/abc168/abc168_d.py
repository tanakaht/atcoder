import sys, math
from collections import deque

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
g = [[] for _ in range(N)]
for a, b in AB:
    g[a-1].append(b-1)
    g[b-1].append(a-1)

q = deque([(0, None)])
appeared = [False]*N
come_from = [None]*N

while q:
    u, p = q.popleft()
    come_from[u] = p
    for v in g[u]:
        if not appeared[v]:
            q.append((v, u))
            appeared[v] = True

print('Yes')
for i in come_from[1:]:
    print(i+1)
