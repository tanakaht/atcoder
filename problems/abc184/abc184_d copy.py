import sys

A, B, C = sorted(map(int, input().split()))


def comb(n, r):
    if n < r or r < 0:
        return 0
    nume = 1
    deno = 1
    for i in range(1, r + 1):
        nume *= (n - i + 1)
        deno *= (i)
    return nume//deno

def n2r(n, r):
    ret = 1
    for i in range(r, n + 1):
        ret *= i
    return ret


if A == 0 and B == 0:
    print(100 - C)
    sys.exit()
elif A == 0:
    ans = 0
    b = 100
    for c in range(C, 100):
        cnt = b - B + c - C
        prob = n2r(b - 1, B) * n2r(c - 1, C)
        prob /= n2r(b+c - 1, B + C)
        prob *= comb(cnt-1, b - B-1)
        ans += cnt * prob
    c = 100
    for b in range(B, 100):
        cnt = b - B + c - C
        prob = n2r(b - 1, B) * n2r(c - 1, C)
        prob /= n2r(b+c - 1, B + C)
        prob *= comb(cnt-1, c - C-1)
        ans += cnt * prob
    print(ans)
    sys.exit()

ans = 0
rot = [(A, B, C), (B, C, A), (C, B, A)]
for A, B, C in rot:
    a = 100
    for b in range(B, 100):
        for c in range(C, 100):
            cnt = a - A + b - B + c - C
            prob = n2r(a - 1, A)
            prob *= n2r(b - 1, B)
            prob *= n2r(c - 1, C)
            prob /= n2r(a+b+c - 1, A + B + C)
            prob *= comb(cnt-1, a - A-1)
            prob *= comb(cnt - (a - A), b - B)
            ans += cnt * prob
print(ans)
