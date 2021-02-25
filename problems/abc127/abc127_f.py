import math
import heapq

Q = int(input())
querys = [list(map(int, input().split())) for _ in range(Q)]
b_sum = 0
left_sum = 0
right_sum = 0
lq, rq = [math.inf], [math.inf]
cnt = 0
for i in range(Q):
    q = querys[i]
    if q[0] == 1:
        cnt += 1
        a, b = q[1], q[2]
        b_sum += b
        if a >= rq[0]:
            heapq.heappush(rq, a)
            right_sum += a
        else:  # if -a >= lq[0]: とりあえず左に入れてしまう
            heapq.heappush(lq, -a)
            left_sum += a
        while len(lq)>len(rq)+(cnt%2):
            tmp = -1*heapq.heappop(lq)
            left_sum -= tmp
            heapq.heappush(rq, tmp)
            right_sum += tmp
        while len(lq)<len(rq)+(cnt%2):
            tmp = heapq.heappop(rq)
            right_sum -= tmp
            heapq.heappush(lq, -tmp)
            left_sum += tmp
    if q[0] == 2:
        piv = -lq[0]
        ans = abs((len(lq)-1)*piv-left_sum) + abs(right_sum-(len(rq)-1)*piv) + b_sum
        print(piv, ans)
