import sys
import math

input = sys.stdin.readline

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        return Vec(self.x+x, self.y+y)

    def rotate(self, theta):
        x = self.x * math.cos(theta) - self.y * math.sin(theta)
        y = self.x * math.sin(theta) + self.y * math.cos(theta)
        return Vec(x, y)

    def theta(self):
        if self.x == 0:
            if self.y > 0:
                return math.pi/2
            elif self.y < 0:
                return 3* math.pi / 2
            else:
                return 0
        ret = math.atan(self.y / self.x)
        if self.x < 0:
            ret += math.pi
        return ret

    def dist(self, other):
        return math.sqrt((self.x - other.x)** 2 + (self.y - other.y)** 2)

    def __str__(self):
        return f'{self.x}, {self.y}'


def intersection(p1, p2, r1, r2):
    p2 = p2.move(-1*p1.x, -1*p1.y)
    theta = p2.theta()
    p2 = p2.rotate(-theta)
    if p2.x + r2 < r1:
        return [p2.rotate(theta).move(p1.x, p1.y)]
    elif r2 - p2.x > r1:
        return [p1]
    elif p2.x > r1 + r2:
        return []
    else:
        x = (r1 * r1 - r2 * r2 + p2.x * p2.x) / (2 * p2.x)
        y = math.sqrt(r1 * r1 - x * x)
        return [p.rotate(theta).move(p1.x, p1.y) for p in [Vec(x, y), Vec(x, -y)]]

N, K = map(int, input().split())
xyc = [list(map(int, input().split())) for _ in range(N)]
points = [Vec(x, y) for x, y, c in xyc]
cs = [c for x, y, c in xyc]
eps = 1e-8
if K == 1:
    print(0)
    sys.exit()

def is_ok(t):
    for i in range(N):
        for j in range(i + 1, N):
            centers = intersection(points[i], points[j], t/cs[i], t/cs[j])
            for center in centers:
                cnt = 0
                for k in range(N):
                    cnt += center.dist(points[k]) <= (t / cs[k])+eps
                if cnt >= K:
                    return True
    return False

def bisect(ng, ok):
    while (abs(ok - ng) > eps):
        mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ans = bisect(0, 1000000)
print(ans)
