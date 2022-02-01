import math
N, P, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def is_ok(X, n=K):
    dists = [[A[i][j] if A[i][j]!=-1 else X for j in range(N)] for i in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            cnt += dists[i][j] <= P
    return cnt<=n


def bisect(ng, ok, n=K):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, n):
            ok = mid
        else:
            ng = mid
    return ok

if is_ok(math.inf, n=K) and (not is_ok(math.inf, n=K-1)):
    print('Infinity')
else:
    print(bisect(0, 10**9, n=K-1)-bisect(0, 10**9, n=K))
