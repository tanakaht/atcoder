import sys
import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353
A[0] -= sum(A[1:])
if A[0]<0:
    print(0)
    sys.exit(0)

# 値が大きくmod MODな時
def comb(n, r):
    if n < r or r < 0:
        return 0
    nume = 1
    deno = 1
    for i in range(1, r + 1):
        nume = (nume * (n - i + 1)) % MOD
        deno = (deno* i ) % MOD
    deno_inv = pow(deno, MOD-2, MOD)
    return nume*deno_inv%MOD

ans = 0
for i in range(K):
    if K-i>A[0]:
        continue
    tmpans = 1
    # i個の入れない箱を決める
    tmpans *= comb(K, i)
    # A[1:]をa[0]とセットで詰める
    for a in A[1:]:
        tmpans = (tmpans*comb(a+(K-i)-1, (K-i)-1))%MOD
    # A[0]を詰める
    tmpans = (tmpans*comb((A[0]-(K-i))+K-1, K-i))%MOD
    # 幇助でansにたす
    ans = (ans+tmpans*pow(-1, i+1))%MOD
print(ans)
