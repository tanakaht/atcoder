import sys
import math

input = sys.stdin.readline
N = int(input())
xyd = [input().split() for _ in range(N)]
p = {k: [math.inf, -1*math.inf] for k in 'RLUD_'}
for x, y, d in xyd:
    x = int(x)
    y = int(y)
    if d in 'RL':
        a = x
        b = y
    else:
        a = y
        b = x
    p[d][0] = min(p[d][0], a)
    p[d][1] = max(p[d][0], a)
    p['_'][0] = min(p['_'][0], b)
    p['_'][1] = max(p['_'][1], b)
print(p)
