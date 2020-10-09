N = int(input())
A = sorted([(i, int(a)) for i, a in enumerate(input().split())], key=lambda x: x[1])[::-1]
dp = [[0] * (N+1) for _ in range(N+1)]  # 先頭からi+j人使ったときに(左にi人, 右にj人) => 最大の嬉しさ
cnt = 0
for k, a in A:
    for i in range(N):
        j = cnt - i
        if j < 0:
            continue
        # 左に移動
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + a*max(0, k-i))
        # 右に移動
        dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + a * max(0, (N - 1) - j - k))
    cnt += 1
ans = 0
for i in range(N+1):
    ans = max(ans, dp[N-i][i])

print(ans)
