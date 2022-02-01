import sys

N, M, K = map(int, input().split())
UV = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
MOD = 998244353
dp = [[0]*N for _ in range(K+1)]
dp[0][0] = 1
for k in range(K):
    pre = dp[k]
    presum = sum(pre)%MOD
    new = dp[k+1]
    for i in range(N):
        new[i] = (presum - pre[i])%MOD
    for u, v in UV:
        new[u] = (new[u]-pre[v])%MOD
        new[v] = (new[v]-pre[u])%MOD
print(dp[-1][0])
