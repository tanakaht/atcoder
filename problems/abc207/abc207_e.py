N = int(input())
A = list(map(int, input().split()))
MOD = int(10**9+7)
dp = [[0]*(N+1) for _ in range(N+1)] # [0, i)をみて、j個の組を作った
dp[0][0] = 1
for k in range(1, N+1):
    cnts = [0]*k
    cur = 0
    cnts[0] = dp[0][k-1]
    for i in range(N):
        cur = (cur+A[i])%k
        dp[i+1][k] = (dp[i+1][k]+cnts[cur])%MOD
        cnts[cur] = (cnts[cur]+dp[i+1][k-1])%MOD

ans = 0
for x in dp[-1]:
    ans = (ans+x)%MOD
print(ans)
