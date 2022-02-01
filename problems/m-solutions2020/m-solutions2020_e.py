import math, sys

N = int(input())
XYP = [list(map(int, input().split())) for _ in range(N)]
anss = [math.inf] * (N + 1)
x_cost = [[abs(XYP[i][0])*XYP[i][2] for i in range(N)] for _ in range(1<<N)]
y_cost = [[abs(XYP[i][1])*XYP[i][2] for i in range(N)] for _ in range(1<<N)]
for bit in range(1<<N):
    available = []
    for i in range(N):
        if bit>>i&1:
            available.append(i)
    for i in range(N):
        x, y, p = XYP[i]
        for j in available:
            x_, y_, _ = XYP[j]
            x_cost[bit][i] = min(x_cost[bit][i], abs(x-x_)*p)
            y_cost[bit][i] = min(y_cost[bit][i], abs(y-y_)*p)

for bit in range(1<<N):
    line_cnt = bin(bit).count("1")
    xbit = bit
    while True:
        ybit = bit ^ xbit
        cost = 0
        xc, yc = x_cost[xbit], y_cost[ybit]
        for i in range(N):
            cost += min(xc[i], yc[i])
        anss[line_cnt] = min(anss[line_cnt], cost)
        xbit -= 1
        if xbit < 0:
            break
        xbit &= bit

for ans in anss:
    print(ans)
