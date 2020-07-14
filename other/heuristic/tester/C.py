import sys
import numpy as np

input = sys.stdin.readline

D = int(input())
c = np.array(list(map(int, input().split())), dtype=int)
S = np.array([list(map(int, input().split())) for _ in range(D)], dtype=int)
T = np.array([int(input()) for _ in range(D)], dtype=int)
M = int(input())
dq = np.array([tuple(map(int, input().split())) for _ in range(M)])
dissatisfactions = np.zeros((D+1, 26), dtype=int)


def findzero(a, after):
    try:
        return after+np.where(a[after:]==0)[0][0]
    except IndexError:
        return len(a)


v = 0
for i, (s, t) in enumerate(zip(S, T)):
    v += s[t-1]
    dissatisfactions[i+1] = dissatisfactions[i] + c
    dissatisfactions[i+1, t-1] = 0
    v -= np.sum(dissatisfactions[i+1])

for d, q in dq:
    pre = T[d-1]
    new = q
    pre0 = findzero(dissatisfactions[:, pre-1], d+1)
    new0 = findzero(dissatisfactions[:, new-1], d+1)

    # 値の更新
    v += S[d - 1, new - 1] - S[d - 1, pre - 1]
    v += (dissatisfactions[d, new-1])*(new0-d) - (dissatisfactions[d-1, pre-1]+c[pre-1])*(pre0-d)
    # 配列書き換え
    T[d - 1] = new
    dissatisfactions[d:new0, new-1] -= dissatisfactions[d, new-1]
    dissatisfactions[d:pre0, pre-1] += dissatisfactions[d-1, pre-1]+c[pre-1]
    print(v)

72882
56634
38425
27930
42884
