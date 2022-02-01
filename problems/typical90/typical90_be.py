import sys
import numpy as np


N, M = map(int, input().split())  # M個のパネル, N個のスイッチ
A = np.zeros((N, M), dtype=bool)
MOD = 998244353
for i in range(N):
    _ = int(input())
    A_ = list(map(int, input().split()))
    for j in A_:
        j -= 1
        A[i, j] = 1
S = np.array(list(map(int, input().split())), dtype=bool)
A = np.concatenate([A, S.reshape((1, M))])
ans = 1
for i in range(N+1):
    j = 0
    flg = False
    for p in range(i):
        while j<M and not (A[p, j] or A[i, j]):
            j += 1
        if j==M:
            break
        elif A[p, j] and A[i, j]:
            A[i] ^= A[p]
        elif A[i, j]:
            A[[i, p]] = A[[p, i]]
            flg = True
        else:
            pass
    if i==N:
        if sum(A[i])!=0 or flg:
            ans = 0
    elif sum(A[i])==0 and not flg:
        ans = (ans*2)%MOD

print(ans)
