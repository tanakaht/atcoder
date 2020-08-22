import sys, time, random
ts = time.time()
import numpy as np

input = sys.stdin.readline

D = int(input())
c = np.array(list(map(int, input().split())), dtype=int)
S = np.array([list(map(int, input().split())) for _ in range(D)], dtype=int)
T = np.zeros(D, dtype=int)
dissatisfactions = np.zeros((D+1, 26), dtype=int)
v = 0


def findzero(a, after):
    try:
        return after+np.where(a[after:]==0)[0][0]
    except IndexError:
        return len(a)


for i, s in enumerate(S):
    dissatisfactions[i+1] = dissatisfactions[i] + c
    t = np.argmax(s+dissatisfactions[i+1])
    dissatisfactions[i+1, t] = 0
    T[i] = (t+1)
    v += s[t]
    v -= np.sum(dissatisfactions[i+1])

while time.time()-ts<1.8:
    # find d, q
    d = np.random.randint(1, D)
    q = np.random.randint(1, 26)
    # update
    pre = T[d - 1]
    new = q
    pre0 = findzero(dissatisfactions[:, pre - 1], d + 1)
    new0 = findzero(dissatisfactions[:, new - 1], d + 1)

    # 値の更新
    diff = S[d - 1, new - 1] - S[d - 1, pre - 1] +(dissatisfactions[d, new - 1]) * (new0 - d) \
           - (dissatisfactions[d - 1, pre - 1] + c[pre - 1]) * (pre0 - d)
    if diff < 0:
        continue
    v += diff
    # 配列書き換え
    T[d - 1] = new
    dissatisfactions[d:new0, new - 1] -= dissatisfactions[d, new - 1]
    dissatisfactions[d:pre0, pre - 1] += dissatisfactions[d - 1, pre - 1] + c[pre - 1]


print('\n'.join([str(int(t)) for t in T]))