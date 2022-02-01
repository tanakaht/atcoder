import math

N = int(input())
x0, y0 = map(int, input().split())
xn, yn = map(int, input().split())
xc, yc = (x0+xn)/2, (y0+yn)/2
r = math.sqrt((x0-xc)**2+(y0-yc)**2)
theta = math.acos((x0-xc)/r) * (1+(-2)*(y0<yc))
theta += 2*math.pi/N
x1, y1 = xc+r*math.cos(theta), yc+r*math.sin(theta)
print(x1, y1)
