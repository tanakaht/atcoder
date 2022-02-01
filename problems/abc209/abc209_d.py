import sys

N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N-1)]
g=[[] for _ in range(N)]
for a, b in AB:
    g[a-1].append(b-1)
    g[b - 1].append(a - 1)

children = [[] for _ in range(N)]
level = [None]*N
q = [(0, None, 0)]
while len(q) > 0:
    v, p, l = q.pop()
    level[v] = l
    for u in g[v]:
        if u != p:
            q.append((u, v, l+1))
            children[v].append(u)

CD = [list(map(int, input().split())) for _ in range(Q)]
for c, d in CD:
    c -= 1
    d -= 1
    if abs(level[c]-level[d])%2==0:
        print('Town')
    else:
        print('Road')
