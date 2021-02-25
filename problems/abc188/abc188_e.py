import sys
import math

input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(M)]
g = [[] for _ in range(N)]
for x, y in XY:
    x -= 1
    y -= 1
    g[x].append(y)

dp = [-math.inf]*N # 売れる価格の最大値
ans = -math.inf
for i in range(N-1, -1, -1):
    max_value = -math.inf
    for j in g[i]:
        max_value = max(max_value, dp[j])
    dp[i] = max(max_value, A[i])
    ans = max(ans, max_value-A[i])
print(ans)
