import sys
import math

N, D = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(N)]
destroyed = [False]*N
L_sorted = sorted(enumerate(LR), key=lambda x: x[1][0])
R_sorted = sorted(enumerate(LR), key=lambda x: x[1][1])

ans = 0
lidx, ridx = 0, 0
while ridx<N:
    i, (l, r) = R_sorted[ridx]
    if destroyed[i]:
        ridx += 1
        continue
    ans += 1
    while lidx<N and L_sorted[lidx][1][0] < r+D:
        destroyed[L_sorted[lidx][0]] = True
        lidx += 1
print(ans)
