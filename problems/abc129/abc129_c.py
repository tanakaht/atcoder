import sys

input = sys.stdin.readline
N, M = map(int, input().split())
a = set(int(input()) for _ in range(M))
P = int(1e9+7)
ans = 1
dp = [[0]*(N+1) for _ in range(2)]
tmp=0
dp[0][0] = 1
for i in range(1, N + 1):
    if i in a:
        dp[1][i] = (dp[0][i-1]) % P
    else:
        dp[0][i] = (dp[0][i-1] + dp[1][i - 1])%P
        dp[1][i] = (dp[0][i-1])%P
print(dp[0][-1])
