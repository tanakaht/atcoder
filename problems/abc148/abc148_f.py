import sys
from collections import deque

input = sys.stdin.readline
N, u, v= map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N-1)]

g = [[] for _ in range(N+1)]
for a, b in AB:
    g[a].append(b)
    g[b].append(a)

parent = [-1] * (N + 1)
children = [[] for _ in range(N+1)]
degree = [0] * (N + 1)
q = deque([v])
while len(q) > 0:
    node = q.popleft()
    node_d = degree[node]
    for i in g[node]:
        if i == parent[node]:
            continue
        parent[i] = node
        degree[i] = node_d + 1
        children[node].append(i)
        q.append(i)

ans = 0
# uができるとこまで登
tmp = (degree[u] - 1) // 2
for _ in range(tmp):
    u = parent[u]
max_deg = 0
q = deque([u])
while len(q) > 0:
    node = q.popleft()
    max_deg = max(max_deg, degree[node])
    for i in children[node]:
        q.append(i)
print(max_deg-1)
