import math
a, b, x = map(int, input().split())
x /= a


def is_ok(theta):
    if math.tan(theta) * b < a:
        return x <= math.tan(theta) * b * b / 2
    else:
        p = a/math.tan(theta)
        return x <= a*p/2+a*(b-p)


def bisect(ng, ok):
    while (abs(ok - ng) > 1e-9):
        mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


ans = bisect(0, math.pi)
ans = 90- ans * 180 / math.pi
print(ans)
