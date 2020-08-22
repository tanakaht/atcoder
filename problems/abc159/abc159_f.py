import sys
input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))
P = 998244353
dp = [[[0 for _ in range(3)] for _ in range(S+1)] for _ in range(N+1)]

dp[0][0][0] = 1
for i in range(N):
    for s in range(S+1):
        a = A[i]
        dp[i+1][s][0] = dp[i][s][0]
        dp[i+1][s][1] = (dp[i+1][s][1] + dp[i][s][0] + dp[i][s][1]) % P
        dp[i+1][s][2] = (dp[i+1][s][2] + dp[i][s][0] + dp[i][s][1] + dp[i][s][2]) % P
        if s+a <= S:
            dp[i+1][s+a][1] = (dp[i][s][0] + dp[i][s][1]) % P
            dp[i+1][s+a][2] = (dp[i][s][0] + dp[i][s][1]) % P

ans = dp[N][S][2]
print(ans%P)
