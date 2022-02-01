import sys
import math

N = int(input())
low = -math.inf
high = math.inf
diff = 0
for _ in range(N):
    a, t = map(int, input().split())
    if t == 1:
        diff += a
    elif t == 2:
        if a-diff > high:
            high = a-diff
        low = max(low, a-diff)
    elif t == 3:
        if a-diff < low:
            low = a-diff
        high = min(high, a-diff)

Q = int(input())
X = list(map(int, input().split()))
for x in X:
    if x < low:
        print(low+diff)
    elif x > high:
        print(high+diff)
    else:
        print(x+diff)
