N = int(input())
H = list(map(int, input().split()))
MOD = int(1e9+7)
dp = [[0]*N for _ in range(N)] # [0, i]までみて、H[i]をj番目に伐採する切り方
dp[0][0] = 1
for i in range(1, N):
    if H[i-1]>H[i]:
        tmp = 0
        for j in range(min(i, N-1)):
            tmp = (tmp+dp[i-1][j])%MOD
            dp[i][j+1] = tmp
    elif H[i-1]<H[i]:
        tmp = 0
        for j in range(N-1, -1, -1):
            tmp = (tmp+dp[i-1][j])%MOD
            dp[i][j] = tmp
    else:
        tmp = sum(dp[i-1])%MOD
        for j in range(i+1):
            dp[i][j] = tmp
print(sum(dp[-1])%MOD)
