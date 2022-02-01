import sys
import math

N, M = map(int, input().split())
AB = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: max(x[0], x[1]))
stA = SegmentTree(N+2, segfunc=max, ele=-math.inf)
stB = SegmentTree(N+2, segfunc=max, ele=-math.inf)
stA.update(0, 0)
stB.update(0, 0)
pre_maxab = -1
batch = []
for a, b in AB:
    if max(a, b) > pre_maxab:
        for a_, b_, v_ in batch:
            stA.update(a_, max(v_, stA.get_val(a_)))
            stB.update(b_, max(v_, stB.get_val(b_)))
        batch = []
    if a < b:
        v = stA.query(0, a) + 1
    else:
        v = stB.query(0, b) + 1
    pre_maxab = max(a, b)
    batch.append((a, b, v))
for a_, b_, v_ in batch:
    stA.update(a_, max(v_, stA.get_val(a_)))
    stB.update(b_, max(v_, stB.get_val(b_)))
print(max(stA.query(0, N+1), stA.query(0, N+1)))
