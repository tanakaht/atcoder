import math
import sys

N, K = map(int, input().split())
H = [0] + list(map(int, input().split()))
if K == 0:
    ans = 0
    pre = 0
    for h in H:
        ans += max(0, h - pre)
        pre = h
    print(ans)
    sys.exit()
dp = [[math.inf]*(K+1) for _ in range(N+1)]  # (直前のインデックス, 使ったk) =>　最小
dp[0][0] = 0
for i in range(1, N + 1):
    for j in range(i):
        for k in range(K+1):
            dp[i][k] = min(dp[j][k] + max(0, H[i] - H[j]), dp[i][k])
    for j in range(i):
        for k in range(K-1, -1, -1):
            dp[j][k + 1] = dp[j][k]
        dp[j][0] = math.inf
ans = math.inf
for i in range(N + 1):
    ans = min(ans, min(dp[i]))
print(ans)
