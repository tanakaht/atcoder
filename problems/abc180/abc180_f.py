N, M, L = map(int, input().split())
P = int(1e9+7)

kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, N+1):
    tmp = (tmp*i) % P
    kaizyo.append(tmp)
    kaizyo_inv.append(pow(tmp, P - 2, P))

pow2_inv = [1]
tmp = 1
for i in range(1, N+2):
    tmp = (tmp*2) % P
    pow2_inv.append(pow(tmp, P - 2, P))

def comb(n, r):
    if n < r or n < 0:
        return 0
    elif n == r or r == 0:
        return 1
    else:
        return (((kaizyo[n] * kaizyo_inv[r]) % P) * kaizyo_inv[n - r]) % P

def solve(L):
    # N頂点確定,Mへん使ったグラフ数
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for n in range(N + 1):
        for m in range(M + 1):
            # パス
            for l in range(1, L + 1):
                if n + l > N or m + l - 1 > M:
                    break
                ptn = comb(N - n - 1, l - 1) * kaizyo[l] % P
                if l != 1:
                    ptn = ptn * pow2_inv[1] % P
                ptn = ptn*dp[n][m]%P
                dp[n + l][m + l - 1] = (dp[n + l][m + l - 1] + ptn) % P
            # サイクル
            for l in range(2, L + 1):
                if n + l > N or m + l > M:
                    break
                ptn = comb(N - n - 1, l - 1) * kaizyo[l-1] % P
                if l != 2:
                    ptn = ptn * pow2_inv[1] % P
                ptn = ptn*dp[n][m] % P
                dp[n + l][m + l] = (dp[n + l][m + l] + ptn) % P
    return dp[-1][-1]

print((solve(L)-solve(L-1))%P)
