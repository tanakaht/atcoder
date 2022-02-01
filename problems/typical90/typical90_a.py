N, L = map(int, input().split())
K = int(input())
A = [0]+list(map(int, input().split()))+[L]
def is_ok(l):
    now_l = 0
    cnt = 0
    for i in range(N+1):
        now_l += A[i+1]-A[i]
        if now_l >= l:
            cnt += 1
            now_l = 0
    return cnt >= K+1


def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(bisect(L+1, 0))
