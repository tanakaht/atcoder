import math

a, b, x, y, r, theta, L = map(int, input().split())
a -= 2*r
b -= 2*r
x -= r
y -= r
X = (L*math.cos(math.pi*(theta/180))+x)%(2*a)
Y = (L*math.sin(math.pi*(theta/180))+y)%(2*b)
if X > a:
    X = 2*a-X
if Y > b:
    Y = 2*b-Y
X += r
Y += r
print(X, Y)
