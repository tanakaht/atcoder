import sys
import math

N = int(input())
A = list(map(int, input().split()))
dp = [[-math.inf]*(N+1) for _ in range(N+1)] # (k, r)=>揃った数の最大値
dpmax = 0
dpmaxs = [-math.inf]*(N+1)
update_que = []
dp[A[0]][A[1]] = 0
dpmaxs[A[0]] = 0
dpmaxs[A[1]] = 0
ans = 0
for i in range(N-1):
    p, q, r = sorted(A[3*i+2:3*i+5])
    if p != q:
        p, r = r, p
    if p == q == r:
        ans += 1
        continue
    elif p == q:
        for k in range(N+1):
            update_que.append((k, r, max(dp[p][k]+1, dp[k][p]+1)))
    for x, y, z in [[p, q, r], [q, r, p], [r, p, q]]:
        update_que.append((y, z, dp[x][x]+1))
        update_que.append((y, z, dpmax))
        for k in range(N+1):
            update_que.append((k, x, dpmaxs[k]))
    while update_que:
        x, y, v = update_que.pop()
        dp[x][y] = max(dp[x][y], v)
        dpmax = max(dpmax, v)
        dpmaxs[x] = max(dpmaxs[x], v)
        dpmaxs[y] = max(dpmaxs[y], v)

dpmax = max(dpmax, dp[A[-1]][A[-1]]+1)
print(ans+dpmax)
