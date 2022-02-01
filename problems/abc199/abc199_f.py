import numpy as np
import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
A = np.array(list(map(int, input().split())), dtype='uint64')
XY = [list(map(int, input().split())) for _ in range(M)]
C = np.eye(N, dtype='uint64')*(2*M)
MOD = int(1e9)+7
for x, y in XY:
    x -= 1
    y -= 1
    C[x, x] -= 1
    C[x, y] += 1
    C[y, x] += 1
    C[y, y] -= 1

def mat_mul(A, B):
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
            ret = mat_mul(ret, tmp)
        tmp = mat_mul(tmp, tmp)
    return ret

C = pow_mat(C, K, MOD)
divi = pow(2*M, K, MOD)
for i in ((mat_mul(C, A)%MOD)*pow(divi, MOD-2, MOD))%MOD:
    print(i)
