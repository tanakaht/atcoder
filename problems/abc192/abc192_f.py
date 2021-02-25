import math
N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = math.inf
for j in range(1, N+1):
    dp = [[[-math.inf for l in range(j)] for k in range(j+1)] for i in range(N+1)] # (i番目まで見て、k子選んで, %j=lのやつの最大)
    dp[0][0][X%j] = 0
    for i in range(1, N+1):
        a = A[i-1]
        for k in range(1, j+1):
            for l in range(j):
                dp[i][k][l] = max(dp[i-1][k][l], dp[i-1][k-1][(l+a)%j]+a)
    ans = min(ans, (X-dp[N][j][0])//j)

print(ans)
