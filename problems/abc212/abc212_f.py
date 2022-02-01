import sys
import bisect

N, M, Q = map(int, input().split())
ABST = []
for _ in range(M):
    a, b, s, t = map(int, input().split())
    a -= 1
    b -= 1
    ABST.append((a, b, s, t))
XYZ = []
for _ in range(Q):
    x, y, z = map(int, input().split())
    y -= 1
    XYZ.append((x, y, z))
doubling = [[(None, None)]*M for _ in range(M.bit_length()+1)]
g = [[] for _ in range(N)]
for i, (a, b, s, t) in enumerate(ABST):
    g[a].append((s, t, b, i))
g = [sorted(g[i]) for i in range(N)]

def find_next_edge(t, x, default=None):
    ng, ok = -1, len(g[x])
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if g[x][mid][0] >= t:
            ok = mid
        else:
            ng = mid
    if ok == len(g[x]):
        return default
    else:
        return g[x][ok][-1]

for i in range(M):
    doubling[0][i] = i
    a, b, s, t = ABST[i]
    idx = find_next_edge(t, b, default=i)
    doubling[1][i] = idx
for k in range(1, M.bit_length()):
    for i in range(M):
        doubling[k+1][i] = doubling[k][doubling[k][i]]

for x, y, z in XYZ:
    pre = None
    new = find_next_edge(x, y)
    if new is None:
        print(y+1)
        continue
    a, b, s, t = ABST[new]
    if s >= z:
        print(y+1)
        continue
    elif t >= z:
        print(a+1, b+1)
        continue
    while pre!=new:
        for idx in range(M.bit_length()+1):
            i = doubling[idx][new]
            a, b, s, t = ABST[i]
            if t >= z:
                break
        idx -= 1
        i = doubling[idx][new]
        pre = new
        new = i
    a, b, s, t = ABST[new]
    new = find_next_edge(t, b)
    if new is None or ABST[new][2] >= z:
        print(b+1)
    else:
        a, b, s, t = ABST[new]
        print(a+1, b+1)
