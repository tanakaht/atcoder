import sys
import math
from collections import Counter

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
maxA = max(A)
sumA = sum(A)
if K >= maxA*N-sumA:
    print((K+sumA)//N)
    sys.exit(0)

cnt = [0]*(maxA+4)
for a in A:
    cnt[a] += 1
for i in range(1, maxA+4):
    cnt[i] = cnt[i]+cnt[i-1]
ans = 1
for x in range(2, maxA+1):
    c = 0
    for k in range(1, maxA//x+2):
        c += (cnt[min(k*x, maxA+3)]-cnt[(k-1)*x])*k
    if c*x-sumA <= K:
        ans = x

print(ans)
