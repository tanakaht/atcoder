import math

N, M, Q = map(int, input().split())
UV = [list(map(int, input().split())) for _ in range(M)]
X = list(map(int, input().split()))
Nsqrt = math.sqrt(N)+1
g = [[] for _ in range(N)]
for a, b in UV:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
g_hab = [[] for _ in range(N)]
for i in range(N):
    for j in g[i]:
        if len(g[j])>Nsqrt:
            g_hab[i].append(j)

status = [(-1, i) for i in range(N)]
hab_updated = [(-1, i) for i in range(N)]
def get(u):
    updated = status[u]
    for v in g_hab[u]:
        if updated[0] < hab_updated[v][0]:
            updated = hab_updated[v]
    return updated[1]

for i, u in enumerate(X):
    u -= 1
    x = get(u)
    if len(g[u]) >= Nsqrt:
        status[u] = (i, x)
        hab_updated[u] = (i, x)
    else:
        status[u] = (i, x)
        for v in g[u]:
            status[v] = (i, x)
ans = []
for u in range(N):
    updated = status[u]
    for v in g[u]:
        if updated[0] < hab_updated[v][0]:
            updated = hab_updated[v]
    ans.append(updated[1]+1)
print(*[get(u)+1 for u in range(N)])
