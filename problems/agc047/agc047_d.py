from cmath import rect
from math import tau
n = int(input())
a, b = [0], [0]
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

# a = 0 + a1x + a2x^2 + ... + anx^n + 0x^(n+1) + ... + 0x^(m-1)
m = 1
while not 2 * n <= m - 1:
    m *= 2
for _ in range(m - 1 - n):
    a.append(0)
    b.append(0)

def fft(a, n):
    if n == 1:
        return a
    a0, a1 = (fft(a[i::2], n // 2) for i in range(2))
    zeta = rect(1, tau / n)
    x = 1
    ret = a0 * 2
    for i, f in enumerate(a1):
        ret[i] += x * f
        ret[i + n // 2] += -x * f
        x *= zeta
    return ret

def ifft(a, n):
    if n == 1:
        return a
    a0, a1 = (ifft(a[i::2], n // 2) for i in range(2))
    zeta = rect(1, -tau / n)
    x = 1
    ret = a0 * 2
    for i, f in enumerate(a1):
        ret[i] += x * f
        ret[i + n // 2] += -x * f
        x *= zeta
    return ret

fa = fft(a, m)
fb = fft(b, m)
fc = [x * y for x, y in zip(fa, fb)]

c = ifft(fc, m)
ans = [int((x / m).real + 0.5) for x in c[1:2*n+1]]
print(*ans, sep='\n')
