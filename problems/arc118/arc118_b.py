import math
K, N, M = map(int, input().split())
A = list(map(int, input().split()))

def get_min_B(maxi):
    B = [0]*K
    for k in range(K):
        B[k] = max(0, math.ceil((M*A[k])/N-maxi*M))
    return B

def get_max_B(maxi):
    B = [0]*K
    for k in range(K):
        B[k] = math.floor((M*A[k])/N+maxi*M)
    return B

def is_ok(maxi):
    if maxi < 0:
        return False
    B1 = get_min_B(maxi)
    B2 = get_max_B(maxi)
    if min(B2) < 0:
        return False
    return sum(B1)<=M<=sum(B2)

def bisect(ng, ok):
    while abs(ok - ng) > 1e-15:
        mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

maxi = bisect(-0.1, 1)
B1 = get_min_B(maxi)
B2 = get_max_B(maxi)
ans = B2
cnt = sum(B2)
for k in range(K):
    if cnt > M:
        v = max(B1[k], ans[k]-(cnt-M))
        cnt -= ans[k]-v
        ans[k] = v
print(*ans)
