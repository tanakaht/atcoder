N, L = map(int, input().split())
XA = [(0, 0)] + [list(map(int, input().split())) for _ in range(N)]

def is_ok(T):
    t = T
    for i in range(N):
        t = min(T, t+XA[i+1][0]-XA[i][0])
        t -= XA[i+1][1]
        if t < 0:
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

print(bisect(-1, N*int(1e9)))
