N = int(input())
L = sorted(list(map(int, input().split())))[::-1]


def is_ok(i, x):
    return L[i] > x


def bisect(ng, ok, x):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, x):
            ok = mid
        else:
            ng = mid
    return ok


ans = 0
for i in range(N):
    for j in range(i + 1, N):
        k = bisect(N, j, L[i] - L[j])
        ans += k - j
print(ans)
