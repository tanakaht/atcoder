import math
N, X = map(int, input().split())
abcd = [map(int, input().split()) for _ in range(N)]
p1, p2 = math.inf, -math.inf
for a, b, c, d in abcd:
    cost = b+(math.ceil(max(0, X-a)/c) + ((X-a)%c==0))*d
    p1, p2 = min(p1, cost), max(p2, cost)
print(p1, p2)
