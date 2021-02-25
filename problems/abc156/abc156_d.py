N, a, b = map(int, input().split())
P = int(1e9+7)
# 値が大きくmod Pな時
def comb(n, r):
    if n < r or r < 0:
        return 0
    nume = 1
    deno = 1
    for i in range(1, r + 1):
        nume = (nume * (n - i + 1)) % P
        deno = (deno* i ) % P
    deno_inv = pow(deno, P-2, P)
    return nume*deno_inv%P

ans = (pow(2, N, P) - 1 - comb(N, a) - comb(N, b))%P
print(ans)
