import sys
import math

N = int(input())
A = list(map(int, input().split()))
minus_cnt = 0
min_abs = math.inf
for a in A:
    minus_cnt += a < 0
    min_abs = min(min_abs, abs(a))

ans = sum(map(abs, A))
if minus_cnt % 2 == 1:
    ans -= 2 * min_abs
print(ans)
