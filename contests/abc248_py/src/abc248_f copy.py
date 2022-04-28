import sys
import math

N, P = map(int, input().split())
dp = [[[0]*4 for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][2] = 1
for i in range(N):
    for j in range(N+1):
        dp[i+1][j][0] = (dp[i+1][j][0]+dp[i][j][0]*0+dp[i][j][1]*0+dp[i][j][2]*0+dp[i][j][3]*0)%P
        dp[i+1][j][1] = (dp[i+1][j][1]+dp[i][j][0]*0+dp[i][j][1]*0+dp[i][j][2]*0+dp[i][j][3]*0)%P
        dp[i+1][j][2] = (dp[i+1][j][2]+dp[i][j][0]*0+dp[i][j][1]*0+dp[i][j][2]*0+dp[i][j][3]*0)%P
        dp[i+1][j][3] = (dp[i+1][j][3]+dp[i][j][0]*1+dp[i][j][1]*1+dp[i][j][2]*1+dp[i][j][3]*1)%P
        if j+1>=N+1:
            continue
        dp[i+1][j+1][0] = (dp[i+1][j+1][0]+dp[i][j][0]*1+dp[i][j][1]*1+dp[i][j][2]*1+dp[i][j][3]*1)%P
        dp[i+1][j+1][1] = (dp[i+1][j+1][1]+dp[i][j][0]*1+dp[i][j][1]*1+dp[i][j][2]*1+dp[i][j][3]*1)%P
        dp[i+1][j+1][2] = (dp[i+1][j+1][2]+dp[i][j][0]*1+dp[i][j][1]*1+dp[i][j][2]*1+dp[i][j][3]*0)%P
        dp[i+1][j+1][3] = (dp[i+1][j+1][3]+dp[i][j][0]*0+dp[i][j][1]*0+dp[i][j][2]*0+dp[i][j][3]*1)%P
        if j+2>=N+1:
            continue
        dp[i+1][j+2][0] = (dp[i+1][j+2][0]+dp[i][j][0]*0+dp[i][j][1]*0+dp[i][j][2]*0+dp[i][j][3]*1)%P
        dp[i+1][j+2][1] = (dp[i+1][j+2][1]+dp[i][j][0]*0+dp[i][j][1]*0+dp[i][j][2]*0+dp[i][j][3]*1)%P
        dp[i+1][j+2][2] = (dp[i+1][j+2][2]+dp[i][j][0]*0+dp[i][j][1]*0+dp[i][j][2]*0+dp[i][j][3]*0)%P
        dp[i+1][j+2][3] = (dp[i+1][j+2][3]+dp[i][j][0]*0+dp[i][j][1]*0+dp[i][j][2]*0+dp[i][j][3]*0)%P
ans = [sum(dp[-2][i])%P for i in range(N+1)]
for i in range(N+1):
    ans[i] = (ans[i]+dp[-2][i-1][3])%P


print(*ans[1:-1])
