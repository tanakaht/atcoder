from collections import defaultdict
N, K = map(int, input().split())
C = list(map(int, input().split()))
d = defaultdict(int)
cnt = 0
ans = 0
for i in range(N):
    cnt += (d[C[i]]==0)
    d[C[i]] += 1
    if i>=K:
        cnt -= d[C[i-K]]==1
        d[C[i-K]] -= 1
    ans = max(ans, cnt)
print(ans)
