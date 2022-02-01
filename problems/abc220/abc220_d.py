import sys

N = int(input())
A = list(map(int, input().split()))
MOD = 998244353
dp = [[0]*10 for _ in range(N)] # [0, i]を消した時、左端がjなもののptn
dp[0][A[0]] = 1
for i in range(1, N):
    a = A[i]
    for j in range(10):
        fidx = (j+a)%10
        gidx = (j*a)%10
        dp[i][fidx] = (dp[i][fidx]+dp[i-1][j])%MOD
        dp[i][gidx] = (dp[i][gidx]+dp[i-1][j])%MOD
print(*dp[-1], sep='\n')
