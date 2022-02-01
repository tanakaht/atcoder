import sys
import math
from collections import deque

M, N = map(int, input().split())
A = [[i for i in input().split()] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if A[i][j] == 's':
            s = (i, j)
appeared = [[False]*M for _ in range(N)]
appeared[s[0]][s[1]] = True
q = deque([(s[0], s[1], 0)])
while q:
    i, j, d = q.popleft()
    for x_, y_ in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        i_, j_ = i+x_, j+y_
        if (not 0<=i_<N) or (not 0<=j_<M):
            continue
        if A[i_][j_] == 'g':
            print(d+1)
            sys.exit(0)
        elif A[i_][j_] == '0' and (not appeared[i_][j_]):
            q.append((i_, j_, d+1))
            appeared[i_][j_] = True
print('Fail')
