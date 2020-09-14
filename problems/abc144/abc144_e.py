import math

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
F = sorted(list(map(int, input().split())))[::-1]


def is_ok(x):
    cnt = 0
    for i in range(N):
        if A[i]*F[i] > x:
            cnt += A[i] - math.floor(x / F[i])
    return cnt <= K


def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


ans = meguru_bisect(-1, max([a * f for a, f in zip(A, F)]))
print(ans)
