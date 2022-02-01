import numpy as np
import math

H, W = map(int, input().split())
n = 1<<H
MOD = 998244353

def mat_mul(A, B, MOD):
    A1, A2 = A >> 15, A & ((1 << 15) - 1)
    B1, B2 = B >> 15, B & ((1 << 15) - 1)
    X = np.dot(A1, B1) % MOD
    Y = np.dot(A2, B2)
    Z = np.dot(A1 + A2, B1 + B2) - X - Y
    return ((X << 30) + (Z << 15) + Y) % MOD

def pow_mat(A, k, MOD=MOD):
    ret = np.eye(A.shape[0], dtype='uint64')
    tmp = A
    for i in range(k.bit_length()):
        if k >> i & 1:
            ret = mat_mul(ret, tmp, MOD)
        tmp = mat_mul(tmp, tmp, MOD)
    return ret

A = np.zeros((n, n), dtype='uint64')
for bit in range(n*n):
    bits = [0]*4 # 横おき、上から,下へ、一個
    for i in range(H):
        bits[bit%4] += 1<<i
        bit //= 4
    # okかチェック
    pre = False
    flg = True
    for i in range(H):
        if pre:
            if not (bits[0]>>i)&1:
                flg = False
                break
            else:
                pre = False
        else:
            pre = (bits[0]>>i)&1
    if pre:
        flg = False
    if not flg:
        continue
    A[bits[1], bits[2]] += 1
ans = pow_mat(A, W)[0, 0]
print(ans)
