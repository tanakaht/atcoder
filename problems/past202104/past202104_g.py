import sys
import heapq

N, M, Q = map(int, input().split())
ABC = [list(map(int, input().split())) for _ in range(M)]
X = list(map(int, input().split()))
g = [[] for _ in range(N)]
for a, b, c in ABC:
    a -= 1
    b -= 1
    g[a].append((c, b))
    g[b].append((c, a))

q = [(c, i) for c, i in g[0]]
appeared = [False]*N
appeared[0] = True
ans = 1
heapq.heapify(q)
for i in range(Q):
    tmps = set()
    while q and q[0][0] <= X[i]:
        _, u = heapq.heappop(q)
        if appeared[u]:
            continue
        tmps.add(u)
        appeared[u] = True
        ans += 1
    for u in tmps:
        for c, v in g[u]:
            if not appeared[v]:
                heapq.heappush(q, (c, v))
    print(ans)
