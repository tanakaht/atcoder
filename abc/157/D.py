import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
ABs = [tuple(map(int, input().split())) for _ in range(M)]
CDs = [tuple(map(int, input().split())) for _ in range(K)]
graph = {i+1: set() for i in range(N)}
block = {i+1: set() for i in range(N)}
ans = {i+1: 0 for i in range(N)}
root = {i+1: i+1 for i in range(N)}


for a, b in ABs:
    graph[a].add(b)
    graph[b].add(a)
    while a != root[a]:
        a = root[a]
    while b != root[b]:
        b = root[b]
    root[a] = min(a, b)
    root[b] = min(a, b)
for c, d in CDs:
    block[c].add(d)
    block[d].add(c)
for connected in connected_components(graph):
    for c in connected:
        ans[c] = len(connected - (graph[c] | block[c]))
for i in range(1, N+1):
    print(ans[i]-1, end=' ')
