import math

N, M= map(int, input().split())
A = list(map(int, input().split()))


def is_ok(x):
    cnt = 0
    for a in A:
        while math.floor(a) > x:
            cnt += 1
            a /= 2
        # cnt += math.ceil(math.log(a / x))
    return cnt <= M

def bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

X = bisect(-1, max(A))
ans = 0
cnt = 0
for a in A:
    while math.floor(a) > X:
        cnt += 1
        a /= 2
    ans += math.floor(a)
ans -= math.ceil(X / 2) * (M - cnt)
print(ans)
