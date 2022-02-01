import sys
from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
appeared = defaultdict(list)
for i in range(N):
    appeared[A[i]].append(i)
for i in range(N+1):
    appeared[i].append(N)
    pre = -1
    for j in appeared[i]:
        if j - pre -1 >= M:
            print(i)
            sys.exit(0)
        pre = j
