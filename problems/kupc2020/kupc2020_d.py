import sys
import heapq
import math
from collections import deque

N = int(input())
if N == 2:
    print('impossible')
    sys.exit(0)
if N % 2 == 0:
    print(N // 2)
    for i in range(N // 2):
        print(f'2 {1+2*i} {2*N-1-2*i}')
    sys.exit(0)

for f in range(2, int(math.sqrt(N))+1):
    if N % f != 0:
        continue
    print(f)
    anss = [[] for _ in range(f)]
    for i in range(f):
        tmp = i
        for j in range(f):
            anss[i].append(2 * (f * j + tmp) + 1)
            tmp = (tmp + 1) % f
    rest = deque(range(2*f * f + 1, 2 * N, 2))
    while len(rest) > 0:
        for i in range(f):
            anss[i].append(rest.pop())
            anss[i].append(rest.popleft())
    for ans in anss:
        print(f'{len(ans)} {" ".join(map(str, ans))}')
    sys.exit(0)

print('impossible')
