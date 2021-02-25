import sys
from collections import Counter, defaultdict

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


input = sys.stdin.readline
N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
n = 0
for a, b in ab:
    n = max(n, a, b)
uf = UnionFind(n+1)
for a, b in ab:
    uf.union(a, b)
count = defaultdict(lambda: 0)
for a, b in ab:
    count[uf.find(a)] += 1
ans = 0
for root_, g in uf.all_group_members().items():
    ans += len(g)
    ans -= len(g) > count[root_]
print(ans)
