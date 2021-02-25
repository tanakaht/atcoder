import sys
import heapq
import math

input = sys.stdin.readline
N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
C = list(map(lambda x: int(x)-1, input().split()))
g = [[] for _ in range(N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

dists = [[math.inf]*N for _ in range(K)] # C[k]から各店への距離
for i in range(K):
    q = [(0, C[i])]
    dists[i][C[i]] = 0
    while q:
        d, u = heapq.heappop(q)
        for v in g[u]:
            if dists[i][v] != math.inf:
                continue
            dists[i][v] = d+1
            heapq.heappush(q, (d+1, v))


ans = math.inf
dp = [[math.inf]*pow(2, K) for _ in range(K)] # 右端, 満たした状態
for k in range(K):
    dp[k][1<<k] = 1
for bit in range(pow(2, K)):
    for right in range(K):
        if not (bit & (1<<right)):
            continue
        v = dp[right][bit]
        for right_ in range(K):
            dp[right_][bit|(1<<right_)] = min(dp[right_][bit|(1<<right_)], dists[right][C[right_]] + v)

ans = math.inf
for k in range(K):
    ans = min(dp[k][-1], ans)
if ans != math.inf:
    print(ans)
else:
    print(-1)
