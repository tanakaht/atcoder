N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def is_ok(k):
    M = [[2*(A[i][j]<=k)-1 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(1, N):
            M[i][j] += M[i][j-1]
    for i in range(1, N):
        for j in range(N):
            M[i][j] += M[i-1][j]
    if M[K-1][K-1] >= 0:
        return True
    for i in range(K, N):
        for j in range(K, N):
            if M[i][j] - M[i-K][j] - M[i][j-K] + M[i-K][j-K] >= 0:
                return True
    for i in range(K, N):
        if M[K-1][i] - M[K-1][i-K] >= 0:
            return True
        if M[i][K-1] - M[i-K][K-1] >= 0:
            return True
    return False


def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
print(bisect(-1, 10**9))
