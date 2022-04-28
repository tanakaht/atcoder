import sys
import math

N, M, K = map(int, input().split())
MOD = 998244353
dp = [[0]*(K+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(K+1):
        for k in range(1, M+1):
            j_ = j+k
            if j_>=K+1:
                break
            dp[i+1][j_] = (dp[i+1][j_]+dp[i][j])%MOD
print(sum(dp[-1])%MOD)
