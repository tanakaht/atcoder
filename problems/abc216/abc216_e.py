import sys

N, K = map(int, input().split())
A = list(map(int, input().split()))

# x以上でK回のれるか
def is_ok(x):
    cnt = 0
    for a in A:
        cnt += max(0, a-x+1)
    return cnt >= K

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

d = bisect(max(A)+1, 0)
ans = 0
for i in range(N):
    if A[i]>=d:
        K -= max(0, A[i]-d)
        ans +=  (A[i]+d+1)*(A[i]-d)//2
print(ans+K*d)
