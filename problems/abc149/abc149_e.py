N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))

def count_bigger_x(x):
    cnt = 0
    piv = N-1
    for a in A:
        while piv >= 0 and a + A[piv] >= x:
            piv -= 1
        cnt += N - piv - 1
    return cnt


def is_ok(x):
    cnt = count_bigger_x(x)
    return cnt >= M


def bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

x = bisect(2 * A[-1] + 1, 2 * A[0] - 1)
ans = 0
piv = N-1
for a in A:
    while piv >= 0 and a + A[piv] >= x:
        piv -= 1
    ans += (N - piv - 1) * a
ans *= 2
ans -= 1 * x * (count_bigger_x(x) - M)
print(ans)
