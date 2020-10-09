import sys

input = sys.stdin.readline
N = int(input())
uvw = [list(map(int, input().split())) for _ in range(N - 1)]
g = [[] for _ in range(N)]
for a, b, w in uvw:
    g[a-1].append((b-1, w))
    g[b - 1].append((a - 1, w))

children = [[] for _ in range(N)]
colors = [None]*N
q = [(0, None, 0)]  # nodeid, parent, color
while len(q) > 0:
    v, p, c = q.pop()
    colors[v] = c
    for u, w in g[v]:
        if u != p:
            c_ = (c+(w%2))%2
            q.append((u, v, c_))
            children[v].append(u)
for c in colors:
    print(c)
