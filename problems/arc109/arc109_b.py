N = int(input())

def is_ok(x):
    cnt = x * (x + 1) // 2
    return cnt <= N+1


def bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


if N == 1:
    print(1)
else:
    cnt = bisect(N+1, 0)
    ans = N - (cnt - 1)
    print(ans)
