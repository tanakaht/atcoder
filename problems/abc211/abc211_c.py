S = input()
MOD = int(1e9+7)
target = 'chokudai'
dp = [[0]*(len(target)+1) for _ in range(len(S)+1)]
dp[0][0] = 1
for i in range(1, len(S)+1):
    for j in range((len(target)+1)):
        dp[i][j] = (dp[i][j] + dp[i-1][j])%MOD
        if j>0 and S[i-1]==target[j-1]:
            dp[i][j] = (dp[i][j] + dp[i-1][j-1])%MOD
print(dp[-1][-1])
