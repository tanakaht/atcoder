import sys

X, Y = map(int, input().split())
P = int(1e9+7)
if (X + Y) % 3 != 0:
    print(0)
    sys.exit()
N = (X + Y) // 3
X -= N
Y -= N
if X < 0 or Y < 0:
    print(0)
    sys.exit()

# 値が大きくmod Pな時
def comb(n, r):
    if n < r or r < 0:
        return 0
    nume = 1
    deno = 1
    for i in range(1, r + 1):
        nume = (nume * (n - i + 1)) % P
        deno = (deno * i) % P
    deno_inv = pow(deno, P-2, P)
    return nume*deno_inv%P

print(comb(X + Y, X))
