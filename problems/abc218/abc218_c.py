import numpy as np
import sys

N = int(input())
S = np.array([list(map(lambda x: x=='#', input())) for _ in range(N)])
T = np.array([list(map(lambda x: x=='#', input())) for _ in range(N)])
if np.sum(S)!=np.sum(T):
    print('No')
    sys.exit(0)
for _ in range(4):
    flg = True
    found = False
    for iS in range(N):
        for jS in range(N):
            if S[iS, jS]:
                found = True
                break
        if found:
            break
    found = False
    for iT in range(N):
        for jT in range(N):
            if T[iT, jT]:
                found = True
                break
        if found:
            break
    idiff, jdiff = iT-iS, jT-jS
    for iS in range(N):
        iT = iS+idiff
        for jS in range(N):
            jT = jS+jdiff
            if S[iS, jS]:
                if 0<=iT<N and 0<=jT<N:
                    flg = flg & T[iT, jT]
                else:
                    flg = False
    if flg:
        print("Yes")
        sys.exit(0)
    S = S[::-1].T
print('No')
