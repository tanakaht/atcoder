N, M = map(int, input().split())
P = int(1e9+7)
ans=0
# 再利用する時あらかじめN以下の計算しとく
kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, M+1):
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

common = (kaizyo[M] * kaizyo_inv[M - N] * kaizyo_inv[M - N]) % P  # Aの撮り方+Bの余分な会場をわる
for i in range(N + 1):
    tmp = (kaizyo[M-i] * comb(N, i))%P
    ans = (ans + pow(-1, i) * tmp) % P
print(common*ans%P)
