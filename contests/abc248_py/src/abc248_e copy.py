import sys
import math
from collections import defaultdict

N, K = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
if K==1:
    print("Infinity")
    sys.exit(0)
lines = set()
for i in range(N):
    xi, yi = XY[i]
    for j in range(i+1, N):
        xj, yj = XY[j]
        if xi==xj:
            lines.add((None, None, xi))
        else:
            if xi > xj:
                xi, yi = XY[j]
                xj, yj = XY[i]
            gcd_ = math.gcd(abs(yj-yi), (xj-xi))
            a = (yi-yj)/(xi-xj)
            b = -xi*a+yi
            lines.add(((xj-xi)//gcd_, (yj-yi)//gcd_, b))
line2cnt = defaultdict(int)
eps = 0.000001
for x, y in XY:
    for ax, ay, b in lines:
        if ax is None:
            line2cnt[(ax, ay, x)] += (b==x)
        else:
            flg = 0
            line2cnt[(ax, ay, b)] += flg

ans = 0
for cnt in line2cnt.values():
    ans += (cnt >= K)
print(ans)
