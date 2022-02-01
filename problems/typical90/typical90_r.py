import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
for _ in range(Q):
    e = int(input())
    theta = 3*math.pi/2 - (e%T)*2*math.pi/T
    yt, zt = L*math.cos(theta)/2, L*math.sin(theta)/2+L/2
    d = math.sqrt(X**2+(Y-yt)**2)
    ans = (math.atan2(zt, d))
    print(180*ans/math.pi)
