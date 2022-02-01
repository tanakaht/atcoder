import heapq
from collections import deque

Q = int(input())
sorted_q = []
rest_l = deque([])
for _ in range(Q):
    c, *x = map(int, input().split())
    if c==1:
        rest_l.append(x[0])
    elif c==2:
        if sorted_q:
            x = heapq.heappop(sorted_q)
        elif rest_l:
            x = rest_l.popleft()
        print(x)
    elif c==3:
        while rest_l:
            x = rest_l.popleft()
            heapq.heappush(sorted_q, x)
