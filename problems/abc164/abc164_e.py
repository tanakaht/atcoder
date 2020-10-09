import sys
import heapq
import math

input = sys.stdin.readline
N, M, S = map(int, input().split())
UVAB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(N)]
n_state = 3000 # 2500以上の状態で交換する必要なし
g = [[] for _ in range(N*n_state)] # (街id*n_state+金) => (行先, かかる時間)のlist

for u, v, a, b in UVAB:
    u -= 1
    v -= 1
    for i in range(n_state):
        if i >= a:
            g[u*n_state+i].append((v*n_state+i-a, b))
            g[v*n_state+i].append((u*n_state+i-a, b))

for u, (c, d) in enumerate(CD):
    for i in range(n_state):
        if i + c < n_state:
            g[u * n_state + i].append((u * n_state + i + c, d))

hq = [(0, min(S, n_state-1))] # (時間, 頂点id)
visited = [False] * N * n_state
ans = [math.inf] * (N) * n_state
ans[min(S, n_state-1)] = 0
while len(hq) > 0:
    t, u = heapq.heappop(hq)
    if visited[u]:
        continue
    ans[u] = t
    visited[u] = True
    for v, cost in g[u]:
        if not visited[v]:
            heapq.heappush(hq, (t + cost, v))

for i in range(1, N):
    print(min(ans[i*n_state:(i+1)*n_state]))
