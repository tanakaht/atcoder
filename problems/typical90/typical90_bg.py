import sys
from collections import defaultdict

N, M, Q = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(M)]
AB = [list(map(int, input().split())) for _ in range(Q)]
g = [[] for _ in range(N)]
n_bit = 1024*16-1
queries = [defaultdict(list) for _ in range(N)]
for x, y in XY:
    g[x-1].append(y-1)
anss = [None]*Q
for i, (a, b) in enumerate(AB):
    queries[a-1][(b-1)//n_bit].append(((b-1)%n_bit, i))
for sep in range(1+(N-1)//n_bit):
    dp = [0 for i in range(N)]
    for u in range(N-1, -1, -1):
        val = 0
        if sep*n_bit<=u<(sep+1)*n_bit:
            val = 1<<(u%n_bit)
        for v in g[u]:
            val |= dp[v]
        dp[u] = val
        for v, i in queries[u][sep]:
            anss[i] = 'Yes' if (val>>(v%n_bit))&1 else 'No'
print(*anss, sep='\n')
