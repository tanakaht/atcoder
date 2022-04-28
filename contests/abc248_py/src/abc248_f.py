import sys
import math

N, P = map(int, input().split())
dp = [[[0]*2 for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1
for i in range(N):
    dp1 = dp[i]
    dp2 = dp[i+1]
    for j in range(N+1):
        dp2[j][1] = (dp2[j][1]+dp1[j][0]*1+dp1[j][1]*1)%P
        if j+1>=N+1:
            continue
        dp2[j+1][0] = (dp2[j+1][0]+dp1[j][0]*3+dp1[j][1]*2)%P
        dp2[j+1][1] = (dp2[j+1][1]+dp1[j][1]*1)%P
        if j+2>=N+1:
            continue
        dp2[j+2][0] = (dp2[j+2][0]+dp1[j][1]*2)%P
ans = [sum(dp[-2][i])%P for i in range(N+1)]
for i in range(N+1):
    ans[i] = (ans[i]+dp[-2][i-1][1])%P


print(*ans[1:-1])
