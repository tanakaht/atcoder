import sys

input = sys.stdin.readline
R, C, K = map(int, input().split())
values = [[0]*C for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, input().split())
    values[r-1][c-1] = v

dp = [[[0 for _ in range(C+1)] for _ in range(R+1)] for _ in range(4)]

for r in range(R-1, -1, -1):
    # dp[0][r][C - 1] = dp[3][r + 1][C - 1]
    # for i in range(1, 4):
    #    dp[i][r][C-1] = dp[3][r + 1][C-1][3]+values[r][C-1]
    for c in range(C-1, -1, -1):
        v = values[r][c]
        for i in range(4):
            if i == 0 or v == 0:
                dp[i][r][c] = max(dp[3][r+1][c], dp[i][r][c+1])
            else:
                dp[i][r][c] = max(dp[3][r + 1][c]+v, dp[i][r][c + 1], dp[i-1][r][c + 1] + v)

print(dp[3][0][0])
