import sys

N = int(input())
XY = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
Xs = [x for x, y in XY]
Ys = [y for x, y in XY]
if len(set(Xs))==1 or len(set(Ys))==1:
    print(0)
    sys.exit(0)
lcummin, lcummax = [Ys[0]], [Ys[0]]
for i in range(1, N):
    lcummin.append(min(Ys[i], lcummin[-1]))
    lcummax.append(max(Ys[i], lcummax[-1]))

def is_ok(arg):
    lidx = 0
    for x, y in XY:
        while x-Xs[lidx]>arg:
            lidx += 1
        if lidx>0 and (abs(lcummin[lidx-1]-y)>arg or abs(lcummax[lidx-1]-y)>arg):
            return False
    return True

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
print(bisect(0, 10**9))
