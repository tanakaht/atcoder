import sys

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
MOD = 998244353
g = [[] for _ in range(2*N)]
for a, b in AB:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, 2*N+2):
    tmp = (tmp*i) % MOD
    kaizyo.append(tmp)
    kaizyo_inv.append(pow(tmp, MOD - 2, MOD))

def comb(n, r):
    if n < r or n < 0:
        return 0
    elif n == r or r==0:
        return 1
    else:
        return (((kaizyo[n] * kaizyo_inv[r])%MOD) * kaizyo_inv[n - r])%MOD


dp = [[0]*(2*N+1) for _ in range(2*N+1)]  # [l, r)→パターン数
for i in range(2*N+1):
    dp[i][i] = 1
for l in range(2*N-1, -1, -1):
    for r in range(l+2, 2*N+1, 2):
        cnt = 0
        for m in g[l]:
            if m < r:
                cnt = (cnt+dp[l+1][m]*dp[m+1][r]*comb((r-l)//2, (r-m)//2))%MOD
        dp[l][r] = cnt
print(dp[0][-1])
