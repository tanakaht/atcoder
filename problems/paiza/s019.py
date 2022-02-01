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

N, H, W = map(int, input().split())
xy = [list(map(int, input().split()))for _ in range(N)]
def dist(i, j):
    xi, yi = xy[i]
    xj, yj = xy[j]
    ret = min(abs(xi-xj), W+min(xi, xj)-max(xi,xj)) + min(abs(yi-yj), H+min(yi, yj)-max(yi, yj))
    return ret
dists = []
for i in range(N):
    for j in range(i+1, N):
        dists.append((dist(i, j), i, j))
dists = sorted(dists, key=lambda x: x[0])
uf = UnionFind(N)
ans = 0
for d, i, j in dists:
    if uf.find(i) != uf.find(j):
        ans += d
        uf.union(i, j)
print(ans)
