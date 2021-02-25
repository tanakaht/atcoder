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

H, W = map(int, input().split())
HW = [input() for _ in range(H)]
uf = UnionFind(H+W)
uf.union(0, H-1)
uf.union(0, H)
uf.union(0, H+W-1)
for h in range(H):
    for w in range(W):
        if HW[h][w] == '#':
            uf.union(h, H+w)
ans1 = 0
ans2 = 0
for root, mems in uf.all_group_members().items():
    ans1 += min(mems) < H
    ans2 += max(mems) >= H
print(min(ans1, ans2) - 1)
