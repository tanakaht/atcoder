import bisect

N = int(input())
P = sorted(enumerate(map(int, input().split())), key=lambda x: x[1])[::-1]
used = [-1, -1, P[0][0], N, N]
ans = 0
for i, p in P[1:]:
    idx = bisect.bisect_left(used, i)
    d = 0
    d += (used[idx] - i) * (used[idx - 1] - used[idx - 2])
    d += (i-used[idx - 1]) * (used[idx + 1] - used[idx])
    ans += p * d
    used.insert(idx, i)
print(ans)
