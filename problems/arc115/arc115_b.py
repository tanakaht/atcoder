import sys
import math

N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]
min_, minidx = math.inf, -1
for i, c in enumerate(C[0]):
    if min_ > c:
        min_, minidx = c, i
A = [C[0][i]-C[0][minidx] for i in range(N)]
B = [C[i][minidx] for i in range(N)]
for i in range(N):
    for j in range(N):
        if A[j]+B[i] != C[i][j]:
            print('No')
            sys.exit(0)
print('Yes')
print(' '.join(map(str, B)))
print(' '.join(map(str, A)))
