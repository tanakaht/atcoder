from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
l, r = 0, 0
d = defaultdict(int)
cnt = 0
for l in range(N):
    while r<N and cnt+(d[A[r]]==0)<=K:
        cnt += d[A[r]]==0
        d[A[r]] += 1
        r += 1
    ans = max(ans, r-l)
    d[A[l]] -= 1
    cnt -= (d[A[l]]==0)
print(ans)
