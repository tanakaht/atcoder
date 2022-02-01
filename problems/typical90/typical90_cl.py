import sys
import numpy as np
import math
from itertools import product

def mat_mul(A, B, MOD):
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
            ret = mat_mul(ret, tmp, MOD)
        tmp = mat_mul(tmp, tmp, MOD)
    return ret

N, K = map(int, input().split())
MOD = 998244353
if K ==1:
    A = np.array([[1, 1], [1, 0]], dtype='uint64')
    ans = 0
    for i in pow_mat(A, N, MOD=MOD)@np.array([1, 0], dtype='uint64'):
        ans = (ans+int(i))%MOD
    print(ans)
elif K<=10:
    ans = 0
    for li in product(range(K+1), repeat=N):
        flg = True
        for l in range(N):
            for r in range(l, N):
                if min(li[l:r+1])*(r-l+1)>K:
                    flg = False
                    break
            if not flg:
                break
        ans += flg
    print(ans)
elif K<=100:
    ptn =  set()
    for i in range(1, N+1):
        ptn.add(K//i)
    ptn = sorted(ptn)
    dp = [[0]*(1<<len(ptn)) for _ in range(N)]
