import math
X = int(input())
A, B = 1, 1


def is_ok(i, x):
    return pow(i, 5) >= x


def bisect(ng, ok, x):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, x):
            ok = mid
        else:
            ng = mid
    return ok


ss = math.ceil(X ** (1 / 4)) + 10
for a in range(1, math.ceil(X ** (1 / 4)) + 10):
    tmp = abs(pow(a, 5) - X)
    b = bisect(-1, ss, tmp)
    if tmp == pow(b, 5):
        A = a
        if a ** 5 - X > 0:
            B = b
        else:
            B = -1 * b
        break
print(A, B)
