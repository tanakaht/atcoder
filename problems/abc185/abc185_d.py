import sys
from collections import defaultdict, Counter
import math

N, M = map(int, input().split())
A = sorted(list(map(int, input().split()))+[N+1])
if M==N:
    print(0)
    sys.exit(0)

diffs = []
pre = 0
min_diff = N
for a in A:
    diffs.append(a-pre-1)
    if a-pre-1 != 0:
        min_diff = min(min_diff, a-pre-1)
    pre = a
ans = 0
for diff in diffs:
    ans += math.ceil(diff/min_diff)
print(ans)
