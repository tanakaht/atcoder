import math

N, M = map(int, input().split())
A = list(map(int, input().split()))
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]

for l, r in LR:
    tmp = sum(A[l-1:r])/(r-l+1)
    if tmp < M:
        x = math.ceil(M-tmp)
        for i in range(l-1, r):
            A[i] += x
print(' '.join(map(str, A)))
