import sys

N = int(input())
S = [input() for _ in range(N)]
dp = [[0]*(N+1) for _ in range(2)] # (is_True, xiまで決めた)=>その個数
dp[0][0] = 1
dp[1][0] = 1
for i in range(1, N+1):
    if S[i-1] == 'AND':
        dp[0][i] = dp[0][i-1]*2 + dp[1][i-1]
        dp[1][i] = dp[1][i-1]
    if S[i-1] == 'OR':
        dp[0][i] = dp[0][i-1]
        dp[1][i] = dp[0][i-1] + dp[1][i-1]*2
print(dp[1][N])
