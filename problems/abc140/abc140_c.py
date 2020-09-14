import sys
import math
N = int(input())
B = list(map(int, input().split()))
pre = math.inf
ans = 0
for b in B:
    ans += min(pre, b)
    pre = b
ans += B[-1]
print(ans)
