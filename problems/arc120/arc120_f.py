N, K, D = map(int, input().split())
A = list(map(int, input().split()))
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


l = N//2
r = N-l-1
base = 0
for i in range(K):
    base = (base+comb(l-i, i)*comb(r-(K-1-i), (K-1-i)))%MOD
l = 2
r = N-l-1
base2 = 0
for i in range(K):
    base2 = (base2+comb(l-i, i)*comb(r-(K-1-i), (K-1-i)))%MOD
# iを取って左にl個右にr個ある=>ptn
def f(l, r):
    l, r = max(l, r), min(l, r)
    if r <= 1:
        return comb(l-(K-1), K-1)
    if r==2:
        return base2
    else:
        return base



    ret = 0
    for i in range(K):
        ret = (ret+comb(l-i, i)*comb(r-(K-1-i), (K-1-i)))%MOD
    return ret

    ret = comb(l+r-(K-1), (K-1))
    if l>0:
        ret = (ret + comb(l+r-(K-1), (K-2)))%MOD
    if r>0 and l>0:
        ret = (ret - comb(l+r-(K-1), (K-2)))%MOD
        ret = (ret + comb(l+r-(K-3), (K-3)))%MOD
    return ret





ans = 0
for i in range(N):
    ans = (ans+A[i]*f(i, N-i-1))%MOD
    # ans = (ans+A[i]*f(max(0, i-1), max(0, N-i-1)))%MOD
print(ans)
