import sys
import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353
A[0] -= sum(A[1:])+K
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

ans = 1
for a in A:
    ans = (ans*comb(a+K-1, K-1))%MOD
print(ans)
