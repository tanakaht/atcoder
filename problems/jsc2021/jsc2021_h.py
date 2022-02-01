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

N, M = map(int, input().split())
AC = [list(map(int, input().split())) for _ in range(N)]
XY = [list(map(lambda x: int(x)-1, input().split())) for _ in range(N)]
edges = []
uf = UnionFind(N)
g = [[] for _ in range(N)]
for i, (a, c) in enumerate(AC):
    a -= 1
    if uf.find(i) == uf.find(a):
        removed = (i, a, c)
    else:
        edges.append((i, a, c))
        g[a].append((i, c))
        g[i].append((a, c))
        uf.union(i, a)

ans1 = 0
for x, y in XY:
