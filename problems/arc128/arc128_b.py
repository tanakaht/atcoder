import sys
import math

def iter_rotate(iter):
    for i in range(len(iter)):
        yield iter[i:]+iter[:i]

T = int(input())
for _ in range(T):
    R, G, B = map(int, input().split())
    ans = math.inf
    for r, g, b in iter_rotate([R, G, B]):
        if (g-b)%3!=0:
            continue
        ans = min(ans, max(g, b))
    print(ans if ans!=math.inf else -1)
