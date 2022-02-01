import sys
K = int(input())
MOD = int(1e9+7)
if K%9!=0:
    print(0)
    sys.exit(0)
dp = [0]*(K+1)
dp[0] = 1
cur = 1
for i in range(1, K+1):
    dp[i] = cur
    if i>=9:
        cur -= dp[i-9]
    cur = (cur + dp[i])%MOD
print(dp[-1])
