import sys

input = sys.stdin.readline
N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]
M = [[0]*1001 for _ in range(1001)]
M_cumsumx = [[0]*1001 for _ in range(1001)]
M_cumsumxy = [[0]*1001 for _ in range(1001)]
anss = [0]*(N+1)
for lx, ly, rx, ry in LR:
    M[lx][ly] += 1
    M[lx][ry] -= 1
    M[rx][ly] -= 1
    M[rx][ry] += 1
for x in range(1001):
    M_ = M[x]
    M_cum_ = M_cumsumx[x]
    M_cum_[0] = M_[0]
    for y in range(1, 1001):
        M_cum_[y] = M_cum_[y-1] + M_[y]


for y in range(1001):
    M_cumsumxy[0][y] = M_cumsumx[0][y]
    anss[M_cumsumxy[0][y]] += 1
    for x in range(1, 1001):
        M_cumsumxy[x][y] = M_cumsumxy[x-1][y] + M_cumsumx[x][y]
        anss[M_cumsumxy[x][y]] += 1


for ans in anss[1:]:
    print(ans)
