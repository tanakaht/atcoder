import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N-1)]
px = [list(map(int, input().split())) for _ in range(Q)]
g = [[] for _ in range(N)]
for a, b in ab:
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

children = [[] for _ in range(N)]
parent = [-1]*N
q = [0]
while len(q) > 0:
    v = q.pop()
    for u in g[v]:
        if u != parent[v]:
            parent[u] = v
            children[v].append(u)
            q.append(u)

counter = [0]*N
for p, x in px:
    counter[p - 1] += x

ans = [0]*N
q = [(0, 0)]
while len(q) > 0:
    v, c = q.pop()
    ans[v] = c + counter[v]
    for u in children[v]:
        q.append((u, ans[v]))
print(' '.join(map(str, ans)))
