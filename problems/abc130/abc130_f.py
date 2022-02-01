import sys
import math

input = sys.stdin.readline
N = int(input())
XYD = [input().split() for _ in range(N)]
Ls, Rs, Ds, Us = [[-math.inf]*3 for _ in range(4)] # 止まってるの、増えてくの、減ってくの
def update(l, i, v):
    l[i] = max(l[i], v)

for x, y, d in XYD:
    x = int(x)
    y = int(y)
    if d == 'R':
        update(Ls, 2, -x)
        update(Rs, 1, x)
        update(Ds, 0, -y)
        update(Us, 0, y)
    elif d == 'L':
        update(Ls, 1, -x)
        update(Rs, 2, x)
        update(Ds, 0, -y)
        update(Us, 0, y)
    elif d == 'D':
        update(Ls, 0, -x)
        update(Rs, 0, x)
        update(Ds, 1, -y)
        update(Us, 2, y)
    elif d == 'U':
        update(Ls, 0, -x)
        update(Rs, 0, x)
        update(Ds, 2, -y)
        update(Us, 1, y)
def f(l, t):
    return max(l[0], l[1]+t, l[2]-t)

def g(t):
    l = -f(Ls, t)
    r = f(Rs, t)
    u = f(Us, t)
    d = -f(Ds, t)
    return (r-l)*(u-d)

times = set([0])
for l in [Ls, Rs, Us, Ds]:
    times.add(l[0]-l[1])
    times.add((l[2]-l[1])/2)
    times.add(l[2]-l[0])
ans = math.inf
for t in times:
    if 0<=t<10**10:
        ans = min(ans, g(t))
if ans-int(ans)==0:
    print(int(ans))
else:
    print(ans)
