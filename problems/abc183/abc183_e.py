H, W = map(int, input().split())
S = [[0] * (W+1)] + [[0] + list(map(lambda x:x == '.', input())) for _ in range(H)]
P = int(1e9+7)
dp=[[[0] * (W+1) for _ in range(H+1)] for _ in range(4)]  # (そこで止まる、 左から止めらない、上から止まらない, 左上から止まらない)
dp[0][1][1] = 1
for h in range(1, H+1):
    for w in range(1, W+1):
        if S[h][w] == 0 or (h==1 and w==1):
            continue
        dp[0][h][w] = (dp[0][h - 1][w - 1] + dp[3][h - 1][w - 1] + dp[0][h - 1][w] + dp[2][h - 1][w] + dp[0][h][w - 1] + dp[1][h][w - 1]) % P
        dp[1][h][w] = (dp[0][h][w - 1] + dp[1][h][w - 1]) % P
        dp[2][h][w] = (dp[0][h - 1][w] + dp[2][h - 1][w]) % P
        dp[3][h][w] = (dp[0][h - 1][w - 1] + dp[3][h - 1][w - 1]) % P
print(dp[0][-1][-1])
