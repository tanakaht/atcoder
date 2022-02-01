import math
import heapq
from collections import defaultdict

W, N = map(int, input().split())
LRV = [list(map(int, input().split())) for _ in range(N)]
dp = [[-math.inf]*(W+1) for _ in range(N+1)]
dp[0][0] = 0
for i, (l, r, v) in enumerate(LRV):
    pre = dp[i]
    new = dp[i+1]
    q = []
    cnt = defaultdict(int)
    for w in range(W+1):
        while q and cnt[-q[0]] == 0:
            heapq.heappop(q)
        if q:
            max_ = -q[0]
        else:
            max_ = -math.inf
        new[w] = max(pre[w], max_+v)
        if w-r >= 0:
            cnt[pre[w-r]] -= 1
        if w-l+1 >= 0:
            cnt[pre[w-l+1]] += 1
            heapq.heappush(q, -pre[w-l+1])

ans = dp[-1][-1]
if ans == -math.inf:
    print(-1)
else:
    print(ans)
