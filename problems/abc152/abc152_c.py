import math

N = int(input())
P = list(map(int, input().split()))

min_ = math.inf
ans = 0
for p in P:
    ans += p <= min_
    min_ = min(min_, p)
print(ans)
