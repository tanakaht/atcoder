import math
import sys

N, K = map(int, input().split())
H = [0]+list(map(int, input().split()))
if K == 0:
    ans = 0
    pre = 0
    for h in H:
        ans += max(0, h - pre)
        pre = h
    print(ans)
    sys.exit()
dp = [[[math.inf]*(K+1) for _ in range(N+1)] for _ in range(N+1)]  # (iまで見た, 直前のインデックス, 使ったk) => 最小の塗り方
dp[0][0][0] = 0
for i in range(1, N + 1):
    for j in range(i):
        for k in range(K + 1):
            dp[i][i][k] = min(dp[i][i][k], dp[i - 1][j][k]+max(0, H[i]-H[j]))
            if k < K:
                dp[i][j][k+1] = dp[i - 1][j][k]
ans = math.inf
for i in range(N + 1):
    ans = min(ans, min(dp[-1][i]))
print(ans)
