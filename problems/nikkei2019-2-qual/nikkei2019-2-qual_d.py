import sys
import heapq

N, M  = map(int, input().split())
LRC = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[0]) + [[N, N, 0]]
q = [(0, 1)]  # (d, r)
for l, r, c in LRC:
    while q and q[0][1] < l:
        heapq.heappop(q)
    if not q:
        print(-1)
        sys.exit()
    heapq.heappush(q, (q[0][0]+c, r))
print(q[0][0])
