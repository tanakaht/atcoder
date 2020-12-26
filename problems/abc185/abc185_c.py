L = int(input())
dp = [[0]*(L+1) for _ in range(12)] # i箇所で分割, jの時点で
for j in range(L+1):
    dp[0][j] = 1
for j in range(1, L+1):
    for i in range(1, 12):
        dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

print(dp[11][-2])
