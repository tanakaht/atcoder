N, K = map(int, input().split())
P = int(1e9+7)

# 再利用する時あらかじめN以下の計算しとく
kaizyo = [0]
kaizyo_inv = [0]
tmp = 1
for i in range(1, N+2):
    tmp = (tmp*i) % P
    kaizyo.append(tmp)
    kaizyo_inv.append(pow(tmp, P - 2, P))


def comb(n, r):
    if n < r or n < 0:
        return 0
    elif n == r or r == 0:
        return 1
    else:
        return kaizyo[n] * kaizyo_inv[r] * kaizyo_inv[n - r]

for i in range(1, K + 1):
    print((comb(K - 1, i - 1) * comb(N - K + 1, i)) % P)
