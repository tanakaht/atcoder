from collections import defaultdict
import sys
from collections import defaultdict

input = sys.stdin.readline
H, W, N = map(int, input().split())
RCA = [list(map(int, input().split())) for _ in range(N)]
hmax, wmax = [-1]*H, [-1]*W
ans = [None]*N
a2rcs = defaultdict(list)
for i, (r, c, a) in enumerate(RCA):
    r -= 1
    c -= 1
    a2rcs[a].append((r, c, i))
anss = [None]*N
for a, l in sorted(a2rcs.items())[::-1]:
    updates = []
    for r, c, i in l:
        v = max(hmax[r], wmax[c])+1
        updates.append((r, c, v))
        anss[i] = v
    for r, c, v in updates:
        hmax[r] = max(hmax[r], v)
        wmax[c] = max(wmax[c], v)
print(*anss, sep='\n')
