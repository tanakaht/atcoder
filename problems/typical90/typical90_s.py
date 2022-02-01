import math
N = int(input())
A = list(map(int, input().split()))
dp = [[math.inf]*(2*N+1) for _ in range(2*N)] # [l, r)のコストの最小値
for i in range(2*N):
    dp[i][i] = 0
for l in range(2*N-1, -1, -1):
    for r in range(l+1, 2*N+1):
        if (r-l)%2==1:
            continue
        dp[l][r] = dp[l+1][r-1]+abs(A[l]-A[r-1])
        for m in range(l, r):
            dp[l][r] = min(dp[l][r], dp[l][m] + dp[m][r])
print(dp[0][-1])
