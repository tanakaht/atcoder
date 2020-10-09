import heapq
import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
STX = [list(map(int, input().split())) for _ in range(N)]
D = [int(input()) for _ in range(Q)]
min_d = []
outed = [False] * N
eventq = []
for i, (s, t, x) in enumerate(STX):
    eventq.append((s-x-0.5, 1, x, i))
    eventq.append((t - x-0.5, -1, x, i))
for d in D:
    eventq.append((d, 0, None, None))
eventq = sorted(eventq)

for t, flg, x, i in eventq:
    if flg == 1:
        heapq.heappush(min_d, (x, i))
    elif flg == -1:
        outed[i] = True
    else:
        ans = -1
        while len(min_d) > 0 and outed[min_d[0][1]]:
            heapq.heappop(min_d)
        ans = -1 if len(min_d) == 0 else min_d[0][0]
        print(ans)
