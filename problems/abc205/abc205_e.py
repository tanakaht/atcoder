import sys

N, M, K = map(int,input().split())
MOD = 10**9+7
if N-M>K:
    print(0)
    sys.exit(0)

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

ans=(comb(N+M, N)-comb(N+M, K+M+1))%MOD
print(ans)
