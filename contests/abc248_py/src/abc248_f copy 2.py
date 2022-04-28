import sys
import math
import numpy as np

N, P = map(int, input().split())
dp = np.zeros((N+1, N+1, 4), dtype=int)
dp[0][0][2] = 1
A1 = np.array([
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 1, 1, 1]
], dtype=int)
A2 = np.array([
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 0],
    [0, 0, 0, 1],
], dtype=int)
A3 = np.array([
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
], dtype=int)
for i in range(N):
    for j in range(N+1):
        dp[i+1][j] = (dp[i+1][j]+A1@dp[i][j])%P
        if j+1>=N+1:
            continue
        dp[i+1][j+1] = (dp[i+1][j+1]+A2@dp[i][j])%P
        if j+2>=N+1:
            continue
        dp[i+1][j+2] = (dp[i+1][j+2]+A3@dp[i][j])%P
ans = [sum(dp[-2][i])%P for i in range(N+1)]
for i in range(N+1):
    ans[i] = (ans[i]+dp[-2][i-1][3])%P

print(*ans[1:-1])
