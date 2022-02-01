import sys

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

N, M, Q = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(M)]
uvw = [list(map(int, input().split())) for _ in range(Q)]
uf = UnionFind(N)
l = []
for a, b, c in abc:
    l.append((c, 0, a-1, b-1, None))
for i, (a, b, c) in enumerate(uvw):
    l.append((c, 1, a-1, b-1, i))
anss = [None]*Q
for w, flg, u, v, i in sorted(l):
    if flg:
        if uf.find(u)==uf.find(v):
            anss[i] = "No"
        else:
            anss[i] = "Yes"
    else:
        uf.union(u, v)
print(*anss,sep="\n")
