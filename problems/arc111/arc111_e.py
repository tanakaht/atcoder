import sys
import math

input = sys.stdin.readline

 # sum_{i = 0}^{n - 1} {floor((a*i+b)/m)}
def floor_sum(n: int, m: int, a: int, b: int) -> int:
    assert 1 <= n
    assert 1 <= m
    ans = 0
    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m
    if b >= m:
        ans += n * (b // m)
        b %= m
    y_max = (a * n + b) // m
    x_max = y_max * m - b
    if y_max == 0:
        return ans
    ans += (n - (x_max + a - 1) // a) * y_max
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)
    return ans


T = int(input())
for _ in range(T):
    A, B, C, D = map(int, input().split())
    tmp = B//D
    A %= D
    B -= tmp*D
    C -= tmp*D
    N = (D-2)//(C-B)
    if N == 0:
        print(0)
        continue
    ans = N - (floor_sum(N+1, D, C, A) - floor_sum(N+1, D, B, A-1))
    print(ans)
