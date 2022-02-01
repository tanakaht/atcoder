import sys
from collections import defaultdict, deque
N = int(input())
X = list(map(int, input().split()))
A = X[:N]
B = X[N:]
v2i = defaultdict(list)
for i, a in enumerate(A):
    v2i[a].append(i)
vmin = min(v2i.keys())
if min([B[i] for i in v2i[vmin]])<=vmin:
    print(vmin, min([B[i] for i in v2i[vmin]]))
    sys.exit(0)


ansi = []
R = deque()
l = -1
for i in v2i[vmin]:
    ansi.append(i)
    l = i
    R.append(B[i])
for v in sorted(v2i.keys())[1:]:
    ri = 0
    while len(R)>ri and R[ri]==v:
        ri += 1
    if len(R)==ri:
        break
    elif R[ri] < v:
        break
    else:
        pass
    for i in v2i[v]:
        if i<l:
            continue
        ansi.append(i)
        R.append(B[i])
        l = i
ans = [A[i] for i in ansi]+[B[i] for i in ansi]
print(*ans)
