import math
from functools import reduce


N = int(input())
A = list(map(int, input().split()))
P = int(1e9+7)

def lcm_base(x, y):
    ret = (x * y) // math.gcd(x, y)
    return ret


def lcm(iter):
    return reduce(lcm_base, iter, 1)


lcm_a = lcm(A) % P
ans = 0
for a in A:
    a_inv = pow(a, P-2, P)
    ans = (ans + lcm_a*a_inv) %P
print(ans)
