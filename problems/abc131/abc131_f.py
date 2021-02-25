from collections import defaultdict

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
XY = []
Xs = set()
Ys = set()
for _ in range(N):
    x, y = map(int, input().split())
    Xs.add(x)
    Ys.add(y)
    XY.append((x, y))

Xs, Ys = list(Xs), list(Ys)
x2idx = {k: v for v, k in enumerate(Xs)}
y2idx = {k: v+len(Xs) for v, k in enumerate(Ys)}
def idx2xy(idx):
    if idx < len(Xs):
        return Xs[idx]
    else:
        return Ys[idx-len(Xs)]

uf = UnionFind(len(Xs)+len(Ys))
for x, y in XY:
    a, b = x2idx[x], y2idx[y]
    uf.union(a, b)

ans = 0
for g in uf.all_group_members().values():
    xs, ys = set(), set()
    for idx in g:
        v = idx2xy(idx)
        if idx < len(Xs):
            xs.add(v)
        else:
            ys.add(v)
    ans += len(xs)*len(ys)
print(ans-N)
