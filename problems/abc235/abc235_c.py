import sys
from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))
xk = [list(map(int, input().split())) for _ in range(Q)]
d = defaultdict(list)
for i, a in enumerate(A):
    d[a].append(i)

for x, k in xk:
    if len(d[x])<k:
        print(-1)
    else:
        print(d[x][k-1]+1)

