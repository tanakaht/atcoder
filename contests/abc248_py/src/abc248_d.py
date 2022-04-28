import sys
import math
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
LRX = [map(int, input().split()) for _ in range(Q)]
events = []
for i, (l, r, x) in enumerate(LRX):
    events.append((l-1, 0, x, i))
    events.append((r, 1, x, i))
for i, a in enumerate(A):
    events.append((i+0.5, 2, a, None))
events = sorted(events)
d = defaultdict(int)
anss = [0]*Q
for idx, flg, v, ins in events:
    if flg == 0:
        anss[ins] -= d[v]
    elif flg == 1:
        anss[ins] += d[v]
    elif flg == 2:
        d[v] += 1
print(*anss, sep='\n')
