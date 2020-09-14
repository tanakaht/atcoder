import sys

n, k = map(int, input().split())
P = int(1e9+7)


def cmb(n, r, P):
    r = min(r, n - r)
    inv_y = 1
    for i in range(1, r + 1):
        inv_y = (inv_y * i) % P
    inv_y = pow(inv_y, P - 2, P)
    x = 1
    for i in range(n - r + 1, n + 1):
        x = x * i % P
    return (x * inv_y) % P


if k >= n:
    print(cmb(2*n-1, n, P))
    sys.exit()
if k == 1:
    print((n * n - 1) % P)
    sys.exit()
ans = 1
comb1 = 1
comb2 = 1
for i in range(1, k + 1):
    iinv = pow(i, P-2, P)
    comb1 = ((comb1 * (n - i)) * (iinv)) % P
    comb2 = ((comb2 * (n - i + 1)) * (iinv)) % P
    ans = (ans + comb1*comb2) % P
print(ans)
