import sys

input = sys.stdin.readline
N, M = map(int, input().split())
MOD = 998244353

# 再利用する時あらかじめN以下の計算しとく
kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, N+2):
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
# modごとに
# k!/(k-n)!
# ただし空のグループあり
N1, N1cnt = N//M, M-(N%M)
N2, N2cnt = N//M+1, N%M
available = N2 if N2cnt else N1
anss = [0]*N
for k in range(1, N+1):
    if available > k:
        ans = 0
    else:
        ans = (pow(kaizyo[k]*kaizyo_inv[k-N1], N1cnt, MOD) * pow(kaizyo[k]*kaizyo_inv[k-N2], N2cnt, MOD))%MOD
        for j in range(1, k-1+1):
            ans = (ans-anss[j-1]*(kaizyo[k]*kaizyo_inv[k-j]))%MOD
        ans = (ans*kaizyo_inv[k])%MOD
        # print(pow(kaizyo[k]*kaizyo_inv[k-N1], N1cnt, MOD),  pow(kaizyo[k]*kaizyo_inv[k-N2], N2cnt, MOD), kaizyo[k])
    anss[k-1] = ans
    print(ans)
