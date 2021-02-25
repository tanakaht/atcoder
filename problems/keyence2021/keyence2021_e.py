N = int(input())
A = [0] + list(map(int, input().split())) + [0]

dp = [[[0]*(N+2) for _ in range(N+2)] for _ in range(N+2)] # ((l,r)が取られている, snukeの取れる数)=>ここから取れる最大値
for l in range(N+1):
    for r in range(N+1, l+1, -1):
        for i in range(N+2):
            if i < N+1:
                dp[l+1][r][i+1] = max(dp[l+1][r][i+1], dp[l][r][i]+A[l+1])
                dp[l][r-1][i+1] = max(dp[l][r-1][i+1], dp[l][r][i]+A[r-1])
            if i>=1:
                if A[l+1] > A[r]:
                    dp[l+1][r][i-1] = max(dp[l+1][r][i-1], dp[l][r][i])
                if A[r-1] > A[l]:
                    dp[l][r-1][i-1] = max(dp[l][r-1][i-1], dp[l][r][i])
for i in range(N+1):
    print(dp[i][i+1][1])
