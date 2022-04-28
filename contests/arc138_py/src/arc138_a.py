import sys
import math

N, K = map(int, input().split())
A = list(map(int, input().split()))
lefts, rights = [], []
for i, a in enumerate(A[:K][::-1]):
    lefts.append((a, i))
for i, a in enumerate(A[K:]):
    rights.append((a, i))
lefts = sorted(lefts)[::-1]
rights = sorted(rights)[::-1]
right_min = math.inf
r_idx = 0
ans = math.inf
for a, i in lefts:
    while r_idx<N-K and rights[r_idx][0]>a:
        a_, i_ = rights[r_idx]
        right_min = min(right_min, i_)
        r_idx += 1
    ans = min(ans, i+right_min)
if ans == math.inf:
    print(-1)
else:
    print(ans+1)
