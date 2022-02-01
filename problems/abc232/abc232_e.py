import sys
import numpy as np
import math

H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
MOD = 998244353

def mat_mul(A, B, MOD=math.inf):
    A1, A2 = A >> 15, A & ((1 << 15) - 1)
    B1, B2 = B >> 15, B & ((1 << 15) - 1)
    X = np.dot(A1, B1) % MOD
    Y = np.dot(A2, B2)
    Z = np.dot(A1 + A2, B1 + B2) - X - Y
    return ((X << 30) + (Z << 15) + Y) % MOD

def pow_mat(A, k, MOD=math.inf):
    ret = np.eye(A.shape[0], dtype='uint64')
    tmp = A
    for i in range(k.bit_length()):
        if k >> i & 1:
            ret = mat_mul(ret, tmp, MOD=MOD)
        tmp = mat_mul(tmp, tmp, MOD=MOD)
    return ret

A = np.array([[W+H-4, 1, 1, 0],
               [W-1, H-2, 0, 1],
               [H-1, 0, W-2, 1],
               [0, H-1, W-1, 0]], dtype="uint64").T
x = np.array([0, 0, 0, 0], dtype="uint64")
if x1==x2 and y1==y2:
    x[3] = 1
elif x1==x2:
    x[2] = 1
elif y1==y2:
    x[1] = 1
else:
    x[0] = 1
print((pow_mat(A, K, MOD)@x)[3])
