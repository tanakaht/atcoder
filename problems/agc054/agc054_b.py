"""
- とったものをその重さに応じた幅をで数直線上に並べてみる
- これからとった列を復元できる
  - 取れるアイテムはl1<l2<r1が必要で片方しか当てはまらない(=はガバってる)
- とった列と順列が一対一対応になるので、同じ長さに並べる方法を考えればよい


"""
import sys

N = int(input())
W = list(map(int, input().split()))
MOD = 998244353
# 再利用する時あらかじめN以下の計算しとく
kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, N+10):
    tmp = (tmp*i) % MOD
    kaizyo.append(tmp)
    kaizyo_inv.append(pow(tmp, MOD - 2, MOD))





sw = sum(W)
if sw%2!=0:
    print(0)
    sys.exit(0)
dp = [[[0]*(sw//2+1) for _ in range(N+1)] for _ in range(N+1)] # [0, i)をみて、青木がjことった, 青木がkgとった→ptn数
dp[0][0][0] = 1
for i in  range(N):
    for j in range(N):
        for k in range(sw//2+1):
            # ao take
            if k+W[i]<sw//2+1:
                dp[i+1][j+1][k+W[i]] = (dp[i+1][j+1][k+W[i]]+dp[i][j][k])%MOD
            # taka take
            dp[i+1][j][k] = (dp[i+1][j][k]+dp[i][j][k])%MOD

ans = 0
for j in range(N+1):
    ans = (ans+kaizyo[j]*kaizyo[N-j]*dp[-1][j][sw//2])%MOD
print(ans)
