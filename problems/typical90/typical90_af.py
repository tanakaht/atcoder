import math

from itertools import permutations

N = int(input())
As = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
XY = [list(map(int, input().split())) for _ in range(M)]
nakawaru = set()
for x, y in XY:
    nakawaru.add((x-1, y-1))
    nakawaru.add((y-1, x-1))

ans = math.inf
for v in permutations(list(range(N))):
    x = None
    ans_ = 0
    for i, y in enumerate(v):
        if (x, y) in nakawaru:
            ans_ = math.inf
            break
        ans_ += As[y][i]
        x = y
    ans = min(ans, ans_)
if ans==math.inf:
    print(-1)
else:
    print(ans)
