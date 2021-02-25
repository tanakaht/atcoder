from operator import mul
from functools import reduce


def combinations_count(n, r, P):
    r = min(r, n - r)
    inv_y = 1
    for i in range(1, r + 1):
        inv_y = (inv_y * i) % P
    inv_y = pow(inv_y, P - 2, P)
    x = 1
    for i in range(n - r + 1, n + 1):
        x = x * i % P
    return (x * inv_y) % P



n, a, b = map(int, input().split())
P = int(1e9+7)
ans = pow(2, n, P) - 1  # 1本以上の花束の種類


ans = (ans - combinations_count(n, a, P))
ans = (ans - combinations_count(n, b, P))
print(ans%P)
