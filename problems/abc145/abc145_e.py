N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * T for _ in range(N + 1)] for _ in range(2)]  # (最後の注文を使ったか, i未満までみた, T)
for i in range(1, N + 1):
    a, b = AB[i-1]
    for t in range(T):
        if t-a>=0:
            dp[0][i][t] = max(dp[0][i - 1][t], dp[0][i - 1][t-a] + b)
        else:
            dp[0][i][t] = dp[0][i - 1][t]
        dp[1][i][t] = max(dp[1][i - 1][t], dp[0][i - 1][t] + b)

print(dp)
print(dp[1][N][T - 1])
