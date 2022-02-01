import sys
import math

N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]
l_, r_ =  -math.inf, math.inf
for l, r in LR:
    l_ = max(l_, l)
    r_ = min(r_, r)
    ans = max(0, math.ceil((l_-r_)/2))
    print(ans)
