from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
d = defaultdict(lambda: 0)
for a in A:
    d[a] += 1
cant_use = [0] * (N+1)
for v in d.values():
    for i in range(v):
        cant_use[i] += v - i


def is_ok(i, k):
    return (N-cant_use[i])/k >= i

def bisect(ng, ok, k):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, k):
            ok = mid
        else:
            ng = mid
    return ok

for k in range(1, N + 1):
    print(bisect(N+1, 0, k))
