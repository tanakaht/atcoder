import sys

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
g=[set([i]) for i in range(N)]
for a, b in AB:
    g[a-1].add(b-1)
    g[b - 1].add(a - 1)

g_inv = [set() for _ in range(N)]
base = set(range(N))
for i in range(N):
    g_inv[i] = base-g[i]

fs = [None]*pow(2, N)
fs[0] = 0
for i in range(1, pow(2, N)):
    if not fs[i] is None:
        continue
    bs = set()
    for b in range(N):
        if i>>b&1:
            bs.add(b)
    found = False
    for b in bs:
        if len(g_inv[b].intersection(bs))>=1:
            found = True
            break
    if not found:
        fs[i] = 1
        continue
    tmp = N
    t = i
    while (t-1)&i > 0:
        t = (t-1)&i
        s_t = i^t
        tmp = min(tmp, fs[t]+fs[s_t])
    fs[i] = tmp
print(fs[-1])
