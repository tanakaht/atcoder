N, M = map(int, input().split())
P = 998244353
kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, N+2):
    tmp = (tmp*i) % P
    kaizyo.append(tmp)
    kaizyo_inv.append(pow(tmp, P - 2, P))

def comb(n, r):
    if n < r or n < 0:
        return 0
    elif n == r or r==0:
        return 1
    else:
        return (((kaizyo[n] * kaizyo_inv[r])%P) * kaizyo_inv[n - r])%P


bitlen = len(bin(M))-2
dp = [[0]*(M+1) for _ in range(bitlen+1)] # ibit未満まで使って,和がjでxorが0なもの
dp[0][0] = 1
for i in range(bitlen):
    for j in range(M+1):
        for k in range(M+1):
            to_ = j + (1<<i)*(2*k)
            if to_ > M or 2*k>N:
                break
            dp[i+1][to_] = (dp[i+1][to_]+comb(N, 2*k)*dp[i][j])%P
print(dp[-1][-1])
