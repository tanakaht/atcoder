import sys
import math

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(N)]
if N==1:
    print('Yes')
    sys.exit(0)
dx, dy = AB[0]
for i in range(N):
    AB[i][0] -= dx
    AB[i][1] -= dy
xc, yc = AB[1]
r = xc*xc+yc*yc
for i in range(N):
    available = set()
    for k in range(N):
        available.add((CD[k][0]-CD[i][0], CD[k][1]-CD[i][1]))
    for j in range(N):
        xj, yj = CD[j][0]-CD[i][0], CD[j][1]-CD[i][1]
        if i==j:
            continue
        if xc**2+yc**2!=xj**2+yj**2:
            continue
        s_nume = -xj*yc+yj*xc
        c_nume = xj*xc+yj*yc
        flg = True
        for k in range(1, N):
            x_, y_ = AB[k]
            x_, y_ = x_*c_nume-y_*s_nume, x_*s_nume+y_*c_nume
            if not (x_%(r)==0 and y_%(r)==0):
                flg = False
                break
            x_, y_ = x_//(r), y_//(r)
            if (x_, y_) not in available:
                flg = False
                break
        if flg:
            print('Yes')
            sys.exit(0)
print('No')
