import math
import sys

N = int(input())
X, Y = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
dp = [[-math.inf]*(301) for _ in range(N+1)] # iこ使って、xこな時のyの最大
dp[0][0] = 0
for a, b in AB:
    for i in range(N-1, -1, -1):
        for x in range(301):
            x_ = min(300, x+a)
            dp[i+1][x_] = max(dp[i+1][x_], dp[i][x]+b)
for i in range(N+1):
    for x in range(X, 301):
        if dp[i][x]>=Y:
            print(i)
            sys.exit(0)
print(-1)
