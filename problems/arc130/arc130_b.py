import sys
import math
from collections import defaultdict

H, W, C, Q = map(int, input().split())
Qs = [list(map(int, input().split())) for _ in range(Q)]
isUsed_H = defaultdict(lambda : False)
isUsed_W = defaultdict(lambda : False)
hcnt, wcnt = H, W
anss = [0]*C
for t, n, c in Qs[::-1]:
    c -= 1
    n -= 1
    if t == 1:
        if isUsed_H[n]:
            continue
        anss[c] += wcnt
        hcnt -= 1
        isUsed_H[n] = True
    else:
        if isUsed_W[n]:
            continue
        anss[c] += hcnt
        wcnt -= 1
        isUsed_W[n] = True
print(*anss)
