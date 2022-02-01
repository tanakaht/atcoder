from collections import defaultdict
N, M = map(int, input().split())
XY = sorted([list(map(int, input().split())) for _ in range(M)])
cnts = defaultdict(int)
cnts[N] = 1
pre_i = 0
pre_j = N
pre_v = 0
for x, y in XY:
    if x==pre_i and y==pre_j+1:
        tmp = cnts[y]
        cnts[y] = pre_v + cnts[y+1]
    else:
        tmp = cnts[y]
        cnts[y] = cnts[y-1]+cnts[y+1]
    pre_i, pre_j = x, y
    pre_v = tmp
ans = 0
for v in cnts.values():
    ans += v>0
print(ans)
