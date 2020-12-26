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
uf = UnionFind(3 * N)
for i in range(N, 2 * N-1):
    uf.union(i, i+1)
for i in range(2*N, 3 * N-1):
    uf.union(i, i+1)
distances = []
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])** 2 + (p1[1] - p2[1])** 2)

for i, (x, y) in enumerate(xy):
    distances.append((i, i+N, y+100))
    distances.append((i, i+2*N, 100-y))
for i, pi in enumerate(xy):
    for j, pj in enumerate(xy):
        distances.append((i, j, dist(xy[i], xy[j])))
distances = sorted(distances, key=lambda x: x[2])

for i, j, d in distances:
    b = uf.find(N)
    t = uf.find(2 * N)
    ip = uf.find(i)
    jp = uf.find(j)
    if ip != b and ip != t:
        uf.union(i, j)
    elif jp != b and jp != t:
        uf.union(i, j)
    elif ip == jp:
        continue
    else:
        print(d/2)
        sys.exit()
