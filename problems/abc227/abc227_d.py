import sys

N, K = map(int, input().split())
A = list(map(int, input().split()))

def is_ok(arg):
    cnt = sum([min(a, arg) for a in A])
    return cnt>=arg*K


def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
print(bisect(sum(A), 0))
