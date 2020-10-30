import sys
N, M, K = map(int, input().split())
P = 998244353
if M == 1:
    print(int(K >= N - 1))
    sys.exit(0)
# 再利用する時あらかじめN以下の計算しとく
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
    elif n == r or r == 0:
        return 1
    else:
        return (((kaizyo[n] * kaizyo_inv[r]) % P) * kaizyo_inv[n - r]) % P

ans = 0
tmp = M * pow(M - 1, N - 1, P) % P
inv = pow(M - 1, P - 2, P)
for k in range(min(K + 1, N)):
    ans = (ans + tmp * comb(N - 1, k)) % P
    tmp = tmp * inv % P
print(ans)
