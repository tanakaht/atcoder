import math

N, M = map(int, input().split())
AC = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[1])
ans = 0
for a, c in AC:
    gcd_ = math.gcd(N, a)
    if N>gcd_:
        ans += c*(N-gcd_)
        N = gcd_
if N!=1:
    print(-1)
else:
    print(ans)
