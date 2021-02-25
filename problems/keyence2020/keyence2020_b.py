import math

N = int(input())
XL = [list(map(int, input().split())) for _ in range(N)]
LR = sorted(map(lambda x: (x[0]-x[1], x[0]+x[1]), XL))
safe, used = 0, (-math.inf, 0)
for i, (l, r) in enumerate(LR):
    if used[0] <= l:
        safe, used = used[1], (r, used[1]+1)
    else:
        safe, used = safe, (min(r, used[0]), used[1])
print(used[1])
