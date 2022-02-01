import sys
import math

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
dp = [[-math.inf]*(W+1) for _ in range(H+1)]
dp[1][1] = 1
ans = 0
for h in range(H):
    for w in range(W):
        if C[h][w]=="#":
            continue
        dp[h+1][w+1] = max(dp[h+1][w+1], dp[h][w+1]+1, dp[h+1][w]+1)
        ans = max(ans, dp[h+1][w+1])
print(ans)
