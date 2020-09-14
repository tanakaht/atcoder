import sys
import math

input = sys.stdin.readline
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
txy = sorted([(math.atan2(y, x), x, y) for x, y in xy])
txy += txy
i = 0
ans = 0
for i in range(N):
    for j in range(i, 2 * N):
        if j - i > N:
            continue
        xs = sum(map(lambda x: x[1], txy[i:j]))
        ys = sum(map(lambda x: x[2], txy[i:j]))
        ans = max(ans, math.sqrt(xs*xs+ys*ys))
print(ans)
