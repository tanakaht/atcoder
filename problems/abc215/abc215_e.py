N = int(input())
S = input()
MOD = 998244353
dp = [[[0]*(1<<10) for _ in range(10)] for _ in range(N+1)]  # [0, i)文字目まで見て、最後の文字がjで、使ったのがk
chr2idx = {k: v for v, k in enumerate('ABCDEFGHIJ')}
for i in range(N):
    idx = chr2idx[S[i]]
    dp[i+1][idx][1<<idx] = 1
    for j in range(10):
        for k in range(1<<10):
            dp[i+1][j][k] = (dp[i+1][j][k]+dp[i][j][k])%MOD
            if (k>>idx)&1==0:
                dp[i+1][idx][k|(1<<idx)] = (dp[i+1][idx][k|(1<<idx)]+dp[i][j][k])%MOD
            elif j==idx:
                dp[i+1][j][k] = (dp[i+1][j][k]+dp[i][j][k])%MOD
ans = 0
for j in range(10):
    for k in range(1<<10):
        ans = (ans+dp[-1][j][k])%MOD

print(ans)
