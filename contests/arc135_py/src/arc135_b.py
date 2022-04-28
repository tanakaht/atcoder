import sys
import math

N = int(input())
S = list(map(int, input().split()))
A = [[0, 0, 0] for _ in range(N+2)]
A[0][0] = 1
A[1][1] = 1
for i in range(N):
    for j in range(3):
        A[i+2][j] = -(A[i+1][j]+A[i][j])
    A[i+2][2] += S[i]
x_min = max(0, max([-A[i][2] for i in  range(0,N+2, 3)]))
y_min = max(0, max([-A[i][2] for i in  range(1,N+2, 3)]))
xy_max = min([A[i][2] for i in  range(2,N+2, 3)])
if x_min+y_min > xy_max:
    print('No')
else:
    print('Yes')
    x = x_min
    y = y_min
    ans = [A[i][0]*x+A[i][1]*y+A[i][2] for i in range(N+2)]
    print(*ans)
