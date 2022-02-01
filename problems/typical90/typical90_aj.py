import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
p1, p2, p3, p4 =[XY[0]]*4
for x, y in XY[1:]:
    if p1[0]+p1[1]<x+y:
        p1 = [x, y]
    if p2[0]-p2[1]<x-y:
        p2 = [x, y]
    if -p3[0]+p3[1]<-x+y:
        p3 = [x, y]
    if -p4[0]-p4[1]<-x-y:
        p4 = [x, y]

for _ in range(Q):
    q = int(input())
    q -= 1
    ans = 0
    x, y = XY[q]
    for p in [p1, p2, p3, p4]:
        ans = max(ans, abs(p[0]-x)+abs(p[1]-y))
    print(ans)
