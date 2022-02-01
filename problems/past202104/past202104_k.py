import sys
import math

N = int(input())
PU = [list(map(int, input().split())) for _ in range(N)]
dp = [[-math.inf]*100 for _ in range(N+1)] # i未満までみて、あまりjの時の最高スコア
dp[0][0] = 0
for i, (p, u) in enumerate(PU):
    for j in range(100):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        dp[i+1][(j+p)%100] = max(dp[i+1][(j+p)%100], dp[i][j]+u-p+((j+p)//100)*20)
print(max(dp[-1]))
