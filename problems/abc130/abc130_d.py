N, K = map(int, input().split())
A = list(map(int, input().split()))
sumA = [0] * (N+1)
for i in range(1, N+1):
    sumA[i] = sumA[i - 1] + A[i - 1]

def is_ok(i, x):
    return sumA[i] >= x

def bisect(ng, ok, x):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, x):
            ok = mid
        else:
            ng = mid
    return ok


ans = 0

for a in sumA:
    i = bisect(0, N+1, K + a)
    ans += N+1-i

print(ans)
