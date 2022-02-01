import math
N = int(input())
APX = [list(map(int, input().split())) for _ in range(N)]
ans = math.inf
for a, p, x in APX:
    if x - a > 0:
        ans = min(ans, p)
if ans == math.inf:
    print(-1)
else:
    print(ans)
