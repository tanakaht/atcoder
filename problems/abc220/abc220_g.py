import sys
from collections import defaultdict
import math

N = int(input())
XYC = [list(map(lambda x: int(x)*2, input().split())) for _ in range(N)]

stats = []
for i in range(N):
    xi, yi, ci = XYC[i]
    for j in range(i+1, N):
        xj, yj, cj = XYC[j]
        xm, ym = (xi+xj)//2, (yi+yj)//2
        x_diff, y_diff = xi-xj, yi-yj
        if x_diff<0:
            x_diff, y_diff = -x_diff, -y_diff
        gcd_ = math.gcd(x_diff, abs(y_diff))
        x_diff, y_diff = x_diff/gcd_, y_diff/gcd_
        y1 = ym+(-xm)*(-x_diff/y_diff) if y_diff!=0 else xm
        y2 = ym+(-xm)*(y_diff/x_diff) if x_diff!=0 else ym
        stats.append((x_diff, y_diff, y1, y2, ci+cj))
availavle = set()
for x_diff, y_diff, y1, y2, c in stats:
    availavle.add((x_diff, y_diff, y1))
d = {idx: {} for idx in availavle}
for x_diff, y_diff, y1, y2, c in stats:
    d_ = d[x_diff, y_diff, y1]
    d_[y2] = max(d_.get(y2, 0), c)
ans = -1
for d_ in d.values():
    vals = sorted(d_.values())[::-1]
    if len(vals) >= 2:
        ans = max(ans, vals[0]+vals[1])
print(ans//2)
