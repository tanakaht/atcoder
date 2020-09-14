import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
ab = [list(map(int, input().split())) for _ in range(N - 1)]
edge_colors = [0]*(N-1)
g = [[] for _ in range(N)]
for i, (a, b) in enumerate(ab):
    a -= 1
    b -= 1
    g[a].append((b, i))
    g[b].append((a, i))

q = deque([(0, 0)])
visited = [False] * N
visited[0] = True
while len(q) > 0:
    node, color = q.popleft()
    i = 1
    for v, edgeid in g[node]:
        if visited[v]:
            continue
        if i == color:
            i += 1
        visited[v] = True
        q.append((v, i))
        edge_colors[edgeid] = i
        i += 1


print(max(edge_colors))
for c in edge_colors:
    print(c)
