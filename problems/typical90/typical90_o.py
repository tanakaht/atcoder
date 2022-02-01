N = int(input())
mod = int(1e9)+7

# 再利用する時あらかじめN以下の計算しとく
kaizyo = [1]
kaizyo_inv = [1]
tmp = 1
for i in range(1, N+2):
    tmp = (tmp*i) % mod
    kaizyo.append(tmp)
    kaizyo_inv.append(pow(tmp, mod - 2, mod))


def comb(n, r):
    if n < r or n < 0:
        return 0
    elif n == r or r==0:
        return 1
    else:
        return (((kaizyo[n] * kaizyo_inv[r])%mod) * kaizyo_inv[n - r])%mod

for k in range(1, N+1):
    ans = 0
    for i in range(1, 1+(N-1)//k+1):
        ans = (ans+comb(N-(i-1)*(k-1), i))%mod
    print(ans)
