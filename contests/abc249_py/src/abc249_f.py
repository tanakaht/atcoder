import sys
import math
import heapq

N, K = map(int, input().split())
ty = [[1, 0]]+[list(map(int, input().split())) for _ in range(N)]
ans = -math.inf
q = []
sum2 = 0
for t, y in ty[::-1]:
    if t==1:
        ans = max(ans, sum2+y)
        K -= 1
        if K<0:
            break
    if t==2:
        if y<0:
            heapq.heappush(q, -y)
        else:
            sum2 += y
    while len(q)>K:
        sum2 += -heapq.heappop(q)
print(ans)
