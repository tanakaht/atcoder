import sys
import math

input = sys.stdin.readline
N, M = map(int, input().split())
ST = [list(map(int, input().split())) for _ in range(M)]
g = [[] for _ in range(N)]
for s, t in ST:
    s -= 1
    t -= 1
    g[s].append(t)

ans = math.inf
for i in range(N):
    Es = [math.inf] * N
    Es[-1] = 0
    for j in range(N - 1, -1, -1):
        tmp = 0
        for t in g[j]:
            tmp += 1+Es[t]
        if i == j and len(g[j])>1:
            tmp -= 1 + max([Es[t] for t in g[j]])
            Es[j] = tmp / (len(g[j]) - 1)
        elif len(g[j]) > 0:
            Es[j] = tmp / len(g[j])
    ans = min(ans, Es[0])

print(ans)
