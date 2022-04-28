import sys
import math

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
g = [[] for _ in range(N)]
g_inv = [[] for _ in range(N)]
cnts = [0]*N
for a, b in AB:
    a -= 1
    b -= 1
    g[a].append(b)
    g_inv[b].append(a)
    cnts[a] += 1

q = [u for u in range(N) if cnts[u]==0]
while q:
    u = q.pop()
    for v in g_inv[u]:
        cnts[v] -= 1
        if cnts[v] == 0:
            q.append(v)
print(len([u for u in range(N) if cnts[u]!=0]))
