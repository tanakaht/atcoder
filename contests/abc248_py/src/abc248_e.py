import sys
import math
from collections import defaultdict
from decimal import Decimal

N, K = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
if K==1:
    print("Infinity")
    sys.exit(0)
appeared = [[False]*N for _ in range(N)]
ans = 0
for i in range(N):
    xi, yi = XY[i]
    for j in range(i+1, N):
        xj, yj = XY[j]
        if appeared[i][j]:
            continue
        tmp_s = set([i, j])
        cnt = 2
        for k in range(j+1, N):
            xk, yk = XY[k]
            flg = (xj-xi)*(yk-yi)==(xk-xi)*(yj-yi)
            if flg:
                cnt += 1
                tmp_s.add(k)
        for s1 in tmp_s:
            for s2 in tmp_s:
                appeared[s1][s2] = True
        ans += (cnt>=K)
print(ans)
