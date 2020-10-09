import sys
import bisect
from collections import deque

input = sys.stdin.readline
N = int(input())
xy = sorted([[i] + list(map(int, input().split())) for i in range(N)], key=lambda x: x[1])


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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

uf = UnionFind(N)
ys = deque([(xy[0][2], xy[0][0])])  # union毎に最小のyのみ保持する
for i, x, y in xy[1:]:
    if ys[0][0] >= y:
        ys.appendleft((y, i))
        continue
    miny, minj = ys[0]
    while len(ys)>0:
        y_, j = ys.popleft()
        if y_ >= y:
            ys.appendleft((y_, j))
            break
        uf.union(i, j)
    ys.appendleft((miny, minj))
for i in range(N):
    print(uf.size(i))
