N, M = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(M)]
edges = []
for l, r in LR:
    l -= 1
    r -= 1
    l, r = min(l, r), max(l, r)
    edges.append((l, r))

edges = sorted(edges)
def is_cross(e1, e2):
    u1, v1 = e1
    u2, v2 = e2
    return u1<u2<v1<v2

ans = 0
for i in range(M):
    for j in range(i+1, M):
        ans = (ans+is_cross(edges[i], edges[j]))
print(ans)
