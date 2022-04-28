import sys
import math

N = int(input())
A = list(map(int, input().split()))
d = {i: 0 for i in range(4)}
for a in A:
    d[a] += 1
dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
for i in range(N+1):
    for j in range(N+1):
        for k in range(N+1):
            if (i+j+k)==0:
                continue
            dp[i][j][k] = N/(i+j+k)
            if i>0 and j<N:
                dp[i][j][k] += i/(i+j+k) * dp[i-1][j+1][k]
            if j>0 and k<N:
                dp[i][j][k] += j/(i+j+k) * dp[i][j-1][k+1]
            if k>0:
                dp[i][j][k] += k/(i+j+k) * dp[i][j][k-1]

print(dp[d[3]][d[2]][d[1]])
