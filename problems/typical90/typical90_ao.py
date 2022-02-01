import math

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
center_x, center_y = XY[0]  # ((XY[0][0]+XY[1][0])/2, (XY[0][1]+XY[1][1])/2)
# center_x, center_y = 62, 2
XY = sorted([[x-center_x, y-center_y] for x, y in XY[1:]], key=lambda x: math.atan2(x[0], x[1]))

# Ray casting algorithm
def inside_polygon(p0, qs):
    cnt = 0
    L = len(qs)
    x, y = p0
    for i in range(L):
        x0, y0 = qs[i-1]; x1, y1 = qs[i]
        x0 -= x; y0 -= y
        x1 -= x; y1 -= y

        cv = x0*x1 + y0*y1
        sv = x0*y1 - x1*y0
        if sv == 0 and cv <= 0:
            # a point is on a segment
            return True

        if not y0 < y1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        if y0 <= 0 < y1 and x0*(y1 - y0) > y0*(x1 - x0):
            cnt += 1
    return (cnt % 2 == 1)

# Winding number algorithm
def inside_polygon1(p0, qs):
    x, y = p0
    L = len(qs)
    theta = 0
    for i in range(L):
        x0, y0 = qs[i-1]; x1, y1 = qs[i]
        x0 -= x; y0 -= y
        x1 -= x; y1 -= y

        cv = x0*x1 + y0*y1
        sv = x0*y1 - x1*y0
        if sv == 0 and cv <= 0:
            # a point is on a segment
            return True

        theta += math.atan2(sv, cv)
    return abs(theta) > 1


maxr, idx = XY[0][1]**2+XY[0][0]**2, 0
for i in range(N-1):
    x, y = XY[i]
    if x*x+y*y > maxr:
        maxr = x*x+y*y
        idx = i
P = [XY[idx]]
for i in range(1, N-1):
    x, y = XY[(idx+i)%(N-1)]
    while len(P) >= 2 and inside_polygon(P[-1], [[0, 0], P[-2], (x, y), (0, 0)]):
        P.pop()
    theta1 = math.atan2(x, y)
    theta2 = math.atan2(P[-1][0], P[-1][1])
    theta1 += math.pi*2*(theta1<theta2)
    if theta1-theta2>math.pi:
        P.append([0, 0])
    P.append([x, y])
x, y = P[0]
while len(P) >= 2 and inside_polygon(P[-1], [[0, 0], P[-2], (x, y), (0, 0)]):
    P.pop()
theta1 = math.atan2(x, y)
theta2 = math.atan2(P[-1][0], P[-1][1])
theta1 += math.pi*2*(theta1<theta2)
if theta1-theta2>math.pi:
    P.append([0, 0])
P.append([x, y])

S = 0
b = 0
for i in range(len(P)-1):
    x1, y1 = P[i]
    x2, y2 = P[i+1]
    S += abs(x1*y2-y1*x2)
    b += math.gcd(abs(x1-x2), abs(y1-y2))
i = (S-b+2)//2
print(i+b-N)
