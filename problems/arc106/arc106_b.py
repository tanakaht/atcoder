import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cd = [list(map(int, input().split())) for _ in range(M)]
g = [[] for _ in range(N)]
for c, d in cd:
    c -= 1
    d -= 1
    g[c].append(d)
    g[d].append(c)
appeared = [False] * N
idx = 0
while idx < N:
    if appeared[idx]:
        idx += 1
        continue
    asum, bsum = 0, 0
    q = [idx]
    while len(q) > 0:
        u = q.pop()
        if appeared[u]:
            continue
        asum += A[u]
        bsum += B[u]
        appeared[u] = True
        for v in g[u]:
            q.append(v)
    if asum != bsum:
        print('No')
        sys.exit(0)
print('Yes')
