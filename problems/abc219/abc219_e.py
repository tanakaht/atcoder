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

A = [list(map(int, input().split())) for _ in range(4)]
ans = 0
for bit in range(1<<16):
    B = [[(bit>>(x*4+y))&1 for y in range(4)] for x in range(4)]
    mura_ok = True
    uf = UnionFind(17)
    for x in range(4):
        for y in range(4):
            if A[x][y]:
                mura_ok = mura_ok and B[x][y]
            if x<3 and B[x][y]==B[x+1][y]:
                uf.union(x*4+y, (x+1)*4+y)
            if y<3 and B[x][y]==B[x][y+1]:
                uf.union(x*4+y, x*4+y+1)
            if (x==0 or x==3 or y==0 or y==3) and (not B[x][y]):
                uf.union(x*4+y, 16)
    ans += mura_ok and (len(uf.roots())==2)
print(ans)
