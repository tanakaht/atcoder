import heapq
import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
STX = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0] - x[2])
D = [int(input()) for _ in range(Q)]
now_t = []
now_x = []
outed = [False] * N
stx_i = 0
for d in D:
    while stx_i < N and STX[stx_i][0] - STX[stx_i][2] <= d:
        stx = STX[stx_i]
        heapq.heappush(now_t, (stx[1] - stx[2], stx_i))
        heapq.heappush(now_x, (stx[2], stx_i))
        stx_i += 1
    while len(now_t) > 0 and now_t[0][0] <= d:
        _, stx_i_ = heapq.heappop(now_t)
        outed[stx_i_] = True
    while len(now_x) > 0 and outed[now_x[0][1]]:
        heapq.heappop(now_x)
    if len(now_x) > 0:
        print(now_x[0][0])
    else:
        print(-1)
