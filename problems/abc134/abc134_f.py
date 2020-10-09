N, K = map(int, input().split())
P = int(1e9+7)
dp=[[[0] * (K + 1) for _ in range(N)] for _ in range(N)]  # (配列のi番目までみた, 奇妙さがj)の個数
dp[0][0][0] = 1
dp[0][1][0] = 1
for i in range(1, N):
    for j in range(N):
        for k in range(K + 1):
            try:
                dp[i][j][k] += (2 * j + 1) * dp[i - 1][j][k - 2 * j]
            except IndexError:
                pass
            try:
                dp[i][j][k] += (j + 1) * (j + 1) * dp[i - 1][j + 1][k - 2 * j]
            except IndexError:
                pass
            try:
                dp[i][j][k] += dp[i-1][j-1][k-2*j]
            except IndexError:
                pass
print(dp)
