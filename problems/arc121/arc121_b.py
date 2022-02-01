import math

N = int(input())
AC = []
color2id = {'R': 0, 'G': 1, 'B': 2}
for _ in range(2*N):
    a, c = input().split()
    AC.append((int(a), color2id[c]))
AC = sorted(AC, key=lambda x: x[0])
dists = [math.inf]*3
cnts = [0]*3
lasts = [-math.inf]*3
for a, c in AC:
    cnts[c] ^= 1
    lasts[c] = a
    for c_  in range(3):
        if c != c_:
            dists[c^c_^3] = min(dists[c^c_^3], abs(lasts[c_]-a))
if sum(cnts) == 0:
    print(0)
else:
    idxs = []
    for i in range(3):
        if cnts[i]:
            idxs.append(i)
    print(min(dists[idxs[0]^idxs[1]^3], sum(dists)-dists[idxs[0]^idxs[1]^3]))
