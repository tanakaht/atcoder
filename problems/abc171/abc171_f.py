K = int(input())
S = input()
P = int(1e9+7)

# 再利用する時あらかじめN以下の計算しとく
kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, K+len(S)+2):
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
base = pow(25, K, P)
update = 26 * pow(25, P - 2, P) % P
for i in range(K + 1):  # Sの最後に何もじたすか
    ans = (ans + base * comb(len(S) + K - i - 1, len(S) - 1)) % P
    base = base * update % P
print(ans)
