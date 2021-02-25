import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))
entire_xor = 0
for a in A:
    entire_xor ^= a
M = np.zeros((N, 60), dtype=bool)
A &= (~entire_xor)
for i in range(60-1, -1, -1):
    bit = 1 << i
    flg1 = A&bit!=0
    idxs = np.where(flg1 & (A<2*bit))[0]
    if len(idxs)==0:
        continue
    tmp = A[idxs[0]]
    A[flg1] ^= A[idxs[0]]
    A[idxs[0]] = tmp

A = sorted(A)[::-1]
ans = 0
for a in A:
    ans = max(ans, ans^a)
print(ans+(ans^entire_xor))
