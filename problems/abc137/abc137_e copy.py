import sys
import math

input = sys.stdin.readline
N, M, P = map(int, input().split())
edges = []
g = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b, -(c - P)))
    g[a].append(b)
    g[b].append(a)



d = [math.inf]*N
d[0] = 0
for _ in range(N+1):
    for a, b, c in edges:
        if d[a]+c < d[b]:
            d[b] = d[a]+c
ans = -d[N-1]

# 負閉路を一周してゴールにつくために2N買い回せば十分(ループでN, ゴールでNとか)
infs = []
for _ in range(1):
    for a, b, c in edges:
        if d[a]+c < d[b]:
            d[b] = -math.inf
            infs.append(b)
q = infs
appeared = [False]*N
while q:
    u = q.pop()
    if appeared[u]:
        continue
    appeared[u] = True
    d[u] = -math.inf
    for v in g[u]:
        if not appeared[v]:
            q.append(v)


# 結果が変わっていればゴールにつける負閉路がある
if ans!=-d[N-1]:
    print(-1)
    sys.exit()
print(max(0, -d[N-1]))
