import bisect
import math
from itertools import product

N = int(input())
A = list(map(int, input().split()))
A_cusum = [0]*(N+1)
for i in range(N):
    A_cusum[i + 1] = A_cusum[i] + A[i]

ans = math.inf
for i in range(1, N):
    l_i = bisect.bisect(A_cusum, A_cusum[i] // 2)
    r_i = bisect.bisect(A_cusum, (A_cusum[-1] + A_cusum[i]) // 2)
    for l_d, r_d in product([-1, 0], repeat=2):
        p = A_cusum[l_i + l_d]
        q = A_cusum[i] - A_cusum[l_i + l_d]
        r = A_cusum[r_i+r_d] - A_cusum[i]
        s = A_cusum[-1] - A_cusum[r_i+r_d]
        ans = min(ans, max(p, q, r, s) - min(p, q, r, s))

print(ans)
