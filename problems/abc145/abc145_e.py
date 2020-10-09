N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * T for _ in range(N+1)] for _ in range(2)]  # (i番目の料理までみた, 時刻, 最後の注文決めたか)=>美味しさの最大値
for i in range(N):
    a, b = AB[i]
    for t in range(T):
        if t < a:
            dp[0][i + 1][t] = dp[0][i][t]
            dp[1][i + 1][t] = max(dp[1][i][t], dp[0][i][t] + b)
        else:
            dp[0][i + 1][t] = max(dp[0][i][t], dp[0][i][t - a] + b)
            dp[1][i + 1][t] = max(dp[1][i][t], dp[0][i][t] + b, dp[1][i][t - a] + b)
print(dp[1][-1][-1])
