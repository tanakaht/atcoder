import sys

X = input()
M = int(input())
d = 0
for x in X:
    d = max(d, int(x))
d += 1


def n_sinsu(n):
    ret = 0
    num = 1
    for x in X[::-1]:
        ret += num*int(x)
        if ret > M or num > M:
            return M+1
        num *= n
    return ret


def is_ok(n):
    return n_sinsu(n) <= M and n <= M

if len(X)==1:
    print(int(int(X)<=M))
    sys.exit(0)

if not is_ok(d):
    print(0)
    sys.exit(0)

def bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ans = max(0, bisect(M+1, d) - d + 1)
print(ans)
