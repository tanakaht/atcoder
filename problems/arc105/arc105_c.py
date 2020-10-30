import sys
from itertools import permutations
import math

input = sys.stdin.readline
N, M = map(int, input().split())
W = list(map(int, input().split()))
lv = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[0])[::-1]
lv_filtered = [(math.inf, math.inf)]
pre_v = math.inf
for l, v in lv:
    if v < pre_v:
        lv_filtered.append((l, v))
        pre_v = v
# lv_filtered はlについて降順, vについて降順で並んでいる
lv_filtered.append((0, 0))

def is_ok(i, v):
    return lv_filtered[i][1] < v

def bisect(v):
    ng = 0
    ok = len(lv_filtered)-1
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, v):
            ok = mid
        else:
            ng = mid
    return ok

def min_dist(v):
    idx = bisect(v)
    if idx == 0:
        return 0
    return lv_filtered[idx][0]

ans = math.inf
for perm in permutations(range(N), N):
    anss = []
    pre_ws = []
    for i in perm:
        if min_dist(W[i]) != 0:
            print(-1)
            sys.exit()
        d = 0
        for j, pos in enumerate(anss):
            pre_ws[j] += W[i]
            d = max(d, pos + min_dist(pre_ws[j]))
        pre_ws.append(W[i])
        anss.append(d)
    ans = min(ans, anss[-1])
print(ans)
