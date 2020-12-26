import sys
import math

input = sys.stdin.readline


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        d = {root: [] for root in self.roots()}
        for i in range(self.n):
            d[self.find(i)].append(i)
        return d

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
# 0~N-1=>X, N~2N-1=>B,2N~3N-1=>T とする
distances = []
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])** 2 + (p1[1] - p2[1])** 2)

for i, (x, y) in enumerate(xy):
    distances.append((i, N, y+100))
    distances.append((i, N+1, 100-y))
for i, pi in enumerate(xy):
    for j, pj in enumerate(xy):
        distances.append((i, j, dist(xy[i], xy[j])))
distances.append((N, N+1, 200))
distances = sorted(distances, key=lambda x: x[2])


def is_ok(r):
    uf = UnionFind(N + 2)
    for i, j, d in distances:
        if d < r:
            uf.union(i, j)
        else:
            break
    return uf.find(N) != uf.find(N + 1)


def bisect(ng, ok):
    while (abs(ok - ng) > 1e-8):
        mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ans = bisect(205, 0)
print(ans/2)
