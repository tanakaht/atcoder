N, Q = map(int, input().split())
A = list(map(int, input().split()))
LRV = [list(map(int, input().split())) for _ in range(Q)]

diffs = [A[i+1]-A[i] for i in  range(N-1)]
ans = sum([abs(d) for d in diffs])
for l, r, v in LRV:
    l -= 1
    r -= 1
    if l > 0:
        ans += abs(diffs[l-1]+v)-abs(diffs[l-1])
        diffs[l-1] += v
    if r < N-1:
        ans += abs(diffs[r]-v)-abs(diffs[r])
        diffs[r] -= v
    print(ans)
